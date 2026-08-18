#!/usr/bin/env python3
"""Normalize the PDF-derived LaTeX source into maintainable LaTeX.

This is intentionally scoped to ``latex/principlesOfMechanics.tex``.  The MyST
chapters are not inputs and are never modified.
"""

from pathlib import Path
import re


SOURCE = Path(__file__).with_name("principlesOfMechanics.tex")


def normalize_headings(text: str) -> str:
    # Replace the transcription of the printed contents pages with a real TOC.
    text = re.sub(
        r"\\section\*\{Contents\}\n.*?(?=\\section\*\{Units and Vectors\})",
        lambda _: "\\tableofcontents\n\\clearpage\n\n",
        text,
        flags=re.S,
    )

    chapters = [
        "Units and Vectors", "Kinematics", "Newton's Laws", "Work and Energy",
        "Impulse, Momentum, and Collisions", "System of Particles",
        "Rotation of Rigid Bodies", "Rolling and Static Equilibrium",
        "Central Force Motion", "Oscillatory Motion",
    ]
    for number, title in enumerate(chapters, 1):
        starred = rf"\\section\*\{{{re.escape(title)}\}}"
        if re.search(starred, text):
            text = re.sub(starred, lambda _, t=title, n=number: rf"\section{{{t}}}\label{{chap:{n}}}", text, count=1)
        else:
            # Three chapter titles survived PDF extraction as unmarked plain text.
            marker = rf"(?m)^{re.escape(title)}\s*$"
            text = re.sub(marker, lambda _, t=title, n=number: rf"\section{{{t}}}\label{{chap:{n}}}", text, count=1)

    # Printed section numbers are replaced by LaTeX counters and stable labels.
    heading = re.compile(r"(?m)^\\subsection\*\{([0-9]+(?:\.[0-9]+)+)\s+([^}]*)\}$")

    def heading_repl(match: re.Match[str]) -> str:
        printed, title = match.groups()
        # Repair three obvious OCR corruptions in chapter 1 headings.
        printed = {"19.2.2": "1.9.2.2", "19.2.2.4": "1.9.2.4", "19.2.5": "1.9.2.5"}.get(printed, printed)
        depth = printed.count(".")
        command = {1: "subsection", 2: "subsubsection"}.get(depth, "paragraph")
        return rf"\{command}{{{title}}}\label{{sec:{printed.replace('.', '-')}}}"

    text = heading.sub(heading_repl, text)
    text = re.sub(r"(?m)^\\section\*\{Problems\}$", lambda _: r"\subsection*{Problems}\addcontentsline{toc}{subsection}{Problems}", text)
    text = re.sub(r"(?m)^\\section\*\{Solution ([^}]*)\}$", lambda m: rf"\paragraph*{{Solution {m.group(1)}}}", text)
    text = text.replace(r"\section*{Scalar Triple Product}", r"\paragraph{Scalar Triple Product}")
    text = text.replace(r"\section*{Vector Triple Product}", r"\paragraph{Vector Triple Product}")
    return text


def normalize_equations(text: str) -> str:
    text = re.sub(
        r"\\tag\{(\d+)\.(\d+)\}",
        lambda m: rf"\label{{eq:{m.group(1)}-{m.group(2)}}}",
        text,
    )
    # Longest spelling first; this deliberately excludes Example/Problem numbers.
    text = re.sub(
        r"\b(?:Equations?|Eqs?\.)\s*\(?\s*(\d+)\.(\d+)\s*\)?",
        lambda m: rf"Eq.~\eqref{{eq:{m.group(1)}-{m.group(2)}}}",
        text,
    )
    labels = set(re.findall(r"\\label\{eq:(\d+)-(\d+)\}", text))
    revised = []
    for line in text.splitlines():
        if r"\eqref{eq:" in line:
            line = re.sub(
                r"\(?\b(\d+)\.(\d+)\b\)?",
                lambda m: rf"\eqref{{eq:{m.group(1)}-{m.group(2)}}}"
                if m.groups() in labels else m.group(0),
                line,
            )
        revised.append(line)
    text = "\n".join(revised) + ("\n" if text.endswith("\n") else "")
    return text


def number_labeled_math(text: str) -> str:
    """Enable numbering only for display environments that now have labels."""
    pattern = re.compile(
        r"\\begin\{(equation|align|gather)\*\}(.*?)\\end\{\1\*\}",
        flags=re.S,
    )

    def repl(match: re.Match[str]) -> str:
        environment, body = match.groups()
        if r"\label{eq:" not in body:
            return match.group(0)
        return rf"\begin{{{environment}}}{body}\end{{{environment}}}"

    return pattern.sub(repl, text)


CAPTION_RE = re.compile(r"^Fig(?:ure)?\.?\s*(\d+)\.(\d+)\s+(.+?)(?:\\\\)?\s*$")
GRAPHIC_RE = re.compile(r"\\includegraphics(?:\[[^]]*\])?\{[^}]+\}(?:\\\\)?")


def normalize_figures(text: str) -> str:
    lines = text.splitlines()
    used_captions: set[int] = set()
    figure_for_graphic: dict[int, tuple[int, re.Match[str]]] = {}

    # Pair each caption with the nearest unpaired graphic. Captions can occur on
    # either side of a graphic and center wrappers may sit between them.
    graphic_lines = [i for i, line in enumerate(lines) if GRAPHIC_RE.search(line)]
    for ci, line in enumerate(lines):
        caption = CAPTION_RE.match(line.strip())
        if not caption:
            continue
        candidates = [gi for gi in graphic_lines if gi not in figure_for_graphic and abs(gi - ci) <= 7]
        if not candidates:
            continue
        gi = min(candidates, key=lambda value: abs(value - ci))
        figure_for_graphic[gi] = (ci, caption)
        used_captions.add(ci)

    output: list[str] = []
    skip = used_captions.copy()
    # Center environments around a paired graphic become redundant and can nest
    # badly inside floats, so omit only immediately adjacent wrapper lines.
    for gi in figure_for_graphic:
        if gi > 0 and lines[gi - 1].strip() == r"\begin{center}":
            skip.add(gi - 1)
        if gi + 1 < len(lines) and lines[gi + 1].strip() == r"\end{center}":
            skip.add(gi + 1)

    for i, line in enumerate(lines):
        if i in skip:
            continue
        if i not in figure_for_graphic:
            output.append(line)
            continue
        _, caption = figure_for_graphic[i]
        chapter, number, title = caption.groups()
        graphic = GRAPHIC_RE.search(line).group(0).removesuffix(r"\\")
        # Standardize converter-only sizing syntax supplied by adjustbox.
        graphic = re.sub(r"\[[^]]*\]", r"[width=0.9\\textwidth]", graphic, count=1)
        output.extend([
            r"\begin{figure}[htbp]",
            r"\centering",
            graphic,
            rf"\caption{{{title}}}\label{{fig:{chapter}-{number}}}",
            r"\end{figure}",
        ])

    text = "\n".join(output) + "\n"
    # Replace prose references after caption lines have been removed.
    text = re.sub(
        r"\b(?:Fig(?:ure)?s?\.)\s*(\d+)\.(\d+)",
        lambda m: rf"Fig.~\ref{{fig:{m.group(1)}-{m.group(2)}}}",
        text,
    )
    text = re.sub(
        r"\bFigure\s+(\d+)\.(\d+)",
        lambda m: rf"Figure~\ref{{fig:{m.group(1)}-{m.group(2)}}}",
        text,
    )
    return text


def repair_orphan_figure_captions(text: str) -> str:
    """Preserve extracted captions whose corresponding graphic was lost/misplaced."""
    pattern = re.compile(
        r"(?m)^Fig\.~\\ref\{fig:(\d+)-(\d+)\}\s+(.+?)(?:\\\\)?\s*$"
    )
    return pattern.sub(
        lambda m: "\n".join([
            r"\begin{figure}[htbp]",
            rf"\caption{{{m.group(3)}}}\label{{fig:{m.group(1)}-{m.group(2)}}}",
            r"\end{figure}",
        ]),
        text,
    )


def remove_duplicate_caption_only_figures(text: str) -> str:
    """Drop caption-only recovery floats when a graphic float has the label."""
    block = re.compile(r"\\begin\{figure\}\[htbp\]\n(.*?)\\end\{figure\}\n?", re.S)
    blocks = list(block.finditer(text))
    graphic_labels = {
        label
        for match in blocks
        if r"\includegraphics" in match.group(1)
        for label in re.findall(r"\\label\{(fig:[^}]+)\}", match.group(1))
    }
    return block.sub(
        lambda m: "" if r"\includegraphics" not in m.group(1)
        and any(label in graphic_labels for label in re.findall(r"\\label\{(fig:[^}]+)\}", m.group(1)))
        else m.group(0),
        text,
    )


def normalize_tables(text: str) -> str:
    # The seven converter tables have a caption immediately before a centered
    # tabular. Turn those blocks into genuine table floats.
    pattern = re.compile(
        r"(?m)^Table\s+(\d+)\.(\d+)\s+([^\n]+)\n\n"
        r"\\begin\{center\}\n(\\begin\{tabular\}.*?\\end\{tabular\})\n\\end\{center\}",
        flags=re.S,
    )

    def table_repl(match: re.Match[str]) -> str:
        chapter, number, title, tabular = match.groups()
        return "\n".join([
            r"\begin{table}[htbp]", r"\centering", tabular,
            rf"\caption{{{title}}}\label{{tab:{chapter}-{number}}}", r"\end{table}",
        ])

    text = pattern.sub(table_repl, text)
    # Caption 3.1 was interleaved with the closing list marker by extraction.
    text = re.sub(
        r"Table~\\ref\{tab:3-1\}\s+([^\n]+)\n\\end\{enumerate\}\n\n"
        r"\\begin\{center\}\n(\\begin\{tabular\}.*?\\end\{tabular\})\n\\end\{center\}",
        lambda m: "\n".join([
            r"\end{enumerate}", r"\begin{table}[htbp]", r"\centering", m.group(2),
            rf"\caption{{{m.group(1)}}}\label{{tab:3-1}}", r"\end{table}",
        ]),
        text,
        flags=re.S,
    )
    text = re.sub(
        r"\bTable\s+(\d+)\.(\d+)",
        lambda m: rf"Table~\ref{{tab:{m.group(1)}-{m.group(2)}}}",
        text,
    )
    return text


def normalize_chapter_references(text: str) -> str:
    # Correct three impossible section numbers introduced by OCR before making
    # them live references.
    text = text.replace("Sect. (4.1.7)", "Sect. 4.3.2")
    text = text.replace("Sect.(4.1.6)", "Sect. 4.3.1")
    text = text.replace("Sect. (4.1.5)", "Sect. 4.3")
    text = re.sub(
        r"\bChap(?:ter)?\.\s*(\d+)|\bChapter\s+(\d+)",
        lambda m: rf"Chapter~\ref{{chap:{m.group(1) or m.group(2)}}}",
        text,
    )
    section_labels = set(re.findall(r"\\label\{sec:([0-9-]+)\}", text))
    text = re.sub(
        r"\bSect(?:ion)?\.?\s*\(?([0-9]+(?:\.[0-9]+)+)\)?",
        lambda m: rf"Section~\ref{{sec:{m.group(1).replace('.', '-')}}}"
        if m.group(1).replace('.', '-') in section_labels else m.group(0),
        text,
    )
    text = re.sub(
        r"\bFigures\s+(\d+)\.(\d+)\s+and\s+(\d+)\.(\d+)",
        lambda m: rf"Figures~\ref{{fig:{m.group(1)}-{m.group(2)}}} and~\ref{{fig:{m.group(3)}-{m.group(4)}}}",
        text,
    )
    return text


def update_preamble(text: str) -> str:
    text = text.replace(r"\documentclass[10pt]{article}", r"\documentclass[10pt]{article}")
    text = text.replace("\\usepackage[utf8]{inputenc}\n", "")
    text = text.replace("\\usepackage[version=4]{mhchem}\n", "")
    text = text.replace("\\usepackage{stmaryrd}\n", "")
    text = text.replace("\\usepackage[fallback]{xeCJK}\n", "")
    text = text.replace("\\setCJKmainfont{Noto Serif CJK JP}\n", "")
    text = text.replace(r"\setmainfont{CMU Serif}", r"\setmainfont{Latin Modern Roman}")
    if r"\numberwithin{equation}{section}" not in text:
        text = text.replace(r"\usepackage{amsmath}", "\\usepackage{amsmath}\n\\numberwithin{equation}{section}")
    text = text.replace(
        r"\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan,}",
        r"\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan, linktoc=all}",
    )
    text = text.replace(r"\graphicspath{ {./images/} }", r"\graphicspath{{./images/}{latex/images/}}")
    text = text.replace(r"\section*{References}", r"\section*{References}\addcontentsline{toc}{section}{References}")
    return text


def restore_missing_chapter_headings(text: str) -> str:
    for number, subsection, title in [
        (6, r"\subsection{System of Particles}\label{sec:6-1}", "System of Particles"),
        (10, r"\subsection{Oscillatory Motion}\label{sec:10-1}", "Oscillatory Motion"),
    ]:
        if rf"\label{{chap:{number}}}" not in text:
            text = text.replace(
                subsection,
                rf"\section{{{title}}}\label{{chap:{number}}}" + "\n" + subsection,
                1,
            )
    return text


def main() -> None:
    text = SOURCE.read_text()
    text = update_preamble(text)
    text = normalize_headings(text)
    text = normalize_equations(text)
    text = number_labeled_math(text)
    text = normalize_figures(text)
    text = repair_orphan_figure_captions(text)
    text = remove_duplicate_caption_only_figures(text)
    text = normalize_tables(text)
    text = normalize_chapter_references(text)
    text = restore_missing_chapter_headings(text)
    SOURCE.write_text(text)


if __name__ == "__main__":
    main()
