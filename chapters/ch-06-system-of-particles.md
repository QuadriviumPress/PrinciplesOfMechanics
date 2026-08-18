---

title: 6. System of Particles

short_title: "Ch. 6 — System of Particles"

label: ch-6

doi: 10.1007/978-3-030-15195-9_6

---

(sec-6-1)=

## 6.1 System of Particles

In the previous chapters, objects that can be treated as particles were only considered. We have seen that this is possible only if all parts of the object move in exactly the same way. An object that does not meet this condition must be treated as a system of particles. Next, we will see that the complex motion of this object or system of particles can be represented by the motion of a point located at the center of mass of the system. The center of mass moves as if all of the mass of the object is concentrated there and as if the net external force acting on the system is applied there (at the center of mass). As well as representing an object by a particle, the concept of the center of mass is used to analyze the motion of many systems such as a system of two colliding blocks (particle-like objects) and the system of two colliding subatomic particles such as the neutron with the nucleus.

(sec-6-2)=

## 6.2 Discrete and Continuous System of Particles

(sec-6-2-1)=

### 6.2.1 Discrete System of Particles

A discrete system of particles is a system in which particles are separated from each other.

(sec-6-2-2)=

### 6.2.2 Continuous System of Particles

A continuous system of particles is a system where the separation of particles is very small such that it approaches zero. An extended object is a continuous system of particles. Now, consider the skateboarder example mentioned in Sect. [](#sec-4-3). It has been shown that the system (man $+$ skateboard) cannot be treated as a particle since different parts of the system move in different ways. By representing the skateboarder as a system of particles its motion can be represented by the motion of its center of mass, hence, the work–energy theorem can be applied to that point. The work done by the force, exerted on the skateboarder by the bar, is not zero because the point of application of that force (which is at the center of mass) has moved.

(sec-6-3)=

## 6.3 The Center of Mass of a System of Particles

For a system of particles of total mass *M* the acceleration of its center of mass is given by

```{math}
\mathbf {a}=\frac{\mathbf {F}}{M}
```

(sec-6-3-1)=

### 6.3.1 Two Particle System

Consider two particles of masses $m_{1}$ and $m_{2}$ moving in space. Suppose that their position vectors at a particular instant of time are given by $\mathbf {r}_{1}$ and $\mathbf {r}_{2}$ as shown in Fig. [](#fig-6-1). The center of mass of the system lies somewhere along the line joining the two particles and its position vector is given by

```{math}
\mathbf {r}_{cm}=\frac{m_{1}\mathbf {r}_{1}+m_{2}\mathbf {r}_{2}}{m_{1}+m_{2}}
```

The *x*, *y* and *z* components of the center of mass is

```{math}
x_{cm}=\frac{m_{1}x_{1}+m_{2}x_{2}}{m_{1}+m_{2}}
```

```{math}
y_{cm}=\frac{m_{1}y_{1}+m_{2}y_{2}}{m_{1}+m_{2}}
```

and

```{math}
z_{cm}=\frac{m_{1}z_{1}+m_{2}z_{2}}{m_{1}+m_{2}}
```

```{figure} ../images/ch-06/459974_1_En_6_Fig1_HTML.png
:name: fig-6-1

Two particles of masses $m_{1}$ and $m_{2}$ moving in space. Their position vectors at a particular instant of time are given by $\mathbf {r}_{1}$ and $\mathbf {r}_{2}$
```

```{figure} ../images/ch-06/459974_1_En_6_Fig2_HTML.png
:name: fig-6-2

A discrete system of particles consisting of *n* particles
```

(sec-6-3-2)=

### 6.3.2 Discrete System of Particles

Consider a discrete system of particles consisting of *n* particles (see Fig. [](#fig-6-2)). The position vector of the center of mass at a particular instant is given by

```{math}
\mathbf {r}_{cm}=\frac{m_{1}\mathbf {r}_{1}+m_{2}\mathbf {r}_{2}+m_{3}\mathbf {r}_{3}.+\cdots \cdot \cdot \cdot \cdot \cdots \cdot \cdot m_{n}\mathbf {r}_{n}}{m_{1}+m_{2}+m_{3}+\cdots +m_{n}}=\frac{\varSigma _{i=1}^{n} m_{i}\mathbf {r}_{i}}{M}
```

where $\mathbf {r}_{i}$ is the position vector of the ith particle and $M=\displaystyle \sum _{i=1}^{n}m_{i}$ is the total mass of the system. In component form,$\mathrm {r}_{i}$ can be written as

```{math}
\mathbf {r}_{i}=x_{i}\mathbf {i}+y_{i}\mathbf {j}+z_{i}\mathbf {k}
```

The *x*, *y* and *z* components of the center of mass vector are

```{math}
x_{cm}=\frac{\sum _{i=1}^{n}m_{i}x_{i}}{M}
```

```{math}
y_{cm}=\frac{\sum _{i=1}^{n}m_{i}y_{i}}{M}
```

and

```{math}
z_{cm}=\frac{\sum _{i=1}^{n}m_{i}z_{i}}{M}
```

````{prf:example}
:label: example-6-1
:enumerator: 6.1

Find the center of mass of the system shown in Fig. [](#fig-6-3) where the three particles have an equal mass of $m=1\, \mathrm {k}\mathrm {g}.$

:::{admonition} Solution 6.1
:class: dropdown

```{math}
x_{cm}=\frac{(1\,\mathrm {k}\mathrm {g})((0.1\,\mathrm {m})+(0.5\,\mathrm {m})+(0.3\,\mathrm {m}))}{(3\,\mathrm {k}\mathrm {g})}=0.3\,\mathrm {m}
```

```{math}
y_{cm}=\frac{0+0+(1\,\mathrm {k}\mathrm {g})(0.2\,\mathrm {m})\tan (60^{\mathrm {o}})}{(3\,\mathrm {k}\mathrm {g})}=0.12\,\mathrm {m}
```

```{math}
\mathbf {r}_{cm}=x_{cm}\mathbf {i}+y_{cm}\mathbf {j}=(0.3\,\mathrm {m})\ \mathbf {i}+\ (0.12\,\mathrm {m}) \; \mathbf {j}
```
:::
````

```{figure} ../images/ch-06/459974_1_En_6_Fig3_HTML.png
:name: fig-6-3

The center of mass of a system in the x-y plane
```

````{prf:example}
:label: example-6-2
:enumerator: 6.2

A system of particles consists of three masses $m_{A}=0.5 $ kg,$m_{B}=2 $ kg and $m_{C}=5 $ kg located at $\mathrm {P}_{\mathrm {A}}(-3,1,2)$,$\mathrm {P}_{\mathrm {B}}(0,1,2)$ and $\mathrm {P}_{\mathrm {C}}(-1,3,0)$, respectively. Find the position vector of the center of mass of the system.

:::{admonition} Solution 6.2
:class: dropdown

The position vector of each particle is

```{math}
\mathbf {r}_{A}=(-3\mathbf {i}+\mathbf {j}+2\mathbf {k})\,\mathrm {m}
```

```{math}
\mathbf {r}_{B}=(\mathbf {j}+2\mathbf {k})\,\mathrm {m}
```

and

```{math}
\mathbf {r}_{C}=(-\mathbf {i}+3\mathbf {j})\,\mathrm {m}
```

The center of mass of the system is

```{math}
\displaystyle \mathbf {r}_{cm}=\frac{\sum _{i=1}^{n}m_{i}\mathbf {r}_{i}}{\sum _{i=1}^{n}m_{i}}=\frac{(0.5\,\mathrm {k}\mathrm {g})((-3\mathbf {i}+\mathbf {j}+2\mathbf {k})\,\mathrm {m})+(2\,\mathrm {k}\mathrm {g})((\mathbf {j}+2\mathbf {k})\,\mathrm {m})+(5\,\mathrm {k}\mathrm {g})((-\mathbf {i}+3\mathbf {j})\,\mathrm {m})}{(7.5\,\mathrm {k}\mathrm {g})}
```

That gives

```{math}
\mathbf {r}_{cm}=(-0.87\mathbf {i}+2.3\mathbf {j}+0.7\mathbf {k})\,\mathrm {m}.
```
:::
````

(sec-6-3-3)=

### 6.3.3 Continuous System of Particles (Extended Object)

A continuous system of particles is a system consisting of a large number of particles separated by very small distances. Consider an extended object of mass *M* divided into small volume elements each of mass $\triangle m_{i}$ and a vector position $\mathrm {r}_{i}$(see Fig. [](#fig-6-4)). The position vector of the center of mass at a particular instant is then approximately given by

```{math}
\mathbf {r}_{cm}\approx \frac{\sum _{i=1}^{n}\mathbf {r}_{i}\triangle m_{i}}{M}
```

For a very large number of particles where $n\rightarrow \infty $ we have $\triangle m_{i}\rightarrow 0 $, that gives

```{math}
\mathbf {r}_{cm}=\lim _{\triangle m_{\mathrm {i}}}\frac{\sum _{i=1}^{n}\mathbf {r}_{i}\triangle m_{i}}{M}=\frac{1}{M}\int \mathbf {r}dm
```

Since $\mathbf {r}=x\mathbf {i}+y\mathbf {j}+z\mathbf {k}$, the *x*, *y* and *z* components of the center of mass are given by

```{math}
x_{cm}=\frac{1}{M}\int xdm
```

```{math}
y_{cm}=\frac{1}{M}\int ydm
```

and

```{math}
z_{cm}=\frac{1}{M}\int zdm
```

```{figure} ../images/ch-06/459974_1_En_6_Fig4_HTML.png
:name: fig-6-4

An extended object of mass *M* divided into small volume elements each of mass $\triangle m_{i}$ and a vector position $\mathrm {r}_{I}$
```

(sec-6-3-4)=

### 6.3.4 Elastic and Rigid Bodies

A body is called an elastic (deformable) body if the separation between its particles changes when a force is applied to it. This change or deformation is sometimes so small that it can be neglected. A body that behaves in this way is called a rigid body. A rigid body can be defined as a body in which the separation between its particles remain constant with time despite the applied force, i.e., the body has a constant size and shape. Therefore, the center of mass of a rigid object remains fixed at the same location at all times. In this book, only rigid bodies are discussed. In solving problems, it is common to use the volume density $\rho $ defined as the mass per unit volume given by

```{math}
\rho =\frac{dm}{dV}
```

Therefore, the total mass of a rigid object is

```{math}
M=\int \rho dV
```

The center of mass of a rigid object can thus be written as

```{math}
\mathbf {r}_{cm}=\frac{1}{M}\int \mathbf {r}dm=\frac{\int \rho \mathbf {r}dV}{\int \rho dV}
```

$\rho $ may be a function of position, i.e., it can vary from point to point in the body If the body has a uniform density (homogeneous body), then $\rho $ can be written as

```{math}
\displaystyle \rho =\frac{dm}{dV}=\frac{\mathrm {T}\mathrm {o}\mathrm {t}\mathrm {a}1\mathrm {M}\mathrm {a}\mathrm {s}\mathrm {s}}{\mathrm {T}\mathrm {o}\mathrm {t}\mathrm {a}1\mathrm {V}\mathrm {o}\mathrm {l}\mathrm {u}\mathrm {m}\mathrm {e}}=\text {constant}
```

If the continuous distribution of particles occupies a surface, then the surface density $\sigma $ is used and is given by

```{math}
\displaystyle \sigma =\frac{dm}{dA} \; \text {(mass\,per\,unit\, area)}
```

```{math}
\displaystyle \sigma =\frac{\mathrm {T}\mathrm {o}\mathrm {t}\mathrm {a}1\mathrm {M}\mathrm {a}\mathrm {s}\mathrm {s}}{\mathrm {T}\mathrm {o}\mathrm {t}\mathrm {a}1\mathrm {A}\mathrm {r}\mathrm {e}\mathrm {a}}=\text {constant} \; \text {(homogeneous body)}
```

If the particles occupy a curve or a line, the linear density $\lambda $ is used given by

```{math}
\displaystyle \lambda =\frac{dm}{dl} \; \text {(mass\,per\,unit\, length)}
```

```{math}
\displaystyle \lambda =\frac{\mathrm {T}\mathrm {o}\mathrm {t}\mathrm {a}1\mathrm {M}\mathrm {a}\mathrm {s}\mathrm {s}}{\mathrm {T}\mathrm {o}\mathrm {t}\mathrm {a}1\mathrm {L}\mathrm {e}\mathrm {n}\mathrm {g}\mathrm {t}\mathrm {h}}= \text {constant (homogeneous body)}
```

The center of mass of any homogeneous symmetric object is at its geometrical center and it is not necessarily located within the object.

````{prf:example}
:label: example-6-3
:enumerator: 6.3

A thin rod of length $L=2\,\mathrm {m}$ has a linear density that increases with *x* according to the expression $\lambda (x)=(2x-1)\,\mathrm {k}\mathrm {g}/\mathrm {m}$(see Fig. [](#fig-6-5)). Locate the center of mass of the rod relative to O.

:::{admonition} Solution 6.3
:class: dropdown

```{math}
x_{cm}=\frac{1}{M}\int xdm=\frac{\int _{0}^{L}x\lambda (x)dx}{\int _{0}^{L}\lambda (x)dx}=\frac{\int _{0}^{L}(2x^{2}-x)dx}{\int _{0}^{L}(2x-1)dx}
```

```{math}
=\frac{((2/3)x^{3}-x^{2}/2)|_{x=0}^{L}}{(x^{2}-x)|_{x=0}^{L}}=\frac{L((2/3)L-1/2)}{(L-1)}
```

Substituting $L=2\,\mathrm {m}$ gives $x_{cm}=1.7\,\mathrm {m}.$
:::
````

```{figure} ../images/ch-06/459974_1_En_6_Fig5_HTML.png
:name: fig-6-5

A thin rod of length $L=2 \; \mathrm {m}$ has a linear density that increases with *x*
```

```{figure} ../images/ch-06/459974_1_En_6_Fig6_HTML.png
:name: fig-6-6

A uniform square sheet suspended by a uniform rod where they both lie in the same plane
```

````{prf:example}
:label: example-6-4
:enumerator: 6.4

A uniform square sheet is suspended by a uniform rod where they both lie in the same plane as shown in Fig. [](#fig-6-6). Find the center of mass of the system.

:::{admonition} Solution 6.4
:class: dropdown

Because the sheet and the rod are homogeneous, the center of mass of each is at its geometric center. Since the center of the sheet is at the origin we have

```{math}
x_{cm}=\frac{\sum _{i}m_{i}x_{i}}{\sum _{i}m_{i}}=\frac{0+({M_{2}L}/2)}{M_{1}+M_{2}}=\frac{LM_{2}}{2(M_{1}+M_{2})}
```
:::
````

````{prf:example}
:label: example-6-5
:enumerator: 6.5

Find the center of mass of the rectangular plate shown in Fig. [](#fig-6-7). The plate has a uniform surface density $\sigma.$

:::{admonition} Solution 6.5
:class: dropdown

- Method 1:

```{math}
x_{cm}=\frac{\int xdm}{M}=\frac{\int x\sigma dA}{\int \sigma dA}=\frac{\int _{y=0}^{b}\int _{x=0}^{a}xdxdy}{\int _{y=0}^{b}\int _{x=0}^{a}dxdy}=\frac{ba^{2}}{2ab}=\frac{a}{2}
```

```{math}
y_{cm}=\frac{\int ydm}{M}=\frac{\int x\sigma dA}{\int \sigma dA}=\frac{\int _{x=0}^{a}\int _{y=0}^{b}ydxdy}{\int _{x=0}^{a}\int _{y=0}^{b}dxdy}=\frac{ab^{2}}{2ab}=\frac{b}{2}
```

Hence

```{math}
\mathbf {r}_{cm}=\frac{a}{2}\mathbf {i}+\frac{b}{2}\mathbf {j}
```
- Method 2:

Dividing the plate into very thin rods each of mass $\sigma bdx $ gives

```{math}
x_{cm}=\frac{\int xdm}{M}=\frac{1}{M}\int x\sigma dA=\frac{1}{M}\bigg (\frac{M}{ab}\bigg )\int _{x=0}^{a}\ xbdx=\frac{1}{a}\bigg [\frac{x^{2}}{2}\bigg ]_{x=0}^{a}=\frac{a}{2}
```

Similarly by dividing the plate into thin horizontal rods each of mass $\sigma ady $ gives

```{math}
y_{cm}=\frac{\int ydm}{M}=\frac{1}{M}\int y\sigma dA=\frac{1}{M}\bigg (\frac{M}{ab}\bigg )\int _{y=0}^{b}\ aydy=\frac{1}{b}\bigg [\frac{y^{2}}{2}\bigg ]_{y=0}^{b}=\frac{b}{2}
```

and

```{math}
\mathbf {r}_{cm}=\frac{a}{2}\mathbf {i}+\frac{b}{2}\mathbf {j}
```
:::
````

```{figure} ../images/ch-06/459974_1_En_6_Fig7_HTML.png
:name: fig-6-7

The center of mass of a rectangular plate
```

````{prf:example}
:label: example-6-6
:enumerator: 6.6

An object of uniform surface density $\sigma $ and mass *M* has the shape shown in Fig. [](#fig-6-8) (half of an ellipse). Find the center of mass of the object.

:::{admonition} Solution 6.6
:class: dropdown

The equation of an ellipse is

```{math}
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1
```

therefore

```{math}
\frac{2xdx}{a^{2}}+\frac{2ydy}{b^{2}}=0
```

or

```{math}
xdx=\frac{-a^{2}}{b^{2}}ydy
```

By dividing the area into very thin rectangles each of mass $\sigma ydx $ gives

```{math}
x_{cm}=\frac{\int xdm}{M}=\frac{1}{M}\int x\sigma dA=\frac{1}{M}\int _{x=-a}^{a}x\bigg (\frac{2M}{\pi ab}\bigg )ydx
```

```{math}
=\frac{2}{\pi ab}\int _{y=0}^{0}\bigg (\frac{-a^{2}}{b^{2}}\bigg )y^{2}dy=\frac{-2a}{\pi b^{3}}\bigg [\frac{y^{3}}{3}\bigg ]_{y=0}^{0}=0
```

To obtain the *y* coordinate of the center of mass we divide the area into very thin rectangles each of mass $\sigma xdy $ as in Fig. [](#fig-6-8). That gives

```{math}
y_{cm}=\displaystyle \frac{1}{M}\int ydm=\frac{1}{M}\int y\sigma dA=\frac{2}{\pi ab}\int _{y=0}^{b}yxdy
```

```{math}
=\frac{2}{\pi ab}\int _{x=a}^{-a}\bigg (\frac{-b^{2}}{a^{2}}\bigg )x^{2}dx=\frac{-2b}{\pi a^{3}}\int _{x=a}^{-a}x^{2}dx=\frac{-2b}{\pi a^{3}}\bigg [\frac{x^{3}}{3}\bigg ]_{x=a}^{-a}
```

```{math}
\frac{-2b}{\pi a^{3}}\bigg [\frac{x^{3}}{3}\bigg ]_{x=a}^{-a}=\frac{-2b}{\pi a^{3}}\bigg (\frac{-a^{3}}{3}-\frac{a^{3}}{3}\bigg )=\frac{4b}{3\pi }
```
:::
````

```{figure} ../images/ch-06/459974_1_En_6_Fig8_HTML.png
:name: fig-6-8

The center of mass of half an ellipse
```

````{prf:example}
:label: example-6-7
:enumerator: 6.7

Determine the center of mass of the cylindrical shell shown in Fig. [](#fig-6-9). The shell has a uniform surface density $\sigma.$

:::{admonition} Solution 6.7
:class: dropdown

From symmetry, the center of mass lies on the $\mathrm {z}$-axis. By dividing the shell into very thin rings each of mass $\sigma 2\pi Rdz $ we have

```{math}
z_{cm}=\displaystyle \frac{\int zdm}{M}=\frac{\int z\sigma dA}{M}=\frac{1}{M}\int _{z=0}^{h}z\sigma 2\pi Rdz=\frac{1}{M} \bigg (\frac{M}{2\pi Rh} \bigg )\int _{z=0}^{h}2\pi Rzdz
```

```{math}
=\frac{1}{h} \bigg [\frac{z^{2}}{2} \bigg ]_{z=0}^{h}=\frac{h}{2}
```
:::
````

```{figure} ../images/ch-06/459974_1_En_6_Fig9_HTML.png
:name: fig-6-9

The center of mass of a cylindrical shell
```

````{prf:example}
:label: example-6-8
:enumerator: 6.8

A boy standing on a smooth ice surface wants to fetch a container that is at a distance of 10 $\mathrm {m}$ away from him. To do that, he throws a rope around the container and start to pull. Because the surface is smooth, both the boy and the container will move until they meet. If the masses of the boy and of the container are 40 kg and 70 kg respectively, how far will the container move when the boy has moved a distance of 2 $\mathrm {m}$?

```{figure} ../images/ch-06/459974_1_En_6_Fig10_HTML.png
:name: fig-6-10

A boy pulling a container on a smooth surface
```

:::{admonition} Solution 6.8
:class: dropdown

By taking the midpoint between the boy and the container as the origin (see Fig. [](#fig-6-10)) and by neglecting the mass of the rope, the center of mass of the system is

```{math}
x_{cm}=\frac{\varSigma _{i}m_{i}x_{i}}{\varSigma _{i}m_{i}}=\frac{(70\,\mathrm {k}\mathrm {g})(5\,\mathrm {m})+(40\,\mathrm {k}\mathrm {g})(-5\,\mathrm {m})}{(110\,\mathrm {k}\mathrm {g})}=1.36\,\mathrm {m}
```

Because the surface may be assumed to be frictionless, the resultant external force on the system is zero and therefore the center of mass must remain stationary at all times. Hence, if the boy has moved a distance of 2 $\mathrm {m}$, he will be at a distance of $-3\,\mathrm {m}$ from the origin. Thus, we have

```{math}
(1.36\,\mathrm {m})=\frac{(70\,\mathrm {k}\mathrm {g})x_{c}+(40\,\mathrm {k}\mathrm {g})(-3\,\mathrm {m})}{(110\,\mathrm {k}\mathrm {g})}
```

That gives $x_{c}=3.86\,\mathrm {m}$, therefore the distance moved by the container towards the center of mass is $(5\,\mathrm {m})-(3.86\,\mathrm {m})=1.14\,\mathrm {m}.$
:::
````

````{prf:example}
:label: example-6-9
:enumerator: 6.9

A boy is standing at the rear of a boat as shown in Fig. [](#fig-6-11). The masses of the boy and of the boat are 45 kg and 80 kg respectively Find the distance that the boat would move relative to the origin if the boy moves a distance of lm from the rear of the boat (the length of the boat is $5\,\mathrm {m}$).

```{figure} ../images/ch-06/459974_1_En_6_Fig11_HTML.png
:name: fig-6-11

A boy walking on a small boat
```

:::{admonition} Solution 6.9
:class: dropdown

By neglecting air and water resistance, the net external force on the $(\mathrm {b}\mathrm {o}\mathrm {y}+$ boat) system is zero. Therefore the center of mass of the system must remain at rest. Suppose that the boat is a symmetrical homogeneous object where its center of mass is at its geometrical center. The center of mass of the boat is therefore at a distance of 2.5 $\mathrm {m}$ from the origin. Thus, the center of mass of the system is

```{math}
\begin{aligned} x_{cm}&=\frac{\sum _{i=1}^{n}m_{i}x_{i}}{M}=\frac{m_{1}x_{1}+m_{2}x_{2}}{m_{1}+m_{2}}\\&=\frac{(45\,\mathrm {k}\mathrm {g})(0)+(80\,\mathrm {k}\mathrm {g})(2.5\,\mathrm {m})}{(125\,\mathrm {k}\mathrm {g})}=1.6\,\mathrm {m} \end{aligned}
```

If the boy moves a distance of 1 $\mathrm {m}$, the center of mass is still at the same position, and we have

```{math}
(1.6\,\mathrm {m})=\frac{(45\,\mathrm {k}\mathrm {g})(1\,\mathrm {m})+(80\,\mathrm {k}\mathrm {g})x_{b}}{(125\,\mathrm {k}\mathrm {g})}
```

That gives $x_{b}=1.94\,\mathrm {m}$. Thus, the displacement of the center of mass of the boat is $(1.94\,\mathrm {m})-(2.5\,\mathrm {m})=-0.56\,\mathrm {m}.$
:::
````

(sec-6-3-5)=

### 6.3.5 Velocity of the Center of Mass

The velocity of the center of mass of a system of particles that has a constant mass *M* is

```{math}
\mathbf {v}_{cm}=\frac{d\mathbf {r}_{cm}}{dt}=\frac{1}{M}\frac{d}{dt}\bigg (\sum _{i=1}^{n}m_{i}\mathbf {r}_{i}\bigg )=\frac{1}{M}\sum _{i=1}^{n}m_{i}\dot{\mathbf {r}}_{i}
```

where $\dot{\mathbf {r}}_{i}=d\mathbf {r}_{i}/dt $, or

```{math}
:label: eq-6-1

\begin{aligned} \displaystyle \mathbf {v}_{cm}=\sum _{i=1}^{n}\frac{m_i{{\mathbf {v}}i}}{M} \end{aligned}
```

where $\mathbf {v}_{i}$ is the ith particle velocity. The acceleration of the center of mass is given by

```{math}
\mathbf {a}_{cm}=\frac{d\mathbf {v}_{cm}}{dt}=\frac{1}{M}\frac{d}{dt}\bigg (\sum _{i=1}^{n}m_{i}\mathbf {v}_{i}\bigg )=\frac{1}{M}\sum _{i=1}^{n}m_{i}\ddot{\mathbf {r}}_{i}
```

```{math}
:label: eq-6-2

\begin{aligned} \displaystyle \mathbf {a}_{cm}=\frac{1}{M}\sum _{i=1}^{n}m_{i}\mathbf {a}_{i} \end{aligned}
```

where $\mathbf {a}_{i}$ is the acceleration of the ith particle.

(sec-6-3-6)=

### 6.3.6 Momentum of a System of Particles

The total linear momentum of a system of particles is the vector sum of the linear momenta of the individual particles:

```{math}
:label: eq-6-3

\begin{aligned} \displaystyle \sum _{i=1}^{n}m_{i}\mathbf {v}_{i}=\sum _{i=1}^{n}\mathbf {p}_{i}=\mathbf {p}_{tot} \end{aligned}
```

By using Eq. [](#eq-6-1)

```{math}
:label: eq-6-4

\begin{aligned} \mathbf {p}_{tot}=M\mathbf {v}_{cm} \end{aligned}
```

````{prf:example}
:label: example-6-10
:enumerator: 6.10

Two particles of masses $m_{1}=1 $ kg and $m_{2}=2 $ kg have position vectors given by $\mathbf {r}_{1}=(2t\mathbf {i}-4\mathbf {j})\,\mathrm {m}$ and $\mathbf {r}_{2}=(5t\mathbf {i}-2t\mathbf {j})\,\mathrm {m}$ respectively where *t* is time. Determine the velocity and linear momentum of the center of mass of the two- particle system at any time and at $t=1\,\mathrm {s}.$

:::{admonition} Solution 6.10
:class: dropdown

```{math}
\mathbf {r}_{cm}=\frac{\sum _{i}m_{i}\mathbf {r}_{i}}{\sum _{i}m_{i}}=\frac{(1\,\mathrm {k}\mathrm {g})(2t\mathbf {i}-4\mathbf {j})+(2\,\mathrm {k}\mathrm {g})(5t\mathbf {i}-2t\mathbf {j})}{(3\,\mathrm {k}\mathrm {g})}
```

That gives

```{math}
\mathbf {r}_{cm}=\left( 4t\mathbf {i}-\frac{4}{3}(t+1)\mathbf {j}\right) \,\mathrm {m}
```

```{math}
\mathbf {v}_{cm}=\frac{d\mathbf {r}_{cm}}{dt}=\left( 4\mathbf {i}-\frac{4}{3}\mathbf {j}\right) \,\mathrm {m}/\mathrm {s}
```

The total linear momentum is

```{math}
\mathbf {p}_{tot}=M\mathbf {v}_{cm}=(3\mathrm {k}\mathrm {g})\left( 4\mathbf {i}-\frac{4}{3}\mathbf {j}\right) =(12\mathbf {i}-4\mathbf {j})\,\mathrm {k}\mathrm {g}.\mathrm {m}/\mathrm {s}
```

at $t=1\mathrm {s}$

```{math}
\mathbf {r}_{cm}=(4\mathbf {i}-\frac{8}{3}\mathbf {j})\,\mathrm {m}
```

```{math}
\mathbf {v}_{cm}=(4\mathbf {i}-\frac{4}{3}\mathbf {j})\,\mathrm {m}/\mathrm {s}
```

and

```{math}
\mathbf {p}_{tot}=(12\mathbf {i}-4\mathbf {j})\,\mathrm {k}\mathrm {g}.\mathrm {m}/\mathrm {s}
```
:::
````

(sec-6-3-7)=

### 6.3.7 Motion of a System of Particles

From Newton’s second law Eq. [](#eq-6-2) can be written as

```{math}
:label: eq-6-5

\begin{aligned} \displaystyle \mathbf {a}_{cm}=\frac{1}{M}\sum _{i=1}^{n}\mathbf {F}_{i} \end{aligned}
```

where $\mathbf {F}_{i}$ is the net force acting on the ith particle. If both the external forces on the system and the internal forces between the particles in the system are included, then $\mathbf {F}_{i}$ may be written as

```{math}
:label: eq-6-6

\begin{aligned} \displaystyle \mathbf {F}_{i}=\mathbf {F}_{i(ext)}+\sum _{j}\mathbf {f}_{ij} \end{aligned}
```

Where $\mathbf {F}_{i(ext)}$ is the resultant external force acting on the ith particle.$\mathbf {f}_{ij}$ is the internal force exerted on the ith particle by the jth particle. Note that it is as- sumed that no force is exerted on the particle by itself, i.e.,$\mathbf {f}_{ii}=0 $. Substituting Eq. [](#eq-6-6) into Eq. [](#eq-6-5) gives:

```{math}
:label: eq-6-7

\begin{aligned} \displaystyle \mathbf {a}_{cm}=\frac{1}{M}\bigg (\sum _{i}\mathbf {F}_{i(ext)}+\sum _{i}\sum _{j}\mathbf {f}_{ij}\bigg ) \end{aligned}
```

Now, from Newton’s third law we have

```{math}
\mathbf {f}_{ij}=-\mathbf {f}_{ji}
```

Therefore, the second term in Eq. [](#eq-6-7) is equal to zero. Hence the net force acting on the system is due only to external forces. That gives

```{math}
\mathbf {F}_{net}=\sum _{i}\mathbf {F}_{i(ext)}=M\mathbf {a}_{cm}
```

where $\mathbf {F}_{net}$ is the resultant external force on the center of mass, i.e.,

```{math}
\mathbf {F}_{net}=\sum \mathbf {F}_{ext}=M\mathbf {a}_{cm}
```

By differentiating Eq. [](#eq-6-4) with respect to time we have

```{math}
M\mathbf {a}_{cm}=\frac{d\mathbf {p}_{tot}}{dt}
```

thus

```{math}
\sum \mathbf {F}_{ext}=\frac{d\mathbf {p}_{tot}}{dt}
```

Thus, the net external force acting on a system of particles is equal to the time rate of change of the total linear momentum of the system.

(sec-6-3-8)=

### 6.3.8 Conservation of Momentum

For an isolated system of particles, we have

```{math}
\sum \mathbf {F}_{ext}=0
```

Thus

```{math}
\frac{d\mathbf {p}_{tot}}{dt}=0
```

and

```{math}
\mathbf {p}_{tot}=M\mathbf {v}_{cm}=\text {constant}
```

Which is the law of conservation of linear momentum for a system of particles.

(sec-6-3-9)=

### 6.3.9 Angular Momentum of a System of Particles

The angular momentum $\mathbf {L}$ of a system of particles about a fixed point is the vector sum of angular momenta of the individual particles:

```{math}
\mathbf {L}=\mathbf {L}_{1}+\mathbf {L}_{2}+\mathbf {L}_{3}+\ +\mathbf {L}_{n}=\sum _{i=1}^{n}\mathbf {L}_{i}=\sum _{i=1}^{n}(\mathbf {r}_{i}\times \mathbf {p}_{i})=\sum _{i=1}^{n}m_{i}(\mathbf {r}_{i}\times \mathbf {v}_{i})
```

(sec-6-3-10)=

### 6.3.10 The Total Torque on a System

The total torque acting on a particle in a system is the sum of torques associated with the internal forces and of torques associated with external forces. Using Eq. [](#eq-6-6) we have

```{math}
\boldsymbol{\tau _{i}}=\mathbf {r}_{i}\times \mathbf {F}_{i}=\mathbf {r}_{i}\times \left( \mathbf {F}_{iext}+\sum _{j}\mathbf {f}_{ij}\right) =\mathbf {r}_{i}\times \mathbf {F}_{iext}+\sum _{j}\mathbf {r}_{i}\times \mathbf {f}_{ij}
```

Summing over $\mathrm {i}$ we get

```{math}
:label: eq-6-8

\begin{aligned} \displaystyle \sum _{i}\boldsymbol{\tau _{i}}=\sum _{i}\mathbf {r}_{i}\times \mathbf {F}_{i}=\sum _{i}\mathbf {r}_{i}\times \mathbf {F}_{iext}+\sum _{i}\sum _{j}\mathbf {r}_{i}\times \mathbf {f}_{ij} \end{aligned}
```

By using Newton’s third law of action and reaction, the double sum in Eq. [](#eq-6-8) has terms of the form

```{math}
\mathbf {r}_{i}\times \mathbf {f}_{ij}+\mathbf {r}_{j}\times \mathbf {f}_{ji}=(\mathbf {r}_{i}-\mathbf {r}_{j})\times \mathbf {f}_{ij}
```

Now, suppose that the internal forces between the two particles lie along the line joining the particles (i.e., the vectors $\mathbf {f}_{ij}$ and $(\mathbf {r}_{i}-\mathbf {r}_{j})$ have the same direction). This condition is known as the strong law of action and reaction. It requires the internal forces to be central. If the internal forces are equal and opposite but not central, then they are said to satisfy the weak law of action and reaction. The force of gravity is an example of a force satisfying the strong law of action and reaction. Some forces such as the forces between two moving charges are not central. From this, it follows that the double summation in Eq. [](#eq-6-8) is equal to zero.

```{math}
\boldsymbol{\tau _{net}}=\sum _{i}\boldsymbol{\tau _{i}}=\sum _{i}\mathbf {r}_{i}\times \mathbf {F}_{i}=\sum _{i}\mathbf {r}_{i}\times \mathbf {F}_{iext}
```

Therefore, the total torque on the system about the origin is only the torque associated with external forces

```{math}
:label: eq-6-9

\begin{aligned} \displaystyle \boldsymbol{\tau _{net}}=\sum \boldsymbol{\tau _{ext}}=\sum _{i=1}^{n}\mathbf {r}_{i}\times \mathbf {F}_{i(ext)} \end{aligned}
```

(sec-6-3-11)=

### 6.3.11 The Angular Momentum and the Total External Torque

The angular momentum of the individual particles may change with time. This will change the total angular momentum of the system

```{math}
\frac{d\mathbf {L}}{dt}=\sum _{i=1}^{n}\frac{d\mathbf {L}_{i}}{dt}
```

Eq. [](#eq-6-9) may be written as

```{math}
\displaystyle \boldsymbol{\tau _{net}}=\sum \boldsymbol{\tau _{ext}}=\sum _{i=1}^{n}\mathbf {r}_{i}\times \mathbf {F}_{i(ext)}=\frac{d}{dt} \bigg \{\sum _{i=1}^{n}m_{i}(\mathbf {r}_{i}\times \mathbf {v}_{i}) \bigg \}=\frac{d}{dt}\bigg \{\sum _{i=1}^{n}\mathbf {L}_{i} \bigg \}=\frac{d\mathbf {L}}{dt}
```

i.e., the net external torque about some origin exerted on a system of particles is equal to the time rate of change of the total angular momentum of the system.

(sec-6-3-12)=

### 6.3.12 Conservation of Angular Momentum

If

```{math}
\sum \boldsymbol{\tau _{ext}}=\mathbf {0}
```

```{math}
\displaystyle \mathbf {L}=\sum _{i=1}^{n}m_{i}(\mathbf {r}_{i}\times \mathbf {v}_{i})=\text {constant}
```

or

```{math}
\mathbf {L}_{i}=\mathbf {L}_{f}
```

Hence, if the resultant external torque acting on a system is zero, the total angular momentum remains constant.

(sec-6-3-13)=

### 6.3.13 Kinetic Energy of a System of Particles

The total kinetic energy of a system of particles is the sum of the kinetic energies of the individual particles

```{math}
K=\frac{1}{2}\sum _{i=1}^{n}m_{i}v_{i}^{2}
```

(sec-6-3-14)=

### 6.3.14 Work

Since the total force acting on the ith particle is given by

```{math}
\mathbf {F}_{i}=\mathbf {F}_{i(ext)}+\sum _{j}\mathbf {f}_{ij}
```

then the total work done on such particle is given by

```{math}
W_{12}=\sum _{i}\int _{1}^{2}\mathbf {F}_{i}\cdot d\mathbf {s}_{i}
```

(sec-6-3-15)=

### 6.3.15 Work–Energy Theorem

The total work done in moving a system from one state to another is

```{math}
W_{12}=\sum _{i}\int _{1}^{2}\mathbf {F}_{i}\cdot d\mathbf {s}_{i}=\sum _{i}\int _{1}^{2}\mathbf {F}_{i} \cdot \frac{d\mathbf {s}_{i}}{dt}dt=\sum _{i}\int _{1}^{2}\mathbf {F}_{i}\cdot \mathbf {v}_{i}dt
```

```{math}
=\sum _{i}\int _{1}^{2}\mathbf {v}_{i}\cdot \mathbf {F}_{i}dt=\sum _{i}\int _{1}^{2}\mathbf {v}_{i}\cdot \frac{d}{dt}(m_i \mathbf {v}_i)dt
```

Since

```{math}
\mathbf {v}_{i}\frac{d}{dt}(m_{i}\mathbf {v}_{i})=\frac{1}{2}\frac{d}{dt}(m_{i}(\mathbf {v}_{i}\cdot \mathbf {v}_{i}))=\frac{1}{2}\frac{d}{dt}(m_{i}v_{i}^{2})
```

it follows that

```{math}
W_{12}=\frac{1}{2}\sum _{i}\int _{1}^{2}\frac{d}{dt}(m_{i}v_{i}^{2})dt=\frac{1}{2}\sum _{i} \big (m_{i}v_{i}^{2} \big )|_{1}^{2}=K_{2}-K_{1}
```

where $\displaystyle \frac{1}{2}\sum _{i}m_{i}v_{i}^{2}$ is the total kinetic energy of the system.

(sec-6-3-16)=

### 6.3.16 Potential Energy and Conservation of Energy of a System of Particles

Consider a system of particles in which the external and internal forces acting on the system are conservative. First, let us calculate the work done by the internal conservative forces. Suppose that $\mathbf {f}_{ij}$ is the conservative force acting on the ith particle due to the jth particle and $\mathbf {f}_{ji}$ is the force acting on the jth particle due to the ith particle. Note that $\mathbf {f}_{ij}$ and $\mathbf {f}_{ji}$ form an action and reaction pair, i.e.,$\mathbf {f}_{ij}=-\mathbf {f}_{ji}$. Because these forces are conservative there is a potential energy associated with each force. That is,

```{math}
\mathbf {f}_{ij}=-\nabla _{i}U_{ij}
```

and

```{math}
\mathbf {f}_{ji}=-\nabla _{j}U_{ij}
```

From the law of action and reaction,$U_{ij}$ is a function only of the distance between the particles. That is

```{math}
U_{ij}=U_{ij}(|\mathbf {r}_{i}-\mathbf {r}_{j}|)=U_{ji}(|\mathbf {r}_{i}-\mathbf {r}_{j}|)
```

or

```{math}
U_{ij}(r_{ij})=U_{ji}(r_{ji})
```

where $|\mathbf {r}_{i}-\mathbf {r}_{j}|=r_{ij}=r_{ji}$ is the distance between the ith and jth particles. The work done by each pair of forces in displacing the ith and jth particles through $d\mathbf {r}_{i}$ and $d\mathbf {r}_{j}$, respectively, is

```{math}
\mathbf {f}_{ij}\cdot d\mathbf {r}_{i}+\mathbf {f}_{ji}\cdot d\mathbf {r}_{j}=-\nabla _{i}U_{ij}\cdot d\mathbf {r}_{i}-\nabla _{j}U_{ij}\cdot d\mathbf {r}_{j}
```

```{math}
=-\bigg [\frac{\partial U_{ij}}{\partial x_{i}}dx_{i}+\frac{\partial U_{ij}}{\partial y_{i}}dy_{i}+\frac{\partial U_{ij}}{\partial z_{i}}dz_{i}+\frac{\partial U_{ij}}{\partial x_{j}}dx_{j}+\cdots \cdots \cdots \bigg ]=-dU_{ij}
```

Hence, the total work done by the internal conservative forces in moving the system from stage 1 to stage 2 is

```{math}
\begin{aligned} W_{12(in, c)}&=\displaystyle \sum _{i}\sum _{j}\int _{1}^{2}\mathbf {f}_{ij}\cdot d\mathbf {r}_{i}=-\frac{1}{2}\sum _{i}\sum _{j}\int _{1}^{2}dU_{ij}\\&=-\frac{1}{2}\sum _{i}\sum _{j}U_{ij} |_{1}^{2}=U_{1(\mathrm {i}\mathrm {n}\mathrm {t})}-U_{2(\mathrm {i}\mathrm {n}\mathrm {t})}=-\triangle U_{(\mathrm {i}\mathrm {n}\mathrm {t})} \end{aligned}
```

The factor 1/2 occurs since each term in the summation appears twice. Now, consider the total work done by the external conservative forces

```{math}
W_{12(ext, c)}=\displaystyle \sum _{i}\int _{1}^{2}\mathbf {F}_{i(ext)} . d\mathbf {s}_{i}=-\sum _{i}\int _{1}^{2}\nabla _{i}U_{i}\cdot d\mathbf {s}_{i} =-\sum _{i}U_{i} |_{1}^{2}=U_{1(ext)}-U_{2(ext)}
```

To show that energy is conserved when both the external and internal forces are conservative, we may define a total potential of the system as

```{math}
U=\sum _{i}U_{i}+\frac{1}{2}\sum _{i}\sum _{j}U_{ij}
```

From the work–energy theorem, the work done by the total force $\mathrm {F}_{i}$ acting on the ith particle is equal to the change in the kinetic energy of that particle

```{math}
W_{12}=\sum _{i}\int _{1}^{2}\mathbf {F}_{i}\cdot d\mathbf {r}_{i}=K_{2}-K_{1}
```

and since

```{math}
W_{12}=W_{12(in, c)}+W_{12(ext, c)}
```

From this, we conclude that for a system of particles in which the internal and external forces are conservative, the total mechanical energy of the system is conserved

```{math}
U_{1(\mathrm {i}\mathrm {n}\mathrm {t})}-U_{2(\mathrm {i}\mathrm {n}\mathrm {t})}+U_{1(ext)}-U_{2(ext)}=K_{2}-K_{1}
```

or

```{math}
U_{1}-U_{2}=K_{2}-K_{1}
```

or

```{math}
\triangle K=-\triangle U
```

Thus

```{math}
\triangle K+\triangle U=0
```

```{math}
\triangle E=0
```

(sec-6-3-17)=

### 6.3.17 Impulse

In Sect. [](#sec-6-3-7), we have seen that the net external force on a system of particles is equal to the rate of change of the total linear momentum of the system

```{math}
\mathbf {F}_{net}=\frac{d\mathbf {p}_{tot}}{dt}
```

The total linear impulse on the system as the system goes from one state to another is defined as

```{math}
\mathbf {I}=\int _{t_{1}}^{t_{2}}\mathbf {F}_{net}dt=\int _{t_{1}}^{t_{2}}\frac{d\mathbf {p}_{tot}}{dt}dt=\mathbf {p}_{tot2}-\mathbf {p}_{tot1}
```

That is, the total linear impulse on the system is equal to the change in the total momentum of the system.

(sec-6-4)=

## 6.4 Motion Relative to the Center of Mass

The motion of a system of particles is sometimes described relative to the center of mass of the system. This method is used in some problems to simplify the analysis and add a particular symmetry to it.

```{figure} ../images/ch-06/459974_1_En_6_Fig12_HTML.png
:name: fig-6-12

The position vector $(\mathbf {r}_{i}')$ of the ith particle relative to the center of mass
```

(sec-6-4-1)=

### 6.4.1 The Total Linear Momentum of a System of Particles Relative to the Center of Mass

The position vector of the center of mass of the system with respect to an origin in an inertial frame of reference (for example, the lab frame) is given by

```{math}
:label: eq-6-10

\begin{aligned} \displaystyle \mathbf {r}_{cm}=\frac{\varSigma _{i}^{n} m_{i}\mathbf {r}_{i}}{M} \end{aligned}
```

From Fig. [](#fig-6-12), the position vector $(\mathbf {r}_{i}')$ of the ith particle relative to the center of mass is

```{math}
\mathbf {r}_{i}'=\mathbf {r}_{i}-\mathbf {r}_{cm}
```

or

```{math}
:label: eq-6-11

\begin{aligned} \mathbf {r}_{i}=\mathbf {r}_{i}'+\mathbf {r}_{cm} \end{aligned}
```

Where $\mathbf {r}_{i}$ is the position vector of the ith particle relative to the origin O. Substituting Eq. [](#eq-6-11) into Eq. [](#eq-6-10) gives

```{math}
\mathbf {r}_{cm}=\frac{1}{M}\sum _{i=1}^{n}m_{i}(\mathbf {r}_{i}'+\mathbf {r}_{cm})=\frac{1}{M}\sum _{i=1}^{n}m_{i}\mathbf {r}_{i}'+\frac{\sum _{i=1}^{n}m_{i}}{M}\mathbf {r}_{cm}
```

```{math}
=\frac{1}{M}\sum _{i=1}^{n}m_{i}\mathbf {r}_{i}'+\mathbf {r}_{cm}
```

therefore

```{math}
\frac{1}{M}\sum _{i=1}^{n}m_{i}\mathbf {r}_{i}'=\mathbf {r}_{cm}-\mathbf {r}_{cm}=0
```

That gives

```{math}
:label: eq-6-12

\begin{aligned} \displaystyle \sum _{i=1}^{n}m_{i}\mathbf {r}_{i}'=\mathbf {0} \end{aligned}
```

Differentiating Eq. [](#eq-6-12) with respect to *t* gives

```{math}
:label: eq-6-13

\begin{aligned} \displaystyle \sum _{i=1}^{n}m{{\mathbf {v}_{i}'=}}\mathbf {0} \end{aligned}
```

or

```{math}
\sum _{i=1}^{n}\mathbf {p}_{i}'=\mathbf {0}
```

or

```{math}
\mathbf {p}'=\mathbf {0}
```

That is, the total linear momentum of the system is zero when observed from the center of mass frame.

(sec-6-4-2)=

### 6.4.2 The Total Angular Momentum About the Center of Mass

By differentiating Eq. [](#eq-6-11) with respect to time gives

```{math}
:label: eq-6-14

\begin{aligned} \mathbf {v}_{i^{=}}\mathbf {v}_{i}'+\mathbf {v}_{cm} \end{aligned}
```

where $\mathbf {v}_{i}$ and $\mathbf {v}_{i}'$ are the velocities of the particle relative to the origin $\mathrm {O}$ and the center of mass respectively $\mathbf {v}_{cm}$ is the velocity of the center of mass relative to O. The angular momentum of the system about the origin $\mathrm {O}$ is

```{math}
\mathbf {L}=\sum _{i}m_{i}(\mathbf {r}_{i}\times \mathbf {v}_{i})=\sum _{i}m_{i}\{(\mathbf {r}_{i}'+\mathbf {r}_{cm})\times (\mathbf {v}_{i}'+\mathbf {v}_{cm})\}
```

```{math}
=\displaystyle \sum _{i}m_{i}(\mathbf {r}_{i}'\times \mathbf {v}_{i}')+\sum _{i}m_{i}(\mathbf {r}_{i}'\times \mathbf {v}_{cm})+\sum _{i}m_{i}(\mathbf {r}_{cm}\times \mathbf {v}_{i}')+\sum _{i}m_{i}(\mathbf {r}_{cm}\times \mathbf {v}_{cm})
```

The second and third terms are zero followed from Eqs. [](#eq-6-12) and [](#eq-6-13) where $\left( \displaystyle \sum _{i}m_{i}\mathbf {r}_{i}'\right) \times \mathbf {v}_{cm}=\mathbf {0}$ and $\displaystyle \mathbf {r}_{cm}\times \left( \sum _{i}m_{i}\mathbf {v}_{i}'\right) =\mathbf {0}$, hence

```{math}
\mathrm {L}=\sum _{i}m_{i}(\mathbf {r}_{i}'\times \mathbf {v}_{i}')+\sum _{i}m_{i}(\mathbf {r}_{cm}\times \mathbf {v}_{cm})
```

Thus, the total angular momentum of the system of particles about an origin $\mathrm {O}$ equals the angular momentum of the system about the center of mass plus the angular momentum of the center of mass about O. Therefore, the total angular momentum $\mathbf {L}'$ about the center of mass is

```{math}
:label: eq-6-15

\begin{aligned} \displaystyle \mathbf {L}'=\sum _{i}m_{i}(\mathbf {r}_{i}'\times \mathbf {v}_{i}')=\sum _{i}m_{i}(\mathbf {r}_{i}\times \mathbf {v}_{i})-M(\mathbf {r}_{cm}\times \mathbf {v}_{cm}) \end{aligned}
```

(sec-6-4-3)=

### 6.4.3 The Total Kinetic Energy of a System of Particles About the Center of Mass

The total kinetic energy of a system of particles relative to an origin in an inertial frame of reference is given by

```{math}
K=\frac{1}{2}\sum _{i}m_{i}v_{i}^{2}=\frac{1}{2}\sum _{i}m_{i}(\mathbf {v}_{i}\cdot \mathbf {v}_{i})
```

From Eq. [](#eq-6-14) we have

```{math}
K=\frac{1}{2}\sum _{i}m_{i}((\mathbf {v}_{i}'+\mathbf {v}_{cm})\cdot (\mathbf {v}_{i}'+\mathbf {v}_{cm}))
```

```{math}
=\frac{1}{2}\sum _{i}m_{i}(\mathbf {v}_{i}'\cdot \mathbf {v}_{i}')+\sum _{i}m_{i}(\mathbf {v}_{i}'\cdot \mathbf {v}_{cm})+\frac{1}{2}\sum _{i}m_{i}(\mathbf {v}_{cm}\cdot \mathbf {v}_{cm})
```

```{math}
=\frac{1}{2}\sum _{i}m_{i}v_{i}^{\prime 2}+\mathbf {v}_{cm}\cdot \bigg (\sum _{i}m_{i}\mathbf {v}_{i}'\bigg )+\frac{1}{2}\bigg (\sum _{i}m_{i}\bigg )v_{cm}^{2}
```

From Eq. [](#eq-6-13), the term in brackets in the second term is equal to zero. Hence

```{math}
K=\frac{1}{2}\sum _{i}m_{i}v_{i}^{\prime 2}+\frac{1}{2}Mv_{cm}^{2}
```

That is the total kinetic energy of a system of particles about an origin is equal to the kinetic energy of the system with respect to the center of mass plus the kinetic energy of the center of mass relative to the origin O. Therefore, the total kinetic energy of the system with respect to the center of mass is

```{math}
K'=\frac{1}{2}\sum _{i}m_{i}v_{i}^{\prime 2}=\frac{1}{2}\sum _{i}m_{i}v_{i}^{2}-\frac{1}{2}Mv_{cm}^{2}
```

(sec-6-4-4)=

### 6.4.4 Total Torque on a System of Particles About the Center of Mass of the System

The total torque acting on a system of particles about the center of mass is (from theorem (5.6.1)) equal to the time rate of change of the angular momentum of the system about the center of mass. That is,

```{math}
\boldsymbol{\tau '}=\frac{d\mathbf {L}'}{dt}
```

````{prf:example}
:label: example-6-11
:enumerator: 6.11

Two particles of masses $m_{1}=1 $ kg and $m_{2}=2 $ kg are moving in the x-y plane. Their position vectors relative to the origin are $\mathbf {r}_{1}=(t^{2}\mathbf {i}-2t\mathbf {j})\,\mathrm {m}$ and $\mathbf {r}_{2}=(3t\mathbf {i}+\mathbf {j})\,\mathrm {m}$ where *t* is time. Find: (a) the total angular momentum of the system; the total external torque acting on the system; and the total kinetic energy of the system all relative to the origin at any time; (b) repeat (a) relative to the center of mass.

:::{admonition} Solution 6.11
:class: dropdown

(a)

```{math}
\mathbf {v}_{1}=\frac{d\mathbf {r}_{1}}{dt}=(2t\mathbf {i}-2\mathbf {j})\,\mathrm {m}/\mathrm {s}
```

```{math}
\mathbf {v}_{2}=\frac{d\mathbf {r}_{2}}{dt}=(3\mathbf {i})\,\mathrm {m}/\mathrm {s}
```

The total angular momentum of the system relative to the origin is

```{math}
\displaystyle \mathbf {L}=\sum _{i}m_{i}(\mathbf {r}_{i}\times \mathbf {v}_{i})=(1)[(t^{2}\mathbf {i}-2t\mathbf {j})\times (2t\mathbf {i}-2\mathbf {j})] +(2)[(3t\mathbf {i}+\mathbf {j})\times (3)\mathbf {i}]
```

that gives

```{math}
\mathbf {L}=((2t^{2}-6)\mathbf {k})\,\mathrm {kg}.\mathrm {m}^{2}/\mathrm {s}
```

The total kinetic energy of the system relative to $\mathrm {O}$ is

```{math}
K=\displaystyle \frac{1}{2}\sum _{i=1}^{n}m_{i}v_{i}^{2}=\frac{1}{2}(m_{1}v_{1}^{2}+m_{2}v_{2}^{2})=\frac{1}{2}[(1)(4t^{2}+4)+(2)(9)]=(2t^{2}+11) \; \mathrm {J}
```

The net external torque about the origin is

```{math}
\displaystyle \sum \boldsymbol{\tau _{ext}}=\frac{d\mathbf {L}}{dt}=((4t)\mathbf {k})\,\text {N.m}
```

(b) To find the total angular momentum relative to the center of mass let’s find first the total angular momentum of the center of mass relative to the origin

```{math}
\mathbf {r}_{cm}=\frac{\sum _{i}m_{i}\mathbf {r}_{i}}{\sum _{i}m_{i}}=\frac{(1)(t^{2}\mathbf {i}-2t\mathbf {j})+(2)(3t\mathbf {i}+\mathbf {j})}{(3)}
```

```{math}
=\bigg (\bigg (\frac{t^{2}}{3}+2t\bigg )\mathbf {i}+\bigg (\frac{2}{3}-\frac{2}{3}t\bigg )\mathbf {j}\bigg )\,\mathrm {m}
```

The velocity of the center of mass is

```{math}
\mathbf {v}_{cm}=\bigg (\bigg (\frac{2}{3}t+2\bigg )\mathbf {i}-\bigg (\frac{2}{3}\bigg )\mathbf {j}\bigg )\,\mathrm {m}/\mathrm {s}
```

and the total angular momentum of the center of mass relative to $\mathrm {O}$ is

```{math}
\displaystyle \mathbf {L}_{cm}=M(\mathbf {r}_{cm}\times \mathbf {v}_{cm})=(3)\bigg [\bigg (\bigg (\frac{t^{2}}{3}+2t\bigg )\mathbf {i}+\bigg (\frac{2}{3}-\frac{2}{3}t\bigg )\mathbf {j}\bigg )\times \bigg (\bigg (\frac{2}{3}t+2\bigg )\mathbf {i}-\bigg (\frac{2}{3}\bigg )\mathbf {j}\bigg )\bigg ]
```

```{math}
=\bigg (-\bigg (\frac{2}{3}t^{2}+\frac{4}{3}t+4\bigg )\mathbf {k}\bigg )\,\mathrm {k}\mathrm {g}.\mathrm {m}^{2}/\mathrm {s}
```

From Eq. [](#eq-6-15), the total angular momentum relative to the center of mass is

```{math}
\mathbf {L}'=\sum _{i}m_{i}(\mathbf {r}_{i}'\times \mathbf {v}_{i}')=\sum _{i}m_{i}(\mathbf {r}_{i}\times \mathbf {v}_{i})-M(\mathbf {r}_{cm}\times \mathbf {v}_{cm})
```

```{math}
=(2t^{2}-6)\displaystyle \mathbf {k}+\bigg (\frac{2t^{2}}{3}+\frac{4}{3}t+4\bigg )\mathbf {k}=\bigg (\bigg (\frac{8}{3}t^{2}+\frac{4}{3}t-2\bigg )\mathbf {k}\bigg )\,\mathrm {kg}.\mathrm {m}^{2}/\mathrm {s}
```

The net external torque about the center of mass is

$\displaystyle \boldsymbol{\tau '}=\frac{d\mathbf {L}'}{dt}=\bigg (\bigg (\frac{16}{3}t+\frac{4}{3}\bigg )\mathbf {k}\bigg )\,\mathrm {N.m}$

The total kinetic energy of the system relative to the center of mass is

```{math}
K'=\frac{1}{2}\sum _{i}m_{i}v_{i}^{\prime 2}=\sum _{i}m_{i}v_{i}^{2}-\frac{1}{2}Mv_{cm}^{2}
```

```{math}
=(2t^{2}+11)-\frac{1}{2}(3)\bigg [\bigg (\frac{2}{3}t+ 2\bigg )^{2}+\frac{4}{9}\bigg ]=\bigg (\frac{4t^{2}}{3}-2t-\frac{13}{3}\bigg ) \; \mathrm {J}
```
:::
````

````{prf:example}
:label: example-6-12
:enumerator: 6.12

Two particles of equal mass *m* are rotating about their center of mass with a constant speed *v* as in Fig. [](#fig-6-13). If they are separated by a distance 2*d*, find the total angular momentum of the system.

:::{admonition} Solution 6.12
:class: dropdown

```{math}
L=mvd+mvd=2mvd
```
:::
````

```{figure} ../images/ch-06/459974_1_En_6_Fig13_HTML.png
:name: fig-6-13

Two particles rotating about their center of mass
```

(sec-6-4-5)=

### 6.4.5 Collisions and the Center of Mass Frame of Reference

In problems involving collisions, it is useful to use an inertial frame of reference that is attached to the center of mass to analyze the collision. This method is most commonly used in analyzing collisions between subatomic particles or atoms. In section (6.4.1), we proved that the total linear momentum of a system when observed from the center of mass frame is equal to zero.

```{math}
:label: eq-6-16

\begin{aligned} \mathbf {p}_{i}'=\mathbf {p}_{f}'=\mathbf {0} \end{aligned}
```

Now consider a system consisting of two bodies undergoing a one-dimensional collision (see Fig. [](#fig-6-14)). Then from Eq. [](#eq-6-16) we have

```{math}
p_{1i}'=-p_{2i}'
```

and

```{math}
p_{1f}'=-p_{2f}'
```

That is, when viewed from the center of mass frame the two objects approach each other with equal and opposite momenta and move away from each other with an equal and opposite momenta. Therefore, the center of mass frame simplifies the analysis since it exhibits a particular symmetry to the problem (see Fig. [](#fig-6-15)).

```{figure} ../images/ch-06/459974_1_En_6_Fig14_HTML.png
:name: fig-6-14

Consider a system consisting of two bodies undergoing a one-dimensional collision
```

```{figure} ../images/ch-06/459974_1_En_6_Fig15_HTML.png
:name: fig-6-15

The center of mass frame analysis of a collision
```

```{figure} ../images/ch-06/459974_1_En_6_Fig16_HTML.png
:name: fig-6-16

A rocket is projected vertically upward and explodes into three fragments of equal mass when it reaches the top of its flight at an altitude of 40 $\mathrm {m}$
```

````{prf:example}
:label: example-6-13
:enumerator: 6.13

A rocket is projected vertically upward and explodes into three fragments of equal mass when it reaches the top of its flight at an altitude of 40 $\mathrm {m}$(see Fig. [](#fig-6-16)). If the two fragments land to the ground after 3 $\mathrm {s}$ from the explosion, find the time it takes the third fragment to hit the ground.

:::{admonition} Solution 6.13
:class: dropdown

When the rocket reaches the top its velocity immediately before explosion is zero. Since $\mathbf {v}_{1},\mathbf {v}_{2}$ and $\mathbf {v}_{3}$ are the velocities of the fragments immediately after explosion, we have from the conservation of momentum

```{math}
m_{1}\mathbf {v}_{1}+m_{2}\mathbf {v}_{2}+m_{3}\mathbf {v}_{3}=\mathbf {0}
```

Since $m_{1}=m_{2}=m_{3}$, then $ v_{1}+v_{2}+v_{3}=0 $. The first and second fragments land at the same time $ t'$and hence they have the same vertical velocity initially which is equal to $-v_{3}/2 $. Therefore

```{math}
h=v_{3}t+\frac{gt^{2}}{2}
```

and

```{math}
h=\frac{-v_{3}t'}{2}+\frac{gt'2}{2}
```

That gives

```{math}
v_3=\frac{g(t^{\prime 2}-t^{2})}{2t+t'}
```

and

```{math}
h=\frac{gtt'(t+2t')}{2(2t+t')}
```

Substituting the values of *h* and $t'$ gives

$29.4t^{2}+160t+63.6=0 $

Thus,$t=2.3\,\mathrm {s}.$
:::
````

````{prf:example}
:label: example-6-14
:enumerator: 6.14

Find the center of mass of the Earth–Moon System and describe its motion around the sun.

```{figure} ../images/ch-06/459974_1_En_6_Fig17_HTML.png
:name: fig-6-17

The center of mass of the Earth-Moon system
```

:::{admonition} Solution 6.14
:class: dropdown

As we shall see in Chap. [](#ch-9), the center of mass of two bodies with different masses moving under gravity will trace an ellipse. Since the external forces on the sun can be neglected, we may consider it to be at rest in an inertial frame of reference and at the origin of a coordinate system (see Fig. [](#fig-6-17)). The center of mass of the Earth–Moon system is

```{math}
\mathbf {r}_{cm}=\frac{M_{E}\mathbf {r}_{E}+M_{M}\mathbf {r}_{M}}{M_{E}+M_{M}}
```

where $\hat{\mathbf {r}}_{E}$ and $\hat{\mathbf {r}}_{M}$ are unit vectors in the direction of $\mathbf {r}_{E}$ and $\mathbf {r}_{M}$ respectively. The equation of motion of the center of mass is

```{math}
\mathbf {F}=(M_{E}+M_{M})\ddot{\mathbf {r}}_{cm}
```

The gravitational force on the Earth–Moon system exerted by the sun is

```{math}
\mathbf {F}=-GM_{S}\left( \frac{M_{E}}{r_{E}^{2}}\hat{\mathbf {r}}_{E}+\frac{M_{M}}{r_{M}^{2}}\hat{\mathbf {r}}_{M}\right)
```

Since the distance between the earth and the moon is so small compared to their distance from the sun we may write $r_{E}\approx r_{M}\approx r_{cm}$

```{math}
\mathbf {F}=-\frac{GM_{S}}{r_{cm}^{2}}(M_{E}+M_{M})\hat{\mathbf {r}}_{cm}=(M_{E}+M_{M})\ddot{\mathbf {r}}_{cm}
```

Hence, the center of mass of the Earth–Moon system moves as a single planet of mass $(M_{E}+M_{M})$ about the sun as shown in Fig. [](#fig-6-18).
:::
````

```{figure} ../images/ch-06/459974_1_En_6_Fig18_HTML.png
:name: fig-6-18

The center of mass of the Earth-Moon system moves as a single planet of mass $(M_{E}+M_{M})$ about the sun
```

````{prf:example}
:label: example-6-15
:enumerator: 6.15

Describe the motion of a rocket in space using the law of conservation of momentum.

```{figure} ../images/ch-06/459974_1_En_6_Fig19_HTML.png
:name: fig-6-19

A rocket moving in space is a system with varying mass. Its motion is analyzed using the law of conservation of momentum
```

:::{admonition} Solution 6.15
:class: dropdown

A rocket moving in space is a system with varying mass. Its motion is analyzed using the law of conservation of momentum. In order for a rocket to move in space, its fuel is burned and gases are produced and ejected from its rear. This will cause the mass of the rocket to decrease continuously The ejected gases produce momentum in the backward direction and as a result the rocket receives a forward momentum and its velocity increases (see Fig. [](#fig-6-19)). Suppose at an instant *t*, the rocket has a mass *M* and velocity *v* relative to a stationary frame of reference. During a time interval t, a mass $\triangle m $ of the fuel is expelled as gas with a velocity *u* relative to the rocket. The speed of the rocket increases to $v+\triangle v $ and the speed of the fuel relative to the stationary frame of reference is $v-u $. The initial momentum of the rocket is

```{math}
\mathbf {p}(t)=(M+\triangle m)\mathbf {v}
```

and the final momentum is

```{math}
\mathbf {p}(t+\triangle t)=M(\mathbf {v}+\triangle \mathbf {v})+\triangle m\ (\mathbf {v}-\mathbf {u})
```

The change in the momentum is

```{math}
\triangle \mathbf {p}(t+\triangle t)=\mathbf {p}(t+\triangle t)-\mathbf {p}(t)=M\triangle \mathbf {v}-(\triangle m)\mathbf {u}
```

Therefore, the force acting on the rocket is

```{math}
\mathbf {F}=\frac{d\mathbf {p}}{dt}=\lim _{\triangle t\rightarrow 0}\frac{\triangle {\mathbf {p}}}{\triangle t}=M\frac{d\mathbf {v}}{dt}-\mathbf {u}\frac{dm}{dt}
```

Since the increase in the exhaust mass produce an equal decrease in the rocket mass, we have

```{math}
dm=-dM
```

Thus

```{math}
\mathbf {F}=M\frac{d\mathbf {v}}{dt}+\mathbf {u}\frac{dM}{dt}
```

If no external forces act on the rocket we have $\mathbf {F}=\mathbf {0}$ and

```{math}
M\frac{d\mathbf {v}}{dt}=-\mathbf {u}\frac{dM}{dt}
```

hence

```{math}
\int _{t_{0}}^{t}\frac{d\mathbf {v}}{dt}dt=-\mathbf {u}\int _{M_{0}}^{M}\frac{1}{M}\frac{dM}{dt}dt=-\mathbf {u}\int _{M_{0}}^{M}\frac{dM}{M}
```

That gives

```{math}
\mathbf {v}-\mathbf {v}_{0}=\mathbf {u}\ln \left( \frac{M_{0}}{M}\right)
```

Therefore, the final speed of the rocket depends on the exhaust speed and on the ratio of the initial and final masses.
:::
````

```{figure} ../images/ch-06/459974_1_En_6_Fig20_HTML.png
:name: fig-6-20

A system of particles in x-y plane
```

```{figure} ../images/ch-06/459974_1_En_6_Fig21_HTML.png
:name: fig-6-21

A homogenous sheet with a hole
```

```{figure} ../images/ch-06/459974_1_En_6_Fig22_HTML.png
:name: fig-6-22

A homogenous sheet in the x-y plane
```

## Problems

```{exercise}
:label: prob-6-1
:enumerator: 6.1

Find the coordinate of the center of mass of the system shown in Fig. [](#fig-6-20).
```

```{exercise}
:label: prob-6-2
:enumerator: 6.2

Find the center of mass of a uniform plate bounded by $y=-0.24x^{2}+6 $ and the $\mathrm {x}$-axis from $ x=-5 $to $ x=5\,\mathrm {m}.$
```

```{exercise}
:label: prob-6-3
:enumerator: 6.3

Find the center of mass of the homogeneous sheet shown in Fig. [](#fig-6-21).
```

```{exercise}
:label: prob-6-4
:enumerator: 6.4

Find the center of mass of the homogeneous sheet shown in Fig. [](#fig-6-22).
```

```{exercise}
:label: prob-6-5
:enumerator: 6.5

Find the center of mass of a uniform solid circular cone of radius *a* and height *h*.
```

```{exercise}
:label: prob-6-6
:enumerator: 6.6

Find the center of mass of a uniform solid hemisphere of radius *R*.
```

```{exercise}
:label: prob-6-7
:enumerator: 6.7

Two masses initially at rest are located at the points shown in Fig. [](#fig-6-23). If external forces act on the particles as in Fig. [](#fig-6-23), find the acceleration of the center of mass.
```

```{exercise}
:label: prob-6-8
:enumerator: 6.8

A projectile of mass 15 kg is fired from the ground with an initial velocity of 12 $\mathrm {m}/\mathrm {s}$ at an angle of $45^{\mathrm {o}}$ to the horizontal. 1 second later, the projectile explodes into two fragments A and B. If immediately after explosion, fragment A has a mass of 5 kg and a speed of 5 $\mathrm {m}/\mathrm {s}$ at an angle of $30^{\mathrm {o}}$ to the horizontal, find the velocity of fragment B (assuming air resistance is neglected).
```

```{exercise}
:label: prob-6-9
:enumerator: 6.9

Two boys of masses 45 and 40 kg are standing on a boat of mass 150 kg and length 5 $\mathrm {m}$ as in Fig. [](#fig-6-24). The boat is initially lm from the pier. Assuming that there is no friction between the boat and the water, find the distance moved by the boat when the two meet at the middle of the boat.
```

```{exercise}
:label: prob-6-10
:enumerator: 6.10

Two particles of masses $m_{1}=3 $ kg and $m_{2}=5 $ kg are moving relative to the lab frame with velocities of 10 $\mathrm {m}/\mathrm {s}$ along the $\mathrm {y}$-axis and 15 $\mathrm {m}/\mathrm {s}$ at an angle of $30^{\mathrm {o}}$ to the $\mathrm {x}$-axis. Find (a) the velocity of their center of mass (b) the momentum of each particle in the center of mass frame (c) the total kinetic energy of the particles relative to the lab frame and relative to the center of mass frame.
```

```{exercise}
:label: prob-6-11
:enumerator: 6.11

Two particles of masses $m_{1}=1 $ kg and $m_{2}=2 $ kg are moving relative to the lab frame with velocities of $\mathbf {v}_{1}=2\mathbf {i}-3\mathbf {j}+\mathbf {k}$ and $\mathbf {v}_{2}=7\mathbf {i}+\mathbf {j}-2\mathbf {k}$. If at a certain instant they are located at $(-1,1,2)$ and (3, 0, 1), find the angular momentum of the system relative to the origin and relative to the center of mass.
```

```{figure} ../images/ch-06/459974_1_En_6_Fig23_HTML.png
:name: fig-6-23

The acceleration of the center of mass of two masses acted upon by different forces
```

```{figure} ../images/ch-06/459974_1_En_6_Fig24_HTML.png
:name: fig-6-24

By neglecting friction between the boat and water, the center of mass can be used to find the distance moved by the boat
```
