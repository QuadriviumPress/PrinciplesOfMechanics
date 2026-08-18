---
title: 1. Units and Vectors
short_title: "Ch. 1 — Units and Vectors"
label: ch-1
doi: 10.1007/978-3-030-15195-9_1
---

(sec-1-1)=
## 1.1 Introduction

Physics is an exciting adventure that is concerned with unraveling the secrets of nature based on observations and measurements and also on intuition and imagination. Its beauty lies in having few fundamental principles being able to reach out to incorporate many phenomena from the atomic to the cosmic scale. It is a science that depends heavily on mathematics to prove and express theories and laws and is considered to be the most fundamental of physical sciences. Astronomy, geology, and chemistry all involve applications of physics’ principles and concepts. Physics doesn’t only provide theories, but it also provides techniques that are used in every area of life. Modern physical techniques were the major contributors to the wealth of mankind’s knowledge in the past century.

A simple law in physics can be used to explain a wide range of complex phenomena that may appear to be not related. When studying a complex physical system, a simplified model of the system is usually used, where the minor effects are neglected and the main features of the system are concentrated upon. For example, when dealing with an object falling near the earth’s surface, air resistance can be neglected. In addition, the earth is usually assumed to be spherical and homogeneous. However, in reality, the earth is an ellipsoid and is not homogeneous. The difference between the calculations of these different models can be assumed to be insignificant.

Physics can be divided into two branches namely: classical physics and modern physics. This book focuses on mechanics, which is a branch of classical physics. Other branches of classical physics are: light and optics, sound, electromagnetism, and thermodynamics. Mechanics is the science of motion of objects and is the core of classical physics. On the other hand, modern branches of physics include theories that have been developed during the past twentieth century. Two main theories are the theory of relativity and the theory of quantum mechanics. Modern physics explains many physical phenomena that cannot be explained by classical physics.

(sec-1-2)=
## 1.2 The SI Units

A physical quantity is a quantitative description of a physical phenomenon. For a precise description, one has to measure the physical quantity and represent this measurement by a number. Such a measurement is made by comparing the quantity with a standard; this standard is called a unit. For example, mass is a physical quantity that refers to the quantity of matter contained in an object. The unit kilogram is one of the units used to measure mass and is defined as the mass of a specific platinum–iridium alloy cylinder, kept at the International Bureau of Weights and Measures. Therefore, when we say that a block’s mass is 300 kg, we mean that it is 300 times the mass of the cylindrical platinum–iridium alloy. All units chosen should obey certain properties such as being accurate, accessible, and should remain stable under varied environmental conditions or time.

In 1960, the International System of units (SI) (formally known as the Metric System MKS) was established. The abbreviation is derived from the French phrase “System International”. As shown in Table [](#tbl-1-1), the SI system consists of seven base fundamental units, each representing a quantity assumed to be naturally independent. The system also includes two supplementary units, the radian which is a unit of the plane angle, and the steradian which is a unit of the solid angle. All other quantities in physics are derived from these base quantities. For example, mechanical quantities such as force, velocity, volume, and energy can be derived from the fundamental quantities length, mass, and time. Furthermore, the powers of ten are used to represent the larger and smaller values for a certain physical quantity as listed in Table [](#tbl-1-2). The most recent definitions of the units of length, mass, and time in the SI system are as follows:

- The Meter: The distance that light travels in vacuum during a time of 1/299792458 s.
- The Kilogram: The mass of a specific platinum–iridium alloy cylinder, which is kept at the International Bureau of Weights and Measures.
- The Second: 9192631770 periods of the radiation from cesium-133 atoms.

(tbl-1-1)=
**Table 1.1** The SI system consists of seven base fundamental units, each representing a quantity assumed to be naturally independent

| Quantity | Unit name | Unit symbol |
| --- | --- | --- |
| Length | Meter | m |
| Mass | Kilogram | kg |
| Time | Second | s |
| Temperature | Kelvin | K |
| Electric Current | Ampere | A |
| Luminous Intensity | Candela | cd |
| Amount of Substance | mole | mol |

(tbl-1-2)=
**Table 1.2** Prefixes for Powers of Ten

| Factor | Prefix | Symbol |
| --- | --- | --- |
| $10^{-24}$ | yocto | y |
| $10^{-21}$ | zepto | z |
| $10^{-18}$ | atto | a |
| $10^{-15}$ | femto | f |
| $10^{-12}$ | pico | p |
| $10^{-9}$ | nano | n |
| $10^{-6}$ | micro | $\mu$ |
| $10^{-3}$ | milli | m |
| $10^{-2}$ | centi | c |
| $10^{-1}$ | deci | d |
| $10^{1}$ | deka | da |
| $10^{2}$ | hecto | h |
| $10^{3}$ | kilo | k |
| $10^{6}$ | mega | M |
| $10^{9}$ | giga | G |
| $10^{12}$ | tera | T |
| $10^{15}$ | peta | P |
| $10^{18}$ | exa | E |
| $10^{21}$ | zetta | Z |

(sec-1-3)=
## 1.3 Conversion Factors

There are two other major systems of units besides the SI units. The (CGS) system of units which uses the centimeter, gram and second as its base units, and the (FPS) system of units which uses the foot, pound, and second as its base units. The conversion factors between the SI units and other systems of units of length, mass, and time are

- $1\,\mathrm{m}=39.37\,\mathrm{in}=3.281\,\mathrm{ft}=6.214\times 10^{-4}\,\mathrm{mi}$
- $1\,\mathrm{kg}=10^{3}\,\mathrm{g}=0.0685$ slug $=6.02\times 10^{26}\,\mathrm{u}$
- $1\,\mathrm{s}=1.667\times 10^{-2}\,\min =2.778\times 10^{-4}\,\mathrm{h}=3.169\times 10^{-8}\,\mathrm{yr}$

````{prf:example}
:label: example-1-1
:enumerator: 1.1

If a tree is measured to be 10 m long, what is its length in inches and in feet?

:::{admonition} Solution 1.1
:class: dropdown

```{math}
10\,\mathrm{m}=(10\,\mathrm{m})\bigg(\frac{39.37\,\mathrm{in}}{1\,\mathrm{m}}\bigg)=393.7\,\mathrm{in}
```

```{math}
10\,\mathrm{m}=(10\,\mathrm{m})\bigg(\frac{3.281\,\mathrm{ft}}{1\,\mathrm{m}}\bigg)=32.81\,\mathrm{ft}
```

:::
````

````{prf:example}
:label: example-1-2
:enumerator: 1.2

If a volume of a room is $32\,\mathrm{m}^{3}$, what is the volume in cubic inches?

:::{admonition} Solution 1.2
:class: dropdown

```{math}
32\,\mathrm{m}^{3}=(32\,\mathrm{m}^{3})\bigg(\frac{39.37\,\mathrm{in}}{1\,\mathrm{m}}\bigg)^{3}=1.95\times 10^{6}\,\mathrm{in}^{3}
```

:::
````

(sec-1-4)=
## 1.4 Dimension Analysis

The symbols used to specify the dimensions of length, mass, and time are $\mathrm{L}, \mathrm{M}$ and $\mathrm{T}$, respectively. Dimension analysis is a method used to check the validity of an equation and to derive correct expressions. Only the same dimensions can be added or subtracted, i.e., they obey the rules of algebra. To check the validity of an equation, the terms on both sides must have the same dimension. The dimension of a physical quantity is denoted using brackets [ ]. For example, the dimension of the volume is $[V]=\mathrm{L}^{3}$, and that of acceleration is $[\mathrm{a}]=\mathrm{L}/\mathrm{T}^{3}$

````{prf:example}
:label: example-1-3
:enumerator: 1.3

Show that the expression $\mathrm{v}^{2}=2ax$ is dimensionally consistent, where $\mathrm{v}$ represents the speed, *x* represent the displacement, and $\mathrm{a}$ represents the acceleration of the object.

:::{admonition} Solution 1.3
:class: dropdown

```{math}
[\mathrm{v}^{2}]=\mathrm{L}^{2}/\mathrm{T}^{2}
```

```{math}
\,[xa]=(\mathrm{L}/\mathrm{T}^{2})(\mathrm{L})=\mathrm{L}^{2}/\mathrm{T}^{2}
```

Each term in the equation has the same dimension and therefore it is dimensionally correct.

:::
````

```{figure} ../images/ch-01/459974_1_En_1_Fig1_HTML.png
:name: fig-1-1

A vector is represented geometrically by an arrow PQ drawn to scale
```

(sec-1-5)=
## 1.5 Vectors

When exploring physical quantities in nature, it is found that some quantities can be completely described by giving a number along with its unit, such as the mass of an object or the time between two events. These quantities are called scalar quantities. It is also found that other quantities are fully described by giving a number along with its unit in addition to a specified direction, such as the force on an object. These quantities are called vector quantities.

Scalar quantities have magnitude but don’t have a direction and obey the rules of ordinary arithmetic. Some examples are mass, volume, temperature, energy, pressure, and time intervals by a letter such as *m*, *t*, *E* $\ldots$, etc. Vector quantities have both magnitude and direction and obey the rules of vector algebra. Examples are displacement, force, velocity, and acceleration. Analytically, a vector is specified by a bold face letter such as $\mathbf{A}$. This notation (as used in this book) is usually used in printed material. In handwriting, the designation $\overrightarrow{A}$ is used. The magnitude of $\mathbf{A}$ is written as $|\mathbf{A}|$ or *A* in print or as $|\overrightarrow{A}|$ in handwriting.

A vector is represented geometrically by an arrow PQ drawn to scale as shown in [](#fig-1-1). The length and direction of the arrow represent the magnitude and direction of the vector, respectively, and is independent of the choice of coordinate system. The point $\mathrm{P}$ is called the initial point (tail of *A*) and $\mathrm{Q}$ is called the terminal point (head of *A*).

(sec-1-6)=
## 1.6 Vector Algebra

In this section, we will discuss how mathematical operations are applied to vectors.

### 1.6.1 Equality of Two Vectors

The two vectors $\mathbf{A}$ and $\mathbf{B}$ are said to be equal $(\mathbf{A}=\mathbf{B})$ only if they have the same magnitude and direction, whether or not their initial points are the same as shown in [](#fig-1-2).

```{figure} ../images/ch-01/459974_1_En_1_Fig2_HTML.png
:name: fig-1-2

The two vectors $\mathbf{A}$ and $\mathbf{B}$ are said to be equal ($\mathbf{A}$ = $\mathbf{B}$) only if they have the same magnitude and direction
```

### 1.6.2 Addition

There are two ways to add vectors, geometrically and algebraically. Here, we will discuss the geometric method which is useful for solving problems without using a coordinate system. The algebraic method will be discussed later. To add two vectors $\mathbf{A}$ and $\mathbf{B}$ using the geometric method, place the head of $\mathbf{A}$ at the tail of $\mathbf{B}$ and draw a vector from the tail of $\mathbf{A}$ to the head of $\mathbf{B}$ as shown in [](#fig-1-3). This method is known as the triangle method. An extension to sum up more than two vectors is shown in [](#fig-1-4). An alternative procedure of vector addition using the geometric method is shown in [](#fig-1-5). This is known as the parallelogram method, where $\mathbf{C}$ is the diagonal of a parallelogram with sides A and B. To find $\mathbf{C}$ analytically, [](#fig-1-6) shows that

```{math}
:label: eq-1-1
(DG)^{2}=(DF)^{2}+(FG)^{2}
```

and that

```{math}
DF=DE+EF=A+B\cos \theta ,
```

Thus, Eq. [](#eq-1-1) becomes

```{math}
C^{2}=(A+B\cos \theta )^{2}+(B\sin \theta )^{2}=A^{2}+B^{2}+2AB\cos \theta ,
```

```{figure} ../images/ch-01/459974_1_En_1_Fig3_HTML.png
:name: fig-1-3

To add two vectors $\mathbf{A}$ and $\mathbf{B}$ using the geometric method, place the head of $\mathbf{A}$ at the tail of $\mathbf{B}$ and draw a vector from the tail of $\mathbf{A}$ to the head of $\mathbf{B}$
```

```{figure} ../images/ch-01/459974_1_En_1_Fig4_HTML.png
:name: fig-1-4

Geometric method for summing more than two vectors
```

```{figure} ../images/ch-01/459974_1_En_1_Fig5_HTML.png
:name: fig-1-5

The parallelogram method of adding two vectors
```

```{figure} ../images/ch-01/459974_1_En_1_Fig6_HTML.png
:name: fig-1-6

Finding the magnitude and the direction of $\mathbf{C}$
```

```{figure} ../images/ch-01/459974_1_En_1_Fig7_HTML.png
:name: fig-1-7

The total displacement of the jogger is the vector $\mathbf{R}$
```

or

```{math}
C=\sqrt{A^{2}+B^{2}+2AB\cos \theta },
```

The direction of $\mathbf{C}$ is

```{math}
\tan \beta =\frac{GF}{DF}=\frac{GF}{DE+EF}=\frac{B\sin \theta }{A+B\cos \theta },
```

Note that only when $\mathbf{A}$ and $\mathbf{B}$ are parallel, the magnitude of the resultant vector $\mathbf{C}$ is equal to $A+B$ (unlike the addition of scalar quantities, the magnitude of the resultant vector $\mathbf{C}$ is not necessarily equal to $A+B$).

````{prf:example}
:label: example-1-4
:enumerator: 1.4

A jogger runs from her home a distance of 0.5 km due south and then 1 km to the west. Find the magnitude and direction of her resultant displacement.

:::{admonition} Solution 1.4
:class: dropdown

From [](#fig-1-7), we can see that the magnitude of the resultant displacement is given by

```{math}
R=\sqrt{(0.5\,\mathrm{km})^{2}+(1\,\mathrm{km})^{2}}=1.1\,\mathrm{m}
```

The direction of $\mathrm{R}$ is

```{math}
\theta =\tan ^{-1}\frac{(0.5\,\mathrm{m})}{(1\,\mathrm{m})}=26.6^{\circ}
```

south of west.

:::
````

### 1.6.3 Negative of a Vector

The negative vector of $\mathbf{A}$ is a vector of the same magnitude of $\mathbf{A}$ but in the opposite direction as shown in [](#fig-1-8), and it is denoted by $-\mathbf{A}$.

```{figure} ../images/ch-01/459974_1_En_1_Fig8_HTML.png
:name: fig-1-8

The negative vector of $\mathbf{A}$ is a vector of the same magnitude of $\mathbf{A}$ but in the opposite direction
```

### 1.6.4 The Zero Vector

The zero vector is a vector of zero magnitude and has no defined direction. It may result from $\mathbf{A}=\mathbf{B}-\mathbf{B}=\mathbf{0}$ or from $\mathbf{A}=c\mathbf{B}=0$ if $c=0.$

### 1.6.5 Subtraction of Vectors

The vector $\mathbf{A}-\mathbf{B}$ is defined as the vector that when added to $\mathbf{B}$ gives us $\mathbf{A}$. Equivalently, $\mathbf{A}-\mathbf{B}$ can be defined as the vector $\mathbf{A}$ added to vector $-\mathbf{B}$ $(\mathbf{A}+(-\mathbf{B}))$ as shown in [](#fig-1-9).

```{figure} ../images/ch-01/459974_1_En_1_Fig9_HTML.png
:name: fig-1-9

Subtraction of two vectors
```

### 1.6.6 Multiplication of a Vector by a Scalar

The product of a vector $\mathbf{A}$ by a scalar *q* is a vector $q\mathbf{A}$ or $\mathbf{A}q$. Its magnitude is *qA* and its direction is the same as $\mathbf{A}$ if *q* is positive and opposite to $\mathbf{A}$ if *q* is negative, as shown in [](#fig-1-10).

```{figure} ../images/ch-01/459974_1_En_1_Fig10_HTML.png
:name: fig-1-10

The product of a vector by a scalar
```

```{figure} ../images/ch-01/459974_1_En_1_Fig11_HTML.png
:name: fig-1-11

Commutative law of addition
```

```{figure} ../images/ch-01/459974_1_En_1_Fig12_HTML.png
:name: fig-1-12

Associative law of addition
```

### 1.6.7 Some Properties

- $\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A}$ (Commutative law of addition). This can be seen in [](#fig-1-11).
- $(\mathbf{A}+\mathbf{B})+\mathbf{C}=\mathbf{A}+(\mathbf{B}+\mathbf{C}),\;$ as seen from [](#fig-1-12) (Associative law of addition).
- $\mathbf{A}+\mathbf{0}=\mathbf{A}$
- $\mathbf{A}+(-\mathbf{A})=\mathbf{0}$
- $p(q\mathbf{A})=(pq)\mathbf{A}=q(p\mathbf{A})\;$ (where *p* and *q* are scalars) (Associative law for multiplication).
- $(p+q)\mathbf{A}=p\mathbf{A}+q\mathbf{A} \;$ (Distributive law).
- $p(\mathbf{A}+\mathbf{B})=p\mathbf{A}+p\mathbf{B} \;$ (Distributive law).
- $1\mathbf{A}=\mathbf{A}, \; 0\mathbf{A}=\mathbf{0}$ (Here, the zero vector has the same direction as $\mathbf{A}$, i.e., it can have any direction), $\; q\mathbf{0}=\mathbf{0}$

### 1.6.8 The Unit Vector

The unit vector is a vector of magnitude equal to 1, and with the same direction of $\mathbf{A}$. For every $\mathbf{A}\ne 0, \mathbf{a}=\mathbf{A}/|\mathbf{A}|$ is a unit vector.

### 1.6.9 The Scalar (Dot) Product

The scalar product is a scalar quantity defined as $\mathbf{A}\cdot \mathbf{B}=AB\cos \theta$, where $\theta$ is the smaller angle between $\mathbf{A}$ and $\mathbf{B}$ $(0\le \theta \le \pi )$ (see [](#fig-1-13)).

```{figure} ../images/ch-01/459974_1_En_1_Fig13_HTML.png
:name: fig-1-13

The scalar product of two vectors
```

#### Some Properties of the Scalar Product

- $\mathbf{A}\cdot \mathbf{B}=\mathbf{B}\cdot \mathbf{A}$ (Commutative law of scalar product).
- $\mathbf{A}\cdot (\mathbf{B}+\mathbf{C})=\mathbf{A}\cdot \mathbf{B}+\mathbf{A}\cdot \mathbf{C}$ (Distributive law).
- $m(\mathbf{A}\cdot \mathbf{B})=(m\mathbf{A})\cdot \mathbf{B}=\mathbf{A}\cdot (m\mathbf{B})=(\mathbf{A}\cdot \mathbf{B})m$, where *m* is a scalar.

### 1.6.10 The Vector (Cross) Product

The vector product is a vector quantity defined as $\mathbf{C}=\mathbf{A}\times \mathbf{B}$ (read A cross B) with magnitude equal to $|\mathbf{A}\times \mathbf{B}|=AB\sin \theta , (0\le \theta \le \pi )$. The direction of $\mathbf{C}$ is found from the right-hand rule or of advance of a right-handed screw rotated from $\mathbf{A}$ to $\mathbf{B}$ as shown in [](#fig-1-14). $\mathbf{C}$ is perpendicular to the plane formed by $\mathbf{A}$ and $\mathbf{B}$.

```{figure} ../images/ch-01/459974_1_En_1_Fig14_HTML.png
:name: fig-1-14

The vector product of two vectors
```

#### Some Properties

- $\mathbf{A}\cdot \mathbf{A}=A^{2}, \mathbf{0}\cdot \mathbf{A}=0$
- $\mathbf{A}\times \mathbf{B}=-\mathbf{B}\times \mathbf{A}$
- $\mathbf{A}\times (\mathbf{B}+\mathbf{C})=\mathbf{A}\times \mathbf{B}+\mathbf{A}\times \mathbf{C}$ (Distributive law).
- $(\mathbf{A}+\mathbf{B})\times \mathbf{C}=\mathbf{A}\times \mathbf{C}+\mathbf{B}\times \mathbf{C}$
- $q(\mathbf{A}\times \mathbf{B})=(q\mathbf{A})\times \mathbf{B}=\mathbf{A}\times (q\mathbf{B})=(\mathbf{A}\times \mathbf{B})q$, where *q* is a scalar.
- $|\mathbf{A}\times \mathbf{B}|=$ The area of a parallelogram that has sides A and $\mathrm{B}$ as shown in [](#fig-1-15).

```{figure} ../images/ch-01/459974_1_En_1_Fig15_HTML.png
:name: fig-1-15

The magnitude of the vector product $|\mathbf{A}\times \mathbf{B}|$ is the area of a parallelogram with sides $A$ and $B$
```

(sec-1-7)=
## 1.7 Coordinate Systems

To specify the location of a point in space, a coordinate system must be used. A coordinate system consists of a reference point called the origin $\mathrm{O}$ and a set of labeled axes. The positive direction of an axis is in the direction of increasing numbers, whereas the negative direction is opposite. Figures [](#fig-1-16) and [](#fig-1-17) show the rectangular (or Cartesian) coordinate system and the polar coordinates of a point, respectively The rectangular coordinates *x* and *y* are related to the polar coordinates *r* and $\theta$ by the following relations:

```{math}
x=r\cos \theta
```

```{math}
y=r\sin \theta
```

```{math}
\tan \theta =y/x
```

```{math}
r=\sqrt{x^{2}+y^{2}}
```

In three dimensions, the cartesian coordinate system is shown in [](#fig-1-18). Other used coordinate systems in three dimensions are the spherical and cylindrical coordinates ([](#fig-1-19) and [](#fig-1-20)).

```{figure} ../images/ch-01/459974_1_En_1_Fig16_HTML.png
:name: fig-1-16

The rectangular (cartesian) coordinate system
```

```{figure} ../images/ch-01/459974_1_En_1_Fig17_HTML.png
:name: fig-1-17

The polar coordinate system
```

```{figure} ../images/ch-01/459974_1_En_1_Fig18_HTML.png
:name: fig-1-18

The cartesian coordinate system in three dimensions
```

```{figure} ../images/ch-01/459974_1_En_1_Fig19_HTML.png
:name: fig-1-19

The spherical coordinate system
```

```{figure} ../images/ch-01/459974_1_En_1_Fig20_HTML.png
:name: fig-1-20

The cylindrical coordinate system
```

(sec-1-8)=
## 1.8 Vectors in Terms of Components

In two dimensions, the vector $\mathbf{A}$ can be expressed as the sum of two other vectors $\mathbf{A}=\mathbf{A}_{x}+\mathbf{A}_{y}$, where $A_{x}=A\cos \theta$ and $A_{y}=A\sin \theta$ as shown in [](#fig-1-21).

```{figure} ../images/ch-01/459974_1_En_1_Fig21_HTML.png
:name: fig-1-21

In two dimensions, the vector $\mathbf{A}$ can be expressed as the sum of two other vectors $\mathbf{A}=\mathbf{A}_{x}+\mathbf{A}_{y}$, where $A_{x}=A\cos \theta$ and $A_{y}=A\sin \theta$
```

$\mathbf{A}_{x}$ and $\mathbf{A}_{y}$ are called the rectangular components, or simply components of $\mathbf{A}$ in the $\mathrm{x}$ and $\mathrm{y}$ directions respectively The magnitude and direction of $\mathbf{A}$ are related to its components through the expressions:

```{math}
A=\sqrt{A_{x}^{2}+A_{y}^{2}}
```

```{math}
\tan \theta =A_{y}/A_{x}
```

In three dimensions (see [](#fig-1-22)), the magnitude of A is given by

```{math}
A=\sqrt{A_{x}^{2}+A_{y}^{2}+A_{z}^{2}}
```

with directions given by

```{math}
\cos \alpha =A_{x}/A,\ \cos \beta =A_{y}/A,\ \cos \gamma =A_{z}/A
```

```{figure} ../images/ch-01/459974_1_En_1_Fig22_HTML.png
:name: fig-1-22

In three dimensions the magnitude of A is $A=\sqrt{A_{x}^{2}+A_{y}^{2}+A_{z}^{2}}$
```

### 1.8.1 Rectangular Unit Vectors

The rectangular unit vectors $\mathbf{i}, \mathbf{j}$, and $\mathbf{k}$ are unit vectors defined to be in the direction of the positive $\mathrm{x}$-, $\mathrm{y}$-, and $\mathrm{z}$-axes, respectively, of the rectangular coordinate system as shown in [](#fig-1-23). Note that labeling the axes in this way forms a right-handed system. This name derives from the fact that a right- handed screw rotated through $90^{\circ}$ from the $\mathrm{x}$-axis into the $\mathrm{y}$-axis will advance in the positive $\mathrm{z}$-direction. (Note that throughout this book the right-handed coordinate system is used). In terms of unit vectors, vector A can be written as

```{math}
\mathbf{A}=A_{x}\mathbf{i}+A_{y}\mathbf{j}+A_{z}\mathbf{k}
```

```{figure} ../images/ch-01/459974_1_En_1_Fig23_HTML.png
:name: fig-1-23

The rectangular unit vectors $\mathbf{i}, \mathbf{j}$ and $\mathbf{k}$ are unit vectors defined to be in the direction of the positive $\mathrm{x}, \mathrm{y}$, and $\mathrm{z}$ axes respectively
```

### 1.8.2 Component Method

Suppose we have $\mathbf{A}=A_{x}\mathbf{i}+A_{y}\mathbf{j}$ and $\mathbf{B}=B_{x}\mathbf{i}+B_{y}\mathbf{j}$

#### Addition

The resultant vector $\mathbf{C}$ is given by

```{math}
\mathbf{C}=\mathbf{A}+\mathbf{B}=(A_{x}+B_{x})\mathbf{i}+(A_{y}+B_{y})\mathbf{j}=C_{x}\mathbf{i}+C_{y}\mathbf{j}
```

```{math}
C_{x}=A_{x}+B_{x}
```

```{math}
C_{y}=A_{y}+B_{y}
```

Thus, the magnitude of $\mathbf{C}$ is

```{math}
C=\sqrt{C_{x}^{2}+C_{y}^{2}}
```

with a direction

```{math}
\tan \theta =\frac{C_{y}}{C_{x}}=\frac{A_{y}+B_{y}}{A_{x}+B_{x}}
```

in three dimensions

```{math}
\mathbf{C}=(A_{x}+B_{x})\mathbf{i}+(A_{y}+B_{y})\mathbf{j}=(A_{z}+B_{z})\mathbf{k}=C_{x}\mathbf{i}+C_{y}\mathbf{j}+C_{z}\mathbf{k}
```

the magnitude of $\mathbf{C}$ is

```{math}
C=\sqrt{C_{x}^{2}+C_{y}^{2}+C_{z}^{2}}
```

And the directions are

```{math}
\cos \alpha =C_{x}/C, \; \cos \beta =C_{y}/C, \; \cos \gamma =C_{z}/C
```

This component method is easy to use in adding any number of vectors.

````{prf:example}
:label: example-1-5
:enumerator: 1.5

A truck travels northwest a distance of 30 km, and then 50 km at $30^{\circ}$ north of east, and finally travels a distance of 20 km due south. Determine both graphically and analytically the magnitude and direction of the resultant displacement of the truck from its starting point.

```{figure} ../images/ch-01/459974_1_En_1_Fig24_HTML.png
:name: fig-1-24

The displacements are drawn to scale with the head of $\mathbf{A}$ placed at the tail of $\mathbf{B}$ and the head of $\mathbf{B}$ placed at the tail of $\mathbf{C}$.The resultant vector $\mathbf{R}$ is the vector that extends from the tail of $\mathbf{A}$ to the head of $\mathbf{C}$
```

:::{admonition} Solution 1.5
:class: dropdown

Graphically, in [](#fig-1-24) the displacements are drawn to scale with the head of $\mathbf{A}$ placed at the tail of $\mathbf{B}$ and the head of $\mathbf{B}$ placed at the tail of $\mathbf{C}$.The resultant vector $\mathbf{R}$ is the vector that extends from the tail of $\mathbf{A}$ to the head of $\mathbf{C}$. By using graph paper and a protractor, the magnitude of $\mathbf{R}$ is measured to have the value of 34.8 km and a direction of $49.8^{\circ}$ from the positive $\mathrm{x}$ axis. Analytically, from [](#fig-1-24), we have

```{math}
A_{x}=A\cos 135^{\circ}=(30\,\mathrm{km})(-0.707)=-21.2\,\mathrm{km}
```

```{math}
A_{y}=A \sin 135^{\circ} =(30\,\mathrm{km})(0.707)=21.2\,\mathrm{km}
```

```{math}
B_{x}=B\cos 30^{\circ}=(50\,\mathrm{km}) (0.866)=43.3\,\mathrm{km}
```

```{math}
B_{y}=B\sin 30^{\circ}=(50\,\mathrm{km} ) (0.5)=25\,\mathrm{km}
```

```{math}
C_{x}=C\cos 270^{\circ}=(20\,\mathrm{km} ) (0) =0
```

```{math}
C_{y}=C\sin 270^{\circ}=(20\,\mathrm{km}) (-1)=-20\,\mathrm{km}
```

```{math}
{\mathbf{R}}={\mathbf{A}}+{\mathbf{B}}+{\mathbf{C}}=(A_{x}+B_{x}+C_{x})\mathbf{i}+(A_{y}+B_{y}+C_{y})\mathbf{j}+(A_{z}+B_{z}+C_{z})\mathbf{k}=22.1\mathbf{i}+26.2\mathbf{j}
```

Thus, the magnitude of $\mathbf{R}$ is given by

```{math}
R=\sqrt{R_{x}^{2}+R_{y}^{2}}=\sqrt{(221\,\mathrm{km})^{2}+(262\,\mathrm{km})^{2}}=34.3\,\mathrm{km}
```

and its direction is

```{math}
\theta =\tan ^{-1}\bigg (\frac{26.2\,\mathrm{km}}{22.1\,\mathrm{km}}\bigg )=49.9^{\circ}
```

north of east.

:::
````

#### Subtraction

```{math}
{\mathbf{C}}={\mathbf{A}}-{\mathbf{B}}=(A_{x}-B_{x})\mathbf{i}+(A_{y}-B_{y})\mathbf{j}+(A_{z}-B_{z})\mathbf{k}
```

The magnitude and direction of $\mathbf{C}$ are as in the case of addition except that the plus sign is replaced by the minus sign.

#### Scalar Product

```{math}
\mathbf{A}\cdot \mathbf{B}=(A_{x}\mathbf{i}+A_{y}\mathbf{j}+A_{z}\mathbf{k})\cdot (B_{x}\mathbf{i}+B_{y}\mathbf{j}+B_{z}\mathbf{k})
```

Using the definition of scalar product and by applying the distributive law we get nine terms: since $\mathbf{i}\cdot \mathbf{i}=\mathbf{j}\cdot \mathbf{j}=\mathbf{k}\cdot \mathbf{k}$ and $\mathbf{i}\cdot \mathbf{j}=\mathbf{j}\cdot \mathbf{k}=\mathbf{j}\cdot \mathbf{k}=0$, we get

```{math}
\mathbf{A}\cdot \mathbf{B}=A_{x}B_{x}+A_{y}B_{y}+A_{z}B_{z}
```

The dot product of any vector (for example $\mathbf{A}$) by itself is

```{math}
\mathbf{A}\cdot \mathbf{A}=A^{2}=A_{x}^{2}+A_{y}^{2}+A_{z}^{2}
```

#### The Angle Between Two Vectors

```{math}
\mathbf{A}\cdot \mathbf{B}=AB\cos \theta =A_{x}B_{x}+A_{y}B_{y}+A_{z}B_{z}
```

```{math}
\cos \theta =\frac{A_{x}B_{x}+A_{y}B_{y}+A_{z}B_{z}}{AB}
```

````{prf:example}
:label: example-1-6
:enumerator: 1.6

Two vectors $\mathbf{A}$ and $\mathrm{B}$ are given by $\mathbf{A}=\mathbf{i}+5\mathbf{j}-7\mathbf{k}$ and $\mathbf{B}=6\mathbf{i}-2\mathbf{j}+3\mathbf{k}$. Find the angle between them.

:::{admonition} Solution 1.6
:class: dropdown

```{math}
\mathbf{A}\cdot \mathbf{B}=AB\cos \phi =A_{x}B_{x}+A_{y}B_{y}+A_{z}B_{z}
```

```{math}
A=\sqrt{A_{x}^{2}+A_{y}^{2}+A_{z}^{2}}=\sqrt{1+25+49}=8.7
```

```{math}
B=\sqrt{B_{x}^{2}+B_{y}^{2}+B_{z}^{2}}=\sqrt{36+4+9}=7
```

```{math}
\cos \phi =\frac{A_{x}B_{x}+A_{y}B_{y}+A_{z}B_{z}}{AB}=\frac{6-10-21}{(8.7)(7)}=-0.4
```

```{math}
\phi =113.6^{\circ}
```

:::
````

#### Perpendicular and Parallel Vectors

Nonzero vectors $\mathbf{A}$ and $\mathbf{B}$ are perpendicular if $\mathbf{A}\cdot \mathbf{B}=0$ or $A_{x}B_{x}+A_{y}B_{y}+ A_{z}B_{z}=0$ and they are parallel if $\mathbf{A}\times \mathbf{B}=\mathbf{0}$. For any two parallel vectors $\mathbf{A}$ and $\mathbf{B}$, we have $\mathbf{A}=q\mathbf{B}$, where they have the same direction if $q>0$, and are in opposite direction if $q<0$. Also we can write

```{math}
\frac{\mathbf{A}}{\mathbf{B}}=q
```

or

```{math}
\frac{A_{x}}{B_{x}}=\frac{A_{y}}{B_{y}}=\frac{A_{z}}{B_{z}}
```

```{figure} ../images/ch-01/459974_1_En_1_Fig25_HTML.png
:name: fig-1-25

If we write the unit vectors around a circle, then reading counter clockwise gives the positive products and reading clockwise gives the negative products
```

#### Vector Product

From the vector product definition, we can see that

```{math}
\mathbf{i}\times \mathbf{i}=\mathbf{j}\times \mathbf{j}=\mathbf{k}\times \mathbf{k}=\mathbf{0}
```

```{math}
\mathbf{i}\times \mathbf{j}=\mathbf{k},\mathbf{j}\times \mathbf{k}=\mathbf{i},\ \mathbf{k}\times \mathbf{i}=\mathbf{j}
```

```{math}
\mathbf{j}\times \mathbf{i}=-\mathbf{k},\ \mathbf{k}\times \mathbf{j}=-\mathbf{i},\ \mathbf{i}\times \mathbf{k}=-\mathbf{j}
```

If we write the unit vectors around a circle as shown in [](#fig-1-25), then reading counterclockwise gives the positive products and reading clockwise gives the negative products. Note that these results are for a right-handed coordinate system. We have

```{math}
\mathbf{A}\times \mathbf{B}=(A_{x}\mathbf{i}+A_{y}\mathbf{j}+A_{z}\mathbf{k})\times (B_{x}\mathbf{i}+B_{y}\mathbf{j}+B_{z}\mathbf{k})
```

using the distributive law and the above relations of unit vectors we get

```{math}
\mathbf{A}\times \mathbf{B}=(A_{y}B_{z}-A_{z}B_{y})\mathbf{i}+(A_{z}B_{x}-A_{x}B_{z})\mathbf{j}+(A_{x}B_{y}-A_{y}B_{x})\mathbf{k}
```

since a determinant of order 2 is defined as

```{math}
\left| \begin{array}{ll} a_{1} & a_{2}\\ b_{1} & b_{2} \end{array}\right| =a_{1}b_{2}-a_{2}b_{1}
```

Then, the above expression can be written as

```{math}
\mathbf{A}\times \mathbf{B}=\left| \begin{array}{ll} A_{y} & A_{z}\\ B_{y} & B_{z} \end{array}\right| \mathbf{i}-\left| \begin{array}{ll} A_{x} & A_{z}\\ B_{x} & B_{z} \end{array}\right| \mathbf{j}+\left| \begin{array}{ll} A_{x} & A_{y}\\ B_{x} & B_{y} \end{array}\right| \mathbf{k}
```

A determinant of order 3 is

```{math}
\left| \begin{array}{lll} c_{1} & c_{2} & c_{3}\\ a_{1} & a_{2} & a_{3}\\ b_{1} & b_{2} & b_{3} \end{array}\right| =\left| \begin{array}{ll} a_{2} & a_{3}\\ b_{2} & b_{3} \end{array}\right| c_{1}-\left| \begin{array}{ll} a_{1} & a_{3}\\ b_{1} & b_{3} \end{array}\right| c_{2}+\left| \begin{array}{ll} a_{1} & a_{2}\\ b_{1} & b_{2} \end{array}\right| c_{3}
```

Hence, the cross product can be expressed as

```{math}
\mathbf{A}\times \mathbf{B}=\left| \begin{array}{lll} \mathbf{i} & \mathbf{j} & \mathbf{k}\\ A_{x} & A_{y} & A_{z}\\ B_{x} & B_{y} & B_{z} \end{array}\right| =(A_{y}B_{z}-A_{z}B_{y})\mathbf{i}+(A_{z}B_{x}-A_{x}B_{z})\mathbf{j}+(A_{x}B_{y}-A_{y}B_{x})\mathbf{k}
```

Note that this is not a determinant since the elements in the first row are vectors and not scalars, but it is a convenient way to represent the cross product.

````{prf:example}
:label: example-1-7
:enumerator: 1.7

Two vectors $\mathbf{A}$ and $\mathbf{B}$ are given by $\mathbf{A}=-\mathbf{i}+3\mathbf{j}$ and $\mathbf{B}=2\mathbf{i}+\mathbf{j}$. Find: (a) the sum of $\mathbf{A}$ and $\mathbf{B}$, (b) $-\mathbf{B}$ and $3\mathbf{A}$, (c) $\mathbf{A}\cdot \mathbf{B}$ and $\mathbf{A}\times \mathbf{B}$.

:::{admonition} Solution 1.7
:class: dropdown

(a)

```{math}
\mathbf{R}=\mathbf{A}+\mathbf{B}=(A_{x}+B_{x})\mathbf{i}+(A_{y}+B_{y})\mathbf{j}=(-1+2)\mathbf{i}+(3+1)\mathbf{j}=\mathbf{i}+4\mathbf{j}
```

```{math}
R_{x}=1
```

```{math}
R_{y}=4
```

(b)

```{math}
-\mathbf{B}=-2\mathbf{i}-\mathbf{j}
```

```{math}
3\mathbf{A}=-3\mathbf{i}+9\mathbf{j}
```

(c)

$\mathbf{A}\cdot \mathbf{B}=(-\mathbf{i}+3\mathbf{j})(2\mathbf{i}+\mathbf{j})=-\mathbf{i}\cdot 2\mathbf{i}-\mathbf{i}\cdot \mathbf{j}+3\mathbf{j}\cdot 2\mathbf{i}+3\mathbf{j}\cdot \mathbf{j}=-2+3=1$

```{math}
\mathbf{A}\times \mathbf{B}=(-\mathbf{i}+3\mathbf{j})\times (2\mathbf{i}+\mathbf{j})=-\mathbf{i}\times \mathbf{j}+3\mathbf{j}\times 2\mathbf{i}=-\mathbf{k}-6\mathbf{k}=-7\mathbf{k}
```

:::
````

````{prf:example}
:label: example-1-8
:enumerator: 1.8

Find a vector of magnitude 1 that is perpendicular to each of the vectors $\mathbf{A}= 5\mathbf{i}+\mathbf{j}-3\mathbf{k}$ and $\mathbf{B}=3\mathbf{i}+7\mathbf{j}-2\mathbf{k}$.

:::{admonition} Solution 1.8
:class: dropdown

By the definition of the unit vector, we have

```{math}
\mathbf{c}=\frac{\mathbf{A}\times \mathbf{B}}{|\mathbf{A}\times \mathbf{B}|}
```

where $\mathrm{c}$ is a unit vector perpendicular to the plane formed by A and B. We have

```{math}
\mathbf{A}\times \mathbf{B}=\left| \begin{array}{lll} \mathbf{i} & \quad \mathbf{j} & \quad \mathbf{k}\\ 5 & \quad 1 & \quad -3 \\ 3 & \quad 7 & \quad -2 \end{array}\right| =19\mathbf{i}+\mathbf{j}+32\mathbf{k}
```

```{math}
|\mathbf{A}\times \mathbf{B}|=\sqrt{(19)^{2}+(1)^{2}+(32)^{2}}=37.23
```

```{math}
\mathbf{C}=\frac{19\mathbf{i}+\mathbf{j}+32\mathbf{k}}{37.23}=0.5\mathbf{i}+0.027\mathbf{j}+0.86\mathbf{k}
```

:::
````

````{prf:example}
:label: example-1-9
:enumerator: 1.9

Given that $\mathbf{A}=2\mathbf{i}-3\mathbf{j}-\mathbf{k}, \mathbf{B}=3\mathbf{i}-\mathbf{j}$ and $\mathbf{C}=\mathbf{j}-4\mathbf{k}$, find (a) $\mathbf{A}\times \mathbf{B}$ (b)$(\mathbf{A}\times \mathbf{B})\times \mathbf{C}$ (c) $\mathbf{A}\cdot (\mathbf{B}\times \mathbf{C})$.

:::{admonition} Solution 1.9
:class: dropdown

(a)

```{math}
\mathbf{A}\times \mathbf{B}=\left| \begin{array}{lll} \mathbf{i} & \quad \mathbf{j} & \quad \mathbf{k}\\ 2 & \quad -3 & \quad -1 \\ 3 & \quad -1 & \quad 0 \end{array}\right| =-\mathbf{i}-3\mathbf{j}+7\mathbf{k}
```

(b)

```{math}
\mathbf{A}\times (\mathbf{B}\times \mathbf{C})=\left| \begin{array}{lll} \mathbf{i} & \quad \mathbf{j} & \quad \mathbf{k}\\ -1 & \quad -3 & \quad 7 \\ 0 & \quad 1 & \quad -4 \end{array}\right| =5\mathbf{i}-4\mathbf{j}-\mathbf{k}
```

(c)

```{math}
\mathbf{B}\times \mathbf{C}=\left| \begin{array}{lll} \mathbf{i} & \quad \mathbf{j} & \quad \mathbf{k}\\ 3 & \quad -1 & \quad 0 \\ 0 & \quad 1 & \quad -4 \end{array}\right| =4\mathbf{i}+12\mathbf{j}+3\mathbf{k}
```

```{math}
\mathbf{A}\cdot (\mathbf{B}\times \mathbf{C})=(2\mathbf{i}-3\mathbf{j}-\mathbf{k})\cdot (4\mathbf{i}+12\mathbf{j}+3\mathbf{k})=8-36-3=-31
```

:::
````

````{prf:example}
:label: example-1-10
:enumerator: 1.10

Using vectors method, find the area of a triangle if the coordinates of its three vertices are $\mathrm{A}(2,1,3)$ , $\mathrm{B}(2,5,7)$ , $\mathrm{C}(-1,4,2)$ .

:::{admonition} Solution 1.10
:class: dropdown

```{math}
\mathbf{AB}=(2-2)\mathbf{i}+(5-1)\mathbf{j}+(7-3)\mathbf{k}=4\mathbf{j}+4\mathbf{k}
```

```{math}
\mathbf{AC}=(-1-2)\mathbf{i}+(4-1)\mathbf{j}+(2-3)\mathbf{k}=-3\mathbf{i}+3\mathbf{j}-\mathbf{k}
```

Area

```{math}
=\frac{1}{2}|\mathbf{A}\mathbf{B}\times \mathbf{A}\mathbf{C}|=\frac{1}{2}|(4\mathbf{j}+4\mathbf{k})\times (-3\mathbf{i}+3\mathbf{j}-\mathbf{k})|=\frac{1}{2}|4(-4\mathbf{i}-3\mathbf{j}+3\mathbf{k})|
```

```{math}
=2\sqrt{(-4)^{2}+(-3)^{2}+(3)^{2}}=11.7
```

:::
````

#### Triple Product

*Scalar Triple Product*

The triple scalar product is a scalar quantity defined as $\mathbf{A}\cdot (\mathbf{B}\times \mathbf{C})$. This quantity can be represented by a determinant that involves the components of the vectors,

```{math}
\mathbf{A}\cdot (\mathbf{B}\times \mathbf{C})=\left| \begin{array}{lll} A_{x} & A_{y} & A_{z}\\ B_{x} & B_{y} & B_{z}\\ C_{x} & C_{y} & C_{z} \end{array}\right|
```

```{figure} ../images/ch-01/459974_1_En_1_Fig26_HTML.png
:name: fig-1-26

The triple scalar product is equal to the volume of a parallepiped with sides $\mathbf{A}, \mathbf{B}$, and $\mathbf{C}$
```

where $\mathbf{A}=A_{x}\mathbf{i}+A_{y}\mathbf{j}+A_{z}\mathbf{k}, \mathbf{B}=B_{x}\mathbf{i}+B_{y}\mathbf{j}+B_{z}\mathbf{k}$, and $\mathbf{C}=C_{x}\mathbf{i}+C_{y}\mathbf{j}+C_{z}\mathbf{k}.$ Furthermore, the triple scalar product is equal to the volume of a parallepiped with sides $\mathbf{A}, \mathbf{B}$, and $\mathbf{C}$ as shown in [](#fig-1-26). Because any edges can be used, the triple scalar product can be written as $\mathbf{A} \cdot (\mathbf{B}\times \mathbf{C})$ or as $\mathbf{A}\cdot (\mathbf{C}\times \mathbf{B})$ . These products are positive and negative for a right-handed coordinate system respectively. Therefore, there are 6 equal triple scalar products or 12 if you include the terms of the form $(\mathbf{B}\times \mathbf{C})\cdot \mathbf{A}$ . Three of these six products are positive and the rest are negative. By expanding the determinant, you can prove that

```{math}
\mathbf{A}\cdot (\mathbf{B}\times \mathbf{C})=\mathbf{B}\cdot (\mathbf{C}\times \mathbf{A})=\mathbf{C}\cdot (\mathbf{A}\times \mathbf{B})=-\mathbf{A}\cdot (\mathbf{C}\times \mathbf{B})=-\mathbf{B}\cdot (\mathbf{A}\times \mathbf{C})=-\mathbf{C}\cdot (\mathbf{B}\times \mathbf{A})
```

*Vector Triple Product*

The triple vector product is a vector quantity defined as $\mathrm{A}\times (\mathrm{B}\times \mathrm{C})$. You can prove by expanding this equation that

```{math}
\mathbf{A}\times (\mathbf{B}\times \mathbf{C})=(\mathbf{A}\cdot \mathbf{C})\mathbf{B}-(\mathbf{A}\cdot \mathbf{B})\mathbf{C}
```

````{prf:example}
:label: example-1-11
:enumerator: 1.11

Given that $\mathbf{A}=A_{x}\mathbf{i},\mathbf{B}=B_{x}\mathbf{i}+B_{z}\mathbf{k}$, and $\mathbf{C}=C_{y}\mathbf{j}$, show that the identity $\mathbf{A}\times (\mathbf{B}\times \mathbf{C})=(\mathbf{A}\cdot \mathrm {C})\mathbf{B}-(\mathbf{A}\cdot \mathbf{B})\mathbf{C}$ is correct.

:::{admonition} Solution 1.11
:class: dropdown

```{math}
(\mathbf{B}\times \mathbf{C})=\left| \begin{array}{lll} \mathbf{i} & \quad \mathbf{j} & \quad \mathbf{k}\\ B_{x} & \quad 0 & \quad B_{z}\\ 0 & \quad C_{y} & \quad 0 \end{array}\right| =-B_{z}C_{y}\mathbf{i}+B_{x}C_{y}\mathbf{k}
```

```{math}
\mathbf{A}\times (\mathbf{B}\times \mathbf{C})=\left| \begin{array}{lll} \mathbf{i} & \quad \mathbf{j} & \quad \mathbf{k}\\ A_{x} & \quad 0 & \quad 0 \\ -B_{z}C_{y} & \quad 0 & \quad B_{x}C_{y} \end{array}\right| =-A_{x}B_{x}C_{y}\mathbf{j}
```

```{math}
(\mathbf{A}\cdot \mathbf{C})\mathbf{B}=0
```

```{math}
-(\mathbf{A}\cdot \mathbf{B})\mathbf{C}=-(A_{x}B_{x})\mathbf{C}=-A_{x}B_{x}C_{y}\mathbf{j}
```

Hence, the identity is valid.

:::
````

(sec-1-9)=
## 1.9 Derivatives of Vectors

If $\mathbf{A}(\mathrm {t})$ is a vector function of *t*, where *t* is a scalar variable such as

```{math}
\mathbf{A}(t)=A_{x}(t)\mathbf{i}+A_{y}(t)\mathbf{j}+A_{z}(t)\mathbf{k}
```

Then

```{math}
\frac{d\mathbf{A}(t)}{dt}=\frac{dA_{x}(t)}{dt}\mathbf{i}+\frac{dA_{y}(t)}{dt}\mathbf{j}+\frac{dA_{z}(t)}{dt}\mathbf{k}
```

### 1.9.1 Some Rules

If $\mathbf{A}(\mathrm {t})$ and $\mathbf{B}(\mathrm {t})$ are vector functions and $\phi (t)$ is a scalar function then

```{math}
\frac{d}{dt}(\phi \mathbf{A})=\phi \frac{d\mathbf{A}}{dt}+\frac{d\phi }{dt}\mathbf{A}
```

```{math}
\frac{d}{dt}(\mathbf{A}\cdot \mathbf{B})=\mathbf{A}\cdot \frac{d\mathbf{B}}{dt}+\frac{d\mathbf{A}}{dt}\cdot \mathbf{B}
```

```{math}
\frac{d}{dt}(\mathbf{A}\times \mathbf{B})=\mathbf{A}\times \frac{d\mathbf{B}}{dt}+\frac{d\mathbf{A}}{dt}\times \mathbf{B}
```

````{prf:example}
:label: example-1-12
:enumerator: 1.12

Two vectors $\mathbf{r}_{1}$ and $\mathbf{r}_{2}$ are given by $\mathbf{r}_{1}=2t^{2}\mathbf{i}+\cos t\mathbf{j}+4\mathbf{k}$ and $\mathbf{r}_{2}=\sin t\mathbf{i}+\cos t \mathbf{k}$, find at $t=0$ (a)$\frac{d^{2}\mathbf{r}_{1}}{dt^{2}}$ and (b)$\frac{d(\mathbf{r}_{1}\cdot \mathbf{r}_{2})}{dt}$

:::{admonition} Solution 1.12
:class: dropdown

(a)

```{math}
\frac{d\mathbf{r}_{1}}{dt}=4t\mathbf{i}-\sin t \mathbf{j}
```

```{math}
\frac{d^{2}\mathbf{r}_{1}}{dt^{2}}=4\mathbf{i}-\cos t \mathbf{j}
```

At $t=0$

```{math}
\frac{d^{2}\mathbf{r}_{1}}{dt^{2}}=4\mathbf{i}-\mathbf{j}
```

(b)

```{math}
\frac{d(\mathbf{r}_{1}\cdot \mathbf{r}_{2})}{dt}=\frac{d\{(2t^{2}\mathbf{i}+\cos t\mathbf{j}+4\mathbf{k})(\sin t\mathbf{i}+\cos t\mathbf{k})\}}{dt}=
```

```{math}
\frac{d(2t^{2}\sin t+4\cos t)}{dt} =4t\sin t+2t^{2}\cos t-4\sin t=4(t-1)\sin t+2t^{2}\cos t
```

At $t=0$

```{math}
\frac{d(\mathbf{r}_{1}\cdot \mathbf{r}_{2})}{dt}=0.
```

:::
````

### 1.9.2 Gradient, Divergence, and Curl

If $\mathbf{A}=\mathbf{A}(x,\ y,\ z)$ is a vector function of *x*, *y*, and *z* then $\mathbf{A}(x,\ y,\ z)$ is called a vector field. Similarly, the scalar function $\phi (x,\ y,\ z)$ is called a scalar field.

#### Del

The vector differential operator *del* is defined as

```{math}
\nabla =\mathbf{i}\frac{\partial }{\partial x}+\mathbf{j}\frac{\partial }{\partial y}+\mathbf{k}\frac{\partial }{\partial z}
```

#### Gradient

```{math}
\nabla \phi =\bigg (\mathbf{i}\frac{\partial }{\partial x}+\mathbf{j}\frac{\partial }{\partial y}+\mathbf{k}\frac{\partial }{\partial z}\bigg )\phi =\mathbf{i}\frac{\partial \phi }{\partial x}+\mathbf{j}\frac{\partial \phi }{\partial y}+\mathbf{k}\frac{\partial \phi }{\partial z}
```

The vector $\nabla \phi$ is called the gradient of $\phi$ (written $\mathrm{grad}\,\phi$).

#### Divergence

```{math}
\nabla \cdot \mathbf{A}=\bigg (\mathbf{i}\frac{\partial }{\partial x}+\mathbf{j}\frac{\partial }{\partial y}+\mathbf{k}\frac{\partial }{\partial z}\bigg )\cdot (A_{x}\mathbf{i}+A_{y}\mathbf{j}+A_{z}\mathbf{k})
```

```{math}
=\frac{\partial A_{x}}{\partial x}+\frac{\partial A_{y}}{\partial y}+\frac{\partial A_{z}}{\partial z}
```

$\nabla \cdot \mathbf{A}$ is called the divergence of $\mathrm {A}$ (written div $\mathbf{A}$).

#### Curl

```{math}
\nabla \times \mathbf{A}=\bigg (\mathbf{i}\frac{\partial }{\partial x}+\mathbf{j}\frac{\partial }{\partial y}+\mathbf{k}\frac{\partial }{\partial z}\bigg )\times (A_{x}\mathbf{i}+A_{y}\mathbf{j}+A_{z}\mathbf{k})
```

```{math}
\left| \begin{array}{lll} \mathbf{i} & \mathbf{j} & \mathbf{k}\\ \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z}\\ A_{x} & A_{y} & A_{z} \end{array}\right| =\bigg (\frac{\partial A_{z}}{\partial y}-\frac{\partial A_{y}}{\partial z}\bigg )\mathbf{i}+\bigg (\frac{\partial A_{x}}{\partial z}-\frac{\partial A_{z}}{\partial x}\bigg )\mathbf{j}+\bigg (\frac{\partial A_{y}}{\partial x}-\frac{\partial A_{x}}{\partial y}\bigg )\mathbf{k}
```

$\nabla \times \mathbf{A}$ is called the curl of $\mathbf{A}$ (written curl $\mathbf{A}$).

#### Some Identities

- $\mathrm{div}\ \mathrm{curl}\ \mathbf{A} =\nabla \cdot (\nabla \times \mathbf{A})=0$.
- $\mathrm{curl}\ \mathrm{grad}\ \phi =\nabla \times (\nabla \phi )=\mathbf{0}$.

````{prf:example}
:label: example-1-13
:enumerator: 1.13

A vector field A and a scalar field *B* are given by $\mathbf{A}=3xy\mathbf{i}+(2y^{2}-x)\mathbf{j}$ and $B=3x^{2}y$, Find at the point (−1,1)(a) $\nabla \cdot \mathbf{A}$ (b) $\nabla \times \mathbf{A}$ (c) $\nabla \mathrm {B}$.

:::{admonition} Solution 1.13
:class: dropdown

(a)

```{math}
\nabla \cdot \mathbf{A}=\frac{\partial A_{x}}{\partial x}+\frac{\partial A_{y}}{\partial y}=3y+4y=7y
```

at $(-1,1)$, $\nabla \cdot \mathbf{A}=7.$

(b)

```{math}
\nabla \times \mathbf{A}=\left| \begin{array}{lll} \mathbf{i} & \quad \mathbf{j} & \quad \mathbf{k}\\ \frac{\partial }{\partial x} & \quad \frac{\partial }{\partial y} & \quad \frac{\partial }{\partial z}\\ 3xy & \quad (2y^{2}-x) & \quad 0 \end{array}\right| =(-3x-1)\mathbf{k}
```

at $(-1,1)$, $\nabla \times \mathbf{A}=2\mathbf{k}.$

(c)

```{math}
\nabla B=\frac{\partial B}{\partial x}\mathbf{i}+\frac{\partial B}{\partial y}\mathbf{j}+\frac{\partial B}{\partial z}\mathbf{k}=6xy\mathbf{i}+3x^{2}\mathbf{j}
```

at $(-1,1)$, $\nabla B=-6\mathbf{i}+3\mathbf{j}.$

:::
````

(sec-1-10)=
## 1.10 Integrals of Vectors

If $\mathbf{A}(t)=A_{x}(t)\mathbf{i}+A_{y}(t)\mathbf{j}+A_{z}(t)\mathbf{k}$, where *t* is a scalar variable, the indefinite integral is defined as

```{math}
\int \mathbf{A}(t)dt=\mathbf{i}\int A_{x}(t)dt+\mathbf{j}\int A_{y}(t)dt+\mathbf{k}\int A(t)dt
```

If $\mathbf{A}(t)=d\mathbf{B}(t)/dt$, then

```{math}
\int \mathbf{A}(t)dt=\int \frac{d}{dt}\ \{\mathbf{B}(t)\} dt=\mathbf{B}(t)+\mathbf{C}
```

where $\mathbf{C}$ is an arbitrary constant vector. The definite integral between the limits $t=a$ and $t=b$ is defined as

```{math}
\int _{a}^{b}\mathbf{A}(t)dt=\int _{a}^{b}\frac{d}{dt}\ \{\mathbf{B}(t)\} dt=\mathbf{B}(t)+\mathbf{C}|_{a}^{b}=\mathbf{B}(b)-\mathbf{B}(a)
```

### 1.10.1 Line Integrals

The line integral refers to an integral along a line or a curve. This curve may be open or closed. The line integral may appear in three different forms shown by $\int _{c}\phi d\mathbf{r}$, $\int _{c}\mathbf{A}\cdot d\mathbf{r}$, and $\int _{c}\mathbf{A}\times d\mathbf{r}$. The second is the most common one and it will be used throughout this book. Suppose the position vector of any point $(x,\ y,\ z)$ on the curve $\mathrm{C}$ (see [](#fig-1-27)) that extends from $\mathbf{P}(x_{1},\ y_{1},\ z_{1})$ at $t_{1}$ to $\mathbf{Q}(x_{2},\ y_{2},\ z_{2})$ at $t_{2}$ is given by

```{math}
\mathbf{r}(t)=x(t)\mathbf{i}+y(t)\mathbf{j}+z(t)\mathbf{k}
```

where *t* is a scalar variable, and suppose that $\mathbf{A}=\mathbf{A}(x,\ y,\ z)=A_{x}\mathbf{i}+A_{y}\mathbf{j}+A_{z}\mathbf{k}$ is a vector field, then the line integral of $\mathbf{A}$ is given by

```{math}
:label: eq-1-2
\int _{P}^{Q}\mathbf{A}\cdot d\mathbf{r}=\int _{C}\mathbf{A}\cdot d\mathbf{r}=\int _{C}(A_{x}dx+A_{y}dy+Adz)
```

Note that $\mathbf{A} \cdot \mathbf{r}$ is the tangential component of $\mathbf{A}$ along C. If $\mathrm{C}$ is a simple closed curve (does not intersect with itself) then the line integral is written as

```{math}
\oint _{C}\mathbf{A}\cdot d\mathbf{r}=\oint _{C}(A_{x}dx+A_{y}dy+Adz)
```

```{figure} ../images/ch-01/459974_1_En_1_Fig27_HTML.png
:name: fig-1-27

The line integral
```

### 1.10.2 Independence of Path

The line integral in general depends on the path, but sometimes it does not. Instead, it depends only on the coordinates of the end points of the curve (path) but not on the curve itself. The line integral in Eq. [](#eq-1-2) is independent of the path, joining the points $\mathrm{P}$ and $\mathrm{Q}$ if and only if $\mathbf{A}=\nabla \phi$, or equivalently $\nabla \times \mathbf{A}=\mathbf{0}$. The value of Eq. ([](#eq-1-2)) is then given by

```{math}
\int _{P}^{Q}\mathbf{A}\cdot d\mathbf{r}=\int _{P}^{Q}d\phi =\phi (P)-\phi (Q)=\phi (x_{2},\ y_{2},\ z_{2})-\phi (x_{1},\ y_{1},\ z_{1})
```

Note that $\phi (x,\ y,\ z)$ has continuous partial derivatives. Furthermore, if the line integral of $\mathbf{A}$ is independent of the path then the line integral of $\mathbf{A}$ about any closed path is equal to zero:

```{math}
\oint _{C}\mathbf{A}\cdot d\mathbf{r}=0
```

````{prf:example}
:label: example-1-14
:enumerator: 1.14

A force field is given by $\mathbf{F}=(4xy^{2}+z^{2})\mathbf{i}+(4yx^{2})\mathbf{j}+(2xz-1)\mathbf{k}$

(a) Show that $\nabla \times \mathbf{F}=\mathbf{0}$,

(b) Find a scalar function $\phi$ such that $\mathbf{F}=\nabla \phi .$

:::{admonition} Solution 1.14
:class: dropdown

(a)

```{math}
\nabla \times \mathbf{F}=\left| \begin{array}{lll} \mathbf{i} & \quad \mathbf{j} & \quad \mathbf{k}\\ \frac{\partial }{\partial x} & \quad \frac{\partial }{\partial y} & \quad \frac{\partial }{\partial z}\\ (4xy^{2}+z^{2}) & \quad (4yx^{2}) & \quad (2xz-1) \end{array}\right| =(2z-2z)\mathbf{j}+(8xy-8xy)\mathbf{k}=\mathbf{0}
```

(b)

```{math}
\mathbf{F}\cdot d\mathbf{r}=\nabla \phi \cdot d\mathbf{r}=\frac{\partial \phi }{\partial x}dx+\frac{\partial \phi }{\partial y}dy+\frac{\partial \phi }{\partial z}dz=d\phi
```

```{math}
d\phi =(4xy^{2}+z^{2})dx+(4yx^{2})dy+(2xz-1)dz
```

Hence

```{math}
\phi =(2x^{2}y^{2}+z^{2}x)+(2y^{2}x^{2})+(z^{2}x-z)
```

:::
````

````{prf:example}
:label: example-1-15
:enumerator: 1.15

A vector $\mathbf{F}$ is given by $\mathbf{F}=3x^{2}y\mathbf{i}-(4y+x)\mathbf{j}$. Compute $\int _{c}\mathbf{F}\cdot d\mathbf{r}$ along each of the following paths:

(a) The straight lines from (0, 0) to (0, 1) and then to (1, 1).

(b) Along the straight line $y=x.$ (c) Along the curve $x=t, y=t^{2}.$

:::{admonition} Solution 1.15
:class: dropdown

(a) Along the straight line from (0,0) to (0,1) we have $x=0$, and $dx=0,$ therefore

```{math}
\int _{C}\mathbf{F}\cdot d\mathbf{r}=\int _{C}3x^{2}ydx-(4y+x)dy=\int _{y=0}^{1}-4ydy=-2y^{2}|_{0}^{1}=-2
```

Along the straight line from (0, 1) to (1, 1) we have $y=1, dy=1$, hence

```{math}
\int _{C}\mathbf{F}\cdot d\mathbf{r}=\int _{x=0}^{1}3x^{2}dx=x^{3}|_{0}^{1}=1
```

Thus, we have for the total path

```{math}
\int _{C}\mathbf{F}\cdot d\mathbf{r}=-2+1=-1
```

(b) Along the straight line $y=x$, we have $dy=dx,$

```{math}
\int _{C}\mathbf{F}\cdot d\mathbf{r}=\int _{C}3x^{2}ydx-(4y+x)dy=\int _{x=0}^{1}(3x^{3}-5x)dx
```

```{math}
=3/4x^{4}-5/2x^{2}|_{0}^{1}=-3/2.
```

(c) Finally along the curve $x=t, y=t^{2}$, we have $dx=dt, dy=2tdt$, furthermore the points (0, 0) and (1, 1) corresponds to $t=0$ and $t=1$, respectively. Hence

```{math}
\int _{C}\mathbf{F}\cdot \, d\mathbf{r}=\int _{C}3x^{2}ydx-(4y+x)dy=\int _{t=0}^{1}3t^{4}dt-2t(4t^{2}+t)dt
```

$=3/5t^{5}-2t^{4}-2/3t^{3}|_{0}^{1}= -31/15$ .

:::
````

````{prf:example}
:label: example-1-16
:enumerator: 1.16

If a vector $\mathbf{A}$ is given by $\mathbf{A}=xy\mathrm {i}-x^{2}\mathrm {j}$, find the line integral $\int _{C}\mathbf{A}\cdot d\mathbf{r}$ along the circular arc shown in [](#fig-1-28).

:::{admonition} Solution 1.16
:class: dropdown

By using the polar coordinates, we have $x=\cos \theta$ and $y=\sin \theta$ (since $r=1$) , $dx=-\sin \theta d\theta$ and $dy=\cos \theta d\theta$, also $x^{2}+y^{2}=r^{2}=1$, therefore we have

```{math}
\int _{c}\mathbf{A}\cdot d\mathbf{r}=\int _{\theta =\pi }^{-\pi /4}-\cos \theta \sin ^{2}\theta d\theta -\cos ^{3}d\theta =\int _{\theta =\pi }^{-\pi /4}-\cos \theta (\sin ^{2}\theta +\cos ^{2}\theta )d\theta
```

```{math}
=\int _{\theta =\pi }^{-\pi /4}-\cos \theta d\theta =-\sin \theta |_{\pi }^{-\pi /4}=0.71
```

:::
````

```{figure} ../images/ch-01/459974_1_En_1_Fig28_HTML.png
:name: fig-1-28

The line integral along the curve using polar coordinates
```

## Problems

```{exercise}
:label: prob-1-1
:enumerator: 1.1

Check if the relation $v=\sqrt{2GM_{E}/R_{E}}$ is dimensionally correct, where *v* represents the escape speed of a body, $M_{E}$ and $R_{E}$ are the mass and radius of the earth, respectively, and *G* is the universal gravitational constant.
```

```{exercise}
:label: prob-1-2
:enumerator: 1.2

If the speed of a car is 180 $\mathrm {k}\mathrm {m}/\mathrm {h}$, find its speed in $\mathrm {m}/\mathrm {s}.$
```

```{exercise}
:label: prob-1-3
:enumerator: 1.3

How many micrometers are there in an area of 3 $\mathrm {k}\mathrm {m}^{2}.$
```

```{exercise}
:label: prob-1-4
:enumerator: 1.4

Figure [](#fig-1-29) shows vectors $\mathbf{A}, \mathbf{B}, \mathbf{C}$, and D. Find graphically the following vectors (a) $\mathbf{A}+2\mathbf{B}-\mathbf{C}$ (b) $2(\mathbf{A}-\mathbf{B})+\mathbf{C}-2\mathbf{D}$ (c) show that $(\mathbf{A}+\mathbf{B})+\mathbf{C}= \mathbf{A}+(\mathbf{B}+\mathbf{C})$ .
```

```{exercise}
:label: prob-1-5
:enumerator: 1.5

A car travels a distance of 1 km due east and then a distance of 0.5 km north of east. Find the magnitude and direction of the resultant displacement of the car using the algebraic method.
```

```{exercise}
:label: prob-1-6
:enumerator: 1.6

Prove that $\mathbf{A}\cdot (\mathbf{B}+\mathbf{C})=\mathbf{A}\cdot \mathbf{B}+\mathbf{A}\cdot \mathbf{C}$.
```

```{exercise}
:label: prob-1-7
:enumerator: 1.7

A parallelogram has sides $\mathbf{A}$ and $\mathbf{B}$. Prove that its area is equal to $|\mathbf{A}\times \mathbf{B}|.$
```

```{exercise}
:label: prob-1-8
:enumerator: 1.8

If $\mathbf{A}=2\mathbf{i}-3\mathbf{j}+4\mathbf{k}$ and $\mathbf{B}=\mathbf{i}+5\mathbf{j}-2\mathbf{k}$, find (a) $\mathbf{A}-2\mathbf{B}$(b)$\mathbf{A}\times \mathbf{B}$ (c)$\mathbf{A}\cdot \mathbf{B}$ (d) the length of $\mathbf{A}$ and the length of $\mathbf{B}$(e) the angle between $\mathbf{A}$ and $\mathbf{B}$(f) the scalar projection of $\mathbf{A}$ on $\mathbf{B}$ and the scalar projection of $\mathbf{B}$ on $\mathbf{A}$.
```

```{exercise}
:label: prob-1-9
:enumerator: 1.9

Show that $\mathbf{A}$ is perpendicular to $\mathbf{B}$ if $|\mathbf{A}+\mathbf{B}|=|\mathbf{A}-\mathbf{B}|.$
```

```{exercise}
:label: prob-1-10
:enumerator: 1.10

Given that $\mathbf{A}=2\mathbf{i}+\mathbf{j}+\mathbf{k}, \mathrm {B}=\mathbf{i}+3\mathbf{j}-5\mathbf{k}$ and $\mathbf{C}=6\mathbf{i}+3\mathbf{j}+3\mathbf{k}$, determine which vectors are perpendicular and which are parallel.
```

```{exercise}
:label: prob-1-11
:enumerator: 1.11

Use the vectors $\mathbf{A}=\cos \theta \mathbf{i}+\sin \theta \mathbf{j}$ and $\mathbf{B}=\cos \phi \mathbf{i}-\sin \phi \mathbf{j}$ to prove that $\cos (\theta +\phi )=\cos \theta \cos \phi -\sin \theta \sin \phi .$
```

```{exercise}
:label: prob-1-12
:enumerator: 1.12

If $\mathbf{A}=5x^{2}y\mathbf{i}+yz\mathbf{j}-3x^{2}z^{2}\mathbf{k}, \mathbf{B}=7y^{3}z\mathbf{i}-2zx\mathbf{j}+xz^{2}y\mathbf{k}$ and $\phi (x,\ y,\ z)= 2z^{2}y$, find at (−1,1,1)(a)$\partial (\phi \mathbf{A})/\partial x$(b)$\partial ^{2}(\mathbf{A}\times \mathbf{B})/\partial z\partial y$(c)$\nabla \phi$ (d)$\nabla \times (\phi \mathbf{A})$ .
```

```{exercise}
:label: prob-1-13
:enumerator: 1.13

Evaluate $\nabla \times (r^{2}\mathbf{r})$ where $\mathbf{r}=x\mathbf{i}+y\mathbf{j}-z\mathbf{k}$ and $r=|\mathbf{r}|.$
```

```{exercise}
:label: prob-1-14
:enumerator: 1.14

If $\mathbf{r}=A\cos \omega t\mathbf{i}+A\sin \omega t\mathbf{j}$, show that $d^{2}\mathbf{r}/dt^{2}+\omega ^{2}\mathbf{r}=0.$
```

```{exercise}
:label: prob-1-15
:enumerator: 1.15

A force field is given by $\mathbf{F}=-kx\mathbf{i}-ky\mathbf{j}$, find (a) $\nabla \times \mathbf{F}$ (b) a scalar field $\phi$ such that $\mathbf{F}=\nabla \phi$ (c) Calculate the line integral along the straight lines from (0, 0) to (1, 0) to (1, 1) and from (0, 0) to (0, 1) to (1, 1). Is the line integral independent of path?
```

```{figure} ../images/ch-01/459974_1_En_1_Fig29_HTML.png
:name: fig-1-29

Vectors $\mathbf{A}, \mathbf{B}, \mathbf{C}$ and $\mathbf{D}$
```
