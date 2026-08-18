# Principles of Mechanics

This repository contains a MyST Markdown edition of *Principles of
Mechanics: Fundamental University Physics* by Salma Alrasheed. The MyST book
is the primary edition maintained here: its configuration, chapters,
bibliography, and figure assets all live at the repository root.

The original book was published by Springer in 2019 and is available as an
open-access work at
[doi:10.1007/978-3-030-15195-9](https://doi.org/10.1007/978-3-030-15195-9).
This rendition preserves the book's prose, equations, figures, worked
examples, problems, and chapter structure in an accessible web-native format.

## Read and edit the MyST edition

The main entry points are:

- [`myst.yml`](myst.yml) — project metadata and table of contents
- [`index.md`](index.md) — book landing page
- [`chapters/`](chapters/) — the ten converted chapters
- [`images/`](images/) — EPUB-derived chapter figures
- [`references.bib`](references.bib) — bibliography data

The project currently targets MyST CLI 1.10.1. To preview it locally:

```bash
npm install -g mystmd@1.10.1
myst start
```

To produce the static HTML build:

```bash
myst build --html
```

Generated output is written to `_build/` and is not committed.

## Validate the conversion

The repository includes a conversion-specific verifier:

```bash
python3 .opencode/skills/book-to-myst/scripts/verify_book.py . \
  --outline outline.json
```

It checks figure paths, labels, math delimiters, source-count parity, and
known extraction artifacts. A clean contribution should pass both the
verifier and `myst build --html` without content warnings or errors.

## Legacy LaTeX edition

The earlier PDF-derived LaTeX conversion remains available under
[`latex/`](latex/). It is retained as a historical and cross-checking source,
but it is not the canonical edition and may contain extraction or OCR errors.
The EPUB XHTML and equation metadata were treated as authoritative during the
MyST conversion.

## Conversion materials

`outline.json` records the source mapping and expected content counts. Local
EPUB/PDF extracts and page renders live under the ignored `tmp/` and `work/`
directories and are not part of the published book.

## License

© The Author(s) 2019. The book is distributed under the
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
