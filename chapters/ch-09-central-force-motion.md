---
title: 9. Central Force Motion
short_title: "Ch. 9 — Central Force Motion"
label: ch-9
doi: 10.1007/978-3-030-15195-9_9
---

(sec-9-1)=
## 9.1 Motion in a Central Force Field

A force is said to be central under two conditions. First, the direction of the force must always be toward or away from a fixed point (see Fig. [](#fig-9-1)). This point is known as the center of the force. Second, the magnitude of the force should only be proportional to the distance *r* between the particle and the center of the force. The central force may be written as

```{math}
\begin{aligned} \mathbf {F}=f(r)\mathbf {r}_{1} \end{aligned}
```

where $\mathbf {r}_{1}$ is a unit vector in the direction of $\mathbf {r}$. Therefore, if $f(r)<0$, then the central force is an attractive force since it is directed toward the center of the force $\mathrm {O}$ (as shown in Fig. [](#fig-9-1)) and if $f(r)>0$, the force is repulsively directed away from O.

````{prf:example}
:label: example-9-1
:enumerator: 9.1

Which of the following forces are repulsive and which are attractive? $(\mathrm {a})\mathbf {F}= \displaystyle \frac{-3}{\sqrt{r}}\mathbf {r}_{1}(\mathrm {b})\mathbf {F}=4r^{2}\mathbf {r}_{1}(\mathrm {c})\mathbf {F}=r(r-2)\mathbf {r}_{1}.$

:::{admonition} Solution 9.1
:class: dropdown

(a) Attractive, (b) repulsive, and (c) attractive if $0<r<2$ and repulsive if $r>2.$
:::
````

(sec-9-1-1)=
### 9.1.1 Properties of a Central Force

1.The resulting motion of the particle takes place in a plane. To show that we have from Eq. 9.1

```{math}
\mathbf {F}=f(r)\mathbf {r}_{1}=m\mathbf {a}
```

thus, a is parallel to $\mathbf {r}(\mathbf {r}=\mathrm {r}\mathbf {r}_1)$ and we may write

```{math}
\mathbf {r}\times \mathbf {a}=\mathbf {0}
```

Hence,

```{math}
\mathbf {r}\times \frac{d\mathbf {v}}{dt}=\mathbf {0}
```

or

```{math}
\frac{d}{dt}(\mathbf {r}\times \mathbf {v})=\mathbf {0}
```

Thus,

```{math}
\begin{aligned} \mathbf {r}\times \mathbf {v}=\mathbf {h}= \text {constant} \end{aligned}
```

where $\mathbf {h}$ is a constant vector. Therefore, $\mathbf {r}$ and $\mathbf {v}$ always lie in the same plane where $\mathbf {h}$ is perpendicular to that plane for every value of *t*. As a result, the path of the particle takes place in a plane. 2.The angular momentum of the particle is conserved. From Eq. 9.2, we have

```{math}
m(\mathbf {r}\times \mathbf {v})=m\mathbf {h}
```

or

```{math}
\mathbf {L}=m\mathbf {h}=\text {constant}
```

Thus, the angular momentum is equal to a constant at all times (conserved). 3.The position vector $\mathbf {r}$ of the particle with respect to the center of force sweeps out equal areas in equal times or in other words, the areal velocity is constant. To show that, consider the plane of motion to be the x–y plane. During an infinitesimally small time interval *dt*, the radius vector $\mathbf {r}$ sweeps out an area equal to *dA*. From Fig. [](#fig-9-2), this area is equal to half of the area of a parallelogram with sides $\mathrm {r}$ and *d*r. That is,

```{math}
d\mathbf {A}=\frac{1}{2}|\mathbf {r}\times d\mathbf {r}|
```

or

```{math}
d\mathbf {A}=\frac{1}{2}|\mathbf {r}\times \mathbf {v}dt|
```

or

```{math}
\frac{d\mathbf {A}}{dt}=\frac{1}{2}|\mathbf {r}\times \mathbf {v}|
```

Thus,

```{math}
\displaystyle \frac{dA}{dt}=\frac{h}{2}= \text {constant}
```

```{figure} ../images/ch-09/459974_1_En_9_Fig1_HTML.png
:name: fig-9-1

The central force
```

```{figure} ../images/ch-09/459974_1_En_9_Fig2_HTML.png
:name: fig-9-2

During an infinitesimally small time interval *dt*, the radius vector $\mathbf {r}$ sweeps out an area equal to *dA*
```

(sec-9-1-2)=
### 9.1.2 Equations of Motion in a Central Force Field

The most convenient coordinate system to describe the motion of a particle, under the influence of a central force, is the polar coordinate system. This convenience lies in the fact that the central force is in the $\mathrm {r}$-direction. In Sect. 2.​6, it has been shown that the acceleration of a particle in a plane, in terms of its polar coordinates, is given by

```{math}
\mathbf {a}=(\ddot{r}-r\dot{\theta }^{2})\mathbf {r}_{1}+(r\ddot{\theta }+2 \dot{r}\dot{\theta })\boldsymbol{\theta }_{1}
```

Applying Newton’s second law to the particle gives

```{math}
\mathbf {F}=m\mathbf {a}
```

```{math}
f(r)\mathbf {r}_{1}=m[(\ddot{r}-r\dot{\theta }^{2})\mathbf {r}_{1}+(r\ddot{\theta }+2\dot{r}\dot{\theta })\boldsymbol{\theta }_{1}]
```

That gives

```{math}
\begin{aligned} f(r)=m(\ddot{r}-r\dot{\theta }^{2}) \end{aligned}
```

```{math}
\begin{aligned} m(r\ddot{\theta }+2\dot{r}\dot{\theta })=0 \end{aligned}
```

In Sect. 2.​6, we’ve also seen that the velocity of a particle in polar coordinates is given by

```{math}
\mathbf {v}=\dot{r}\mathbf {r}_{1}+r\dot{\theta }\boldsymbol{\theta }_{1}
```

Therefore, we have

```{math}
\mathbf {r}\times \mathbf {v}=r\mathbf {r}_{1}\times (\dot{r}\mathbf {r}_{1}+r\dot{\theta }\boldsymbol{\theta }_{1})=r\dot{r}\ (\mathbf {r}_{1}\times \mathbf {r}_{1})+r^{2}\dot{\theta }(\mathbf {r}_{1}\times \boldsymbol{\theta }_{1})
```

```{math}
=\mathbf {0}+r^{2}\dot{\theta }(\mathbf {r}_{1}\times \boldsymbol{\theta }_{1})=\mathbf {h}
```

Taking the plane of motion to be the x–y plane, then $\mathbf {r}_{1}\times \boldsymbol{\theta }_{1}$ is parallel to the $\mathrm {z}$-direction and we have

```{math}
\mathbf {h}=r^{2}\dot{\theta }\mathbf {k}=h\mathbf {k}
```

Hence,

```{math}
\begin{aligned} r^{2}\dot{\theta }=h \end{aligned}
```

and Eq. 9.2 can be written as

```{math}
\frac{d}{dt}(r^{2}\dot{\theta })=0
```

or

```{math}
r^{2}\dot{\theta }= \text {constant}
```

Substituting Eq. 9.5 into Eq. 9.3 gives

```{math}
\begin{aligned} f(r)=m\bigg (\displaystyle \ddot{r}-\frac{h^{2}}{r^{3}}\bigg ) \end{aligned}
```

Let $u=1/r$, then $\dot{r}=-\dot{u}(1/u^{2})$. Since $r^{2}\dot{\theta }=h$, we have $u^{2}=\dot{\theta }/h$. Thus

```{math}
\begin{aligned} \displaystyle \dot{r}=-h\bigg (\frac{\dot{u}}{\dot{\theta }}\bigg )=-h\bigg (\frac{du/dt}{d\theta /dt}\bigg )=-h\bigg (\frac{du}{d\theta }\bigg ) \end{aligned}
```

And

```{math}
\ddot{r}=\frac{d}{dt}\bigg (-h\frac{du}{d\theta }\bigg )=\frac{d}{d\theta }\bigg (-h\frac{du}{d\theta }\bigg )\frac{d\theta }{dt}
```

```{math}
\begin{aligned} \displaystyle \ddot{r}=-h\bigg (\frac{d^{2}u}{d\theta ^{2}}\bigg )\dot{\theta }=-h^{2}u^{2}\bigg (\frac{d^{2}u}{d\theta ^{2}}\bigg ) \end{aligned}
```

Substituting Eq. 9.8 into Eq. 9.6 gives

```{math}
f(1/u)=m\big (-h^{2}u^{2}\bigg (\frac{d^{2}u}{d\theta ^{2}}\bigg )-h^{2}u^{3}\big )
```

or

```{math}
\begin{aligned} \displaystyle \frac{d^{2}u}{d\theta ^{2}}+u=\frac{-1}{mh^{2}u^{2}}f(1/u) \end{aligned}
```

This is the equation of path in a central force field.

(sec-9-1-3)=
### 9.1.3 Potential Energy of a Central Force

Consider a particle moving from point $P_{1}$ to $P_{2}$ (see Fig. [](#fig-9-3)) while a central force that has its center at the origin acts on it. The path of the particle may be considered as a combination of radial and curved segments. The central force is always acting in the direction of the radial segments and is perpendicular to the displacement along any of the curved segments. Thus, the work done by the central force along any curved segment is zero and the total work done in moving the particle along any path is equal to the work done along a radial line from $\mathrm {r}_{i}$ to $\mathrm {r}_{f}$ (see Fig. [](#fig-9-4)). That is, the work done by a central force is independent of path. It depends only on the initial and final positions of the particle.

```{figure} ../images/ch-09/459974_1_En_9_Fig3_HTML.png
:name: fig-9-3

A particle moving from point $P_{1}$ to $P_{2}$, while a central force that has its center at the origin acts on it
```

```{figure} ../images/ch-09/459974_1_En_9_Fig4_HTML.png
:name: fig-9-4

The central force is always acting in the direction of the radial segments and is perpendicular to the displacement along any of the curved segments. Therefore, the total work done in moving the particle along any path is equal to the work done along a radial line from $\mathrm {r}_{i}$ to $\mathrm {r}_{f}$
```

From this, we conclude that the central force is a conservative force. You may also prove that $\nabla \times \mathbf {F}=\mathbf {0}$. Hence, there exists a potential energy and the work done by the gravitational force may be written as

```{math}
W=-\triangle U
```

The work done in moving the particle from $P_{1}$ to $P_{2}$ is

```{math}
W=\int _{P_{1}}^{P_{2}}\mathbf {F}\cdot d\mathbf {r}=\int _{r_{i}}^{r_{f}}f(r)\mathbf {r}_{1}\cdot d\mathbf {r}=\int _{r_{i}}^{r_{f}}f(r)\frac{\mathbf {r}}{r}\cdot d\mathbf {r}
```

Since $\mathbf {r}\cdot d\mathbf {r}=rdr$, we have

```{math}
W=\int _{r_{i}}^{r_{f}}f(r)dr
```

or

```{math}
\begin{aligned} \displaystyle \triangle U=U_{f}-U_{i}=-\int _{r_{i}}^{r_{f}}f(r)dr \end{aligned}
```

(sec-9-1-4)=
### 9.1.4 The Total Energy

Since $\mathrm {F}$ is a conservative force, it follows that the total energy is conserved (constant), that is,

```{math}
E=\frac{1}{2}mv^{2}+U(r)
```

Since

```{math}
v^{2}=\mathbf {v}\cdot \mathbf {v}=\dot{r}^{2}+r^{2}\dot{\theta }^{2}
```

we have

```{math}
\begin{aligned} E=\displaystyle \frac{1}{2}m(\dot{r}^{2}+r^{2}\dot{\theta }^{2})+U(r) \end{aligned}
```

Substituting Eqs. 9.5 and 9.7 into Eq. 9.11 gives

```{math}
E=\frac{1}{2}m\bigg (h^{2}\bigg (\frac{du}{d\theta }\bigg )^{2}+\bigg (\frac{1}{u^{2}}\bigg )(hu^{2})^{2}\bigg )+U
```

or

```{math}
\begin{aligned} \bigg (\displaystyle \frac{du}{d\theta }\bigg )^{2}+u^{2}=\frac{2(E-U)}{mh^{2}} \end{aligned}
```

(sec-9-2)=
## 9.2 The Law of Gravity

In 1687, Isaac Newton made a remarkable discovery. Newton stated that the force that holds planets in their orbit is the same force that makes an apple fall from a tree. Newton’s law of gravity states that *every particle in the universe attracts every other particle with a force that is directly proportional to the product of the masses of the particles and inversely proportional to the square of the distance between them*. The magnitude of this gravitational force is given by

```{math}
F=\frac{Gm_{1}m_{2}}{r^{2}}
```

where $m_{1}$ and $m_{2}$ are the masses of the particles, *r* is the distance between them, and *G* is the universal gravitational constant. *G* has the same value if the particles (or objects) are located anywhere in the universe and it is given by

```{math}
G=6.672\times 10^{-11}\,\mathrm {N}.\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2}
```

The gravitational force is effective when one or both the masses are very large. This is because *G* is a very small number. Note that, the gravitational force is not a contact force; it is a field force that can act through any medium. The direction of the gravitational force is along the line joining the two particles.

Therefore, the gravitational force is a central force since its magnitude is proportional only to the distance between the two particles (where one of the particles can be considered as the center of force), and its direction is along the line joining them (toward the center of force).

```{figure} ../images/ch-09/459974_1_En_9_Fig5_HTML.png
:name: fig-9-5

Two particles of masses $m_{1}$ and $m_{2}$. Each particle exerts a gravitational force on the other
```

Figure [](#fig-9-5) shows two particles of masses $m_{1}$ and $m_{2}$. Each particle exerts a gravitational force on the other. Let the gravitational force exerted on $m_{2}$ by $m_{1}$ to be $\mathbf {F}_{21}$, and that exerted on $m_{1}$ by $m_{2}$ to be $\mathbf {F}_{12}$. From Newton’s third law of action and reaction, we have

```{math}
\mathbf {F}_{12}=-\mathbf {F}_{21}
```

That is, the two forces form an action and reaction pair. In terms of unit vectors, we may write

```{math}
\mathbf {F}_{21}=-\frac{Gm_{1}m_{2}}{r_{12}^{2}}\mathbf {r}_{12}
```

and

```{math}
\mathbf {F}_{12}=-\frac{Gm_{1}m_{2}}{r_{21}^{2}}\mathbf {r}_{21}
```

where $\mathrm {r}_{12}$ is a unit vector that is directed along the line joining the two particles (directed from $m_{1}$ to $m_{2}$) and $\mathbf {r}_{21}$ is a unit vector directed from $m_{2}$ to $m_{1}$. The negative sign indicates that the force is attractive. That is, the force exerted on $m_{1}$ by $m_{2}$ will move $m_{1}$ in the direction opposite of $\mathrm {r}_{21}$, i.e., toward $m_{2}$. Where the force exerted on $m_{2}$ by $m_{1}$ will move $m_{2}$ opposite to $\mathrm {r}_{12}$ (toward $m_{1}$). If particle $\mathrm {P}$ of mass of $m_{P}$ interacts with a system of particles, the resultant gravitational force $\mathbf {F}_{P}$ exerted on particle $\mathrm {P}$ due to all particles in the system is the vector sum of the individual forces that each particle in the system exerts on particle $\mathrm {P}$:

```{math}
\mathbf {F}_{P}=\sum _{i=1}^{n}\mathbf {F}_{Pi}=\sum _{i=1}^{n}\frac{-Gm_{P}m_{i}}{r_{iP}^{2}}\mathbf {r}_{iP}
```

where $\mathbf {r}_{iP}$ is a unit vector directed from the ith particle in the system toward the particle $\mathrm {P}$ and $\mathbf {F}_{Pi}$ is the force exerted on particle $\mathrm {P}$ by the *i*th particle. If particle $\mathrm {P}$ of mass *m* interacts with an extended body of mass *M*, the resultant gravitational force $\mathbf {F}_{P}$ exerted on particle $\mathrm {P}$ is the vector sum of the individual forces $d\mathbf {F}$ exerted on particle $\mathrm {P}$ due to each mass element *dM* in the object, but in this case, the sum is replaced by an integral

```{math}
\mathbf {F}_{P}=\int d\mathbf {F}=-Gm\ \int \frac{dM}{r^{2}}\mathbf {r}_{1}
```

where $\mathbf {r}_{1}$ is a unit vector directed from the mass element *dM* to the particle as shown in Fig. [](#fig-9-6). The force of gravity gives planets and other heavy celestial bodies their spherical shape. That is because as the mass of the body becomes larger the force of gravity becomes stronger and all particles from all sides are attracted evenly toward the center. As a result, the body tends to have a spherical shape.

```{figure} ../images/ch-09/459974_1_En_9_Fig6_HTML.png
:name: fig-9-6

A particle $\mathrm {P}$ of mass *m* interacting with an extended body of mass *M*
```

````{prf:example}
:label: example-9-2
:enumerator: 9.2

Two particles of masses $m_{1}=0.2$ kg and $m_{2}=0.3$ kg are separated by a distance of 0.05 $\mathrm {m}$. Find (a) the gravitational force that each particle exerts on the other; (b) at what distance a third particle $m_{3}=0.5$ kg must be placed at the other side of $m_{1}$ such that the net gravitational force on $m_{1}$ is zero. (All particles lie on a straight line).

:::{admonition} Solution 9.2
:class: dropdown

(a)

```{math}
F_{12}=F_{21}=\displaystyle \frac{Gm_{1}m_{2}}{r_{12}^{2}}=\frac{(6.67\times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(0.2 \; \mathrm {k}\mathrm {g})(0.3 \; \mathrm {k}\mathrm {g})}{(0.05 \; \mathrm {m})^{2}}=1.6 \; \times 10^{-9}\mathrm {N}
```

(b)

```{math}
F_{13}=\frac{Gm_{1}m_{3}}{r_{31}^{2}}
```

```{math}
F_{12}=\frac{Gm_{1}m_{2}}{r_{21}^{2}}
```

If the net force on $m_{1}$ is zero, we have

```{math}
\sum F_{1}=F_{13}-F_{12}=0
```

or

```{math}
F_{13}=F_{12}
```

```{math}
\frac{Gm_{1}m_{3}}{r_{31}^{2}}=\frac{Gm_{1}m_{2}}{r_{21}^{2}}
```

that gives

```{math}
r_{31}^{2}=\frac{m_{3}}{m_{2}}r_{21}^{2}=\frac{(0.5 \; \mathrm {k}\mathrm {g})}{(0.3 \; \mathrm {k}\mathrm {g})}(0.05 \; \mathrm {m})^{2}
```

```{math}
r_{31}=0.064 \; \mathrm {m}
```
:::
````

(sec-9-2-1)=
### 9.2.1 The Gravitational Force Between a Particle and a Uniform Spherical Shell

**Case I: A Particle outside the Shell** Consider a particle of mass *m* located outside a uniform spherical shell at point $\mathrm {P}$ as in Fig. [](#fig-9-7). Imagine this shell to be made of a large number of thin rings each of outer thickness $Rd\theta$ and inner thickness *l*. The ring is so thin (since $d\theta$ is used) that every particle in the ring is at a distance *s* from P Furthermore, each particle in the ring exerts a gravitational force on the particle at P.

```{figure} ../images/ch-09/459974_1_En_9_Fig7_HTML.png
:name: fig-9-7

Because $\mathbf {F}_{1}$ and $\mathbf {F}_{2}$ are equal in magnitude, then their $\mathrm {y}$ components cancel each other out and their $\mathrm {x}$ components add up
```

From the symmetry of the ring, if a particle (1) on the upper side exerts a gravitational force $\mathbf {F}_{1}$ on *m*, there is always another particle (2) at the opposite side of the ring exerting another force ($\mathbf {F}_{2}$) on the particle. Because $\mathbf {F}_{1}$ and $\mathbf {F}_{2}$ are equal in magnitude, then their $\mathrm {y}$ components cancel each other out and their $\mathrm {x}$ components add up (see Fig. [](#fig-9-7)). Thus, the resultant force exerted on *m* due to all particles of the sphere is the sum of the $\mathrm {x}$ components of their forces. Therefore the resultant force on *m* is along the $\mathrm {x}$ direction (toward the center of the shell). The gravitational force exerted on *m* by a thin ring of mass *dM* is

```{math}
dF_{g}=\frac{GmdM}{s^{2}}\cos \phi
```

To express *dM* in terms of the density of the ring, we find the volume of the thin ring

```{math}
dV=(2\pi R\sin \theta )(Rd\theta )l=2\pi lR^{2}\sin \theta d\theta
```

Since the shell has a uniform volume density $\rho , dM$ is given by

```{math}
dM=\rho dV=\rho 2\pi lR^{2}\sin \theta d\theta
```

Thus,

```{math}
\begin{aligned} dF_{g}=\displaystyle \frac{2\pi \rho lmGR^{2}\cos \phi \sin \theta d\theta }{s^{2}} \end{aligned}
```

From Fig. [](#fig-9-7),

```{math}
\begin{aligned} \displaystyle \cos \phi =\frac{r-R\cos \theta }{s} \end{aligned}
```

From the cosines law, we have

```{math}
\begin{aligned} s^{2}=R^{2}+r^{2}-2Rr\cos \theta \end{aligned}
```

Substituting Eqs. 9.14 and 9.15 into Eq. 9.13 gives

```{math}
\begin{aligned} dF_{g}=\displaystyle \frac{2\pi \rho lmGR^{2}(r-R\cos \theta )\sin \theta d\theta }{(r^{2}+R^{2}-2rR\cos \theta )^{3/2}} \end{aligned}
```

From Eq. 9.15, we have

```{math}
2sds=2rR\sin \theta d\theta
```

To integrate over all rings, $\theta$ will change from $\theta =0$ to $\pi$. From Eq. 9.15, we have at $\theta =0, s=r-R$ since $(r\ge R)$, and at $\theta =\pi , s=r+R$. Also, we have from Eq. 9.15

```{math}
\cos \theta =\frac{R^{2}+r^{2}-s^{2}}{2rR}
```

Thus

```{math}
r-R\cos \theta =\frac{r^{2}+s^{2}-R^{2}}{2r}
```

Substituting this into Eq. 9.16 gives

```{math}
\begin{aligned} F_{g}=\displaystyle \frac{\pi G\rho lRm}{r^{2}}\int _{r-R}^{r+R}\bigg (1+\frac{r^{2}-R^{2}}{s^{2}}\bigg )ds=\frac{4\pi G\rho lR^{2}m}{r^{2}} \end{aligned}
```

Since $4\pi R^{2}\rho l=M$, it follows that

```{math}
F_{g}=\frac{GMm}{r^{2}}
```

That is, the spherical shell behaves as a particle of mass *M* located at its center.

**Case II: A Particle inside the Shell** If a particle is inside a uniform spherical shell, the derivation of the gravitational force exerted on the particle by the spherical shell is the same as if the particle were outside the shell, except that the lower integration limit is different. At $\theta =0, s=R-r$ since $r<R$. Thus, we have

```{math}
F_{g}=\frac{\pi G\rho lRm}{r^{2}}\int _{R-r}^{r+R}\bigg (1+\frac{r^{2}-R^{2}}{s^{2}}\bigg )ds=0
```

where $r<R$. That is, if the particle is inside the shell, the gravitational force exerted on it by the shell is zero. However, objects outside the shell may still exerts forces on the particle. In summary, we have

```{math}
F_{g}=\frac{GMm}{r^{2}} \; (r\ge R)
```

```{math}
F_{g}=0 \; (r<R)
```

Figure [](#fig-9-8) shows the force exerted on a particle as a function of its location.

```{figure} ../images/ch-09/459974_1_En_9_Fig8_HTML.png
:name: fig-9-8

The force exerted on a particle as a function of its $\mathrm {r}$
```

(sec-9-2-2)=
### 9.2.2 The Gravitational Force between a Particle and a Uniform Solid Sphere

**Case I: A Particle outside the Sphere** Consider a particle of mass *m* located outside a uniform solid sphere. The sphere may be considered to be made of a series of concentric spherical shells. The force exerted on the particle by each shell is given by

```{math}
dF_{g}=\frac{GdMm}{r^{2}}
```

The mass of each shell is $dM=\rho dV=\rho 4\pi a^{2}da$. Where $\rho$ is the volume density of the sphere and *a* is the distance from the shell to the center of the sphere and *da* is the thickness of the shell, Hence,

```{math}
dF_{g}=\frac{Gm\rho 4\pi a^{2}da}{r^{2}}
```

The total force exerted on *m* by the sphere is

```{math}
F_{g}=\frac{Gm\rho 4\pi }{r^{2}}\int _{0}^{R}a^{2}da
```

```{math}
F_{g}=\frac{G(\rho ^{4}/{3}\pi R^{3})m}{r^{2}}
```

```{math}
\begin{aligned} F_{g}=\displaystyle \frac{GMm}{r^{2}} \end{aligned}
```

Thus, the solid sphere behaves as a particle of mass *M* located at the center of the sphere.

```{figure} ../images/ch-09/459974_1_En_9_Fig9_HTML.png
:name: fig-9-9

If a particle of mass *m* is located inside a uniform solid sphere of mass *M*, then the gravitational force exerted on the particle is due only to the part of the sphere of radius $r<R$ and of mass of $\mathrm {M}$
```

**Case II: A Particle inside the Sphere** If a particle of mass *m* is located inside a uniform solid sphere of mass *M*, then the gravitational force exerted on the particle is due only to the part of the sphere of radius $r<R$ and of mass of $\mathrm {M}$ (see Fig. [](#fig-9-9)). The remaining part of the sphere is a spherical shell which exerts no force on the particle since the particle is located inside it. From Eq. 9.18, the gravitational force exerted on the particle due to a sphere of radius *r* and mass $M_{1}$ is given by

```{math}
\begin{aligned} F_{g}=\displaystyle \frac{GM_{1}m}{r^{2}} \end{aligned}
```

Since the sphere has a uniform density, we have

```{math}
\rho =\frac{M_{1}}{V_{1}}=\frac{M}{V}
```

or

```{math}
\frac{M_{1}}{M}=\frac{V_{1}}{V}=\frac{4/3{\pi r^{3}}}{4/3{\pi R^{3}}}=\frac{r^{3}}{R^{3}}
```

or

```{math}
\begin{aligned} M_{1}=M\displaystyle \frac{r^{3}}{R^{3}} \end{aligned}
```

Substituting Eq. 9.20 into Eq. 9.19 gives

```{math}
F_{g}=\frac{GmMr}{R^{3}}
```

where $r<R$. Therefore at the center of the sphere,

```{math}
F_{g}=0
```

Figure [](#fig-9-10) shows the force exerted on a particle as a function of its location.

```{figure} ../images/ch-09/459974_1_En_9_Fig10_HTML.png
:name: fig-9-10

The force exerted on a particle as a function of its $\mathrm {r}$
```

````{prf:example}
:label: example-9-3
:enumerator: 9.3

(a) Find the gravitational force exerted on a particle of mass *m* that is at a distance of *a* from a thin rod of mass *M* and length *L* as in Fig. [](#fig-9-11); (b) find the force in (a) if $a\gg L.$
````

```{figure} ../images/ch-09/459974_1_En_9_Fig11_HTML.png
:name: fig-9-11

The force exerted on a particle of mass *m* that is at a distance of *a* from a thin rod of mass *M* and length *L*
```

(a)

```{math}
dF=\frac{GmdM}{x^{2}}
```

since the rod is uniform we have

```{math}
dM=\lambda dx=\frac{M}{L}dx
```

Thus

```{math}
dF=\frac{GmM}{Lx^{2}}dx
```

Integrating from *a* to $a+L$ gives

```{math}
F=\displaystyle \frac{GmM}{L}\int _{a}^{a+L}\frac{dx}{x^{2}}=\frac{GmM}{L}\bigg [\frac{-1}{x}\bigg ]_{a}^{a+L}=\frac{GmM}{L}\bigg [\frac{1}{a}-\frac{1}{a+L}\bigg ]=\frac{GmM}{a(a+L)}
```

In vector form,

```{math}
\mathbf {F}=\frac{GmM}{a(a+L)}\mathbf {i}
```

(b) if $a\gg L$, then

```{math}
\mathbf {F}=\frac{GmM}{a^{2}}\mathbf {i}
```

That is, the rod can be considered as a particle of mass *M* that is at a distance *a* from *m*.

````{prf:example}
:label: example-9-4
:enumerator: 9.4

Find the gravitational force exerted on a particle of mass *m* that is at a distance *a* from the center of a uniform solid disk of radius *R* and mass *M* as shown in Fig. [](#fig-9-12).
````

```{figure} ../images/ch-09/459974_1_En_9_Fig12_HTML.png
:name: fig-9-12

The gravitational force exerted on a particle of mass *m* that is at a distance *a* from the center of a uniform solid disk of radius *R* and mass *M*
```

Let us divide the disk into thin concentric rings of radius *r* and thickness *dr*. By symmetry, the resultant force on the particle is directed along the axis of the ring, since the $\mathrm {y}$-components of the forces exerted by all particles of the ring will cancel out, where their $\mathrm {x}$-components will add up. That is,

```{math}
dF=\frac{GdMm\cos \theta }{r^{2}+a^{2}}
```

Since the mass element *dM* is given by $dM=\sigma (2\pi rdr)$, we have

```{math}
dF=\frac{G\sigma (2\pi rdr)m\cos \theta }{r^{2}+a^{2}}
```

or

```{math}
dF=\frac{G\sigma (2\pi rdr)ma}{(r^{2}+a^{2})^{3_{/2}}}
```

The total force is

```{math}
F=2\pi G\sigma ma\int _{r=0}^{R}\frac{rdr}{(r^{2}+a^{2})^{3_{/2}}}=\pi G\sigma ma\bigg [\frac{(r^2+a^2)^{-1/2}}{-1/2} \bigg ]_{0}^{R}
```

```{math}
F=2\pi G\sigma m\bigg [1-\frac{a}{\sqrt{a^{2}+R^{2}}}\bigg ]
```

````{prf:example}
:label: example-9-5
:enumerator: 9.5

A uniform solid sphere has a mass of 4.7 kg and a radius of 0.05 $\mathrm {m}$. Find the magnitude of the gravitational force that the sphere exerts on a 0.02 kg particle located at (a) 0.5 $\mathrm {m}$ from the center of the sphere; (b) 0.03 $\mathrm {m}$ from the center of the sphere; (c) at the surface of the sphere; (d) at the center of the sphere.

:::{admonition} Solution 9.5
:class: dropdown

(a)

```{math}
F_{1s}=\displaystyle \frac{GmM}{r^{2}}=\frac{(6.67\times 10^{-11} \; \mathrm {N} \mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(0.02 \; \mathrm {k}\mathrm {g})(4.7 \; \mathrm {k}\mathrm {g})}{(0.5 \; \mathrm {m})^{2}}=2.5\times 10^{-11} \; \mathrm {N}
```

(b)

```{math}
F_{1s}=\displaystyle \frac{GmMr}{R^{3}}=\frac{(6.67\times 10^{-11} \; \mathrm {N} \mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(0.02 \;\mathrm {k}\mathrm {g})(4.7 \;\mathrm {k}\mathrm {g})(0.03 \; \mathrm {m})}{(0.05 \; \mathrm {m})^{3}}=1.5\times 10^{-9} \; \mathrm {N}
```

(c)

```{math}
F_{1s}=\displaystyle \frac{GmM}{R^{2}}= \frac{(6.67\times 10^{-11} \; \mathrm {N} \mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(0.02 \; \mathrm {k}\mathrm {g})(4.7 \; \mathrm {k}\mathrm {g})}{(0.05 \; \mathrm {m}^{2})}=2.5\times 10^{-9} \; \mathrm {N}
```

(d)

```{math}
F_{1s}=0
```
:::
````

````{prf:example}
:label: example-9-6
:enumerator: 9.6

Three concentric spherical shells have masses of $M_{1}, M_{2}$, and $M_{3}$ and radius of $R_{1}, R_{2}$, and $R_{3}$, respectively, as in Fig. [](#fig-9-13). Find the gravitational force exerted on a particle of mass *m* located at (a) $r=a(\mathrm {b})r=b(\mathrm {c})r=c(\mathrm {d})r=d.$
````

```{figure} ../images/ch-09/459974_1_En_9_Fig13_HTML.png
:name: fig-9-13

Three concentric spherical shells
```

(a)

```{math}
F=0
```

(b)

```{math}
F=\frac{GM_{1}m}{b^{2}}
```

(c)

```{math}
F=\frac{GM_{1}m}{c^{2}}+\frac{GM_{2}m}{c^{2}}=\frac{Gm}{c^{2}}(M_{1}+M_{2})
```

(d)

```{math}
F=\frac{Gm}{d^{2}}(M_{1}+M_{2}+M_{3})
```

````{prf:example}
:label: example-9-7
:enumerator: 9.7

A spaceship of mass $m_{1}$ is moving along a straight line path between the earth and the sun. At what distance from the center of the earth will the gravitational force of the sun balances that of the earth?

:::{admonition} Solution 9.7
:class: dropdown

At that point, we have

```{math}
F_{1E}=F_{1S}
```

```{math}
\frac{Gm_{1}M_{E}}{r^{2}}=\frac{Gm_{1}M_{S}}{(d-r)^{2}}
```

or

```{math}
\frac{(d-r)^{2}}{r^{2}}=\frac{M_{S}}{M_{E}}
```

```{math}
r=\frac{d[M_{E}-(M_{E}M_{S})^{1_{/2}}]}{M_{E}-M_{S}}
```
:::
````

````{prf:example}
:label: example-9-8
:enumerator: 9.8

An artificial satellite is moving in a circular orbit about the earth at a distance of 1500 km above the earth’s surface. Find its speed and period.

:::{admonition} Solution 9.8
:class: dropdown

```{math}
\frac{Gm_{s}M_{E}}{r^{2}}=\frac{m_{s}v^{2}}{r}
```

```{math}
v=\sqrt{\frac{GM_{E}}{r}}
```

where *r* is the distance between the center of the earth and the satellite. That is,

```{math}
r=(6.37\times 10^{6}\mathrm {m})+(1500\times 10^{3}\mathrm {m})=7.9\times 10^{6}\mathrm {m}
```

Hence,

```{math}
v=\sqrt{\frac{GM_{E}}{r}}=\sqrt{\frac{(6.67\times 10^{-11}\mathrm {N}\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(5.98\times 10^{24}\mathrm {k}\mathrm {g})}{(7.9\times \mathrm {l0}^{6}\mathrm {m})}}=7.1\times 10^{3}\mathrm {m}/\mathrm {s}
```

```{math}
T=\frac{2\pi r}{v}=\frac{2(3.1.4)(7.9\times 10^{6}\mathrm {m})}{(71\times 10^{3}\mathrm {m}/\mathrm {s})}=6968.8\mathrm {s}=116.15\min
```
:::
````

(sec-9-2-3)=
### 9.2.3 Weight and Gravitational Force

In Chap. 4, we’ve seen that the weight of an object is defined as the gravitational force exerted on the object by the earth (or any other astronomical object) and it is directed toward the center of the earth. The weight of an object is given by $\mathbf {w}=m\mathbf {g}$, where $\mathbf {g}$ is the free-falling acceleration and its value near the earth’s surface is 9.8 $\mathrm {m}/\mathrm {s}^{2}$. The exact form of the gravitational force between any two objects was given earlier in this chapter by Newton’s law of gravity In the case of an earth–particle system, the gravitational force that each one exerts on the other is

```{math}
F_{g}=\frac{GM_{E}m}{r^{2}}
```

where $M_{E}$ is the mass of the earth and *m* is the mass of the particle that is at a distance *r* from the center of the earth. Note that, it is assumed that the earth is a perfect sphere of uniform mass distribution, and therefore behaves as a particle. In reality, the earth is not a perfect sphere but rather an ellipsoid. Furthermore, the earth’s density is not uniform since it varies with the radius of earth.

The earth’s density also varies at the earth’s surface from one region to another. In addition, if the earth’s rotation is included, then the resultant force on an object will be its weight plus the centripetal force exerted on the object due to the rotation. However, these variations are often neglected. From the definition of weight, we have

```{math}
w=mg=F_{g}=\frac{GM_{E}m}{r^{2}}
```

therefore

```{math}
\begin{aligned} g=\displaystyle \frac{GM_{E}}{r^{2}} \end{aligned}
```

As you can see the free-falling acceleration does not depend on the mass of the object as was predicted before. If the object is falling near the earth’s surface, then distance *r* in Eq. 9.21 can be replaced by $R_{E}$ which is the radius of the earth and we have

```{math}
g=\frac{GM_{E}}{R_{E}^{2}}
```

If the object is at a distance *h* from the earth’s surface, we may write

```{math}
g=\frac{GM_{E}}{(R_{E}+h)^{2}}
```

Thus, the weight of an object decreases with increasing altitude. Table 9.1 shows the variation of *g* with altitude.

| Altitude *h* (km) | $g\,(\mathrm{m}/\mathrm{s}^2)$ |
| --- | --- |
| 1000 | 7.34 |
| 6000 | 2.6 |
| 10000 | 1.49 |
| 30000 | 0.3 |
| 60000 | 0.09 |

````{prf:example}
:label: example-9-9
:enumerator: 9.9

A man can jump vertically upward from the earth’s surface and reach an altitude of 0.2 $\mathrm {m}$. Find the altitude the man can reach if he jumps with the same initial velocity on the surface of the moon.

:::{admonition} Solution 9.9
:class: dropdown

Using the formula $y-y_{0}=\frac{v^{2}-v_{0}^{2}}{-2g}$ and by taking $y_{0}=0$ at the earth’s surface and $y=h$ at the maximum height and that $v=0$ there, we have

```{math}
h=\frac{v_{0}^{2}}{2g}
```

Since the initial velocity of the man is the same on earth and on moon, we have

```{math}
h_{E}g_{E}=h_{m}g_{m}
```

At the surface of the moon

```{math}
g_{m}=\frac{GM_{m}}{R_{m}^{2}}=\frac{(6.67\times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(7.36\times 10^{22} \; \mathrm {k}\mathrm {g})}{(1.74\times \mathrm {l0}^{6} \; \mathrm {m})^{2}}=1.6 \; \mathrm {m}/\mathrm {s}^{2}
```

```{math}
h_{m}=h_{E}\frac{g_{E}}{g_{m}}=(0.2 \; \mathrm {m})\frac{(9.8 \; \mathrm {m}/\mathrm {s}^{2})}{(1.6 \; \mathrm {m}/\mathrm {s}^{2})}=1.2 \; \mathrm {m}
```

That is, the maximum height reached by the man on the moon is six times the height reached on earth.
:::
````

````{prf:example}
:label: example-9-10
:enumerator: 9.10

A neutron star of radius of 12 km has a gravitational acceleration of $1\times 10^{12}$ $\mathrm {m}/\mathrm {s}^{2}$ at its surface. Calculate its average density.

:::{admonition} Solution 9.10
:class: dropdown

The gravitational acceleration of a particle near the surface of the star is

```{math}
g=\frac{GM_{n}}{R_{n}^{2}}
```

```{math}
M_{n}=\frac{gR_{n}^{2}}{G}=\frac{(1\times 10^{12} \; \mathrm {m}/\mathrm {s}^{2})(12\times 10^{3} \; \mathrm {m})^{2}}{(6.67\times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})}=2\times 10^{30}\ \; \mathrm {k}\mathrm {g}
```

```{math}
\rho =\frac{3M_{n}}{4\pi R_{n}^{3}}=\frac{3(2\times 10^{30} \; \mathrm {k}\mathrm {g})}{4(3.14)(12\times 10^{3} \; \mathrm {m})^{3}}=2.8\times 10^{17} \; \mathrm {k}\mathrm {g}/\mathrm {m}^{3}
```
:::
````

````{prf:example}
:label: example-9-11
:enumerator: 9.11

Find the free-fall acceleration of a body that is at a distance of $0.05R_{E}$ above the surface of the earth.

:::{admonition} Solution 9.11
:class: dropdown

```{math}
g=\frac{GM_{E}}{(R_{E}+h)^{2}}=\frac{GM_{E}}{(R_{E}+0.05R_{E})^{2}}=\frac{GM_{E}}{(1.05R_{E})^{2}}
```

```{math}
=\frac{(6.67\times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(5.98\times 10^{24} \; \mathrm {k}\mathrm {g})}{(6.7\times 10^{6} \; \mathrm {m})^{2}}=8.9 \; \mathrm {m}/\mathrm {s}^{2}
```
:::
````

(sec-9-2-4)=
### 9.2.4 The Gravitational Field

As mentioned previously, the gravitational force is a field force that can act through empty space, i.e., physical contact between objects is not necessary for such a force to act. An alternative way in describing the gravitational attraction is by introducing the concept of the gravitational field. Suppose a test particle of mass $m_{0}$ is placed at different points from another mass *M*(which represents the center of the gravitational force). At each point, the test particle will experience a gravitational force that depends on its distance from *M* and is given by

```{math}
\mathbf {F}_{g}=\frac{-GMm_{0}}{r^{2}}\mathbf {r}_{1}
```

where $\mathbf {r}_{1}$ is a unit vector that points radially outwards. Therefore, *M* may be considered as producing a gravitational field in the space around it. This field can be sensed by the force that the test particle experience when placed in the vicinity of *M*. The gravitational field produced by *M* at any point in space is thus given by

```{math}
\mathbf {g}=\frac{\mathbf {F}_{g}}{m_{0}}=\frac{-GM}{r^{2}}\mathbf {r}_{1}
```

That is, the gravitational field at a point is defined as the gravitational force per unit mass at that point. A map of the field can be drawn showing the gravitational field at any point in space. Figure [](#fig-9-14) shows the gravitational field vectors near the earth’s surface and at large distances from the earth. Note that, the gravitational field is an example of a static field since the field at any point is constant with time.

```{figure} ../images/ch-09/459974_1_En_9_Fig14_HTML.png
:name: fig-9-14

The gravitational field vectors near the earth’s surface and at large distances from the earth
```

````{prf:example}
:label: example-9-12
:enumerator: 9.12

Find the magnitude and direction of the gravitational field at the point $\mathrm {P}$ in the arrangement shown in Fig. [](#fig-9-15), where all particles have equal masses.

:::{admonition} Solution 9.12
:class: dropdown

Since all masses are equal, the net gravitational force at $\mathrm {P}$ is due to the sum of the $\mathrm {x}$-components of $\mathrm {F}_{3}$ and $\mathrm {F}_{2}$. That is,

```{math}
\mathbf {F}=2F_{3}\cos \theta \mathbf {i}=\frac{4Gmm_{0}}{5a^{2}}\cos \theta \mathbf {i}=\frac{4Gmm_{0}}{5a^{2}}\frac{2}{\sqrt{5}}\mathbf {i}=\frac{8Gmm_{0}}{5\sqrt{5}a^{2}}\mathbf {i}
```

```{math}
\mathbf {g}=\frac{8Gm}{5\sqrt{5}a^{2}}\mathbf {i}
```
:::
````

```{figure} ../images/ch-09/459974_1_En_9_Fig15_HTML.png
:name: fig-9-15

Finding the magnitude and direction of the gravitational field at P
```

(sec-9-3)=
## 9.3 Conic Sections

Conic sections are produced if a double right circular cone intersects with a plane. It may be a circle, a parabola, an ellipse, or a hyperbola.

```{figure} ../images/ch-09/459974_1_En_9_Fig16_HTML.png
:name: fig-9-16

A conic section has the property that the ratio *e* (called the eccentricity) of the distance between any point on the curve (for example point *P*) and another point called the focus (*F*) to the distance between *P* and a line called the directrix is equal to a constant
```

(sec-9-3-1)=
### 9.3.1 The Polar Equation of a Conic Section

A conic section has the property that the ratio *e* (called the eccentricity) of the distance between any point on the curve (for example point *P*) and another point called the focus (*F*) to the distance between *P* and a line called the directrix is equal to a constant (see Fig. [](#fig-9-16)). This constant differs from one conic section to another. Consider Fig. [](#fig-9-16) where the focus $\mathrm {F}$ is at the origin $\mathrm {O}$ of the $\mathrm {x}$ and $\mathrm {y}$ coordinate system and the directrix is at $x=d$. Since the distance between *P* and *F* is

```{math}
PF=r
```

then, the nearest distance between *P* and the directrix is

```{math}
PD=d-FE=d-r\cos \theta
```

The eccentricity is therefore given by

```{math}
e=\frac{PF}{PD}=\frac{r}{d-r\cos \theta }
```

Hence,

```{math}
\begin{aligned} r=\displaystyle \frac{ed}{1+e\cos \theta } \end{aligned}
```

This equation is the polar equation of a conic section.

1. **Ellipse**: $e<1$ From Fig. [](#fig-9-17), you can see that at $\theta =0, r=OV$ and at $\theta =\pi , r=OV'$. Substituting this into Eq. 9.22 gives

```{math}
OV=\frac{ed}{1+e}
```

and

```{math}
OV'=\frac{ed}{1-e}
```

Since $VV'$ is the length of the major axis which is equal to 2*a*, (*a* is the length of the semimajor axis) we have

```{math}
\begin{aligned} OV+OV'=2a \end{aligned}
```

or

```{math}
\frac{ed}{1+e}+\frac{ed}{1-e}=2a
```

```{figure} ../images/ch-09/459974_1_En_9_Fig17_HTML.png
:name: fig-9-17

In an ellipse, at $\theta =0, r=OV$ and at $\theta =\pi , r=OV'$
```

Hence,

```{math}
a=\frac{ed}{1-e^{2}}
```

Or

```{math}
ed=a(1-e^{2})
```

Substituting into Eq. 9.22, the polar equation of an ellipse is

```{math}
r=\frac{a(1-e^{2})}{1+e\cos \theta }
```

That gives

```{math}
\begin{aligned} OV=\displaystyle \frac{a(1-e^{2})}{1+e}=a(1-e) \end{aligned}
```

and

```{math}
\begin{aligned} OV'=\displaystyle \frac{a(1-e^{2})}{1-e}=a(1+e) \end{aligned}
```

The distance *C* between the center of the ellipse and the focus is

```{math}
C=CV-OV=a-a(1-e)=ae
```

Since from Fig. [](#fig-9-17), we have $c<a$, i.e., the distance between the foci is less than that between the vertices, then $e<1$. Furthermore, you can prove that $c=\sqrt{a^{2}-b^{2}}$ or $b=a\sqrt{1-e^{2}}$ where *b* is the length of the semiminor axis of the ellipse.

2. **Parabola**: $e=1$ Since $e=1$, Eq. 9.22 becomes

```{math}
r=\frac{d}{1+\cos \theta }
```

(Polar Equation of a Parabola) As $\theta$ approaches $\pi , r$ becomes infinite and hence $a\rightarrow \infty$ (see Fig. [](#fig-9-18)).

```{figure} ../images/ch-09/459974_1_En_9_Fig18_HTML.png
:name: fig-9-18

In a parabola, as $\theta$ approaches $\pi , r$ becomes infinite and hence $a\rightarrow \infty$
```

3. **Hyperbola**: $e>1$ The hyperbola has two branches as shown in Fig. [](#fig-9-19). For the gravitational force, only the first branch (I) represents a possible motion of the particle since $GM/h^{2}$ must be positive. The polar equation of a hyperbola is given by

```{math}
r=\frac{a(e^{2}-1)}{1+e\cos \theta }
```

```{figure} ../images/ch-09/459974_1_En_9_Fig19_HTML.png
:name: fig-9-19

The hyperbola
```

(sec-9-3-2)=
### 9.3.2 Motion in a Gravitational Force Field

The path of a particle in any central force field can be found by solving the equation of motion $(d^{2}u/d\theta ^{2}+u=-1/(mh^{2}u^{2})f(1/u)$ (Eq. 9.9) if the form of the force is known. In the case of a gravitational force, we have

```{math}
f(r)=\frac{-GMm}{r^{2}}
```

where *M* is assumed to be fixed and that it is attracting a particle of mass *m* and *r* is the distance between them. In terms of *u*, we have

```{math}
f({1}/{u})=-GMmu^2
```

Substituting this into the equation of motion gives

```{math}
\frac{d^{2}u}{d\theta ^{2}}+u=\frac{-1}{mh^{2}u^{2}}(-GMmu^{2})
```

or

```{math}
\begin{aligned} \displaystyle \frac{d^{2}u}{d\theta ^{2}}+u=\frac{GM}{h^{2}} \end{aligned}
```

This equation is a nonhomogeneous linear differential equation. Its solution may be given by

```{math}
u=\frac{1}{r}=C\cos (\theta -\phi )+\frac{GM}{h^{2}}
```

where *C* and $\phi$ are integration constants. $\phi$ is known as the phase angle and it can be chosen to be $\phi =0$ if the $\mathrm {x}$-axis is chosen such that at $\theta =0, r$ is a minimum. That gives

```{math}
\begin{aligned} u=\displaystyle \frac{1}{r}=C\cos \theta +\frac{GM}{h^{2}} \end{aligned}
```

or

```{math}
r=\frac{h^{2}/GM}{1+\frac{Ch^{2}}{GM}\cos \theta }=\frac{ed}{1+e\cos \theta }
```

Thus, the path of the particle under the influence of the gravitational force field is a conic with $ed=h^{2}/GM$ and $d=1/C$ and $e=h^{2}C/GM$. If a planet is moving in elliptical orbit about the sun, then the maximum and minimum distances of the planet from the sun (*OV* and $OV')$ are called the aphelion and perihelion respectively If a satellite is moving about a planet in an elliptical orbit, the maximum and minimum distances of the satellite from the planet are called the apogee and perigee respectively.

(sec-9-3-3)=
### 9.3.3 The Gravitational Potential Energy

Consider a particle of mass *m* moving under the influence of a larger particle of mass $M(M\gg m)$. By using Eq. 9.10 $(\displaystyle \triangle U=U_{f}-U_{i}=-\int _{r_{i}}^{r_{f}}f(r)dr)$ and noting that $f(r)=-GMm/r^{2}$, the change in the gravitational potential energy of the system as *m* moves from $r_{i}$ to $r_{f}$ in the field of *M* is

```{math}
\triangle U_{g}=U_{gf}-U_{gi}=\int _{r_{i}}^{r_{f}}\frac{GMm}{r^{2}}dr=GMm\int _{r_{i}}^{r_{f}}\frac{dr}{r^{2}}
```

```{math}
=GMm\bigg [\frac{-1}{r}\bigg ]_{r_{i}}^{r_{f}}=GMm\bigg (\frac{1}{r_{i}}-\frac{1}{r_{f}}\bigg )
```

That is, as the particle of mass *m* moves toward or away from *M*, the potential energy of the system decreases and increases respectively Note that, the lighter particle (*m*) gains most of the kinetic energy as the potential energy changes. By choosing the reference point at infinity $(r_{i}=\infty )$ then $U_{i}=0$ and taking $r_{f}=r$ gives

```{math}
U_{g}(r)=\frac{-GMm}{r}
```

For more than two-particle systems, there is more than one gravitational force (one for each pair of particles). Hence, there is more than one potential energy The total potential energy is the sum of the potential energies of each pair. For example if there are three particles, the total potential energy is

```{math}
U_{tot}=U_{12}+U_{13}+U_{23}=-\bigg (\frac{Gm_{1}m_{2}}{r_{12}}+\frac{Gm_{1}m_{3}}{r_{13}}+\frac{Gm_{2}m_{3}}{r_{23}}\bigg )
```

**Force from Potential Energy** The gravitational force may be obtained from its corresponding potential energy. That is,

```{math}
\mathbf {F}_{g}=-\frac{d}{dr}\bigg (\frac{-GMm}{r}\bigg )\mathbf {r}_{1}=\frac{-GMm}{r^{2}}\mathbf {r}_{1}
```

````{prf:example}
:label: example-9-13
:enumerator: 9.13

Find the potential energy of the system as shown in Fig. [](#fig-9-20).

:::{admonition} Solution 9.13
:class: dropdown

```{math}
U=U_{12}+U_{13}+U_{23}
```

```{math}
=-G\bigg (\frac{m_{1}m_{2}}{r_{12}}+\frac{m_{1}m_{3}}{r_{13}}+\frac{m_{2}m_{3}}{r_{23}}\bigg )
```

```{math}
=-(6.67\displaystyle \times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})\bigg (\frac{(8\times 10^{4} \; \mathrm {k}\mathrm {g})}{(0.3 \; \mathrm {m})}+\frac{(12\times 10^{4} \; \mathrm {k}\mathrm {g})}{(0.32 \; \mathrm {m})}+\frac{(6\times 10^{4} \; \mathrm {k}\mathrm {g})}{(0.36 \; \mathrm {m})}\bigg )=-5.4\times 10^{-5} \; \mathrm {J}
```
:::
````

```{figure} ../images/ch-09/459974_1_En_9_Fig20_HTML.png
:name: fig-9-20

The gravitational potential energy of a system of three particles
```

````{prf:example}
:label: example-9-14
:enumerator: 9.14

Two particles of equal masses $(3\mathrm {k}\mathrm {g})$ are separated by a distance of 0.3 $\mathrm {m}:(\mathrm {a})$ Find the potential energy of the system; (b) how much work is required to reduce their separation to 0.1 $\mathrm {m}, (\mathrm {c})$ to increase their separation to 0.5 $\mathrm {m}.$

:::{admonition} Solution 9.14
:class: dropdown

(a)

```{math}
U=\frac{-Gm^{2}}{r}=\frac{-(6.67\times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(3 \; \mathrm {k}\mathrm {g})^{2}}{(0.3 \; \mathrm {m})}=-2\times 10^{-9} \; \mathrm {J}
```

(b) The work done by the gravitational force is

```{math}
W=-\triangle U=U_{i}-U_{f}=-Gm^{2} \bigg (\frac{1}{r_{i}}-\frac{1}{r_{f}}\bigg )
```

```{math}
=-(6.67\times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(3 \; \mathrm {k}\mathrm {g})^{2}\bigg (\frac{1}{(0.3 \; \mathrm {m})}-\frac{1}{(0.1 \; \mathrm {m})}\bigg )
```

that gives $W=4\times 10^{-9}$ J. The work done by an external agent is $W=-4\times 10^{-9}$ J.

(c) The work done by the gravitational force is

```{math}
W=-\displaystyle \triangle U=-Gm^{2}\left( \frac{1}{r_{i}}-\frac{1}{r_{f}}\right) =-(6.67\times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(3 \; \mathrm {k}\mathrm {g})^{2}\bigg (\frac{1}{(0.3 \; \mathrm {m})}-\frac{1}{(0.5 \; \mathrm {m})}\bigg )
```

```{math}
W=-8\times 10^{-10} \; \mathrm {J}
```

The work done by an external agent is $+8\times 10^{-10}\mathrm {J}.$
:::
````

(sec-9-3-4)=
### 9.3.4 Energy in a Gravitational Force Field

The equation of motion in terms of energy is given by Eq. 9.12:

```{math}
\bigg (\frac{du}{d\theta }\bigg )^{2}+u^{2}=\frac{2(E-U)}{mh^{2}}
```

The gravitational potential energy of a two-particle system of masses *M* and *m* is given by

```{math}
U_{g}(r)=\frac{-GMm}{r}
```

In terms of *u* we may write

```{math}
\begin{aligned} U_{g}(1/u)=-GMmu \end{aligned}
```

Furthermore, the solution of the equation (Eq. 9.26) of motion in the gravitational force field is

```{math}
\begin{aligned} u=\displaystyle \frac{1}{r}=C\cos \theta +\frac{GM}{h^{2}} \end{aligned}
```

Substituting Eqs. 9.28 and 9.29 into Eq. 9.12 gives

```{math}
(C\displaystyle \sin \theta )^{2}+\bigg (C\cos \theta +\frac{GM}{h^{2}}\bigg )^{2}=\frac{2E}{mh^{2}}-\frac{2}{mh^{2}} \bigg (- GMm\bigg (C\displaystyle \cos \theta +\frac{GM}{h^{2}}\bigg )\bigg )
```

That gives

```{math}
C^{2}=\frac{2E}{mh^{2}}+\frac{G^{2}M^{2}}{h^{4}}
```

or

```{math}
C=\sqrt{\frac{2E}{mh^{2}}+\frac{G^{2}M^{2}}{h^{4}}} \quad (assuming \; C >0)
```

Substituting this value of *C* into Eq. 9.29 gives

```{math}
u=\frac{GM}{h^{2}}+\sqrt{\frac{2E}{mh^{2}}+\frac{G^{2}M^{2}}{h^{4}}}\cos \theta
```

```{math}
=\frac{GM}{h^{2}}+\frac{GM}{h^{2}}\sqrt{1+\frac{2Eh^{2}}{G^{2}M^{2}m}}\cos \theta
```

or

```{math}
\begin{aligned} u=\displaystyle \frac{GM}{h^{2}}\bigg [1+\sqrt{1+\frac{2Eh^{2}}{G^{2}M^{2}m}}\cos \theta \bigg ] \end{aligned}
```

Comparing this equation with the polar equation of a conic section (Eq. 9.22), we have

```{math}
e=\sqrt{1+\frac{2Eh^{2}}{G^{2}M^{2}m}}
```

```{figure} ../images/ch-09/459974_1_En_9_Fig21_HTML.png
:name: fig-9-21

Different paths
```

Thus the trajectory of the particle is an ellipse if $e<1$, that is if $E<0$. Therefore, if the potential energy of the particle is greater than its kinetic energy the particle’s path is an ellipse since it does not have enough energy to reach infinity. The trajectory of the particle is a parabola if $e=1$ and hence if $E=0$. In that case, the kinetic energy of the particle is equal to its potential energy and thus it can reach infinity with zero kinetic energy. Finally, the trajectory of the particle is a hyperbola if $e>1$ and therefore if $E>0$. That is, if the kinetic energy of the particle is greater than its potential energy, then it will reach infinity with positive kinetic energyElliptical Orbit $E<0$Parabolic Orbit $E=0$Hyperbolic Orbit $E>0$

Different paths are shown in Fig. [](#fig-9-21).

(sec-9-4)=
## 9.4 Kepler’s Laws

After analyzing the astronomical data of the Danish astronomer Tycho Brahe, the German astronomer Johannes Kepler formulated his three laws of planetary motion.

(sec-9-4-1)=
### 9.4.1 Kepler’s First Law

Every planet moves in an elliptical orbit with the sun at one focus as shown in Fig. [](#fig-9-21).

```{figure} ../images/ch-09/459974_1_En_9_Fig22_HTML.png
:name: fig-9-22

From the first property of a central force we have $\mathbf {r}\times \mathbf {v}=\mathbf {h}=$constant, where $\mathbf {h}$ is a constant vector perpendicular to the x-y plane
```

The gravitational force between the sun and a planet is

```{math}
\mathbf {F}=\frac{-GM_{S}M_{P}}{r^{2}}\mathbf {r}_{1}
```

where $M_{S}$ and $M_{P}$ are the masses of the sun and the planet, respectively The acceleration of the planet is

```{math}
\mathbf {a}=\frac{-GM_{S}}{r^{2}}\mathbf {r}_{1}
```

From the first property of a central force, we have $\mathbf {r}\times \mathbf {v}=\mathbf {h}=$constant, where $\mathbf {h}$ is a constant vector perpendicular to the x–y plane (see Fig. [](#fig-9-22)). Since $\mathbf {r}=r\mathbf {r}_{1}$ and $\mathbf {v}=d\mathbf {r}/dt=dr\mathbf {r}_{1}/dt=rd\mathbf {r}_{1}/dt+(dr/dt)\mathbf {r}_{1}$ we have

```{math}
\mathbf {h}=r\mathbf {r}_{1}\times \bigg (r\frac{d\mathbf {r}_{1}}{dt}+\frac{dr}{dt}\mathbf {r}_{1}\bigg )=r^{2}\bigg (\mathbf {r}_{1}\times \frac{d\mathbf {r}_{1}}{dt}\bigg )+r\frac{dr}{dt}\bigg (\mathbf {r}_{1}\times \mathbf {r}_{1}\bigg )
```

```{math}
=r^{2}\bigg (\mathbf {r}_{1}\times \frac{d\mathbf {r}_{1}}{dt}\bigg )
```

```{math}
\displaystyle \mathbf {a}\times \mathbf {h}=\bigg (\frac{-GM_{S}}{r^{2}}\mathbf {r}_{1}\bigg )\times \bigg (r^{2}\bigg (\mathbf {r}_{1}\times \frac{d\mathbf {r}_{1}}{dt}\bigg )\bigg )=-GM_{\mathrm {S}}\bigg [\bigg (\mathbf {r}_{1}\frac{d\mathbf {r}_{1}}{dt}\bigg )\mathbf {r}_{1}-(\mathbf {r}_{1} \cdot \mathbf {r}_{1})\frac{d\mathbf {r}_{1}}{dt}\bigg ]
```

Using

```{math}
\mathbf {A}\times (\mathbf {B}\times \mathbf {C})=(\mathbf {A}\cdot \mathbf {C})\mathbf {B}-(\mathbf {A}\cdot \mathbf {B})\mathbf {C}
```

Since $\mathbf {r}_{1} \cdot d\mathbf {r}_{1}/dt=0$ and $\mathbf {r}_{1}\cdot \mathbf {r}_{1}=r_{1}^{2}=1$, we have

```{math}
\mathbf {a}\times \mathbf {h}=GM_{S}\frac{d\mathbf {r}_{1}}{dt}=\frac{d}{dt}(GM_{S}\mathbf {r}_{1})
```

Also we have

```{math}
\mathbf {a}\times \mathbf {h}=\frac{d\mathbf {v}}{dt}\times \mathbf {h}=\frac{d}{dt}(\mathbf {v}\times \mathbf {h})
```

since $\mathbf {h}$ is a constant vector. That gives

```{math}
\frac{d}{dt}(\mathbf {v}\times \mathbf {h})=\frac{d}{dt}(GM_{\mathrm {S}}\mathbf {r}_{1})
```

or

```{math}
\mathbf {v}\times \mathbf {h}=GM_{S}\mathbf {r}_{1}+\mathbf {C}
```

where $\mathbf {C}$ is a constant vector. Since

```{math}
h^{2}=\mathbf {h}\cdot \mathbf {h}=(\mathbf {r}\times \mathbf {v})\cdot \mathbf {h}=\mathbf {r}\cdot (\mathbf {v}\times \mathbf {h})
```

```{math}
=(r\mathbf {r}_{1})\cdot (GM_{S}\mathbf {r}_{1}+\mathbf {C})=rGM_{S}(\mathbf {r}_{1} \cdot \mathbf {r}_{1})+r(\mathbf {r}_{1}\cdot \mathbf {C})
```

and since

```{math}
\mathbf {r}_{1}\cdot \mathbf {C}=C\cos \theta
```

we have

```{math}
h^{2}=rGM_{S}+rC\cos \theta
```

or

```{math}
r=\frac{h^{2}}{GM_{S}+C\cos \theta }=\frac{h^{2}/GM_{S}}{1+C/GM_{S}{\cos \theta }}
```

This equation is of a conic section and since the only closed conic section is an ellipse the law is proved.

(sec-9-4-2)=
### 9.4.2 Kepler’s Second Law

The radius vector drawn from the sun to the planet sweeps out equal areas in equal periods of time.

This was proved in Sect. 9.1 as a property of a central force, where we’ve seen that for any central force, the position vector $\mathrm {r}$ of the particle from the center of force $\mathrm {O}$ sweeps out equal areas in equal times. That is,

```{math}
\displaystyle \frac{dA}{dt}=\frac{h}{2}= \text {constant}
```

or

```{math}
\displaystyle \frac{dA}{dt}=\frac{L}{2m}= \text {constant}
```

Here, the center of force is the sun and the particle is the planet, hence we have

```{math}
\frac{dA}{dt}=\frac{L}{2M_{P}}
```

(sec-9-4-3)=
### 9.4.3 Kepler’s Third Law

The square of the period of revolution of any planet about the sun is proportional to the cube of the semimajor axis of its orbit.

The area of an ellipse is given by $A=\pi ab$, where *a* and *b* are the semimajor and semiminor axis of the ellipse, respectively. From Kepler’s second law, the areal velocity is a constant given by

```{math}
\displaystyle \frac{dA}{dt}=\frac{h}{2}= \text {constant}
```

Therefore, the period of revolution may be considered as the time it takes the radius vector to sweep an area of $\pi ab$

```{math}
T=\frac{\pi ab}{h/2}
```

From Sect. 9.3, we have $b=a\sqrt{1-e^{2}}$. That gives

```{math}
T=\frac{\pi a^{2}\sqrt{1-e^{2}}}{h/2}
```

Also, we’ve seen that the eccentricity for the gravitational force is given by $e=h^{2}C/GM$ or $e=h^{2}C/GM_{S}$ in the case of the planet–sun system. Since $ed=a(1-e^{2})$, we have

```{math}
\frac{h^{2}}{GM_{S}}=a(1-e^{2})
```

or

```{math}
\sqrt{1-e^{2}}=\frac{h}{\sqrt{GM_{S}a}}
```

Thus,

```{math}
T=\frac{2\pi a^{2}h}{h\sqrt{GM_{S}a}}=\frac{2\pi }{\sqrt{GM_{S}}}a^{3/2}
```

or

```{math}
T^{2}=\bigg (\frac{4\pi ^{2}}{GM_{S}}\bigg )a^{3}=K_{S}a^{3}
```

where $K_{S}$ is a constant that has a value given by

```{math}
K_{S}=\frac{4\pi ^{2}}{GM_{S}}=2.97\times 10^{-19} \; \mathrm {s}^{2}/\mathrm {m}^{3}
```

This proves Kepler’s third law. Note that, Kepler’s laws apply also for satellites. In such cases, the mass of the sun in the previous equations is replaced by the earth or any other planet about which the satellite revolves.

(sec-9-5)=
## 9.5 Circular Orbits

The orbits of most planets in our solar system are almost circular. Next, we will find the total energy of a body of mass *m* moving in a circular orbit about a massive body of mass *M* that is assumed to be fixed (at rest) in an inertial frame of reference. From that energy, we will find the eccentricity and prove that the orbit is circular. The potential energy of such system is

```{math}
U=\frac{-GMm}{r}
```

where *r* is the radius of the circular orbit. Applying Newton’s second law to *m* gives

```{math}
\begin{aligned} \displaystyle \frac{GMm}{r^{2}}=m\frac{v^{2}}{r} \end{aligned}
```

Therefore, the kinetic energy of the particle is

```{math}
K=\frac{1}{2}mv^{2}=\frac{GMm}{2r}
```

The total energy of *m* is therefore given by

```{math}
E=K+U=\frac{GMm}{2r}-\frac{GMm}{r}
```

or

```{math}
\begin{aligned} E=-\displaystyle \frac{GMm}{2r} \end{aligned}
```

In Sect. 9.4, the eccentricity of orbit in terms of energy was given by

```{math}
\begin{aligned} e=\sqrt{1+\frac{2Eh^{2}}{G^{2}M^{2}m}} \end{aligned}
```

Substituting Eq. 9.32 into Eq. 9.33 gives

```{math}
e=\sqrt{1+\bigg (\frac{-GMm}{2r}\frac{2h^{2}}{G^{2}M^{2}m}\bigg )}
```

Since $h=rv$ for a circular orbit and since $GMm/r^{2}=mv^{2}/r$ and thus $v= \sqrt{GM/r}$, we have

```{math}
h=\sqrt{rGM}
```

and

```{math}
e=\sqrt{1+\bigg (\frac{-GMm}{2r}\frac{2rGM}{G^{2}M^{2}m}\bigg )}=0
```

Hence the orbit is circular. The potential, kinetic, and total energy as functions of *r* of an object in circular orbit are shown in Fig. [](#fig-9-23).

```{figure} ../images/ch-09/459974_1_En_9_Fig23_HTML.png
:name: fig-9-23

The potential, kinetic and total energy as functions of *r* of an object in a circular orbit
```

````{prf:example}
:label: example-9-15
:enumerator: 9.15

A satellite of mass of 1000 kg is in circular orbit about the earth at an altitude of $R_{E}/2$. What is the amount of work required to move the satellite to an altitude of $2R_{E}.$

:::{admonition} Solution 9.15
:class: dropdown

```{math}
W=\displaystyle \triangle E=E_{f}-E_{i}=GM_{E}m_{s}\bigg (\frac{-1}{2r_{f}}-\bigg (\frac{-1}{2r_{i}}\bigg )\bigg )=GM_{E}m_{s}\bigg (\frac{-1}{4R_{E}}+\frac{1}{R_{E}}\bigg )
```

```{math}
=\displaystyle \frac{3GM_{E}m_{s}}{4R_{E}}= \frac{3(6.67\times 10^{-11} \; \mathrm {N} \mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(5.98\times 10^{24} \; \mathrm {k}\mathrm {g})(1000 \; \mathrm {k}\mathrm {g})}{4(6.37\times 10^{6} \; \mathrm {m})}=4.7\times 10^{10} \; \mathrm {J}
```
:::
````

(sec-9-6)=
## 9.6 Elliptical Orbits

For an elliptical orbit, we have

```{math}
\begin{aligned} ed=a(1-e^{2})=\displaystyle \frac{h^{2}}{GM} \end{aligned}
```

Substituting Eq. 9.33 into Eq. 9.34 gives

```{math}
a\bigg (1-\bigg (1+\frac{2Eh^{2}}{G^{2}M^{2}m}\bigg )\bigg )=\frac{h^{2}}{GM}
```

That gives

```{math}
E=\frac{-GMm}{2a}
```

The speed of an object in an elliptical orbit can be found from

```{math}
K=E-U
```

```{math}
\frac{1}{2}mv^{2}=\frac{-GmM}{2a}+\frac{GmM}{r}
```

```{math}
v^{2}=GM\bigg (\frac{2}{r}-\frac{1}{a}\bigg )
```

```{math}
v=\sqrt{GM\bigg (\frac{2}{r}-\frac{1}{a}\bigg )}
```

(sec-9-7)=
## 9.7 The Escape Speed

The escape speed $v_{esc}$ is the speed required for an object to escape from the influence of the gravitational field of an astronomical object or system. Suppose an object of mass *m* is projected from the surface of a planet of mass *M*. The minimum speed for the object to escape the gravitational field of the planet is that in which the object has zero total mechanical energy at infinity. From conservation of energy, we have

```{math}
K_{i}+U_{i}=K_{f}+U_{f}
```

| Body | Mass (kg) | Radius (m) | Semimajor axis *a* (m) | Escape speed (km/s) |
| --- | --- | --- | --- | --- |
| Mercury | $3.18\times 10^{23}$ | $2.43\times 10^{6}$ | $5.79\times 10^{10}$ | 4.3 |
| Venus | $4.88\times 10^{24}$ | $6.06\times 10^{6}$ | ${0}1.08\times 10^{11}$ | 10.3 |
| Earth | $5.98\times 10^{24}$ | $6.37\times 10^{6}$ | $1.496\times 10^{11}$ | 11.2 |
| Mars | $6.42\times 10^{23}$ | $3.37\times 10^{6}$ | $2.28\times 10^{11}$ | 5 |
| Jupiter | $1.90\times 10^{27}$ | $6.99\times 10^{7}$ | $7.78\times 10^{11}$ | 60 |
| Saturn | $5.68\times 10^{26}$ | $5.85\times 10^{7}$ | $1.43\times 10^{12}$ | 36 |
| Uranus | $8.68\times 10^{25}$ | $2.33\times 10^{7}$ | $2.87\times 10^{12}$ | 22 |
| Neptune | $1.03\times 10^{26}$ | $2.21\times 10^{7}$ | $4.5\times 10^{12}$ | 24 |
| Pluto | $1.4\times 10^{22}$ | $1.5\times 10^{6}$ | $5.91\times 10^{12}$ | 1.1 |
| Moon | $7.36\times 10^{22}$ | $1.74\times 10^{6}$ | | 2.3 |
| Sun | $1.99\times 10^{30}$ | $6.96\times 10^{8}$ | | 618 |

```{math}
\frac{1}{2}mv_{esc}^{2}+\bigg (\frac{-GMm}{R}\bigg )=0
```

Hence

```{math}
v_{esc}=\sqrt{\frac{2GM}{R}}
```

where *R* is the radius of the planet. If the object’s initial speed is greater than the escape speed from that planet, then the object will still have some kinetic energy at infinity. Table.9.2 shows planetary data escape speeds

````{prf:example}
:label: example-9-16
:enumerator: 9.16

What is the escape speed from the surface of: (a) Earth; (b) Mars; (c) Pluto.

:::{admonition} Solution 9.16
:class: dropdown

(a)

```{math}
v_{esc}=\sqrt{\frac{2GM_{E}}{R_{E}}}=\sqrt{\frac{2(6.67\times 10^{-11} \; \mathrm {N}\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(5.98\times 10^{24} \; \mathrm {k}\mathrm {g})}{(6.37\times 10^{6} \; \mathrm {m})}}=1.12\times 10^{4} \; \mathrm {m}/\mathrm {s}
```

(b)

```{math}
v_{esc}=\sqrt{\frac{2GM_{M}}{R_{M}}}=\sqrt{\frac{2(6.67\times 10^{-11} \; \mathrm {N}\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(6.42\times 10^{23} \; \mathrm {k}\mathrm {g})}{(3.37\times 10^{6} \; \mathrm {m})}}=5\times 10^{3} \; \mathrm {m}/\mathrm {s}
```

(c)

```{math}
v_{esc}=\sqrt{\frac{2GM_{P}}{R_{P}}}=\sqrt{\frac{2(6.67\times 10^{-11} \; \mathrm {N}\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(1.4\times 10^{22} \; \mathrm {k}\mathrm {g})}{(1.5\times 10^{6} \; \mathrm {m})}}=1.1\times 10^{3} \; \mathrm {m}/\mathrm {s}
```
:::
````

````{prf:example}
:label: example-9-17
:enumerator: 9.17

What must be the minimum speed of a spacecraft that is at a distance of $3R_{E}$ from the center of the earth in order for it to escape the gravitational field of the earth?

:::{admonition} Solution 9.17
:class: dropdown

The minimum speed is that in which the spacecraft has zero total mechanical energy at infinity,

```{math}
K_{i}+U_{i}=K_{f}+U_{f}
```

```{math}
\frac{1}{2}mv_{esc}^{2}+\bigg (\frac{-GM_{E}m}{3R_{E}}\bigg )=0
```

```{math}
v_{esc}=\sqrt{\frac{2GM_{E}}{3R_{E}}}=\sqrt{\frac{2(6.67\times 10^{-11} \; \mathrm {N}\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(5.98\times 10^{24} \; \mathrm {k}\mathrm {g})}{3(6.37\times \mathrm {l0}^{6} \; \mathrm {m})}}=6.46\times 10^{3} \; \mathrm {m}/\mathrm {s}
```
:::
````

````{prf:example}
:label: example-9-18
:enumerator: 9.18

Given that the period of Mars in its orbit about the sun is 1.88 years and its semimajor axis of the orbit is $22.8\times 10^{10} \; \mathrm {m}$, find the mass of the sun.

:::{admonition} Solution 9.18
:class: dropdown

The period in seconds is

```{math}
T=5.94\times 10^{7}\mathrm {s}
```

From Kepler’s second law, we have

```{math}
M_{S}=\displaystyle \frac{4\pi ^{2}a^{3}}{GT^{2}}=\frac{4(3.14)^{2}(22.8\times 10^{10} \; \mathrm {m})^{3}}{(6.67\times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(5.94\times 10^{7} \; \mathrm {s})^{2}}=1.99\times 10^{30} \; \mathrm {kg}
```
:::
````

````{prf:example}
:label: example-9-19
:enumerator: 9.19

Halley’s Comet moves in an elliptical orbit about the sun. Its semimajor axis of orbit is $2.7\times 10^{12} \; \mathrm {m}$ and its farthest distance $(OV'=R_{a})$ from the sun (the aphelion) is $5.3\times 10^{12} \; \mathrm {m}$. Find its period and its closest approach to the sun (the perihelion $OV=R_{p}$).

:::{admonition} Solution 9.19
:class: dropdown

From Kepler’s third law,

```{math}
T^{2}=K_{S}a^{3}=(2.97\times 10^{-19} \; \mathrm {s}^{2}/\mathrm {m}^{3})(2.7\times 10^{12} \; \mathrm {m})^{3}
```

```{math}
T=2.4\times 10^{9} \; \mathrm {s}=76 \; \text{ years }
```

From Eq. 9.23, we have

```{math}
OV+OV'=2a
```

or

```{math}
R_{p}+R_{a}=2a
```

```{math}
R_{p}=2a-R_{a}=2(2.7\times 10^{12} \; \mathrm {m})-(5.3\times 10^{12} \; \mathrm {m})=1\times 10^{11} \; \mathrm {m}
```
:::
````

````{prf:example}
:label: example-9-20
:enumerator: 9.20

If Pluto’s distance from the sun at perihelion is $4.43\times 10^{12}\mathrm {m}$, find (a) the ratio of its speed at perihelion to its speed at aphelion; (b) the eccentricity of orbit; (c) the total energy.

:::{admonition} Solution 9.20
:class: dropdown

From Table. 9.2, we have $a=5.9\times 10^{12} \; \mathrm {m}$, therefore

```{math}
R_{a}=2a-R_{p}=2(5.9\times 10^{12} \; \mathrm {m})-(4.43\times 10^{12} \; \mathrm {m})=7.37\times 10^{12} \; \mathrm {m}
```

From the conservation of angular momentum,

```{math}
M_{P}v_{a}R_{a}=M_{P}v_{p}R_{p}
```

hence,

```{math}
\frac{v_{p}}{v_{a}}=\frac{R_{a}}{R_{p}}=\frac{(7.37\times 10^{12}\mathrm {m})}{(4.43\times 10^{12}\mathrm {m})}=1.7
```

(b) From Eq. 9.24 $(OV=R_{p}=a(1-e))$, we have

```{math}
e=1-\frac{R_{p}}{a}=1-\frac{(4.43\times 10^{12} \; \mathrm {m})}{(5.9\times 10^{12} \; \mathrm {m})}=0.25
```

(c)

```{math}
E=\displaystyle \frac{-GMm}{2a}=\frac{-(6.67\times 10^{-11} \; \mathrm {N} \mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(1.99\times 10^{30} \; \mathrm {k}\mathrm {g})(1.4\times 10^{22} \; \mathrm {k}\mathrm {g})}{2(5.9\times 10^{12} \; \mathrm {m})}=-1.6\times 10^{29} \; \mathrm {J}
```
:::
````

````{prf:example}
:label: example-9-21
:enumerator: 9.21

Two stars of equal mass *M* revolve about their center of mass with a speed *v* as shown in Fig. [](#fig-9-24). Find the period of motion of each star.
````

```{figure} ../images/ch-09/459974_1_En_9_Fig24_HTML.png
:name: fig-9-24

Two stars of equal mass *M* revolve about their center of mass with a speed *v*
```

The gravitational force that one star exerts on the other is

```{math}
F=\frac{GM^{2}}{4r^{2}}=\frac{Mv^{2}}{r}
```

where *r* is the radius of orbit. Therefore,

```{math}
v=\sqrt{\frac{GM}{4r}}
```

and

```{math}
T=\frac{2\pi r}{v}=2\pi r\sqrt{\frac{4r}{GM}}=4\pi \sqrt{\frac{r^{3}}{GM}}
```

````{prf:example}
:label: example-9-22
:enumerator: 9.22

A spaceship is fired from the surface of Mars with a speed of $12\times 10^{3}\mathrm {m}/\mathrm {s},$ find its speed at a very far distance from Mars.

:::{admonition} Solution 9.22
:class: dropdown

```{math}
K_{i}+U_{i}=K_{f}+U_{f}
```

```{math}
\frac{1}{2}mv_{i}^{2}-\bigg (\frac{GmM_{M}}{R_{M}}\bigg )=\frac{1}{2}mv_{f}^{2}+0
```

```{math}
v_{f}^{2}=v_{i}^{2}-\displaystyle \frac{2GM_{M}}{R_{M}}
```

```{math}
=(12\times 10^{3} \; \mathrm {m}/\mathrm {s})^{2}-\frac{2(6.67\times 10^{-11} \; \mathrm {N}\,\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(6.42\times 10^{23} \; \mathrm {k}\mathrm {g})}{(3.37\times 10^{6} \; \mathrm {m})}
```

That gives $v_{f}=1.1\times 10^{4} \; \mathrm {m}/\mathrm {s}.$
:::
````


## Problems

```{exercise}
:label: prob-9-1
:enumerator: 9.1

Calculate the gravitational force between the earth and (a) the sun, (b) the moon.
```

```{exercise}
:label: prob-9-2
:enumerator: 9.2

Calculate the gravitational acceleration at the surface of Mars.
```

```{exercise}
:label: prob-9-3
:enumerator: 9.3

Three particles of masses $m_{1}=2\,\mathrm{kg}$, $m_{2}=6\,\mathrm{kg}$, and $m_{3}=3\,\mathrm{kg}$ are located at the points $(0,0)$, $(0,5)$, and $(5,0)$, respectively. Find magnitude and direction of the resultant gravitational force exerted on $m_{3}$.
```

```{exercise}
:label: prob-9-4
:enumerator: 9.4

The Geosynchronous satellites move in a circular orbit in the equatorial plane of the earth. They move in such a way that they always remain over the same point on the earth. Find the height and velocity of this satellite.
```

```{exercise}
:label: prob-9-5
:enumerator: 9.5

If the eccentricity of the orbit of Mercury about the sun is $e=0.206$ and its semimajor axis is $a=0.387\,\mathrm{AU}$, find (a) the distance of its farthest and closest approach to the sun (the aphelion and perihelion), (b) its period, (c) its total energy, (d) its angular momentum. ($1\,\mathrm{AU}=1.495\times 10^{11}\,\mathrm{m}$).
```

```{exercise}
:label: prob-9-6
:enumerator: 9.6

A body is released at a distance $r$ from the center of the earth. Find its velocity just as it hits the surface of the earth.
```

```{exercise}
:label: prob-9-7
:enumerator: 9.7

Show that the speed of a satellite in an elliptical orbit about the earth at apogee and perigee are given by
```

```{math}
v_{p}=\sqrt{\frac{GM}{a}}\sqrt{\frac{1+e}{1-e}}=\sqrt{\frac{GM}{a}}\sqrt{\frac{R_{a}}{R_{p}}}
```

and

```{math}
v_{a}=\sqrt{\frac{GM}{a}}\sqrt{\frac{1-e}{1+e}}=\sqrt{\frac{GM}{a}}\sqrt{\frac{R_{p}}{R_{a}}}.
```

```{exercise}
:label: prob-9-8
:enumerator: 9.8

An artificial satellite moves in an elliptical orbit about the earth. Its perigee and apogee altitudes are 1100 km and 4100 km respectively. Find (a) the velocity of the satellite at perigee and apogee, (b) its semimajor axis, (c) its eccentricity, (d) the equation of its orbit, (e) its period, (f) its speed when it is at a distance of 3000 km above the earth's surface.
```

```{exercise}
:label: prob-9-9
:enumerator: 9.9

A satellite is at a distance of $1.2R_{E}$ from the center of the earth. Find the speed required for the satellite at this altitude (where it represents the orbit perigee) to be in (a) circular orbit, (b) parabolic orbit, (c) elliptical orbit of eccentricity $e=0.7$.
```

```{exercise}
:label: prob-9-10
:enumerator: 9.10

Suppose the earth suddenly stops moving about the sun; find the time it would take the earth to fall to the sun.
```
