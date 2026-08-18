---
title: 8. Rolling and Static Equilibrium
short_title: "Ch. 8 — Rolling and Equilibrium"
label: ch-8
doi: 10.1007/978-3-030-15195-9_8
---

(sec-8-1)=
## 8.1 Rolling Motion

Rolling motion represents the general plane motion of a rigid body It can be considered as a combination of pure translational motion parallel to a fixed plane plus a pure rotational motion about an axis that is perpendicular to that plane. The axis of rotation usually passes through the center of mass. In Sect. [](#sec-6-4), we’ve seen that the motion of an object (or a system of particles) can always be considered as a combination of the motion of the object relative to its center of mass plus the motion of its center of mass relative to some origin O. From Sect. [](#sec-6-4-3), the kinetic energy of an object relative to the origin is

```{math}
:label: eq-8-1
\begin{aligned} K=\displaystyle \frac{1}{2}\sum _{i}m_{i}v_{i}^{\prime 2}+\frac{1}{2}Mv_{cm}^{2} \end{aligned}
```

where $v_{cm}$ is the velocity of the center of mass of the object relative to the origin $\mathrm {O}, m_{i}$ is the mass of the *i*th particle and $v_{i}'$ is the linear velocity of the ith particle relative to the center of mass. In the case of the general plane motion of a rigid body, the motion can be considered as a combination of pure translational motion of the center of mass plus pure rotational motion about an axis passing through the center of mass and perpendicular to the plane of motion. Therefore, the first term in Eq. [](#eq-8-1) can be written as

```{math}
v_{{i}}'=\omega r_{{i}}'
```

where $r_{i}'$ is the perpendicular distance from the *i*th particle to the center of mass axis. Hence

```{math}
K=\frac{1}{2}\left( \sum _{i}m_{i}r_{i}^{\prime 2}\right) \omega ^{2}+\frac{1}{2}Mv_{cm}^{2}
```

```{math}
K=\frac{1}{2}I_{cm}\omega ^{2}+\frac{1}{2}Mv_{cm}^{2}
```

Thus, the total kinetic energy of a rolling object is the sum of the translational kinetic energy of its center of mass and the rotational kinetic energy about its center of mass.

(sec-8-2)=
## 8.2 Rolling Without Slipping

An important special case of the general plane motion is rolling without slipping. Such motion occurs if a perfectly rigid body rolls on a perfectly rigid surface. As the object rolls without slipping, the instantaneous $\mathrm {s}'$ point of contact between the object and the surface is at rest relative to the surface since there is no slipping. Now, consider a wheel of radius *R* rolling without slipping along the straight track shown in Fig. [](#fig-8-1). The center of mass of the wheel moves along a straight line, while a point on the rim such as $\mathrm {P}$ moves in a cycloid path. As the wheel rotates through an angle $\theta$, its center of mass moves through a distance equal to the arc length *s* (see Fig. [](#fig-8-2)) given by

```{figure} ../images/ch-08/459974_1_En_8_Fig1_HTML.png
:name: fig-8-1

A wheel of radius *R* rolling without slipping along the straight track
```

```{figure} ../images/ch-08/459974_1_En_8_Fig2_HTML.png
:name: fig-8-2

As the wheel rotates through an angle $\theta$, its center of mass moves through a distance equal to the arc length *s*
```

```{figure} ../images/ch-08/459974_1_En_8_Fig3_HTML.png
:name: fig-8-3

The combination of pure rotational and translational motions
```

```{math}
s=R\theta
```

Hence, the speed of the center of mass is

```{math}
v_{cm}=\frac{ds}{dt}=R\frac{d\theta }{dt}=R\omega
```

The acceleration of the center of mass is given by

```{math}
a_{cm}=\frac{dv_{cm}}{dt}=R\frac{d\omega }{dt}=R\alpha
```

The combination of pure rotational and translational motions is viewed in Fig. [](#fig-8-3). In the pure translational motion (see Fig. [](#fig-8-3) part a) every particle in the wheel moves with the velocity $\mathbf {v}_{cm}$. In pure rotational motion (see Fig. [](#fig-8-3) part b), each particle moves with an angular speed $\omega$ about the center of mass axis and the linear speed of any particle at the rim is

```{math}
:label: eq-8-2
\begin{aligned} v_{cm}=R\omega \end{aligned}
```

The resulting motion of these two combined motions is shown in Fig. [](#fig-8-3) part $\mathrm {c}$, where the linear velocity of each particle is the vector sum of its linear velocity in pure translational motion and its linear velocity in pure rotational motion. Therefore, the instantaneous velocity of the point of contact is equal to zero $(\mathbf {v}_{1}=0)$ and of a point at the top of the wheel is equal to twice the velocity of the center of mass $(\mathbf {v}_{2}=2\mathbf {v}_{cm})$. Note that Eq. [](#eq-8-2) is valid only in the special case of rolling without slipping; in the general rolling motion this equation does not hold. The total kinetic energy of a rigid object rolling without slipping is therefore given by

```{math}
K=\frac{1}{2}I_{cm}\omega ^{2}+\frac{1}{2}Mv_{cm}^{2}
```

```{math}
=\frac{1}{2}I_{cm}\omega ^{2}+\frac{1}{2}MR^{2}\omega ^{2}
```

Another way to view rolling without slipping is to consider the wheel to be in pure rotational motion about an instantaneous axis that passes through the point of contact $\mathrm {P}$ (see Fig. [](#fig-8-4)). In that case, the velocity of the point of contact $\mathrm {P}$ is zero and the velocity of the center of mass is $v_{cm}=R\omega$ (since it is at a distance *R* from the axis of rotation) and the velocity of a point at the top is $v_{t}=2R\omega =2v_{cm}$. Note that the angular velocity $\omega$ of the wheel is the same as its angular velocity if the axis of rotation is at the center of mass.

```{figure} ../images/ch-08/459974_1_En_8_Fig4_HTML.png
:name: fig-8-4

Another way to view rolling without slipping is to consider the wheel to be in pure rotational motion about an instantaneous axis that passes through the point of contact $\mathrm {P}$
```

For simplicity, only homogeneous symmetrical objects will be considered here such as hoops, cylinders, and spheres. When a rigid body rolls without slipping with a constant speed, there will be no frictional force acting on the body at the instantaneous point of contact. However, if the object is accelerating, then a statistical frictional force acts on it at the instantaneous point of contact producing a torque about the center (see Fig. [](#fig-8-5)). This will cause the object to rotate about its center of mass. The direction of the statistical force opposes the tendency of the object to slide. For example, if a wheel is rolling down an incline, the direction of the frictional force will be opposing the downward motion.

```{figure} ../images/ch-08/459974_1_En_8_Fig5_HTML.png
:name: fig-8-5

A statistical frictional force acts on it at the instantaneous point of contact producing a torque about the center
```

In most situations, the body and the surface are not perfectly rigid. As a result, the normal force would not be a single force; rather it would be a number of forces that are distributed over the area of contact (see Fig. [](#fig-8-6)). Therefore, each normal force will exert an opposing torque since its line of action will not pass through the center of mass. Furthermore, as the object rolls over the surface, both the object and the surface undergo deformation resulting in a loss in the mechanical energy.

```{figure} ../images/ch-08/459974_1_En_8_Fig6_HTML.png
:name: fig-8-6

If the body and the surface are not perfectly, the normal force would not be a single force; rather it would be a number of forces that are distributed over the area of contact
```

````{prf:example}
:label: example-8-1
:enumerator: 8.1

A uniform solid hoop of mass of 32 kg and radius of 1.2 $\mathrm {m}$ rolls without slipping on a horizontal track where the center of mass speed is 2 $\mathrm {m}/\mathrm {s}$. Find: (a) the total energy of the hoop and compare it with its total energy if it would slide without rolling; (b) the speed of the hoop at its top and bottom.


:::{admonition} Solution 8.1
:class: dropdown

(a) the total energy is given by

```{math}
K=\frac{1}{2}I_{cm}\omega ^{2}+\frac{1}{2}Mv_{cm}^{2}
```

```{math}
=\frac{1}{2}(MR^{2})\bigg (\frac{v_{cm}}{R}\bigg )^{2}+\frac{1}{2}Mv_{cm}^{2}=Mv_{cm}^{2}=(32 \; \mathrm {k}\mathrm {g})(2 \; \mathrm {m}/\mathrm {s})^{2}=128 \; \mathrm {J}
```

If the hoop slides without rolling its total kinetic energy is $\displaystyle \frac{1}{2}Mv_{cm}^{2}$, that is, its value is half of that if the hoop were to roll without slipping.

(b)

```{math}
v_{\mathrm {t}\mathrm {o}\mathrm {p}}=2v_{cm}=2(2 \; \mathrm {m}/\mathrm {s})=4 \; \mathrm {m}/\mathrm {s}
```

```{math}
v_{\mathrm {b}\mathrm {o}\mathrm {t}\mathrm {t}\mathrm {o}\mathrm {m}}=0
```

:::
````

````{prf:example}
:label: example-8-2
:enumerator: 8.2

A uniform solid cylinder, sphere, and hoop roll without slipping from rest at the top of an incline (see Fig. [](#fig-8-7)). Find out which object would reach the bottom first.


:::{admonition} Solution 8.2
:class: dropdown

For each object, we have

```{math}
K_{i}+U_{i}=K_{f}+U_{f}
```

```{math}
0+Mgh=\frac{1}{2}Mv_{cm}^{2}+\frac{1}{2}I_{cm}\bigg (\frac{v_{cm}}{R}\bigg )^{2}
```

```{math}
v_{cm}=\sqrt{\frac{2gh}{1+I_{cm}/MR^{2}}}
```

Hence, the speed of the center of mass of any object at the bottom of the incline does not depend on its mass or size; it depends only on its shape. Therefore, all objects of the same shape such as spheres (of any mass or size) have the same speed at the bottom. That is, the smaller the ratio $I_{cm}/MR^{2}$ the faster the object moves since less of its energy goes to rotational kinetic energy and more goes to translational kinetic energy The ratio $I_{cm}/MR^{2}$ is equal to 0.4, 0.5, and 1 for a sphere, cylinder, and hoop, respectively Therefore, these objects will finish in the order of any sphere, any cylinder, and any hoop.

:::
````

```{figure} ../images/ch-08/459974_1_En_8_Fig7_HTML.png
:name: fig-8-7

A uniform solid cylinder, sphere and hoop roll without slipping from rest at the top of an incline
```

````{prf:example}
:label: example-8-3
:enumerator: 8.3

A marble ball of radius *R* and mass *M* rolls without slipping down the incline shown in Fig. [](#fig-8-8). Find: (a) its acceleration; (b) the minimum coefficient of static friction that is required to prevent slipping.


:::{admonition} Solution 8.3
:class: dropdown

(a) Applying Newton’s second law in both linear and angular form (see Fig. [](#fig-8-7)) we have

```{math}
:label: eq-8-3
\begin{aligned} \displaystyle \sum F_{x}=Mg\ \sin \theta -f_{s}=Ma_{cm} \end{aligned}
```

```{math}
\sum F_{y}=n-Mg\cos \theta =0
```

and

```{math}
\sum \tau =f_{s}R=I_{cm}\alpha =\bigg (\frac{2}{5}MR^{2}\bigg )\bigg (\frac{a_{cm}}{R}\bigg )
```

that gives

```{math}
:label: eq-8-4
\begin{aligned} f_{s}=\displaystyle \frac{2}{5}Ma_{cm} \end{aligned}
```

Substituting Eq. [](#eq-8-4) into Eq. [](#eq-8-3) gives

```{math}
\displaystyle M g \sin \theta -\frac{2}{5}Ma_{cm}=Ma_{cm}
```

hence

```{math}
a_{cm}=\frac{5}{7}g\sin \theta
```

and

```{math}
f_{s}==\frac{2}{7}Mg\sin \theta
```

(b) At the verge of slipping, the statistical frictional force is a maximum given by

```{math}
f_{s\max }=\mu _{s}n=\frac{2}{7}Mg\sin \theta
```

Hence, the coefficient of static friction must be at least as great as $\displaystyle \mu _{s}=\frac{2}{7}\tan \theta$ in order for the ball not to slip.

:::
````

```{figure} ../images/ch-08/459974_1_En_8_Fig8_HTML.png
:name: fig-8-8

A marble ball of radius *R* and mass *M* rolls without slipping down the incline
```

````{prf:example}
:label: example-8-4
:enumerator: 8.4

A string is wrapped around a uniform solid cylinder of radius of *R* and mass of *M* as in Fig. [](#fig-8-9). If the cylinder is released from rest while the string is fixed in place and assuming that the string does not slip at the cylinder’s surface, find: (a) the acceleration of the center of mass using Newton’s laws (b) the acceleration of the center of mass using energy methods if the cylinder descends a distance $h(\mathrm {c})$ the tension in the string.


:::{admonition} Solution 8.4
:class: dropdown

(a) Applying Newton’s second law in both the linear and angular form gives

```{math}
:label: eq-8-5
\begin{aligned} \displaystyle \sum F_{y}=T-Mg=-Ma_{cm} \end{aligned}
```

```{math}
\sum \tau =TR=I_{cm}\alpha =\frac{1}{2}MR^{2}(\frac{a_{cm}}{R})
```

hence

```{math}
:label: eq-8-6
\begin{aligned} T=\displaystyle \frac{1}{2}Ma_{cm} \end{aligned}
```

Substituting Eq. [](#eq-8-6) into Eq. [](#eq-8-5) gives

```{math}
-M_{9}+\frac{1}{2}Ma_{cm}=-Ma_{cm}
```

that gives

```{math}
a_{cm}=\frac{2}{3}g
```

(b) Energy Method

```{math}
K_{i}+U_{i}=K_{f}+U_{f}
```

```{math}
0+Mgh=\frac{1}{2}Mv_{cm}^{2}+\frac{1}{2}I_{cm}\omega ^{2}
```

```{math}
0+Mgh=\frac{1}{2}Mv_{cm}^{2}+\frac{1}{2}\bigg (\frac{1}{2}MR^{2}\bigg )\bigg (\frac{v_{cm}}{R}\bigg )^{2}
```

that gives

```{math}
v_{cm}=\sqrt{\frac{4}{3}gh}
```

From the expression $v^{2}=v_{0}^{2}+2a_{cm}h$, and since $v_{0}=0$ we have

```{math}
a_{cm}=\frac{v_{cm}^{2}}{2h}=\frac{4gh}{3(2h)}=\frac{2}{3}g
```

(b) From Eq. [](#eq-8-6),

```{math}
T=\frac{1}{2}Ma_{cm}=\frac{1}{2}M\bigg (\frac{2}{3}g\bigg )=\frac{1}{3}Mg
```

:::
````

```{figure} ../images/ch-08/459974_1_En_8_Fig9_HTML.png
:name: fig-8-9

A string wrapped around a uniform solid cylinder of radius of *R* and mass of *M*
```

````{prf:example}
:label: example-8-5
:enumerator: 8.5

A uniform solid sphere of radius *R* and mass *M* is released from rest at the top of an incline at a distance *h* above the ground. If it rolls without slipping, find the speed of the center of mass at the bottom of the incline.


:::{admonition} Solution 8.5
:class: dropdown

```{math}
K_{i}+U_{i}=K_{f}+U_{f}
```

```{math}
0+Mgh=\frac{1}{2}Mv_{cm}^{2}+\frac{1}{2}I_{cm}\omega ^{2}
```

```{math}
0+Mgh=\frac{1}{2}Mv_{cm}^{2}+\frac{1}{2}\bigg (\frac{2}{5}MR^{2}\bigg )\bigg (\frac{v_{cm}}{R}\bigg )^{2}
```

That gives

```{math}
v_{cm}=\sqrt{\frac{10}{7}gh}
```

:::
````

````{prf:example}
:label: example-8-6
:enumerator: 8.6

A block of mass *m* is attached to a light string that passes over a light pulley and is connected to a uniform solid sphere of radius *R* and mass *M* as in Fig. [](#fig-8-10). Show that the acceleration of the system is $a=\displaystyle \frac{g}{1+{7}/5({M_{/m}})}$ when the block is released from rest.


:::{admonition} Solution 8.6
:class: dropdown

From conservation of energy, we have

```{math}
mgh=\frac{1}{2}Mv_{cm}^{2}+\frac{1}{2}I_{cm}\omega ^{2}+\frac{1}{2}mv^{2}
```

Since the block and the sphere are connected, they have the same speed, therefore

```{math}
mgh=\frac{1}{2}Mv^{2}+\frac{1}{2}\bigg (\frac{2}{5}MR^{2}\bigg )\bigg (\frac{v^{2}}{R}\bigg )^{2}+\frac{1}{2}mv^{2}
```

Therefore, the speed of the system when the block is at the bottom of the incline is

```{math}
v=\sqrt{\frac{2gh}{1+7M/5m}}
```

The acceleration of the system is

```{math}
v^{2}-v_{0}^{2}=2ah
```

or

```{math}
a=\frac{v^{2}}{2h}=\frac{2gh}{2h(1+7/{5}(M/{m}))}
```

that gives

```{math}
a=\frac{g}{(1+7/{5}(M/{m}))}
```

:::
````

```{figure} ../images/ch-08/459974_1_En_8_Fig10_HTML.png
:name: fig-8-10

A block of mass *m* is attached to a light string that passes over a light pulley connected to a uniform solid sphere of radius *R* and mass *M*
```

(sec-8-3)=
## 8.3 Static Equilibrium

An extended object is said to be in equilibrium if two conditions are satisfied. First, the net external force acting on the object must be equal to zero. Second, the net external torque on the object about any origin must also be equal to zero. In other words, an object is in equilibrium if its total linear momentum and its total angular momentum (about any origin) are constants. Only the first condition is necessary if the object can be treated as a particle. Thus, the conditions of equilibrium may be written as

```{math}
:label: eq-8-7
\begin{aligned} \displaystyle \sum \mathbf {F}= \mathbf {0} \; (Translational\, Equilibrium) \end{aligned}
```

```{math}
:label: eq-8-8
\begin{aligned} \displaystyle \sum \boldsymbol{\tau }=\mathbf {0} \; (Rotational\, Equilibrium) \end{aligned}
```

In terms of components, we may write

```{math}
:label: eq-8-9
\begin{aligned} \displaystyle \sum F_{x}=0, \; \sum F_{y}=0, \; \sum F_{z}=0 \end{aligned}
```

```{math}
:label: eq-8-10
\begin{aligned} \displaystyle \sum \tau _{x}=0, \; \sum \tau _{y}=0, \; \sum \tau _{z}=0 \end{aligned}
```

An object is said to be in static equilibrium if it is at rest (there isn’t any kind of motion with respect to our inertial frame of reference). Now consider the case in which all external forces acting on the object lie in the same plane (for example the x–y plane). Such forces are called coplanar forces. The net external torque due to these forces is then perpendicular to the x–y plane and parallel to the $\mathrm {z}$-axis. Equations [](#eq-8-9) and [](#eq-8-10) are, therefore, reduced to

```{math}
\sum F_{x}=0, \; \sum F_{y}=0, \; \sum \tau _{z}=0
```

Next, we will prove that if the object is in translational equilibrium where $(\varSigma \mathbf {F}=\mathbf {0})$ and the net external torque on the object is equal to zero about some origin, it is also equal to zero about any other origin. Note that the origin may be chosen anywhere inside or outside the object. Suppose that a number of forces $\mathbf {F}_{1},\mathbf {F}_{2},\mathbf {F}_{3}, \ldots \mathbf {F}_{n}$ are acting on a rigid object at different points (see Fig. [](#fig-8-11)) and that the object is in translational equilibrium. The point of application of $\mathbf {F}_{1}$ relative to $\mathrm {O}$ is $\mathrm {r}_{1}$ and of $\mathbf {F}_{2}$ is $\mathrm {r}_{2}$ and so on. The net external torque about $\mathrm {O}$ is given by

```{math}
\sum \boldsymbol{\tau }_{0}=\boldsymbol{\tau }_{1}+\boldsymbol{\tau }_{2}+ \cdots +\boldsymbol{\tau }_{n}=\mathbf {r}_{1}\,\times \,\mathbf {F}_{1}+\mathbf {r}_{2}\,\times \,\mathbf {F}_{2}+\ + \cdots \mathbf {r}_{n}\,\times \,\mathbf {F}_{n}
```

The net external torque about $\mathrm {O}'$ (see Fig. [](#fig-8-12)) is

```{math}
\sum \boldsymbol{\tau }_{0'}=\boldsymbol{\tau }_{1}'+\boldsymbol{\tau }_{2}'+\ + \cdots \boldsymbol{\tau }_{n}'=\mathbf {r}_{1}'\times \mathbf {F}_{1}+\mathbf {r}_{2}'\times \mathbf {F}_{2}+\ + \cdots \mathbf {r}_{n}'\times \mathbf {F}_{n}
```

```{math}
=(\mathbf {r}_{1}-\mathbf {r}_{0'})\times \mathbf {F}_{1}+(\mathbf {r}_{2}-\mathbf {r}_{0'})\times \mathbf {F}_{2}+ \cdot + \cdots (\mathbf {r}_{n}-\mathbf {r}_{0'})\times \mathbf {F}_{n}
```

```{math}
=\mathbf {r}_{1}\times \mathbf {F}_{1}+\mathbf {r}_{2}\times \mathbf {F}_{2}+. + \cdots \mathbf {r}_{n}\times \mathbf {F}_{n}-(\mathbf {r}_{0'}\times \mathbf {F}_{1}+\mathbf {r}_{0'}\times
```

```{math}
\,\mathbf {F}_{2}+\ + \cdots \mathbf {r}_{0'}\times \mathbf {F}_{n})
```

```{math}
=\sum \boldsymbol{\tau }_{0}-\ (\mathbf {r}_{0'}\times \ (\mathbf {F}_{1}+\mathbf {F}_{2}+\ +\mathbf {F}_{n}))=\sum \tau _{0}-(\mathbf {r}_{0'}\times \sum \mathbf {F})
```

Since $\varSigma \mathbf {F}=\mathbf {0}$ we have

```{math}
\sum \boldsymbol{\tau }_{0'}=\sum \boldsymbol{\tau }_{0}
```

```{figure} ../images/ch-08/459974_1_En_8_Fig11_HTML.png
:name: fig-8-11

A number of forces $\mathbf {F}_{1},\mathbf {F}_{2},\mathbf {F}_{3},..\mathbf {F}_{n}$ act on a rigid object at different points
```

```{figure} ../images/ch-08/459974_1_En_8_Fig12_HTML.png
:name: fig-8-12

The net external torque on the object about $\mathrm{O}'$
```

(sec-8-4)=
## 8.4 The Center of Gravity

The resultant gravitational force acting on an object is the resultant of the individual gravitational forces acting on different mass elements of the object (see Fig. [](#fig-8-13)), i.e.,

```{math}
:label: eq-8-11
\begin{aligned} \displaystyle \sum \mathbf {F}=\sum m_{i}\mathbf {g} \end{aligned}
```

This force can be replaced by a single force that is equal to the weight of the object (*M*g) and that acts at a single point called the center of gravity Now consider an object that is near the earth’s surface where the force of gravity is assumed to be constant over that range. Equation [](#eq-8-11) becomes

```{math}
\sum \mathbf {F}=\sum m_{i}\mathbf {g}=\mathbf {g}\sum m_{i}=M\mathbf {g}=\mathbf {w}
```

To locate the center of gravity, let us calculate the net torque acting on an object about an origin due to gravity This torque is the vector sum of the individual torques acting on different mass elements. That is,

```{math}
\boldsymbol{\tau }=\sum _{i}\boldsymbol{\tau }_{i}=\sum _{i}(\mathbf {r}_{i}\times m_{i}\mathbf {g})=\bigg (\sum _{i}m_{i}\mathbf {r}_{i}\bigg )\times \mathbf {g}
```

```{math}
\boldsymbol{\tau }=\frac{\bigg (\sum _{i}m_{i}\mathbf {r}_{i}\bigg )}{M}\times M\mathbf {g}\ =\mathbf {r}_{cm}\times \mathbf {w}
```

```{math}
\boldsymbol{\tau }=\mathbf {r}_{cm}\times \mathbf {w}
```

Therefore, we conclude that if the gravitational field (g) is constant over the body, the center of gravity of the object coincides with its center of mass.

```{figure} ../images/ch-08/459974_1_En_8_Fig13_HTML.png
:name: fig-8-13

The resultant gravitational force acting on an object is the resultant of the individual gravitational forces acting on different mass elements of the object
```

````{prf:example}
:label: example-8-7
:enumerator: 8.7

Two blocks of masses $m_{2}=20$ kg and $m_{1}=10$ kg are supported by a uniform horizontal beam of length $L=1.5\mathrm {m}$ and mass $M=6$ kg (see Fig. [](#fig-8-14)). Find: (a) the normal force exerted by the fulcrum (supporting point) on the beam if it is placed under the center of gravity of the beam; (b) the distance *x* in which $m_{2}$ must be placed in order for the system to be balanced.


:::{admonition} Solution 8.7
:class: dropdown

(a) The free-body diagram of the system in shown in Fig. [](#fig-8-14) where $w_{1}= 196 \; \mathrm {N}, w_{2}=98 \; \mathrm {N}$, and $w=58.8 \; \mathrm {N}$. Applying Newton’s second law to the beam gives

```{math}
\sum F_{y}=n-(59 \; \mathrm {N})-(98 \; \mathrm {N})-(196 \; \mathrm {N})=0
```

and

```{math}
n=353 \; \mathrm {N}
```

(b) The net external torque about an axis passing through the center of the beam and perpendicular to the page is

```{math}
\sum \tau _{z}=(98 \; \mathrm {N})(0.75 \; \mathrm {m})-(196 \; \mathrm {N})x=0
```

```{math}
x=0.37 \; \mathrm {m}
```

:::
````

```{figure} ../images/ch-08/459974_1_En_8_Fig14_HTML.png
:name: fig-8-14

Two blocks supported by a uniform horizontal beam
```

```{figure} ../images/ch-08/459974_1_En_8_Fig15_HTML.png
:name: fig-8-15

The free-body diagram of a ladder of length *L* and mass $M=20$ kg resting against a smooth vertical wall
```

````{prf:example}
:label: example-8-8
:enumerator: 8.8

A ladder of length *L* and mass $M=20$ kg rests against a smooth vertical wall as shown in Fig. [](#fig-8-15). If the center of gravity of the ladder is at a distance of *L*/3 from the base, determine: (a) the minimum coefficient of static friction such that the ladder does not slip; (b) the magnitude and direction of the resultant of the contact forces acting on the ladder at the base; (c) if a man of mass of $70 \; \mathrm {k}\mathrm {g}$ climbs up the ladder, what is the maximum distance the man can climb before the ladder slips if $\mu _{s}=0.4.$


:::{admonition} Solution 8.8
:class: dropdown

(a) Figure [](#fig-8-15) shows the free-body diagram of the ladder. Applying Newton’s second law to the ladder gives

```{math}
\sum F_{x}=f_{s}-n_{2}=0
```

```{math}
f_{s}=n_{2}
```

and

```{math}
\sum F_{y}=n_{1}-Mg=0
```

```{math}
n_{1}=Mg
```

Applying Newton’s second law in angular form about $\mathrm {O}$ (the point must be chosen to give minimum unknowns) we have

```{math}
:label: eq-8-12
\begin{aligned} \displaystyle \sum \tau _{z}=n_{2}L\sin \theta -\frac{1}{3}MgL\cos \theta =0 \end{aligned}
```

If the ladder is at the verge of slipping the statistical frictional force is maximum $f_{s}=\mu _{s}n_{1}$. From Eq. [](#eq-8-12), we have

```{math}
n_{2}=\frac{Mg}{3\tan \theta }=\frac{(196 \; \mathrm {N})}{3\tan (51^{\circ })}=53 \; \mathrm {N}=f_{s}
```

hence

```{math}
\mu _{s}=\frac{f_{s}}{n_{1}}=\frac{(53 \; \mathrm {N})}{(196 \; \mathrm {N})}=0.27
```

(b) The resultant of the contact forces on the ladder at the base is

```{math}
F_{R}=\sqrt{f_{s}^{2}+n_{1}^{2}}=\sqrt{(53 \; \mathrm {N})^{2}+(196)^{2} \; \mathrm {N}}=203 \; \mathrm {N}
```

the direction of $F_{R}$ is

```{math}
\phi =\tan ^{-1}\frac{n_{1}}{f_{s}}=\tan ^{-1}\frac{(196 \; \mathrm {N})}{(52.9 \; \mathrm {N})}=75^{\circ }
```

(c) The free-body diagram is shown in Fig. [](#fig-8-15). From the equilibrium condition, we have

```{math}
\sum F_{x}=f_{s}-n_{2}=0
```

and

```{math}
\sum F_{y}=n_{1}-mg-Mg=0
```

or

```{math}
f_{s}=n_{2}
```

and

```{math}
n_{1}=(m+M)g
```

Furthermore, the resultant external torque about $\mathrm {O}$ is

```{math}
\sum \tau _{z}=n_{2}L\sin \theta -\frac{1}{3}MgL\cos \theta -mgx\cos \theta =0
```

thus

```{math}
n_{2}=\frac{g}{\tan \theta }\bigg (\frac{M}{3}+m\bigg (\frac{x}{L}\bigg )\bigg )
```

at the verge of slipping

```{math}
f_{s}=\mu _{s}n_{1}=\mu _{s}g(M+m)=(0.4)(9.8 \; \mathrm {m}/\mathrm {s}^{2})(90 \; \mathrm {k}\mathrm {g})=353 \; \mathrm {N}=n_{2}
```

Hence

```{math}
x=0.54 \; L
```

:::
````

````{prf:example}
:label: example-8-9
:enumerator: 8.9

A uniform beam of weight *w* and length *L* is held by two supports as in Fig. [](#fig-8-16). A block of weight $w_{1}$ is resting on the beam at a distance of *L*/6 from the center of gravity of the beam. Find the magnitude of the forces exerted by the supports on the beam.


:::{admonition} Solution 8.9
:class: dropdown

The free-body diagram of the system is shown in Fig. [](#fig-8-16). Because the beam has a uniform density its center of mass and gravity are located at its geometrical center. Applying Newton’s second law gives

```{math}
\sum F_{y}=0
```

```{math}
:label: eq-8-13
\begin{aligned} F_{2}+F_{1}-w-w_{1}=0 \end{aligned}
```

Taking the torque about an axis passing through one end (at $F_{1}$) gives

```{math}
\sum \tau _{z}=0
```

```{math}
:label: eq-8-14
\begin{aligned} F_{2}L-\displaystyle \frac{2}{3}Lw_{1}-\frac{L}{2}w=0 \end{aligned}
```

From Eqs. [](#eq-8-13) and [](#eq-8-14) we have

```{math}
F_{2}=\frac{2}{3}w_{1}+\frac{w}{2}
```

and

```{math}
F_{1}=\frac{w_{1}}{3}+\frac{w}{2}
```

:::
````

```{figure} ../images/ch-08/459974_1_En_8_Fig16_HTML.png
:name: fig-8-16

A uniform beam of weight *w* and length *L* balanced by two supports
```

````{prf:example}
:label: example-8-10
:enumerator: 8.10

A man of mass of 80 kg is standing at the end of a uniform beam of mass of 30 kg and length of 12 $\mathrm {m}$ as shown in Fig. [](#fig-8-17). Find the tension in the rope and the reaction force exerted by the hinge on the beam.


:::{admonition} Solution 8.10
:class: dropdown

(a) The free-body diagram is shown in Fig. [](#fig-8-17). Applying Newton’s second law to the beam gives

```{math}
\sum F_{y}=T\sin 50^{\circ }+F_{R}\sin \theta -(294 \; \mathrm {N})-(784 \; \mathrm {N})=0
```

```{math}
\sum F_{x}=F_{R}\cos \theta -T\cos 50^{\circ }=0
```

The resultant torque about an axis passing through $\mathrm {O}$ is

```{math}
\sum \tau _{z}=T\sin 50^{\circ }L-L(784\,\mathrm {N})-\frac{L}{2}(294\,\mathrm {N})=0
```

That gives $T=1215.3$ N. Hence

```{math}
:label: eq-8-15
\begin{aligned} F_{R}\cos \theta =T \cos 50^{\circ } = (1215.3 \; \mathrm {N} ) (0.64)=781.2 \; \mathrm {N} \end{aligned}
```

and

```{math}
:label: eq-8-16
\begin{aligned}&F_{R}\sin \theta =-T \sin 50^{\circ } +(294 \; \mathrm {N})+(784 \; \mathrm {N}) \nonumber \\&=-(1215.3 \; \mathrm {N})(0.76)+(294 \; \mathrm {N})+(784 \; \mathrm {N})=147 \; \mathrm {N} \end{aligned}
```

Dividing Eq. [](#eq-8-16) by Eq. [](#eq-8-15) gives

```{math}
\tan \theta =\frac{(147 \; \mathrm {N})}{(781.2 \; \mathrm {N})}=0.2
```

```{math}
\theta =10.6^{\circ }
```

and

```{math}
F_{R}=\sqrt{(147)^{2}+(7812)^{2}}=795 \; \mathrm {N}
```

:::
````

```{figure} ../images/ch-08/459974_1_En_8_Fig17_HTML.png
:name: fig-8-17

A man standing at the end of a uniform beam
```

````{prf:example}
:label: example-8-11
:enumerator: 8.11

A uniform beam of weight of 120 $\mathrm {N}$ and length of *L* is in horizontal static equilibrium as in Fig. [](#fig-8-18). Neglecting the masses of the ropes, find the tension in each string. (The center of mass is at *L*/3 from one end).


:::{admonition} Solution 8.11
:class: dropdown

The free-body diagram is shown in Fig. [](#fig-8-18). Applying Newton’s second law to the beam gives

```{math}
\displaystyle \sum F_{y}=T_{1}\cos \theta +T_{2} \cos 30^{\circ }-(120 \; \mathrm {N})=0
```

or

```{math}
:label: eq-8-17
\begin{aligned} T_{1}\cos \theta +T_{2}(0.87)=(120 \; \mathrm {N}) \end{aligned}
```

Also

```{math}
\sum F_{x}=T_{1}\sin \theta -T_{2}\sin 30^{\circ }=0
```

or

```{math}
:label: eq-8-18
\begin{aligned} T_{1}\sin \theta =T_{2}\sin 30^{\circ } \end{aligned}
```

Taking the resultant torque on the beam about one end (at $T_{1}$) gives

```{math}
\sum \tau =(120 \; \mathrm {N})\frac{L}{3}-LT_{2}\cos 30^{\circ }=0
```

or

```{math}
T_{2}=46.2 \; \mathrm {N}
```

Substituting $T_{2}$ into Eqs. [](#eq-8-18) and [](#eq-8-17) gives

```{math}
T_{1}\sin \theta =(46.2 \; \mathrm {N}) \sin 30^{\circ } = 23.1 \; \mathrm {N}
```

and

```{math}
T_{1}\cos \theta +(46.2 \; \mathrm {N})(0.87)=(120 \; \mathrm {N})
```

```{math}
T_{1}\cos \theta =80 \; \mathrm {N}
```

Hence

```{math}
\tan \theta =\frac{(23.1 \; \mathrm {N})}{(80 \; \mathrm {N})}=0.3
```

That gives $\theta =16.7^{\circ }$ and $T_{1}=(23.1 \; \mathrm {N})/\sin 16.7^{\circ }=80.3 \; \mathrm {N}$.

:::
````

```{figure} ../images/ch-08/459974_1_En_8_Fig18_HTML.png
:name: fig-8-18

A uniform beam held by ropes in static equilibrium
```

````{prf:example}
:label: example-8-12
:enumerator: 8.12

A solid sphere of mass of 12 kg is in static equilibrium inside the wedge shown in Fig. [](#fig-8-19). If the surface of the wedge is frictionless, find the forces that the wedge exerts on the sphere.


:::{admonition} Solution 8.12
:class: dropdown

Applying Newton’s second law gives

```{math}
\sum F_{x}=F_{1}\sin 50^{\circ }-F_{2}\sin 30^{\circ }=0
```

or

```{math}
F_{1}=0.65F_{2}
```

Also we have

```{math}
\sum F_{y}=F_{1}\cos 50^{\circ }+F_{2}\cos 30^{\circ }-Mg=0
```

or

```{math}
0.65F_{2}\cos 50^{\circ }+F_{2}\cos 30^{\circ }-Mg=0
```

That gives $F_{2}=91.6 \; \mathrm {N}$. Therefore

```{math}
F_{1}=0.65F_{2}=0.65(91.6 \; \mathrm {N})=59.5 \; \mathrm {N}
```

:::
````

```{figure} ../images/ch-08/459974_1_En_8_Fig19_HTML.png
:name: fig-8-19

A solid sphere in static equilibrium inside a wedge
```

## Problems

```{exercise}
:label: prob-8-1
:enumerator: 8.1

A uniform cylinder of mass 3 kg and radius of 0.05 $\mathrm {m}$ rolls without slipping along a horizontal surface. Find the total energy of the cylinder at the instant its speed is 2 $\mathrm {m}/\mathrm {s}.$
```

```{exercise}
:label: prob-8-2
:enumerator: 8.2

A uniform solid cylinder of mass 10 kg and radius of 0.2 $\mathrm {m}$ rolls up the incline of angle $45^{\circ }$ with an initial velocity of 15 $\mathrm {m}/\mathrm {s}$. Find the height in which the cylinder will stop.
```

```{exercise}
:label: prob-8-3
:enumerator: 8.3

A wheel of mass 2 kg and radius of 0.05 $\mathrm {m}$ rolls without slipping with an angular speed of 3 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$ on a horizontal surface. How much work is required to accelerate the wheel to an angular speed of 15 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}.$
```

```{exercise}
:label: prob-8-4
:enumerator: 8.4

A block weighing 1000 $\mathrm {N}$ is held by a cable that is attached to a uniform rod of weight 500 $\mathrm {N}$ (see Fig. [](#fig-8-20)). Find (a) the tension in the cable, (b) the horizontal and vertical components of the force exerted on the base of the rod.
```

```{exercise}
:label: prob-8-5
:enumerator: 8.5

A uniform sphere of radius *r* and mass *m* is held by a light string and leans on a frictionless wall as in Fig. [](#fig-8-21). If the string is attached a distance *d* above the center of the sphere, find (a) the tension in the string, (b) the reaction force exerted by the wall on the sphere.
```

```{exercise}
:label: prob-8-6
:enumerator: 8.6

Find the minimum force applied at the top of a wheel of mass *M* and radius *R* to raise it over a step of height *h* as in Fig. [](#fig-8-22). Assume that the wheel does not slip on the step.
```

```{exercise}
:label: prob-8-7
:enumerator: 8.7

Three identical uniform blocks each of length *L* are on top of each other as in Fig. [](#fig-8-23). Find the maximum value of *h* in order for the stack to be in equilibrium.
```

```{figure} ../images/ch-08/459974_1_En_8_Fig20_HTML.png
:name: fig-8-20

A block suspended by a cable attached to a uniform rod
```

```{figure} ../images/ch-08/459974_1_En_8_Fig21_HTML.png
:name: fig-8-21

A uniform sphere suspended by a light string and leaning on a frictionless wall
```

```{figure} ../images/ch-08/459974_1_En_8_Fig22_HTML.png
:name: fig-8-22

A wheel raised over a step
```

```{figure} ../images/ch-08/459974_1_En_8_Fig23_HTML.png
:name: fig-8-23

Three identical uniform blocks on top of each other
```
