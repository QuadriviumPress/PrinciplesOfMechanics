---
title: 4. Work and Energy
short_title: "Ch. 4 — Work and Energy"
label: ch-4
doi: 10.1007/978-3-030-15195-9_4
---

(sec-4-1)=
## 4.1 Introduction

Energy is a very important concept that is heavily used in everyday life. Everything around us, including ourselves, needs energy to function. For example, electricity provides home appliances with the energy they require, food gives us energy to survive, and the sun provides earth with the energy needed for the existence of life!

Experiments show that energy is a scalar quantity related to the state of an object. Energy may exist in various forms: mechanical, chemical, gravitational, electromagnetic, nuclear, and thermal. Furthermore, energy cannot be created or destroyed; it can only be transformed from one form to another. In other words, if energy were to be exchanged between objects inside a system, then the total amount of energy (the sum of all forms of energy) in the system will remain constant.

A transformation of energy occurs due to the action of a force known as work or due to heat exchange between objects (or between an object and its environment). If energy is transferred due to work then it may be defined as the capacity of doing work. This book is concerned with mechanical energy which involves kinetic energy (associated with the object’s motion) and potential energy (associated with the position of the object in space).

(sec-4-2)=
## 4.2 Work

Work may have many meanings. Sometimes, work is said to be done when a muscular activity is performed. Work may also refer to mental activity (mental work). In physics, the definition of work is different. Work is said to be done if a force is applied to an object while it is moving, i.e., if there is no resulting displacement, no work is done. Suppose that a person holds a heavy box for sometime and then starts to feel tired. The reason he/she feels tired is because chemical energy in his/her body is converted into internal microscopic motions of the muscles. Since the energy is not transferred to the box being carried (the box did not move), the work done on the box is equal to zero.

(sec-4-2-1)=
### 4.2.1 Work Done by a Constant Force

Consider an object exposed to a constant force $\mathrm {F}$ (see Fig. [](#fig-4-1)). If the object is displaced through a displacement $\mathrm {s}$, then the work done on the object is a scalar quantity defined as

```{math}
W=Fs\cos \theta =\mathbf {F}\cdot \mathbf {s}
```

where $\theta$ is the smaller angle between $\mathbf {F}$ and $\mathbf {s}$. The component of $\mathbf {F}$ in the direction of $\mathbf {s}$ $(F\cos \theta )$ is the only effective component that produces motion. The work done represents energy transferred to or from the object via that force. If $(\theta =0)$, the work done on the object is positive, i.e. energy is transferred to the object. If $(\theta =180^{\mathrm {o}})$, the work done is negative, i.e., energy is transferred from the object. The SI unit of work is Newton meter (N.m) also named as the Joule.

```{math}
1\,\text {Joul}\, =1\,\mathrm {J}=1\,\text {kg}.\mathrm {m}^{2}/\mathrm {s}^{2}
```

Note that energy and work have the same units.

(sec-4-2-2)=
### 4.2.2 Work Done by Several Forces

Consider an object exposed to several forces as in Fig. [](#fig-4-2). The work done by all of these forces is the sum of the individual amounts of work done by each force:

```{math}
W=\mathbf {F}_{1}\cdot \mathbf {s}+\mathbf {F}_{2}\cdot \mathbf {s}+\mathbf {F}_{3}\cdot \mathbf {s}+\cdots
```

```{math}
W=W_{1}+W_{2}+W_{3}+
```

Another method to find the work is by considering the resultant of these forces:

```{math}
W=\bigg (\sum \mathbf {F}\bigg )\cdot \mathbf {s}
```

where

```{math}
\Sigma \mathbf {F}=\mathbf {F}_{1}+\mathbf {F}_{2}+\mathbf {F}_{3}+
```

```{figure} ../images/ch-04/459974_1_En_4_Fig1_HTML.png
:name: fig-4-1

An object exposed to a constant force $\mathbf {F}$ and undergoes a displacement of $\mathbf {s}$
```

```{figure} ../images/ch-04/459974_1_En_4_Fig2_HTML.png
:name: fig-4-2

An object exposed to several forces undergoes a displacement of $\mathbf {s}$
```

````{prf:example}
:label: example-4-1
:enumerator: 4.1

A lady pulls an 80 kg block horizontally on a rough surface by a constant force of 400 $\mathrm {N}$ that is at $20^{\mathrm {o}}$ to the horizontal. If the block is pulled a distance of $6\,\mathrm {m}$ and if the opposing force of friction has a magnitude of 118 $\mathrm {N}:(\mathrm {a})$ determine the work done on the block by each of the applied force, the frictional force, the normal force, and the force of gravity; (b) find the total work done on the block; (c) determine if it is easier for the lady to pull the block at an angle larger than $20^{\circ }$.

:::{admonition} Solution 4.1
:class: dropdown

(a) The work done by the applied force is

```{math}
W_{app}=\mathbf {F}\cdot \mathbf {s}=Fs\cos \theta =(400\,\mathrm {N})(6\,\mathrm {m}) \cos 20^{\circ } =2255.3\,\mathrm {J}
```

The work done by the frictional force is

```{math}
W_{f}=Fs\cos \theta =(118\,\mathrm {N})(6\,\mathrm {m}) \cos 180^{\circ } =-708\,\mathrm {J}
```

The work done by the normal force and the force of gravity are both zero since each force is perpendicular to the displacement.

(b) The total work done is

$W_{tot}=W_{app}+W_{f}= (2255.3\,\mathrm {J})-(708\,\mathrm {J})=1547.3\,\mathrm {J}$

The total work done can also be found by computing the net force acting on the block and calculating its work.

(c) For $(0\le \theta \le 90^{\mathrm {o}})$, If $\theta _{2}>\theta _{1}$, then $\cos \theta _{2}<\cos \theta _{1}$ and therefore $W_{app2}< W_{app1}$, i.e., it is easier for the man to pull at an angle larger than $20^{\mathrm {o}}$.

:::
````

````{prf:example}
:label: example-4-2
:enumerator: 4.2

A delivery man wants to push a crate up a ramp of length *s*: (a) find the minimum work the man must do to lift the crate to the top of the ramp; (b) determine if a ramp with a steeper incline would be more difficult for the man to push the crate.

:::{admonition} Solution 4.2
:class: dropdown

(a) The minimum work that the delivery man must do is the work done against gravity The work done on the crate by the force of gravity is

```{math}
W_{g}=-mgs\sin \theta
```

Hence the minimum work $W_{w}$ that the delivery man must do is equal to $+mgs\sin \theta.$

(b) For angles between 0 and $90^{\mathrm {o}}$, if $\theta _{2}>\theta _{1}$, then $\sin \theta _{2}>\sin \theta _{1}$. Hence $W_{w2}\ge W_{w1}$, i.e., the more inclined the ramp is the more difficult it is to move the crate.

:::
````

(sec-4-2-3)=
### 4.2.3 Work Done by a Varying Force

Previously, the work done in the special case of a force that is constant in both magnitude and direction was discussed. The object there moved along a straight line. In many situations, the force may vary in magnitude or in direction or in both, and the object may move along a curved path. To find the work done in this case, consider a particle moving along the curved path shown in Fig. [](#fig-4-3). While it is moving, a force $\mathbf {F}$ that varies in both magnitude and direction with the position of the particle acts on it. Let us divide the path into a large number *n* of very small displacements where each is tangent to the path. For each displacement, the force can be approximated to be constant in both magnitude and direction. The total work done as the particle moves from $\mathrm {P}$ to $\mathrm {Q}$ is the sum of the individual amounts of work done along each displacement, that is

```{math}
W=\mathbf {F}_{1}\cdot \triangle \mathbf {r}_{1}+\mathbf {F}_{2}\cdot \triangle \mathbf {r}_{2}+\mathbf {F}_{3}\cdot \triangle \mathbf {r}_{2}+\cdots \mathbf {F}_{n}\cdot \triangle \mathbf {r}_{n}
```

```{math}
W=\sum _{i=1}^{n}\mathbf {F}_{i}\cdot \triangle \mathbf {r}_{i}
```

By dividing the path into more displacements we have

```{math}
W=\lim _{\triangle \mathbf {r}_{i}\rightarrow 0}\sum _{i=1}^{n}\mathbf {F}_{i}\cdot \triangle \mathbf {r}_{i}
```

or

```{math}
W=\int _{C}\mathbf {F}\cdot d\mathbf {r}=\int _{P}^{Q}\mathbf {F}\cdot d\mathbf {r}
```

As mentioned in Sect. 1.​10.​1, this integral is called the line integral. Each component of $\mathbf {F} (F_{x},\ F_{y}\ \mathrm {o}\mathrm {r}\ F_{z})$ may be a function of *x*, *y*, and *z*, and the curve can be determined by its equations that relates *x*, *y*, and *z* to each other. The component form of the above equation is

```{math}
\begin{aligned} W=\displaystyle \int _{\mathbf {r}_{i}}^{\mathbf {r}_{f}}\mathbf {F}\cdot d\mathbf {r}=\int _{x_{i}}^{x_{f}}F_{x}dx+\int _{y_{i}}^{y_{f}}F_{y}dy+\int _{z_{i}}^{z_{f}}F_{z}{dz} \end{aligned}
```

Now consider the case in which the particle moves along a straight line (for example the positive $\mathrm {x}$-axis) and in which the force acting on the particle has a constant direction along the $\mathrm {x}$-axis and a magnitude that varies with *x*. Equation 4.1 is then reduced to

```{math}
\begin{aligned} W=\displaystyle \int _{x_{i}}^{x_{f}}F_{x}(x)dx \end{aligned}
```

This equation represents the area under the curve in Fig. [](#fig-4-4). If *F*(*x*) is constant then we have

```{math}
W=\int _{x_{i}}^{x_{f}}F_{x}(x)dx=F\int _{x_{i}}^{x_{f}}dx=F(x_{f}-x_{i})=Fs
```

The work is then equal to the rectangular area shown in Fig. [](#fig-4-5).

```{figure} ../images/ch-04/459974_1_En_4_Fig3_HTML.png
:name: fig-4-3

A particle moving along a curved path. While itõs moving, a force $\mathbf {F}$ that varies in both magnitude and direction with the position of the particle acts on it
```

```{figure} ../images/ch-04/459974_1_En_4_Fig4_HTML.png
:name: fig-4-4

The area under the curve represents the work
```

```{figure} ../images/ch-04/459974_1_En_4_Fig5_HTML.png
:name: fig-4-5

The work is equal to the rectangular area
```

````{prf:example}
:label: example-4-3
:enumerator: 4.3

In Example 3.3, find the work done by the force in moving the particle during the time interval from $t=0$ to $t=1\,\mathrm {s}.$

:::{admonition} Solution 4.3
:class: dropdown

The work done from $t=0$ to $t=1\,\mathrm {s}$ is

```{math}
\begin{aligned} W= & {} \displaystyle \int _{t=0}^{t=1}\mathbf {F}\cdot \mathbf {d}\mathrm {r}=\int _{t=0}^{t=1}(2t^{2}\mathbf {i}-3t\mathbf {j}). (1/3t^{4}\displaystyle \mathbf {i}-t^{3}\mathbf {j})dt\\ {}= & {} \int _{t=0}^{t=1}(0.66t^{6}+3t^{4})dt \end{aligned}
```

```{math}
=(0.1t^{7}+0.6t^{5})|_{t=0}^{t=1}=0.7\,\mathrm {J}
```

:::
````

````{prf:example}
:label: example-4-4
:enumerator: 4.4

A force acting on a particle is a function of position according to Fig. [](#fig-4-6). Find the work done by this force as the particle moves from $x_{i}=0$ to $x_{f}=9\,\mathrm {m}.$

:::{admonition} Solution 4.4
:class: dropdown

The work done is equal to the area of the triangle under the curve between $x_{i}=0$ to $x_{f}=9\,\mathrm {m}$, i.e.

```{math}
W=\frac{1}{2}(9\,\mathrm {m})(4\,\mathrm {N})=18\,\mathrm {J}
```

:::
````

```{figure} ../images/ch-04/459974_1_En_4_Fig6_HTML.png
:name: fig-4-6

A force acting on a particle is a function of position
```

````{prf:example}
:label: example-4-5
:enumerator: 4.5

A ball that is suspended from a ceiling by a light rope is displaced a small distance to the position shown in Fig. [](#fig-4-7). If it is released from rest at $\mathrm {B}$, find the work done by the tension force and the force of gravity as the ball moves from $\mathrm {B}$ to A.

:::{admonition} Solution 4.5
:class: dropdown

Because the tension force is always perpendicular to the displacement, the work done by it is zero at all times. The only component of the gravitational force that does work is its tangential component. Therefore,

```{math}
W=\int _{0}^{\theta _{0}}\mathbf {F}\cdot d\mathbf {s}=\int _{0}^{\theta _{0}}mg\sin \theta \cos (0)\mathrm {d}\mathrm {s}
```

Since $s=R\theta$, then $ds=Rd\theta$, and we have

```{math}
W=mgR\int _{0}^{\theta _{0}}\sin \theta d\theta =-mgR\cos \theta |_{0}^{\theta _{0}}=mgR(1-\cos \theta _{0})
```

:::
````

```{figure} ../images/ch-04/459974_1_En_4_Fig7_HTML.png
:name: fig-4-7

A ball suspended by a light rope and displaced a small distance from the position of equilibrium
```

```{figure} ../images/ch-04/459974_1_En_4_Fig8_HTML.png
:name: fig-4-8

The center of mass of the system (man+skateboard) moves and the work-energy theorem can be applied to that point
```

(sec-4-3)=
## 4.3 Kinetic Energy (KE) and the Work–Energy Theorem

Consider a particle that is exposed to a net field force and is moving along a curve in space. Suppose that the particle is at $\mathrm {P}$ at $t_{i}$ and at $\mathrm {Q}$ at $t_{f}$ and that its velocity at $\mathrm {P}$ and $\mathrm {Q}$ is $\mathbf {v}_{i}$ and $\mathbf {v}_{f}$, respectively. The net work done on the particle as it moves from $\mathrm {P}$ to $\mathrm {Q}$ is then given by

```{math}
W=\int _{P}^{Q}\mathbf {F}\cdot d\mathbf {r}=\int _{t_{\mathrm {i}}}^{t_{f}} \mathbf {F}\cdot \frac{d\mathbf {r}}{dt}dt=\int _{t_{i}}^{t_{f}}\mathbf {F} \cdot \mathbf {v}dt=\int _{t_{\mathrm {i}}}m\frac{d\mathbf {v}}{dt}\cdot \mathbf {v}dt
```

```{math}
=m\int _{\mathbf {v}_{i}}^{\mathbf {v}_{f}}\mathbf {v}\cdot d\mathbf {v}=\frac{1}{2}m\int _{\mathbf {v}_{\mathrm {i}}}^{\mathbf {v}_{f}}d(\mathbf {v}\cdot \mathbf {v})=\frac{1}{2}m(\mathbf {v}\cdot \mathbf {v})|_{\mathbf {v}_{i}}^{\mathbf {v}_{f}}
```

```{math}
=\frac{1}{2}mv_{f}^{2}-\frac{1}{2}mv_{i}^{2}
```

The quantity $\displaystyle \frac{1}{2}mv^{2}$ is the energy associated with the motion of the particle called the kinetic energy (KE). Thus, if a particle of constant mass *m* is moving with a speed *v*, its KE is a scalar quantity defined as

```{math}
K=\frac{1}{2}mv^{2}
```

It also can be written as $K=\displaystyle \frac{1}{2}m(\mathbf {v}\cdot \mathbf {v})$. Hence, the total work done by the net force in displacing the particle is equal to the change in the KE of the particle

```{math}
W_{net}=K_{f}-K_{i}=\triangle K
```

Similar to work, the SI unit of kinetic energy is the Joul. Note that the work–energy theorem is applied only if the object is treated as a particle (all of its parts move in exactly the same way). As an example of how the theorem is applied only for particle-like objects consider a man standing on a skateboard on a horizontal surface (see Fig. [](#fig-4-8)). If the man pushes the bar then that would move him backwards along with his skateboard. This motion is due to the reaction force $\mathbf {F}$ exerted on him by the bar. The work done by $\mathbf {n}$ or $\mathbf {w}$ is equal to zero since each force is perpendicular to the displacement. Because the point of application of $\mathbf {F}$ did not move it follows that the work done by that force is zero. Thus, from the work–energy theorem the man should not move. The question is why did he move?

The fact here is that it is incorrect to treat the man as a particle, since different parts of his body move in different ways as he pushes the bar. Therefore, the work–energy theorem does not hold. The man must be treated as a system of particles. In Chap. 6, we will see that the motion of a system of particles can be represented by the motion of its center of mass. The center of mass behaves as if all of the mass of the object (or system) is concentrated there and as if the net external force is applied there. In the case of the skateboarder, the center of mass of the system (man $+$ skateboard) moves and the work–energy theorem can be applied to that point.

The work–energy theorem is an alternative method for describing motion without using Newton’s laws. It is especially useful in problems involving a varying force. Note that the work and the kinetic energy are not invariant quantities; they have different values when measured in different inertial frames of reference. However, from the principle of invariance, the equation $W_{net}=\triangle K$ still holds for any inertial frame.

````{prf:example}
:label: example-4-6
:enumerator: 4.6

A 5 kg block resting on a surface is given an initial velocity of 5 $\mathrm {m}/\mathrm {s}$. If the coefficient of kinetic friction of the surface is $\mu _{k}=0.2$, find the distance the block would move before it stops.

:::{admonition} Solution 4.6
:class: dropdown

As we will see later in Sect. [](#sec-4-3-1), the change in the kinetic energy of the block due to friction is $\triangle K=-f_{k}s$, where *s* is the displacement of the block.

```{math}
W_{f}=\triangle K=-f_{k}d=-\mu _{k}mgd=\frac{1}{2}mv_{f}^{2}-\frac{1}{2}mv_{i}^{2}
```

```{math}
=-(0.2)(5\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})d=0-\frac{1}{2}(5\,\mathrm {k}\mathrm {g})(5\,\mathrm {m}/\mathrm {s})^{2}
```

```{math}
d=6.4\,\mathrm {m}
```

:::
````

````{prf:example}
:label: example-4-7
:enumerator: 4.7

A 10 kg block is pushed on a frictionless horizontal surface by a constant force of magnitude of 100 $\mathrm {N}$ and that is at $30^{\mathrm {o}}$ below the horizontal. If the block starts from rest, find its final speed after it has moved a distance of $3\,\mathrm {m}$ using work–energy theorem.

:::{admonition} Solution 4.7
:class: dropdown

```{math}
W=\mathrm {F}\cdot \mathrm {s}=Fs\cos \theta =(100\,\mathrm {N})(3\,\mathrm {m})\cos (-30^{\mathrm {o}})=259.8\,\mathrm {J}
```

From the work–energy theorem, we have

```{math}
W=\frac{1}{2}mv_{f}^{2}-\frac{1}{2}mv_{i}^{2}
```

since $v_{i}=0$ we get

```{math}
v_{f}^{2}=\frac{2W}{m}=\frac{2(259.8\,\mathrm {J})}{(10\,\mathrm {k}\mathrm {g})}=52\,\mathrm {m}^{2}/\mathrm {s}^{2}
```

```{math}
v_{f}=7.2\,\mathrm {m}/\mathrm {s}
```

:::
````

```{figure} ../images/ch-04/459974_1_En_4_Fig9_HTML.png
:name: fig-4-9

A block attached to a light spring on a frictionless surface
```

(sec-4-3-1)=
### 4.3.1 Work Done by a Spring Force

Consider a block attached to a light spring fixed at the other end on a frictionless horizontal surface as in Fig. [](#fig-4-9). Suppose an external force $\mathbf {F}_{ext}$ is applied to the block by either stretching or compressing it through a small displacement from its equilibrium (relaxed) position taken at $x=0$. The spring will then exert a restoring force $\mathbf {F}_{s}$ on the block that opposes the applied force and restores the block to its equilibrium position. For many kinds of springs and in the case of small displacements, the spring force varies linearly with the displacement *x* of the block (or any other object) from its equilibrium position $(x=0)$. That is

```{math}
F_{s}=-kx
```

where *k* is a constant called the force or spring constant. *k* measures the stiffness of the spring. The stiffer the spring the larger is *k*. This equation is known as Hook’s law. The minus sign indicates that the spring force is always acting in a direction opposing the displacement. The work done by the spring force in moving the block from an initial position $x_{i}$ to a final position $x_{f}$ is:

```{math}
W_{s}=\int _{x_{i}}^{x_{f}}F_{x}dx=\int _{x_{i}}^{x_{f}}(-kx)dx=-k\int _{x_{i}}^{x_{f}}xdx
```

```{math}
W_{s}=\frac{1}{2}kx_{i}^{2}-\frac{1}{2}kx_{f}^{2}
```

The work done on the block by the spring as it moves from an initial position $x_{i}=x$ to a final position $x_{f}=0$ is

```{math}
W_{s}=\frac{1}{2}kx^{2}
```

Figure [](#fig-4-10) shows a plot of $F_{s}$ versus *x* for the mass–spring system.

```{figure} ../images/ch-04/459974_1_En_4_Fig10_HTML.png
:name: fig-4-10

A plot of $F_{s}$ versus *x* for the mass-spring system
```

````{prf:example}
:label: example-4-8
:enumerator: 4.8

A 2 kg block is attached to a light spring of force constant 300 $\mathrm {N}/\mathrm {m}$ on a horizontal smooth surface as shown in Fig. [](#fig-4-11). If the system is initially at rest at the position of equilibrium and is then stretched a distance of 3 cm, find the work done by the spring on the block as it moves from $x_{i}=0$ to $x_{f}=3$ cm.

:::{admonition} Solution 4.8
:class: dropdown

```{math}
W_{s}=\frac{1}{2}kx_{i}^{2}-\frac{1}{2}kx_{f}^{2}=0-\frac{1}{2}(300\,\mathrm {N}/\mathrm {m})(0.03\,\mathrm {m})^{2}=-0.135\,\mathrm {J}
```

:::
````

```{figure} ../images/ch-04/459974_1_En_4_Fig11_HTML.png
:name: fig-4-11

A 2 kg block attached to a light spring of force constant 300 $\mathrm {N}/\mathrm {m}$ on a horizontal smooth surface
```

(sec-4-3-2)=
### 4.3.2 Work Done by the Gravitational Force (Weight)

If a particle-like object of mass *m* is moving vertically upward or downward near the surface of the earth where $\mathrm {g}$ is assumed to be constant (see Fig. [](#fig-4-12)), and if air resistance is neglected, then the only force that does work on the object is the gravitational force *m*g. By taking the $\mathrm {y}$-axis along the line of motion (positive upwards) with $y=0$ at the earth’s surface, the work done by the gravitational force is

```{math}
W_{g}=\int _{y_{\mathrm {i}}}^{y_{f}}F_{y}dy=-mg\int _{y_{i}}^{y_{f}}dy
```

```{math}
W_{g}=mgy_{i}-mgy_{f}
```

Note that unlike the spring force the reference point $y_{i}$ may be chosen anywhere. If the object moved downwards from $y_{i}=y$ to $y_{f}=0$, the work done by the gravitational force is

```{math}
W_{g}=mgy
```

Now suppose the object moves along a curved path from $\mathrm {P}$ to $\mathrm {Q}$ as in Fig. [](#fig-4-13). The work done by the gravitational force is

```{math}
W=\int _{P}^{Q}m \mathbf {g} \cdot d \mathbf {s}=-\int _{P}^{Q}mg \mathbf {i} \cdot d (dx\mathbf {i}+dy\mathbf {j})=-\int _{y_{i}}^{y_{f}} mg dy=mgy_{i}-mgy_{f}
```

This result is the same as if the object has followed a straight vertical path. Therefore, the work done by the gravitational force depends only on the initial and final positions of the object.

```{figure} ../images/ch-04/459974_1_En_4_Fig12_HTML.png
:name: fig-4-12

By taking $y=0$ at the hand level, in the work done by gravity **a** is $-mgy_{f}$ and in **b** is $+mgy_{i}$
```

```{figure} ../images/ch-04/459974_1_En_4_Fig13_HTML.png
:name: fig-4-13

**a** The total work done by the spring force on the block is zero since $x_{i}=x_{f}$. **b** Along any path the work done by the gravitational force is the same since the initial and final positions are the same
```

````{prf:example}
:label: example-4-9
:enumerator: 4.9

A man lifts a 300 kg weight a distance of 2 $\mathrm {m}$ above the ground. Find the work done by the force of gravity on the weight.

:::{admonition} Solution 4.9
:class: dropdown

```{math}
W=mgy_{i}-mgy_{f}=0-(300\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})(2\,\mathrm {m})=-5880\,\mathrm {J}
```

:::
````

(sec-4-3-3)=
### 4.3.3 Power

Power is a quantity that defines how much work is done over a period of time, i.e., power is the time rate of doing work, or more generally, it is the time rate of energy transfer. If an external force $\mathrm {F}$ does work *W* on an object for a time interval $\triangle t$, then the average power during that time is

```{math}
\overline{P}=\frac{W}{\triangle t}
```

The instantaneous power is

```{math}
P=\lim _{\triangle t\rightarrow 0}\frac{W}{\triangle t}=\frac{dW}{dt}
```

Our concern in this book is the mechanical power since it involves mechanical work. If $\mathrm {y}$ is the velocity of the object, we have

```{math}
P=\frac{dW}{dt}=\mathbf {F}\cdot \frac{d\mathbf {s}}{dt}
```

for a constant force, or

```{math}
P=\mathbf {F}\cdot \mathbf {v}
```

The SI unit of power is joules per second $(\mathrm {J}/\mathrm {s})$ and is called the watt (W).

```{math}
1\ \mathrm {W}=1\,\mathrm {J}/\mathrm {s}=1\,\mathrm {k}\mathrm {g}.\mathrm {m}^{2}/\mathrm {s}^{3}
```

Another unit of power that is often used is the horsepower:

```{math}
1\,\text {hp} =746\,\mathrm {W}
```

(sec-4-4)=
## 4.4 Conservative and Nonconservative Forces

In nature, there are two kinds of forces: conservative and nonconservative forces. A conservative force is a force that conserves the energy of a system when acting upon it. The action of this force results in changing the kinetic energy of any object in the system. This change will be stored in the system in the form of potential energy. For every conservative force, there is a certain potential energy that is associated with it. Such potential energy can be retransformed into kinetic energy Thus, the total energy of the system would not be dissipated, instead it would be conserved. A force that does not act in this way is said to be a nonconservative force. Properties of a conservative force are given as follows:

1. The net work done by a conservative force on a particle moving from one point to another is independent of the path taken by the particle;

1. The net work done by a conservative force in moving a particle through any closed path is equal to zero.

A force not meeting these conditions is a nonconservative force. As mentioned in Sect. 1.​10.​2, property 2 of a conservative force can be obtained from property 1 (if $\mathbf {A}$ is a vector field and the line integral of $\mathbf {A}$ between any two points is independent of path, then $\displaystyle \oint _{C}\mathbf {A}\cdot \mathbf {r}=0$). That is, these two properties are equivalent. Examples of conservative forces in mechanics are the gravitational and spring forces. To show this let us go back to Sects. [](#sec-4-3-1) and [](#sec-4-3-2), where the work done by the gravitational force or the spring force was calculated. We have seen that the work done in each case depends only on the initial and final positions of the object. Therefore, the work done by any of these forces is independent of the path joining the initial and final positions. Furthermore, if $(x_{i}=x_{f})$ in the case of the spring or $(y_{i}=y_{f})$ in the case of the gravitational force the net work done is zero. Hence, these forces are conservative.

The force of friction is an example of a nonconservative force. To show that, consider a block sliding on a rough surface. Figure [](#fig-4-14) shows two possible paths connecting two points. The longer the path the more interaction between the block and the surface and the more the force of friction will act and do work on the block. Thus, the work depends on the path taken between the two points and therefore the frictional force is a nonconservative force.

```{figure} ../images/ch-04/459974_1_En_4_Fig14_HTML.png
:name: fig-4-14

The longer the path the more interaction between the block and the surface and the more the force of friction will act and do work on the block
```

(sec-4-4-1)=
### 4.4.1 Potential Energy

For a system consisting of two or more objects, the potential energy *U* of the system is the energy associated with the configuration of the system. That is, the potential energy is the energy associated with the position of objects in the system relative to each other. If the configuration of the system is changed, then the potential energy of the system also changes. Such energy is defined only in terms of a conservative force because if such a force acts on a system then it can transform the kinetic energy of any object in the system into potential energy of the system and vice versa. The potential energy means that the system has potential to do work.

In Sect. 1.​10.​2 it has been proven that the line integral in Eq. (1.​2) is independent of the path joining the points $\mathrm {P}$ and $\mathrm {Q}$ if and only if $\mathbf {A}=\nabla \phi,$ or equivalently $\nabla \times \mathbf {A}=0$. Where $\phi (x,\ y,\ z)$ is some scalar that has continuous partial derivatives. Therefore, for a conservative force field $\mathbf {F}(x,\ y,\ z)$, there always exist a scalar field $U=U(x,\ y,\ z)$ (called the potential energy) such that

```{math}
\mathbf {F}=-\nabla U=-\left( \frac{\partial U}{\partial x}\mathbf {i}+\frac{\partial U}{\partial y}\mathbf {j}+\frac{\partial U}{\partial z}\mathbf {k}\right)
```

Furthermore

```{math}
\nabla \times \mathbf {F}=\mathbf {0}
```

Thus, the total work done by a conservative force in moving a particle from $P_{i}$ to $P_{f}$ (see Fig. [](#fig-4-15)) is

```{math}
W=\int _{P_{i}}^{P_{f}}\mathbf {F}\cdot d\mathbf {s}=\int _{P_{i}}^{P_{f}}-\nabla U\cdot d\mathrm {s}=\int _{\prime P_{\mathrm {i}}}^{P_{f}}-dU=U_{i}-U_{f}=-\triangle U
```

or

```{math}
\triangle U=-\int _{P_{i}}^{P_{f}}\mathrm {F}\cdot d\mathrm {s}
```

where $U=U(x,\ y,\ z)$. Because only the change in the potential energy is significant, it does not matter where the reference point (*U*) is chosen. This is because if $U_{i}$ is changed $U_{f}$ will be also changed but $\triangle U$ will remain constant.

```{figure} ../images/ch-04/459974_1_En_4_Fig15_HTML.png
:name: fig-4-15

The total work done by a conservative force in moving a particle from $P_{i}$ to $P_{f}$
```

````{prf:example}
:label: example-4-10
:enumerator: 4.10

A force acting on a particle is given by $\mathbf {F}=-k\mathbf {r}$. Determine: (a) whether or not the force is conservative; (b) the potential energy associated with the force if it is conservative.

:::{admonition} Solution 4.10
:class: dropdown

(a)

```{math}
\nabla \times \mathbf {F}=\left| \begin{array}{lll} \mathbf {i} &{} \quad \mathbf {j} &{} \quad \mathbf {k}\\ \frac{\partial }{\partial x} &{} \quad \frac{\partial }{\partial y} &{} \quad \frac{\partial }{\partial z}\\ -kx &{} \quad -ky &{} \quad -kz \end{array}\right|
```

```{math}
=\bigg [\displaystyle \frac{\partial }{\partial y}(-kz)-\frac{\partial }{\partial z}(-ky)\bigg ]\mathbf {i}+\bigg [\frac{\partial }{\partial z}(-kx)-\frac{\partial }{\partial x}(-kz)\bigg ]\mathbf {j}+\bigg [\frac{\partial }{\partial x}(-ky)-\frac{\partial }{\partial y}(-kx)\bigg ]\mathbf {k}=\mathbf {0}
```

Therefore, the force is conservative.

(b)

```{math}
U=-\int \mathbf {F}\cdot d\mathbf {r}=-\int -k\mathbf {r}\cdot d\mathbf {r}=\int krdr=\frac{1}{2}kr^{2}=\frac{1}{2}k(x^{2}+y^{2}+z^{2})
```

:::
````

````{prf:example}
:label: example-4-11
:enumerator: 4.11

If a force acting on a particle is given by $\mathbf {F}=ay\mathbf {j}$, where *a* is a positive constant: (a) find the work done in moving the particle along the closed path shown in Fig. [](#fig-4-16); (b) determine if the force is conservative.

:::{admonition} Solution 4.11
:class: dropdown

(a) Along path 1 we have $y=1$ and $dy=0$ and along path 3 we have $y=2$ and $dy=0.$

```{math}
W=\displaystyle \oint _{\mathrm {c}}\mathbf {F}\cdot d\mathbf {r}=\int _{1}\mathbf {F}\cdot d\mathbf {r}+\int _{2}\mathbf {F}\cdot d\mathbf {r}+\int _{3}\mathbf {F}\cdot d\mathbf {r}+\int _{4}\mathbf {F}\cdot d\mathbf {r}=0+\int _{y=1}^{2}aydy+0+\int _{y=2}^{1} aydy=0
```

(b) Since the total work done through the closed path is zero, the force is conservative.

:::
````

```{figure} ../images/ch-04/459974_1_En_4_Fig16_HTML.png
:name: fig-4-16

The work done in moving the particle along a closed path
```

````{prf:example}
:label: example-4-12
:enumerator: 4.12

Find the force acting on a particle if the potential energy associated with it is $U=5y^{2}-3z.$

:::{admonition} Solution 4.12
:class: dropdown

```{math}
F_{y}=-\frac{\partial U}{\partial y}=-10y
```

```{math}
F_{z}=-\frac{\partial U}{\partial z}=3
```

and therefore $\mathbf {F}=-10y\mathbf {j}+3\mathbf {k}.$

:::
````

(sec-4-4-1-1)=
#### 4.4.1.1 The Gravitational Potential Energy

As we have mentioned in Sect. (4.1.7), the work done by the gravitational force in displacing a particle near the earth’s surface from $y_{i}$ to $y_{f}$ is

```{math}
W_{g}=mgy_{i}-mgy_{f}
```

Since $W_{g}=-\triangle U_{g}=U_{gi}-U_{gf}$, we have

```{math}
U_{gi}-U_{gf}=mgy_{i}-mgy_{f}
```

If $y_{f}=0$ and $y_{i}=y$, the gravitational potential energy of the object–earth system may be written as

```{math}
U_{g}=mgy
```

The force of gravity near the surface of the earth can be found from the gravitational potential energy In general we have $\mathbf {F}=-\nabla U$ here, since the motion is in one direction we have

```{math}
\mathbf {F}_{g}=-\frac{dU}{dy}\mathbf {j}=-\frac{d}{dy}(mgy)\mathbf {j}=-mg\mathbf {j}
```

(sec-4-4-1-2)=
#### 4.4.1.2 The Elastic Potential Energy

It was found in Sect. (4.1.6) that the work done by the spring force when moving a block from $x_{i}$ to $x_{f}$ (when it is stretched or compressed) is

```{math}
W_{s}=\frac{1}{2}kx_{i}^{2}-\frac{1}{2}kx_{f}^{2}
```

Since $W_{s}=-\triangle U_{s}=U_{si}-U_{sf}$, we have

```{math}
U_{si}-U_{sf}=\frac{1}{2}kx_{i}^{2}-\frac{1}{2}kx_{f}^{2}
```

If $x_{i}=0$ and $x_{f}=x$, the elastic potential energy of the block-spring system can be written as

```{math}
U_{s}=\frac{1}{2}kx^{2}
```

The spring force can be found from the elastic potential energy

```{math}
\mathbf {F}=-\frac{dU}{dx}\mathbf {i}=-\frac{d}{dx}\left( \frac{1}{2}kx^{2}\right) \mathbf {i}=-kx\mathbf {i}
```

(sec-4-5)=
## 4.5 Conservation of Mechanical Energy

The total mechanical energy of a system is defined as the sum of all of the kinetic energies of the objects within the system plus all of the potential energies of the system.

```{math}
E_{tot}=K_{tot}+U_{tot}
```

Now, consider an isolated system in which there are no external forces acting on it, or the net external force is zero. The only forces acting on the system will be the internal forces within the system. These forces may be conservative or nonconservative. If only internal conservative forces exist, then the work done by any of these forces on an object in the system will transform its kinetic energy into potential energy (associated with that force), or vice versa. The internal conservative force can also transform one form of potential energy into another. The work done by such a force on an object in the system is

```{math}
W=\triangle K
```

The change in potential energy due to this work is

```{math}
W=-\triangle U
```

Thus,

```{math}
\triangle K=-\triangle U
```

or

```{math}
\triangle K+\triangle U=0
```

or

```{math}
K_{i}+U_{i}=K_{f}+U_{f}
```

If more than one conservative force acts, there will be a potential energy associated with each force. That is

```{math}
K_{i}+\sum U_{i}=K_{f}+\sum U_{f}
```

Therefore we have

```{math}
E_{i}=E_{f}
```

or

```{math}
\triangle E=0
```

From the previous discussion, we conclude that for an isolated system in which only conservative forces act, the total mechanical energy of the system remains constant (conserved). Figure [](#fig-4-17) shows the changes of energy of a ball thrown upwards. Now suppose that the system is not isolated and that the external forces acting on the system are conservative. The change in the kinetic energy of the system is then equal to the work done on the system by an internal conservative force plus the amount of kinetic energy changed due to an external conservative force, that is,

```{math}
\triangle K=W_{\mathrm {i}\mathrm {n}\mathrm {t}c}+\triangle K_{ext}
```

or

```{math}
\triangle K=-\triangle U-\triangle U_{ext}
```

Hence

```{math}
\triangle K+\triangle U+\triangle U_{ext}=0
```

Therefore, the total mechanical energy of the system remains constant under both external and internal conservative forces. If external nonconservative forces act on the system, or if there is heat transfer, or if internal nonconservative forces act, then the total mechanical energy may change and is no longer conserved.

```{figure} ../images/ch-04/459974_1_En_4_Fig17_HTML.png
:name: fig-4-17

Changes in the kinetic and potential energies of a ball thrown vertically upwards
```

(sec-4-5-1)=
### 4.5.1 Changes of the Mechanical Energy of a System due to External Nonconservative Forces

External nonconservative forces may act on a system if it is not isolated. Consider a system that is not isolated in which only internal conservative forces act. The change in the kinetic energy of the system is then equal to the work done on the system by an internal conservative force plus the amount of kinetic energy changed due to an external nonconservative force. This can be expressed as

```{math}
\triangle K=W_{\mathrm {i}\mathrm {n}\mathrm {t}c}+\triangle K_{ext}
```

or

```{math}
\triangle K=-\triangle U+\triangle K_{ext}
```

Thus

```{math}
\begin{aligned} \triangle E=\triangle K_{ext} \end{aligned}
```

This implies that the total mechanical energy has changed by an amount of $\triangle K_{ext}$. Not that the work done by a nonconservative force cannot be calculated generally but the change in the kinetic energy can be observed.

(sec-4-5-2)=
### 4.5.2 Friction

Friction is a nonconservative force as seen in Sect. [](#sec-4-2). If this force is applied externally to a system in which only internal conservative forces act, it will decrease (dissipate) the kinetic energy of the system by transforming it into thermal energy The change in the mechanical energy of the system is

```{math}
\triangle E=\triangle K_{ext}
```

The work done by friction or any other nonconservative force cannot be calculated. In other words, the work done by friction is not simply ${-}f_{k}s$, where *s* is the displacement of the object in the system. The reason behind not being able to calculate the work done by friction is that at a microscopic level the frictional force is not a single force that acts at one point. Rather, it is a combination of forces acting at different points in the object. However, the loss in kinetic energy of the object can be calculated as shown below: Consider a block sliding on a rough surface. Let’s choose the block only to be our system. From the equation of motion, we have

```{math}
v_{f}^{2}-v_{i}^{2}=2as
```

Newton’s second law gives

```{math}
-f_{k}=ma
```

Thus

```{math}
- fs=mas
```

or

```{math}
-f_{s}s=\frac{1}{2}mv_{f}^{2}-\frac{1}{2}mv_{i}^{2}
```

Therefore

```{math}
\triangle K_{ext}=-f_{k}s
```

This quantity represents the magnitude of the loss in the kinetic energy of the block due to friction. This loss of energy appears as thermal energy of the block and of the surface on which it slides.

(sec-4-5-3)=
### 4.5.3 Changes in Mechanical Energy due to Internal Nonconservative Forces

In solving problems you are free to choose the system. If we considered the block plus the surface as our system, then friction will be an internal nonconservative force and we may write

```{math}
\triangle E=-\triangle E_{\mathrm {i}\mathrm {n}\mathrm {t}}=\triangle K_{in, nc}=-f_{k}s
```

where $\triangle K_{in, nc}$ is the change in the kinetic energy of the system due to an internal nonconservative force. Another example of a nonconservative force is the force that you exert on your body by your muscles. This force transfers the chemical energy of your body into kinetic energy In Sect. (4.1.5), we have seen that the motion of the skateboarder can be explained using the concept of the center of mass. Another way to explain the motion of the skateboarder is that the internal chemical energy of the man is transformed into kinetic energy, and we may write

```{math}
\triangle E=\triangle K=-\triangle E_{\mathrm {i}\mathrm {n}\mathrm {t}}
```

Since $\triangle U=0$ in his case. An additional example of nonconservative forces is the forces that different parts in an object exert on each other when the object is deformed. These forces transform the kinetic energy of the object into internal energy. In all cases, even though energy can transfer from one object to another or to the environment, the total amount of energy in the universe is constant. That is, energy gained by a system is lost by another system. In other words, *energy cannot be created or destroyed it can only be transformed from one form to another and the total energy of an isolated system is conserved* (*constant*). This statement is known as the law of conservation of energy The law of conservation of energy is also valid in relativity and quantum mechanics.

(sec-4-5-4)=
### 4.5.4 Changes in Mechanical Energy due to All Forces

Consider a system in which there are both internal and external conservative and nonconservative forces acting on it. In this case, the change in the total mechanical energy of the system can be written as

```{math}
\triangle E=\triangle K+\triangle U+\triangle U_{ext}=\triangle K_{ext}-\triangle E_{\mathrm {i}\mathrm {n}\mathrm {t}}
```

````{prf:example}
:label: example-4-13
:enumerator: 4.13

A 0.2 kg apple falls from a tree at a distance of 3 $\mathrm {m}$ above the ground. Find: (a) the velocity of the apple at an altitude of 2 $\mathrm {m}$ and at the instance just before it hits the ground; (b) the altitude of the apple when its velocity is 4 $\mathrm {m}/\mathrm {s}.$

:::{admonition} Solution 4.13
:class: dropdown

(a) Consider the system to be the earth $+$ the apple. By neglecting air resistance (the apple is in free-fall), the only internal force that acts within the earth–apple system is the force of gravity. Because the gravitational force is a conservative force, the total mechanical energy of the system is conserved. Therefore as the apple falls its gravitational potential energy is converted into kinetic energy such that at any instant the total mechanical energy of the system is constant. Applying the law of conservation of energy to the system and by taking $y=0$ at the earth’s surface and the gravitational potential energy to be zero at $y=0$, we have

```{math}
K_{f}+U_{f}=K_{i}+U_{i}
```

```{math}
\frac{1}{2}mv_{f}^{2}+mgy=0+mgh
```

where *h* is its initial altitude. That gives

```{math}
v_{f}=\sqrt{2g(h-y)}
```

At $y=2\,\mathrm {m},$

```{math}
v_{f}=\sqrt{2(9.8\,\mathrm {m}/\mathrm {s}^{2})(1\,\mathrm {m})}=4.43\,\mathrm {m}/\mathrm {s}
```

At $y=0$

```{math}
v_{f}=\sqrt{2(9.8\,\mathrm {m}/\mathrm {s}^{2})(3\,\mathrm {m})}=7.7\,\mathrm {m}/\mathrm {s}
```

(b)

```{math}
y=h-\frac{v_{f}^{2}}{2g}=(3\,\mathrm {m})-\frac{(4\,\mathrm {m}/\mathrm {s})^{2}}{2(9.8\,\mathrm {m}/\mathrm {s}^{2})}=2.2\,\mathrm {m}
```

:::
````

````{prf:example}
:label: example-4-14
:enumerator: 4.14

A roller coaster of mass 500 kg starts from rest at point $\mathrm {A}$, and rolls down the track as shown in Fig. [](#fig-4-18). Ignoring friction, determine: (a) the roller coaster speed at $\mathrm {B}$ and $\mathrm {C}$; (b) the work done by gravity as the rollercoaster moves from A to B.

```{figure} ../images/ch-04/459974_1_En_4_Fig18_HTML.png
:name: fig-4-18

By ignoring friction, the total energy of the roller coaster can be considered to be conserved
```

:::{admonition} Solution 4.14
:class: dropdown

(a) Consider the system to consist of the rollercoaster $+$ the track $+$ the earth. Taking the gravitational potential energy to be zero at the earth’s surface and from the conservation of energy we have

```{math}
K_{f}+U_{f}=K_{i}+U_{i}
```

```{math}
\frac{1}{2}mv_{B}^{2}+mgh_{B}=0+mgh_{A}
```

Therefore,

```{math}
v_{B}=\sqrt{2g(h_{A}-h_{B})}=\sqrt{2(9.8\,\mathrm {m}/\mathrm {s}^{2})(25\,\mathrm {m})}=22.13\,\mathrm {m}/\mathrm {s}
```

Similarly, the velocity at $\mathrm {C}$ is

```{math}
v_{C}=\sqrt{2g(h_{A}-h_{C})}=\sqrt{2(9.8\,\mathrm {m}/\mathrm {s}^{2})(20\,\mathrm {m})}=19.8\,\mathrm {m}/\mathrm {s}
```

You may also calculate the velocity at C by taking B as the initial point.

(b) As the car moves from A to $\mathrm {B}$ the work done by gravity is

```{math}
W_{g}=-\triangle U
```

```{math}
W_{g}=-(mgh_{b}-mgh_{a})=1.22\times 10^{5}\,\mathrm {J}
```

:::
````

````{prf:example}
:label: example-4-15
:enumerator: 4.15

A block of mass 5 kg is released from rest at the top of a $45^{\mathrm {o}}$ incline that is 0.5 $\mathrm {m}$ long as shown in Fig. [](#fig-4-19). It then slides on a horizontal surface that is 0.7 $\mathrm {m}$ long and goes up again on a second ramp that is at $30^{\mathrm {o}}$ to the horizontal. If the coefficient of kinetic friction between the block and all three surfaces is 0.2, find the maximum distance that the block would move up the second ramp?

```{figure} ../images/ch-04/459974_1_En_4_Fig19_HTML.png
:name: fig-4-19

A block released from rest on top of an incline
```

:::{admonition} Solution 4.15
:class: dropdown

First, we divide the path into three parts. Let us consider the system as the block only Along the first part the change in the total mechanical energy of the system is equal to the energy dissipated by friction. Thus,

```{math}
\triangle E=\triangle K_{ext}
```

```{math}
K_{f}+U_{f}=K_{i}+U_{i}+\triangle K_{ext}
```

```{math}
\displaystyle \frac{1}{2}mv_{f1}^{2}+0=0+mgh-f_{k1}s_{1}
```

the force of kinetic friction is

```{math}
f_{k1}=\mu _{k}n=\mu _{k}mg\cos \theta _{1}=(0.2)(5\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2}) \cos 45^{o}=6.93\,\mathrm {N}
```

That gives

```{math}
\begin{aligned} \displaystyle \frac{1}{2}mv_{f1}^{2}&=mgs_{1}\sin \theta _{1}-f_{k1}s_{1}=(5\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.5\,\mathrm {m})\sin 45^{\mathrm {o}} \nonumber \\&-(6.93\,\mathrm {N})(0.5\,\mathrm {m}) =13.9\,\mathrm {J} \end{aligned}
```

$v_{f1}=2.35\,\mathrm {m}/\mathrm {s}$. Along the second path we have again

```{math}
K_{f}+U_{f}=K_{i}+U_{i}+\triangle K_{ext}
```

```{math}
\frac{1}{2}mv_{f2}^{2}+0=\frac{1}{2}mv_{i2}^{2}+0-f_{k2}s_{2}
```

The force of kinetic friction is given by

```{math}
f_{k2}=\mu _{k}mg=(0.2)(5\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})=9.8\,\mathrm {N}
```

and therefore

```{math}
\frac{1}{2}mv_{f2}^{2}=\frac{1}{2}(5\,\mathrm {k}\mathrm {g})(2.35)^{2}-(9.8\,\mathrm {N})(0.7\,\mathrm {m})=6.95\,\mathrm {J}
```

```{math}
v_{f2}=\sqrt{2\frac{(6.94\,\mathrm {J})}{(5\,\mathrm {k}\mathrm {g})}}=1.7\,\mathrm {m}/\mathrm {s}
```

Finally, along the third path, we also have

```{math}
K_{f}+U_{f}=K_{i}+U_{i}+\triangle K_{ext}
```

and

```{math}
0+mgs_{3} \sin 30^{o} =\displaystyle \frac{1}{2}mv_{i3}^{2}+0-f_{k3}s_{3}
```

but we have

```{math}
f_{k3}=\mu _{k}mg \cos 30^{o} =(0.2)(5\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.866)=8.5\,\mathrm {N}
```

and thus

```{math}
(5\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})s_{3}(0.5)=\frac{1}{2}(5\,\mathrm {k}\mathrm {g})(1.7\,\mathrm {m}/\mathrm {s})^{2}-(8.5\,\mathrm {N})s_{3}
```

That gives $s_{3}=0.2\,\mathrm {m}.$

:::
````

````{prf:example}
:label: example-4-16
:enumerator: 4.16

Two masses $m_{1}=5$ kg and $m_{2}=9$ kg are connected by a light rope that passes over a massless frictionless pulley as in Fig. [](#fig-4-20). If the system is released from rest when $m_{2}$ is at 0. $5\,\mathrm {m}$ above the ground, use the principle of conservation of energy to determine the speed with which $m_{2}$ will hit the ground.

```{figure} ../images/ch-04/459974_1_En_4_Fig20_HTML.png
:name: fig-4-20

Two masses connected by a light rope that passes over a massless frictionless pulley
```

:::{admonition} Solution 4.16
:class: dropdown

If air resistance is neglected, the only force acting in the masses-earth system is the gravitational force between them and hence the total mechanical energy of the system is conserved, i.e.,

```{math}
K_{f}+U_{f}=K_{i}+U_{i}
```

Because the two masses are connected by a rope, they have the same speed at any instant. If $m_{2}$ descends a distance $h, m_{1}$ will rise through the same distance and we have

```{math}
\frac{1}{2}m_{1}v^{2}+\frac{1}{2}m_{2}v^{2}+m_{1}gh=m_{2}gh
```

```{math}
\frac{1}{2}(m_{1}+m_{2})v^{2}=g(m_{2}-m_{1})h
```

and therefore

```{math}
v=\sqrt{\frac{2gh(m_{2}-m_{1})}{(m_{1}+m_{2})}}=\sqrt{\frac{2(0.5\,\mathrm {m})(9.8\,\mathrm {m}/\mathrm {s}^{2})(4\,\mathrm {k}\mathrm {g})}{(14\,\mathrm {k}\mathrm {g})}}=1.7\,\mathrm {m}/\mathrm {s}
```

:::
````

````{prf:example}
:label: example-4-17
:enumerator: 4.17

A 0.25 kg ball is attached to alight string of length $L=0.5\,\mathrm {m}$ as in Fig. [](#fig-4-21). Find (a) the tension in the string at $\mathrm {B}(\theta =10^{\circ })$ if the ball is given an initial velocity $v_{a}=0.5\,\mathrm {m}/\mathrm {s}$ at its lowest position; (b) the velocity of the ball at A if the ball is released from rest at B.

```{figure} ../images/ch-04/459974_1_En_4_Fig21_HTML.png
:name: fig-4-21

A ball attached to a light string
```

:::{admonition} Solution 4.17
:class: dropdown

(a) At point $\mathrm {B}$ some of the kinetic energy of the ball is converted into potential energy By taking the origin of the x-y coordinates at the lowest point $\mathrm {A}$, we have

```{math}
K_{f}+U_{f}=K_{i}+U_{i}
```

```{math}
\frac{1}{2}mv_{b}^{2}+mgL(1-\cos \theta )=\frac{1}{2}mv_{a}^{2}+0
```

and therefore we get

```{math}
\begin{aligned} v_{b}^{2}=v_{a}^{2}-2gL(1-\cos \theta ) \end{aligned}
```

Applying Newton’s second law along the radial direction to the ball at $\mathrm {B}$ we have

```{math}
\begin{aligned} T-mg\displaystyle \cos \theta =\frac{mv_{b}^{2}}{L} \end{aligned}
```

Substituting Eq. 4.4 into Eq. 4.5 gives

```{math}
T=mg\cos \theta +\frac{m}{L}(v_{a}^{2}-2gL(1-\cos \theta ))
```

thus

```{math}
T=m\bigg (g\cos \theta +\frac{v_{a}^{2}}{L}-2g+2g\cos \theta \bigg )
```

and hence

```{math}
T=m\bigg (3g\cos \theta -2g+\frac{v_{a}^{2}}{L}\bigg )
```

Substituting the values of $\theta$ and $v_{a}$ gives $T=2.5$ N.

(b) If $v_{b}=0$, we have from $K_{f}+U_{f}=K_{i}+U_{i}$

```{math}
\frac{1}{2}mv_{a}^{2}+0=0+mgL(1-\cos \theta )
```

hence

```{math}
v_{a}=\sqrt{2gL(1-\cos \theta )}=\sqrt{2(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.5\,\mathrm {m})(1-\cos 10^{\mathrm {o}})}=0.4\,\mathrm {m}/\mathrm {s}
```

:::
````

````{prf:example}
:label: example-4-18
:enumerator: 4.18

A 3 kg block compresses a spring of negligible mass a distance of 0.1 $\mathrm {m}$ from its equilibrium position as in Fig. [](#fig-4-22). If the surface is frictionless and the force constant of the spring is 200 $\mathrm {N}/\mathrm {m}$, and the block is free to move, find: (a) the speed of the block just as it leaves the spring; (b) the maximum height that the block will reach; (c) suppose that a part of the horizontal track is rough with a length of 0.05 m, find the coefficient of kinetic friction if the block reaches a maximum height of 0.014 $\mathrm {m}$.

```{figure} ../images/ch-04/459974_1_En_4_Fig22_HTML.png
:name: fig-4-22

A 3 kg block compresses a spring of negligible mass a distance of 0.1 $\mathrm {m}$ from its equilibrium position
```

:::{admonition} Solution 4.18
:class: dropdown

(a) The only force acting inside the spring–mass–earth system is the spring force that acts on the block. This force is conservative and therefore the total mechanical energy of the system is conserved. The potential energy of the spring is transformed into kinetic energy of the block,

```{math}
K_{f}+U_{f}=K_{i}+U_{i}
```

```{math}
\frac{1}{2}mv_{f}^{2}+0=0+\frac{1}{2}kx^{2}
```

and therefore

```{math}
v_{f}^{2}=\frac{k}{m}x^{2}=\frac{(200\,\mathrm {N}/\mathrm {m})}{(3\,\mathrm {k}\mathrm {g})}(-0.1\,\mathrm {m})^{2}
```

this gives $v_{f}=0.82\,\mathrm {m}/\mathrm {s}.$

(b)

```{math}
K_{f}+U_{f}=K_{i}+U_{i}
```

```{math}
0+mgh=\frac{1}{2}mv_{i}^{2}+0
```

and hence

```{math}
h=\frac{v_{i}^{2}}{2g}=\frac{(0.8.2\,\mathrm {m}/\mathrm {s})^{2}}{2(9.8\,\mathrm {m}/\mathrm {s}^{2})}=0.034\,\mathrm {m}
```

We can also take the initial position before the block is released.

(c)

```{math}
K_{f}+U_{f}=K_{i}+U_{i}+\triangle K_{in, nc}
```

```{math}
0+mgh=0+\frac{1}{2}kx^{2}-f_{k}d
```

along the rough surface $f_{k}=\mu _{k}mgd$, and therefore

```{math}
\mu _{k}mgd=\frac{1}{2}kx^{2}-mgh
```

thus

```{math}
\displaystyle \mu _{k}(3\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.05\,\mathrm {m})=\frac{1}{2}(200\,\mathrm {N}/\mathrm {m})(0.1)^{2}-(3\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.014)
```

That gives $\mu _{k}=0.2$

:::
````

````{prf:example}
:label: example-4-19
:enumerator: 4.19

A small stone of mass 0.1 kg is released from rest inside a large hemispherical bowl of radius $R=0.2\,\mathrm {m}$. It then slides along the surface as in Fig. [](#fig-4-23). (a) Find the speed of the stone at point $\mathrm {B}$ and $\mathrm {C}$; (b) If the surface of the bowl is not frictionless, how much energy is dissipated by friction as the stone moves from A to $\mathrm {B}$ if the speed at $\mathrm {B}$ is 1.7 $\mathrm {m}/\mathrm {s}$?

```{figure} ../images/ch-04/459974_1_En_4_Fig23_HTML.png
:name: fig-4-23

A small stone of mass 0.1 kg is released from rest inside a large hemispherical bowl of radius $R=0.2\mathrm {m}$
```

:::{admonition} Solution 4.19
:class: dropdown

(a)

```{math}
K_{f}+U_{f}=K_{i}+U_{i}
```

```{math}
\frac{1}{2}mv_{B}^{2}+0=0+mgR
```

thus

```{math}
v_{B}=\sqrt{2gR}=\sqrt{2(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.2\,\mathrm {m})}=2\,\mathrm {m}/\mathrm {s}
```

At point $\mathrm {C}$ some of the kinetic energy at $\mathrm {B}$ is converted into potential energy and we have

```{math}
\frac{1}{2}mv_{C}^{2}+mg\bigg (R-\frac{R}{4}\bigg )=\frac{1}{2}mv_{B}^{2}+0
```

```{math}
v_{C}^{2}=v_{B}^{2}-\frac{3}{2}gR=(2\,\mathrm {m}/\mathrm {s})^{2}-\frac{3}{2}(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.2\,\mathrm {m})
```

and therefore $v_{C}=1\,\mathrm {m}/\mathrm {s}.$

(b) If a force of kinetic friction exists between the stone and the bowl, the total mechanical energy at point $\mathrm {B}$ is given by

```{math}
E_{f}=E_{i}+\triangle K_{ext}
```

where the stone is considered as the system, therefore

```{math}
K_{f}+U_{f}=K_{i}+U_{i}+\triangle K_{ext}
```

```{math}
\frac{1}{2}mv_{b}^{2}+0=0+mgR+\triangle K_{ext}
```

hence the energy dissipated by friction is

$\displaystyle \triangle K_{ext}=\frac{1}{2}mv_{b}^{2}-mgR=(0.1\,\mathrm {k}\mathrm {g})\left( \frac{1}{2}(1.7\,\mathrm {m}/\mathrm {s})^{2}-(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.2\,\mathrm {m})\right) =-0.05\,\mathrm {J}$

:::
````

````{prf:example}
:label: example-4-20
:enumerator: 4.20

A skier starts at the top of a frictionless incline as in Fig. [](#fig-4-24). Find the velocity with which he will leave the second incline.

:::{admonition} Solution 4.20
:class: dropdown

From the conservation of energy the velocity when he leaves the track is

```{math}
K_{f}+U_{f}=K_{i}+U_{i}
```

```{math}
\frac{1}{2}mv^{2}+mgh_{2}=mgh_{1}
```

```{math}
v=\sqrt{2g(h_{1}-h_{2})}=\sqrt{2(98\,\mathrm {m}/\mathrm {s}^{2})((20\,\mathrm {m})-(10\,\mathrm {m}))}
```

That gives $v=14\,\mathrm {m}/\mathrm {s}.$

:::
````

```{figure} ../images/ch-04/459974_1_En_4_Fig24_HTML.png
:name: fig-4-24

A skier slides from rest on top of an incline
```

````{prf:example}
:label: example-4-21
:enumerator: 4.21

A 0.4 kg stone is released from rest at point A where $h_{A}=2\,\mathrm {m}$ (see Fig. [](#fig-4-25)). It then slides without friction along the track shown where $R=0.5\,\mathrm {m}$. Determine: (a) the speed of the stone at $\mathrm {B}$; (b) the normal force exerted on the stone at $\mathrm {B}$; (c) the magnitude of the total acceleration of the stone at $\mathrm {C}$; (d) the minimum height in which the stone must be released such that it does not fall off the track.

```{figure} ../images/ch-04/459974_1_En_4_Fig25_HTML.png
:name: fig-4-25

A 0.4 kg stone is released from rest at point A where $h_{A}=2\mathrm {m}$
```

:::{admonition} Solution 4.21
:class: dropdown

(a) From the conservation of energy, we have

```{math}
mgh_{A}=\frac{1}{2}mv_{B}^{2}+2mgR
```

```{math}
v_{B}=\sqrt{2g(h_{A}-2R)}=\sqrt{2(9.8\,\mathrm {m}/\mathrm {s}^{2})((2\,\mathrm {m})-2(0.5\,\mathrm {m}))}=4.43\,\mathrm {m}/\mathrm {s}
```

(b) From Newton’s second law, we have

```{math}
n+mg=m\frac{v_{B}^{2}}{R}
```

```{math}
n=m\frac{v_{B}^{2}}{R}-mg=(0.4\,\mathrm {k}\mathrm {g})\bigg [\frac{(4.43\,\mathrm {m}/\mathrm {s})^{2}}{(0.5\,\mathrm {m})}-(9.8\,\mathrm {m}/\mathrm {s}^{2})\bigg ]=11.78\,\mathrm {N}
```

(c) The velocity of the stone at $\mathrm {C}$ is

```{math}
v_{C}=\sqrt{2g(h_{A}-R)}=\sqrt{2(9.8\,\mathrm {m}/\mathrm {s}^{2})((2\,\mathrm {m})-(0.5\,\mathrm {m}))}=5.42\,\mathrm {m}/\mathrm {s}
```

Therefore, the radial acceleration at $\mathrm {C}$ is

```{math}
a_{r}=\frac{v_{C}^{2}}{R}=\frac{(5.42\,\mathrm {m}/\mathrm {s})^{2}}{(0.5\,\mathrm {m})}=58.8\,\mathrm {m}/\mathrm {s}^{2}
```

The tangential force exerted on the stone at $\mathrm {C}$ is its weight $F_{t}=-mg,$ hence the tangential acceleration of the stone at $\mathrm {C}$ is $a_{t}=-g$ and the magnitude of the total acceleration is

```{math}
a=\sqrt{a_{r}^{2}+a_{t}^{2}}=\sqrt{(58.8\,\mathrm {m}/\mathrm {s}^{2})^{2}+(-9.8\,\mathrm {m}/\mathrm {s}^{2})^{2}}=59.6\,\mathrm {m}/\mathrm {s}^{2}
```

(d) When the stone is at the verge of falling at $\mathrm {B}$, then the only force acting on it is the force of gravity and we have $mg=mv_{B}^{2}/R, v_{B}^{2}=gR$. From conservation of energy

```{math}
v_{B}=\sqrt{2g(h_{A\min }-2R)}
```

or

```{math}
2g(h_{A\min }-2R)=gR
```

and

```{math}
h_{A\min }=\frac{R}{2}+2R=(0.25\,\mathrm {m})+(1\,\mathrm {m})=1.25\,\mathrm {m}
```

:::
````

(sec-4-5-5)=
### 4.5.5 Power

Expanding on the definition of power, power is the rate of energy transfer due to a force. If $\triangle E$ is the amount of energy transferred in an amount of time $\triangle t,$ the average power is

```{math}
\overline{P}=\frac{\triangle E}{\triangle t}
```

The instantaneous power is then

```{math}
P=\lim _{\triangle t\rightarrow 0}\frac{\triangle E}{\triangle t}=\frac{dE}{dt}
```

(sec-4-5-6)=
### 4.5.6 Energy Diagrams

Consider a particle that is a part of an isolated system where only internal conservative forces act. Suppose this particle is moving along the $\mathrm {x}$-axis while a conservative force that depends only on the position of the particle acts on it. For simplicity, we will assume that is the only force acting on the system and that it does work only on that particle. The potential energy of the system as a function of the particle’s position (*x*) is shown in Fig. [](#fig-4-26). At any point *F*(*x*) is given by

```{math}
F(x)=-\frac{dU(x)}{dx}
```

That is, it is the negative of the slope of the curve at that point. Because this force is conservative it follows that the total mechanical energy of the system is conserved. Therefore the kinetic energy of the particle as a function of position is given by

```{math}
K(x)=E-U(x)
```

On the *U* versus *x* curve, the kinetic energy at any point can be found by subtracting the value of *U* (at that certain point) from *E*.

```{figure} ../images/ch-04/459974_1_En_4_Fig26_HTML.png
:name: fig-4-26

The potential energy of the system as a function of the particle’s position $({ x})$
```

(sec-4-5-7)=
### 4.5.7 Turning Points

A turning point is a point in which the particle changes its direction of motion. The points $x_{1}$, $x_{3}$, $x_{5}$ and $x_{7}$ are all turning points.

(sec-4-5-8)=
### 4.5.8 Equilibrium Points

Equilibrium points occur in general when $\nabla U=0$. In the case of one dimensional motion it occurs when $dU(x)/dx=0$, i.e. when $F(x)=0.$

(sec-4-5-9)=
### 4.5.9 Positions of Stable Equilibrium

If at an equilibrium point $d^{2}U(x)/dx^{2}>0$, then *U*(*x*) is a minimum at that point. The point is then said to be a position of stable equilibrium, i.e., any minimum on the *U*(*x*) curve is a position of stable equilibrium. Another method to find the position of stable equilibrium is to find the sign of *F*(*x*) at each side of the point. As an example, consider the point $x_{2}$.

This point is a position of stable equilibrium since if the particle is displaced slightly to the right of $x_{2}$ then *dU*(*x*) / *dx* is positive which leads to *F*(*x*) being negative and the particle will accelerate back towards $x_{2}$. On the other hand, if the particle is displaced slightly to the left of $x_{2}$, then *dU*(*x*) / *dx* is negative and thus *F*(*x*) is positive and the particle will also accelerates back to $x_{2}$. Therefore, because *F*(*x*) tends to restore the particle back to that position when the particle is displaced in either direction, it is called a position of stable equilibrium. $x_{6}$ is also a position of stable equilibrium.

(sec-4-5-10)=
### 4.5.10 Positions of Unstable Equilibrium

If at an equilibrium point $d^{2}U(x)/dx^{2}<0$, then *U*(*x*) is maximum at that point, and the point is called a position of unstable equilibrium. In Fig. [](#fig-4-26), $x_{4}$ is a position of unstable equilibrium since if the particle is slightly displaced to the right of $x_{4}, F(x)$ is positive and the particle will accelerate away from $x_{4}$. If the particle is displaced to the left of $x_{4}, F(x)$ is negative and the particle will also accelerate away from that position. Therefore, because *F*(*x*) tends to repel the particle away from that position, it is called a position of unstable equilibrium. In general this force tends to move the particle towards the minimum value of *U*(*x*). Figure [](#fig-4-27) shows the potential energy of a mass–spring system as a function of *x*.

```{figure} ../images/ch-04/459974_1_En_4_Fig27_HTML.png
:name: fig-4-27

The potential energy of a mass-spring system as a function of *x*
```

(sec-4-5-11)=
### 4.5.11 Positions of Neutral Equilibrium

Any point in a region where *U*(*x*) is constant and $F(x)=0$ is called a position of neutral equilibrium. $x_{8}$ is a position of neutral equilibrium. If the particle is slightly displaced to the right or left of $x_{8}$, no restoring or repelling forces will act on the particle and it will remain stationary The position of the particle as a function of time can be obtained from

```{math}
U(x)+K(x)=E
```

```{math}
U(x)+\frac{1}{2}mv^{2}=E
```

```{math}
v=\pm \sqrt{\frac{2}{m}[E-U(x)]}
```

or

```{math}
\frac{dx}{dt}=\pm \sqrt{\frac{2}{m}[E-U(x)]}
```

hence

```{math}
t=\int _{x_{\mathrm {i}}}^{x}\frac{dx}{\pm \sqrt{\frac{2}{m}[E-U(x)]}}
```

By evaluating this integral, we would obtain the time as a function of the position, then by solving for *x* we get the position as a function of time.

````{prf:example}
:label: example-4-22
:enumerator: 4.22

Figure [](#fig-4-28) shows the potential energy of a particle as a function of its displacement. Find: (a) the values of *x* where the particle is in stable or unstable equilibrium; (b) the direction of the force acting on the particle at 0.5 $\mathrm {m}.$

:::{admonition} Solution 4.22
:class: dropdown

(a) We have $x=1\,\mathrm {m}$ and $x=4\,\mathrm {m}$ are positions of stable equilibrium, $x=3\,\mathrm {m}$ is a position of unstable equilibrium.

(b) At 0.5 $\mathrm {m}, dU(x)/dx$ is negative and hence *F*(*x*) is positive which means that the particle will accelerate in the positive $\mathrm {x}$-direction.

:::
````

```{figure} ../images/ch-04/459974_1_En_4_Fig28_HTML.png
:name: fig-4-28

The potential energy of a particle as a function of its displacement
```

````{prf:example}
:label: example-4-23
:enumerator: 4.23

Consider a block attached to a light spring and released from rest at $x=A.$ Find the position of the block as a function of time using energy methods.

:::{admonition} Solution 4.23
:class: dropdown

```{math}
t=\int _{x_{i}=A}^{x_{f}=x}\frac{dx}{\pm \sqrt{\frac{2}{m}[E-U(x)]}}=\int _{x_{i}=A}^{x_{f}=x} \frac{dx}{\pm \sqrt{\frac{2}{m}[{({1/2})kA^{2}}-{({1/2})kx^{2}]}}}
```

```{math}
=\int _{x_{i}=A}^{x_{f}=x}\frac{dx}{\pm \sqrt{\frac{k}{m}[A^{2}-x^{2}]}}=\pm \sqrt{\frac{m}{k}}\int _{x_{i}=A}^{x_{f}=x}\ \frac{dx}{\sqrt{[A^{2}-x^{2}]}}
```

```{math}
=\pm \sqrt{\frac{m}{k}}\left[ -\cos ^{-1}\left( \frac{x}{A}\right) \right] _{x_{i}=A}^{x_{f}=x}=\pm \sqrt{\frac{m}{k}}\left[ -\cos ^{-1}(\frac{x}{A})\right]
```

```{math}
-\cos \bigg (\pm \sqrt{\frac{k}{m}t}\bigg )=\cos \left( \cos ^{-1}\left( \frac{x}{A}\right) \right)
```

or

```{math}
x=A\cos \sqrt{\frac{k}{m}t}
```

Since $\cos (\pm \theta )=\theta$ and $-\cos \theta =\cos \theta$. In Chap. 10, we will see that this equation represents the equation of a simple harmonic motion.

:::
````

```{figure} ../images/ch-04/459974_1_En_4_Fig29_HTML.png
:name: fig-4-29

A force acting on a particle varies with position
```

## Problems

```{exercise}
:label: prob-4-1
:enumerator: 4.1

A force acting on a particle varies with position as in Fig. [](#fig-4-29). Find the work done by the force as the particle moves from $x=0$ to $x=8\,\mathrm {m}.$
```

```{exercise}
:label: prob-4-2
:enumerator: 4.2

A force $\mathbf {F}=(3\mathbf {i}+\mathbf {j}-5\mathbf {k})\,\mathrm {N}$ acts on a particle that undergoes a displacement $\mathbf {r}=(-2\mathbf {i}+3\mathbf {j}-\mathbf {k})\,\mathrm {m}$. Find the work done by the force on the particle.
```

```{exercise}
:label: prob-4-3
:enumerator: 4.3

A 5 $\mathrm {k}\mathrm {g}$ block is pulled from rest on a rough surface by a constant force of 10 $\mathrm {N}$ that is at $30^{\mathrm {o}}$ to the horizontal. If the coefficient of kinetic friction between the block and the surface is 0.15, find the final speed of the block as it moves through a displacement of $2\,\mathrm {m}$ using the work–energy theorem.
```

```{exercise}
:label: prob-4-4
:enumerator: 4.4

Calculate the work done against gravity in moving a 30 kg box through a height of 6 $\mathrm {m}.$
```

```{exercise}
:label: prob-4-5
:enumerator: 4.5

A 1600 kg car accelerates from rest at a rate of 1 $\mathrm {m}/\mathrm {s}^{2}$. Find the average power delivered to the car during the first 5 $\mathrm {s}.$
```

```{exercise}
:label: prob-4-6
:enumerator: 4.6

Determine whether or not the force $\mathbf {F}=-m\omega ^{2}(x\mathbf {i}+y\mathbf {j})$ is conservative, where $\omega$ is constant and *m* is the mass of the particle. If the force is conservative determine the potential energy associated with it.
```

```{exercise}
:label: prob-4-7
:enumerator: 4.7

A 5 $\mathrm {k}\mathrm {g}$ block slides down an inclined plane of angle $50^{\mathrm {o}}$ (see Fig. [](#fig-4-30)). Using energy methods, find the speed of the block just as it reaches the bottom if the coefficient of kinetic friction is $\mu _{k}=0.2.$
```

```{exercise}
:label: prob-4-8
:enumerator: 4.8

A block of mass of 2 kg is pressed against a light spring of force constant 400 $\mathrm {N}/\mathrm {m}$ (see Fig. [](#fig-4-31)). If the compression of the spring is 10 cm, find the maximum height the block will reach when it is released.
```

```{exercise}
:label: prob-4-9
:enumerator: 4.9

A force acting on a particle is given by $\mathbf {F}=-\beta y^{2}\mathbf {j}$. Find the work done in moving the particle along the path shown in Fig. [](#fig-4-32).
```

```{exercise}
:label: prob-4-10
:enumerator: 4.10

Two blocks are connected by a light rope that passes over a massless frictionless pulley (see Fig. [](#fig-4-33)). If the system is released from rest, find the total kinetic energy of the blocks when the 5 kg block descends a distance of 0.5 $\mathrm {m}$ assuming that the surface is frictionless.
```

```{exercise}
:label: prob-4-11
:enumerator: 4.11

A particle of mass 1.5 kg moves along the $\mathrm {x}$-axis where its potential energy varies as in Fig. [](#fig-4-34). Plot the force $F_{x}(x)$ versus *x* from $x=0$ to $x=8\,\mathrm {m}.$
```

```{exercise}
:label: prob-4-12
:enumerator: 4.12

A block of mass *m* rests on a hemispherical mound of ice as shown in Fig. [](#fig-4-35). If it is given a very small push and start sliding, find the height of the point in which the block will lose contact with the mound.
```

```{exercise}
:label: prob-4-13
:enumerator: 4.13

A 3 kg block hangs from a spring as in Fig. [](#fig-4-36). If the spring stretches a distance of 10 cm, find (a) the force constant of the spring (b) the work done in expanding the spring a distance of 5 cm without accelerating it.
```

```{exercise}
:label: prob-4-14
:enumerator: 4.14

In Fig. [](#fig-4-37), determine the Turning points and the positions of stable and unstable equilibrium.
```

```{figure} ../images/ch-04/459974_1_En_4_Fig30_HTML.png
:name: fig-4-30

A block slides down an inclined plane
```

```{figure} ../images/ch-04/459974_1_En_4_Fig31_HTML.png
:name: fig-4-31

A block pressed against a light spring and released
```

```{figure} ../images/ch-04/459974_1_En_4_Fig32_HTML.png
:name: fig-4-32

The work done in moving the particle along a closed path
```

```{figure} ../images/ch-04/459974_1_En_4_Fig33_HTML.png
:name: fig-4-33

Two blocks connected by a light rope that passes over a massless frictionless pulley
```

```{figure} ../images/ch-04/459974_1_En_4_Fig34_HTML.png
:name: fig-4-34

The potential energy versus displacement of a particle
```

```{figure} ../images/ch-04/459974_1_En_4_Fig35_HTML.png
:name: fig-4-35

A block of mass *m* resting on a hemispherical mound of ice
```

```{figure} ../images/ch-04/459974_1_En_4_Fig36_HTML.png
:name: fig-4-36

A block hanging from a spring
```

```{figure} ../images/ch-04/459974_1_En_4_Fig37_HTML.png
:name: fig-4-37

The potential energy versus position of a particle
```
