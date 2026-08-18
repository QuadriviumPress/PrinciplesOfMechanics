---
title: 5. Impulse, Momentum, and Collisions
short_title: "Ch. 5 — Impulse & Momentum"
label: ch-5
doi: 10.1007/978-3-030-15195-9_5
---

(sec-5-1)=
## 5.1 Linear Momentum and Collisions

When two billiard balls collide, in which direction would they travel after the collision? If a meteorite hits the earth, why does the earth remain in its orbit? When two cars collide with each other, why is one of the cars more damaged than the other? We will find that to answer such questions, new concepts must be introduced.

Consider the situation where two bodies collide with each other. During the collision, each body exerts a force on the other. This force is called an impulsive force, because it acts for a short period of time compared to the whole motion of the objects, and its value is usually large. To solve collision problems by using Newton’s second law, it is required to know the exact form of the impulsive forces. Because these forces are complex functions of the collision time, it is difficult to find their exact form and would make it difficult to use Newton’s second law to solve such problems. Thus, new concepts known as momentum and impulse were introduced. These concepts enable us to analyze problems that involve collisions, as well as many other problems.

The law of conservation of momentum is especially used in analyzing collisions and is applied immediately before and immediately after the collision. Therefore, it is not necessary to know the exact form of the impulsive forces, which makes the problem easy to analyze. Next, we will discuss and verify the concepts of momentum and impulse, and the law of conservation of momentum. The linear momentum (or quantity of motion as was called by Newton) of a particle of mass m is a vector quantity defined as

```{math}
\mathbf{p}=m\mathbf{v}
```

where $\mathbf{v}$ is the velocity of the particle. A fast moving car has more momentum than a slow moving car of the same mass. Another example is that a bowling ball has more momentum than a basketball moving at the same speed. The SI unit of linear momentum is $\mathrm{kg}\cdot\mathrm{m}/\mathrm{s}$. In terms of components, we may write $p_{x}=mv_{x}, p_{y}=mv_{y}$, and $p_{z}=mv_{z}$. Newton’s second law can be expressed in terms of momentum for a particle-like object of constant mass as

```{math}
\Sigma \mathbf{F}=m\mathbf{a}=m\frac{d\mathbf{v}}{dt}=\frac{d(m\mathbf{v})}{dt}
```

or

```{math}
\Sigma \mathbf{F}=\frac{d\mathbf{p}}{dt}
```

That is, the rate of change of the linear momentum of an object is equal to the resultant force acting on the object and is in the same direction as that force.

(sec-5-2)=
## 5.2 Conservation of Linear Momentum

The law of conservation of linear momentum states that if the net external force acting on a system equals zero (isolated) and if there is no mass exchange with the surroundings of the system (closed), then the total linear momentum of the system remains constant. To show that, consider an isolated system consisting of two particles where the only forces that act in the system are internal forces (see [](#fig-5-1)). The total linear momentum of the system at any particular time is given by

```{math}
:label: eq-5-1

\mathbf{p}_{tot}=\mathbf{p}_{1}+\mathbf{p}_{2}
```

If the net force exerted on particle 2 by particle 1 is $\mathbf{F}_{21}$, then from Newton’s third law, the net force exerted on particle 1 by particle 2 is $\mathbf{F}_{12}$, That is

```{math}
\mathbf{F}_{12}=-\mathbf{F}_{21}
```

Differentiating Eq. [](#eq-5-1) with respect to time and by using Newton’s second law, we have

```{math}
\frac{d\mathbf{p}_{tot}}{dt}=\frac{d\mathbf{p}_{1}}{dt}+\frac{d\mathbf{p}_{2}}{dt}=\mathbf{F}_{12}+\mathbf{F}_{21}=\mathbf{F}_{12}-\mathbf{F}_{12}=0
```

```{figure} ../images/ch-05/459974_1_En_5_Fig1_HTML.png
:name: fig-5-1

An isolated system consisting of two particles where the only forces that act in the system are internal forces
```

That is,

```{math}
\mathbf{p}_{tot}=\mathrm{constant}
```

or

```{math}
\mathbf{p}_{i}=\mathbf{p}_{f}
```

That is, the linear momentum of each particle may change, but the total linear momentum of the system is the same at all times. This statement is known as the law of conservation of linear momentum: If the net external force on a system is zero, the total linear momentum of the system remains unchanged (constant). In terms of components, we have $p_{ix}=p_{fx}, p_{iy}=p_{fy}$, and $p_{iz}=p_{fz}$. In solving problems involving collisions, $\mathrm{p}_{i}$ and $\mathrm{p}_{f}$ refers to the total momentum of the system immediately before and immediately after the collision, respectively. For a two-particle system, we have

```{math}
\mathbf{p}_{1i}+\mathbf{p}_{2i}=\mathbf{p}_{1f}+\mathbf{p}_{2f}
```

From the principle of invariance, the law of conservation of momentum is valid with respect to any inertial frame of reference. Furthermore, as the law of conservation of energy, the law of conservation of momentum is valid in relativity and quantum mechanics.

(sec-5-3)=
## 5.3 Impulse and Momentum

Impulse is a quantity that defines how a certain force acting on a particle changes the linear momentum of that particle. Now, consider a time-dependent force acting on a particle. From Newton’s second law $(\mathbf{F}=d\mathbf{p}/dt)$, we have

```{math}
d\mathbf{p}=\mathbf{F}dt
```

```{math}
\int_{p_{i}}^{p_{f}}\,d\mathbf{p}=\int_{t_{\mathrm{i}}}\mathbf{F}dt
```

```{math}
\mathbf{p}_{f}-\mathbf{p}_{i}=\triangle \mathbf{p}=\int_{t_{i}}^{t_{f}}\mathbf{F}dt
```

The right side of the equation is a vector quantity known as the impulse I

```{math}
\mathbf{I}=\int_{t_{i}}^{t_{f}}\mathbf{F}dt
```

Hence,

```{math}
\mathbf{I}=\triangle \mathbf{P}
```

Which is known as the impulse–momentum theorem. In component form, we have $I_{x}=\triangle p_{x}, I_{y}=\triangle p_{y}$, and $I_{z}=\triangle p_{z}$. That is, the impulse of a force that acts on a particle during a time interval is equal to the change in the momentum of the particle during that interval. The direction of the impulse is in the same direction as the change of momentum. If $\mathrm{F}$ has a constant direction, the variation of its magnitude with time may be of the form as shown in Fig. 5.2. The average of $\mathrm{F}$ is given by

```{math}
\overline{\mathbf{F}}=\frac{1}{\triangle t}\int_{t_{i}}^{t_{f}}\mathbf{F}dt
```

And thus, I can be written as

```{math}
\mathbf{I}=\triangle \mathbf{p}=\overline{\mathbf{F}}\triangle t
```

That is, $\overline{\mathbf{F}}$ is a constant force that gives the same impulse as F. In the case of a collision between two bodies, the variation of the impulsive force that each body exerts on the other during the collision time takes the form as shown in [](#fig-5-2).

```{figure} ../images/ch-05/459974_1_En_5_Fig2_HTML.png
:name: fig-5-2

One example of the variation of $\mathrm{F}$ over time
```

(sec-5-4)=
## 5.4 Collisions

As discussed previously, when two bodies collide, they exert large forces on one another (during the time of the collision) called impulsive forces. These forces are very large such that any other forces (e.g., friction or gravity) present during the short time of the collision can be neglected. This approximation is known as the impulse approximation. For example, if a golf ball was hit by a golf club, the change in the momentum of the ball can be assumed to be only due to the impulsive force exerted on it by the club. The change in its momentum due to any other force present during the collision can be neglected. That is, the force in the expression I $=\triangle \mathrm{p}=\overline{\mathrm{F}}\triangle t$ can be assumed to be the impulsive force only. The neglected forces present during the collision time are external to the two-body system, whereas the impulsive forces are internal. The two-body system can therefore be considered to be isolated during the short time of the collision (which is in the order of a few milliseconds). Hence, the total linear momentum of the system is conserved during the collision, which enables us to apply the law of conservation of momentum immediately before and immediately after the collision. In general, for any type of collision, the total linear momentum is conserved during the time of the collision. That is, $\mathrm{p}_{i}=\mathrm{p}_{f}$, where $\mathrm{p}_{i}$ and $\mathrm{p}_{f}$ are the momenta immediately before and after the collision. In the next sections, we will define various types of two- body collisions, depending on whether or not the kinetic energy of the system is conserved.

````{prf:example}
:label: example-5-1
:enumerator: 5.1

A 50 $\mathrm{g}$ golf ball initially at rest is struck by a golf club. The golf club exerts a force on the ball that varies during a very short time interval from zero before impact, to a maximum value and back to zero when the ball is no longer in contact with the club. If the ball is given a speed of 25 $\mathrm{m}/\mathrm{s}$, and if the club is in contact with the ball for $7\times 10^{-4}\,\mathrm{s}$, find the average force exerted by the club on the ball.

:::{admonition} Solution 5.1
:class: dropdown

The impulse of the force is

```{math}
I=\triangle p=mv_{f}-0=(0.05\,\mathrm{kg})(25\,\mathrm{m}/\mathrm{s})=1.25\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s}
```

the average force exerted on the ball by the club is then

```{math}
\overline{F}=\frac{I}{\triangle t}=\frac{(1.25\,\mathrm{kg}\mathrm{m}/\mathrm{s})}{(7\times 10^{-4}\,\mathrm{s})}=1785.7\,\mathrm{N}
```

:::
````

````{prf:example}
:label: example-5-2
:enumerator: 5.2

A canon placed on a carriage fires a 250 kg ball to the horizontal with a speed of 50 $\mathrm{m}/\mathrm{s}$. If the mass of the canon and the carriage is 4000 kg, find the recoil speed of the canon.

:::{admonition} Solution 5.2
:class: dropdown

Because there are no external horizontal forces acting on the cannon-carriage-ball system, then the total momentum of the system is constant (conserved) in the $\mathrm{x}$-direction

```{math}
p_{fx}=p_{ix}
```

```{math}
m_{1}v_{1f}+m_{2}v_{2f}=0
```

therefore,

```{math}
v_{2f}=\frac{-m_{1}}{m_{2}}v_{1f}=-\frac{(250\,\mathrm{kg})}{(4000\,\mathrm{kg})}(50\,\mathrm{m}/\mathrm{s})=-3.1\,\mathrm{m}/\mathrm{s}
```

i.e., the cannon recoils in the negative $\mathrm{x}$-direction.

:::
````

````{prf:example}
:label: example-5-3
:enumerator: 5.3

A hockey puck of mass 0.16 kg traveling on a smooth ice surface collides with the court’s edge. If its initial and final velocities are $\mathbf{v}_{i}=-2\,\mathbf{i}\,\mathrm{m}/\mathrm{s}$ and $\mathbf{v}_{f}=1\,\mathbf{i}\,\mathrm{m}/\mathrm{s}$ and if the hockey puck is in contact with the wall for 2 ms, find the impulse delivered to the puck and the average force exerted on it by the wall.

:::{admonition} Solution 5.3
:class: dropdown

```{math}
\mathbf{I}=\triangle \mathbf{p}=\mathbf{p}_{f}-\mathbf{p}_{i}=m\mathbf{v}_{f}-m\mathbf{v}_{i}=(0.16\,\mathrm{kg})((1\,\mathrm{m}/\mathrm{s})-(-2\,\mathrm{m}/\mathrm{s}))\mathbf{i}=0.48\mathbf{i}\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s}
```

```{math}
\overline{\mathbf{F}}=\frac{\mathbf{I}}{\triangle t}=\frac{(0.48\,\mathbf{i}\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s})}{(0.002\,\mathrm{s})}=240\,\mathbf{i}\,\mathrm{N}
```

:::
````

```{figure} ../images/ch-05/459974_1_En_5_Fig3_HTML.png
:name: fig-5-3

A hockey player changing the momentum of the puck
```

````{prf:example}
:label: example-5-4
:enumerator: 5.4

A 0.5 kg hockey puck is initially moving in the negative $\mathrm{y}$-direction as shown in [](#fig-5-3), with a speed of 7 $\mathrm{m}/\mathrm{s}$. If a hockey player hits the puck giving it a velocity of magnitude 12 $\mathrm{m}/\mathrm{s}$ in a direction of $60^{\circ}$ to the vertical, and if the collision lasts for 0.008 $\mathrm{s}$, find the impulse due to the collision and the average force exerted on the puck.

:::{admonition} Solution 5.4
:class: dropdown

Along the $\mathrm{x}$-direction, we have

```{math}
p_{ix}=mv_{ix}=0
```

and

```{math}
p_{fx}=mv_{fx}=(0.5\,\mathrm{kg})(12\,\mathrm{m}/\mathrm{s})\cos 30^{\circ}=5.2\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s}
```

along the $\mathrm{y}$-direction, we have

```{math}
p_{iy}=mv_{iy}=(0.5\,\mathrm{kg})(-7\,\mathrm{m}/\mathrm{s})=-3.5\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s}
```

and

```{math}
p_{fy}=mv_{fy}=(0.5\,\mathrm{kg})(12\,\mathrm{m}/\mathrm{s})\sin 30^{\circ}=3\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s}
```

Therefore, the impulse of the force in each direction is

```{math}
I_{x}=p_{fx}-p_{ix}=(5.2\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s})-0=5.2\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s}
```

and

```{math}
I_{y}=p_{fy}-p_{iy}=(3\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s})-(-3.5\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s})=6.5\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s}
```

```{math}
\mathbf{I}=(5.2\,\mathbf{i}+6.5\,\mathbf{j})\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s}
```

```{math}
I=\sqrt{(5.2\,\mathrm{kg}\mathrm{m}/\mathrm{s})^{2}+(6.5\,\mathrm{kg}\mathrm{m}/\mathrm{s})^{2}}=8.3\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s}
```

The direction of the impulse is

```{math}
\tan \theta=\frac{I_{y}}{I_{x}}=\frac{(6.5\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s})}{(5.2\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s})}=1.25
```

```{math}
\theta=51.3^{\circ}
```

where $\theta$ is measured from the positive $\mathrm{x}$-axis. The average force acting on the puck is

```{math}
\overline{F}=\frac{I}{\triangle t}=\frac{(8.3\,\mathrm{kg}\cdot \mathrm{m}/\mathrm{s})}{(0.008\,\mathrm{s})}=1037.5\,\mathrm{N}
```

:::
````

````{prf:example}
:label: example-5-5
:enumerator: 5.5

Two ice skaters of masses $m_{1}=50$ kg and $m_{1}=62$ kg standing face to face push each other on a frictionless horizontal surface. If skater (1) recoils with a speed of 5 $\mathrm{m}/\mathrm{s}$, find the recoil speed of the other skater.

:::{admonition} Solution 5.5
:class: dropdown

For the two-skater system, the sum of the vertical forces are zero (weight and normal forces) and the forces exerted by one skater on the other is internal to the system. That is, there are no external forces acting on the system and the total momentum is conserved. Because the motion takes place in a straight line, we have

```{math}
p_{1i}+p_{2i}=p_{1f}+p_{2f}
```

```{math}
0=m_{1}v_{1f}+m_{2}v_{2f}
```

and hence,

```{math}
v_{2f}=\frac{-m_{1}}{m_{2}}v_{1f}=\frac{-(50\,\mathrm{kg})}{(62\,\mathrm{kg})}(5\,\mathrm{m}/\mathrm{s})=-4.03\,\mathrm{m}/\mathrm{s}
```

:::
````

````{prf:example}
:label: example-5-6
:enumerator: 5.6

A particle is moving in space under the influence of a force. If its momentum as a function of time is

```{math}
\mathbf{p}=((4t^{2}+t)\mathbf{i}-(3t-1)\mathbf{j}+(5t^{3}+2t)\mathbf{k})\,\mathrm{kg}\cdot\mathrm{m}/\mathrm{s}
```

(a) Find the force acting on the particle at any time; (b) Find the impulse of the force from $t=0$ to $t=1\,\mathrm{s}$.

:::{admonition} Solution 5.6
:class: dropdown

(a)

```{math}
\mathbf{F}=\frac{d\mathbf{p}}{dt}=((8t+1)\mathbf{i}-3\mathbf{j}+(15t^{2}+2)\mathbf{k})\,\mathrm{N}
```

(b)

```{math}
\mathbf{I}=\triangle \mathbf{p}=(5\mathbf{i}-2\mathbf{j}+7\mathbf{k})-\mathbf{j}=(5\mathbf{i}-3\mathbf{j}+7\mathbf{k})\,\mathrm{kg}\cdot\mathrm{m}/\mathrm{s}
```

:::
````

### 5.4.1 Elastic Collisions

An elastic collision is one in which the total kinetic energy, as well as momentum, of the two-colliding-body system is conserved. These collisions exist when the impulsive force exerted by one body on the other is conservative. Such force converts the kinetic energy of the body into elastic potential energy when the two bodies are in contact. It then reconverts the elastic potential energy into kinetic energy when there is no more contact. After collision, each body may have a different velocity and therefore a different kinetic energy. However, the total energy as well as the total momentum of the system is constant during the time of the collision. An example of such collisions is those between billiard balls.

### 5.4.2 Inelastic Collisions

An inelastic collision is one in which the total kinetic energy of the two-colliding-body system is not conserved, although momentum is conserved. In such a collision, some of the kinetic energy of the system is lost due to deformation and appear as internal or thermal energy. In other words, the (internal) impulsive forces are not conservative. Therefore, the kinetic energy of the system before the collision is less than that after the collision. If the two colliding objects stick together, the collision is said to be perfectly inelastic. There are some types of collisions in which the total kinetic energy after the collision occurs is greater than that before it occurs. This type of collision is called an explosive collision.

```{figure} ../images/ch-05/459974_1_En_5_Fig4_HTML.png
:name: fig-5-4

Two particles of masses $m_{1}$ and $m_{2}$ experiencing an elastic head-on collision
```

### 5.4.3 Elastic Collision in One Dimension

When a collision takes place in one dimension, it is referred to as a head-on collision. Consider two particles of masses $m_{1}$ and $m_{2}$ experiencing an elastic head-on collision as in [](#fig-5-4). Applying the law of conservation of energy and the law of conservation of linear momentum gives

```{math}
m_{1}\mathbf{v}_{1i}+m_{2}\mathbf{v}_{2i}=m_{1}\mathbf{v}_{1f}+m_{2}\mathbf{v}_{2f}
```

```{math}
\frac{1}{2}m_{1}v_{1i}^{2}+\frac{1}{2}m_{2}v_{2i}^{2}=\frac{1}{2}m_{1}v_{1f}^{2}+\frac{1}{2}m_{2}v_{2f}^{2}
```

Solving these equations for $v_{1f}$ and $v_{2f}$, we get

```{math}
:label: eq-5-2

v_{1f}=\bigg(\frac{m_{1}-m_{2}}{m_{1}+m_{2}}\bigg)v_{1i}+\bigg(\frac{2m_{2}}{m_{1}+m_{2}}\bigg)v_{2i}
```

```{math}
:label: eq-5-3

v_{2f}=\bigg(\frac{2m_{1}}{m_{1}+m_{2}}\bigg)v_{1i}+\bigg(\frac{m_{2}-m_{1}}{m_{1}+m_{2}}\bigg)v_{2i}
```

#### 5.4.3.1 Special Cases

1. If $m_{1}=m_{2}$, it follows from Eqs. [](#eq-5-2) and [](#eq-5-3) that $v_{1f}=v_{2i}$ and $v_{2f}=v_{1i}$. In other words, if the particles have equal masses they exchange velocities.

2. If $m_{2}$ is stationary $(v_{2i}=0)$, then from Eqs. [](#eq-5-2) and [](#eq-5-3), we have

```{math}
:label: eq-5-4

v_{1f}=\bigg(\frac{m_{1}-m_{2}}{m_{1}+m_{2}}\bigg)v_{1i}
```

```{math}
:label: eq-5-5

v_{2f}=\bigg(\frac{2m_{1}}{m_{1}+m_{2}}\bigg)v_{1i}
```

In that case $m_{2}$ is called the target and $m_{1}$ is called the projectile. Furthermore, if $m_{1}\gg m_{2}$, then from Eqs. [](#eq-5-4) and [](#eq-5-5), we find that $v_{1f}\approx v_{1i}$ and $v_{2f}\approx 2v_{1i}$. While if $m_{2}\gg m_{1}$, then from Eqs. [](#eq-5-4) and [](#eq-5-5), we see that $v_{1f}\approx -v_{1i}$, and $v_{2f}\approx v_{2i}=0$.

```{figure} ../images/ch-05/459974_1_En_5_Fig5_HTML.png
:name: fig-5-5

A one dimensional (head-on) perfectly inelastic collision between two particles of mass $m_{1}$ and $m_{2}$
```

### 5.4.4 Inelastic Collision in One Dimension

[](#fig-5-5) shows a one-dimensional (head-on) perfectly inelastic collision between two particles of mass $m_{1}$ and $m_{2}$. Here, the kinetic energy of the system is not conserved, but the law of conservation of linear momentum still holds

```{math}
m_{1}\mathbf{v}_{1i}+m_{2}\mathbf{v}_{2i}=(m_{1}+m_{2})\mathbf{v}_{f}
```

```{math}
\mathbf{v}_{f}=\frac{m_{1}\mathbf{v}_{1i}+m_{2}\mathbf{v}_{2i}}{m_{1}+m_{2}}
```

### 5.4.5 Coefficient of Restitution

For any collision between two bodies in one dimension, the coefficient of restitution is defined as

```{math}
e=\frac{v_{2f}-v_{1f}}{v_{1i}-v_{2i}}
```

where $v_{1i}$ and $v_{2i}$ are velocities before the collision. $v_{1f}$ and $v_{2f}$ are velocities after the collision. $|v_{1i}-v_{2i}|$ is called the relative speed of approach and $|v_{2f}-v_{1f}|$ is the relative speed of recession.

If $e=1$ the collision is perfectly elastic. If $e<1$ the collision is inelastic. If $e=0$ the collision is perfectly inelastic (the two bodies stick together).

````{prf:example}
:label: example-5-7
:enumerator: 5.7

Two marble balls of masses $m_{1}=7$ kg and $m_{2}=3$ kg are sliding toward each other on a straight frictionless track. If they experience a head-on elastic collision and if the initial velocities of $m_{1}$ and $m_{2}$ are 0.5 $\mathrm{m}/\mathrm{s}$ to the right and 2 $\mathrm{m}/\mathrm{s}$ to the left, respectively, find the final velocities of $m_{1}$ and $m_{2}$.

:::{admonition} Solution 5.7
:class: dropdown

For an elastic head-on collision, we have

```{math}
v_{1f}=\bigg(\frac{m_{1}-m_{2}}{m_{1}+m_{2}}\bigg)v_{1i}+\bigg(\frac{2m_{2}}{m_{1}+m_{2}}\bigg)v_{2i}=(0.4)(0.5\,\mathrm{m}/\mathrm{s})+(0.6)(-2\,\mathrm{m}/\mathrm{s})=-1\,\mathrm{m}/\mathrm{s}
```

```{math}
v_{2f}=\bigg(\frac{2m_{1}}{m_{1}+m_{2}}\bigg)v_{1i}+\bigg(\frac{m_{2}-m_{1}}{m_{1}+m_{2}}\bigg)v_{2i}=(1.4)(0.5\,\mathrm{m}/\mathrm{s})+(-0.4)(-2\,\mathrm{m}/\mathrm{s})=1.5\,\mathrm{m}/\mathrm{s}
```

:::
````

````{prf:example}

:label: example-5-8

:enumerator: 5.8

The ballistic pendulum consists of a large wooden block suspended by a light wire (see [](#fig-5-6)). The system is used to measure the speed of a bullet where the bullet is fired horizontally into the block. The collision is perfectly inelastic and the system (bullet$+$block) swings up a height *h*. If $M=3$ kg, $m=5\,\mathrm {g}$ and $h=5$ cm, find (a) the initial speed of the bullet; (b) the mechanical energy lost due to the collision.

```{figure} ../images/ch-05/459974_1_En_5_Fig6_HTML.png
:name: fig-5-6

The ballistic pendulum consists of a large wooden block suspended by a light wire
```

:::{admonition} Solution 5.8

:class: dropdown

(a) Using the impulse approximation, the law of conservation of momentum gives the velocities just before and after the collision when the string is still nearly vertical. For a perfectly inelastic collision, the total momentum is conserved but the total kinetic energy is not conserved during the collision. Thus, we have

```{math}
mv_{1i}=(m+M)v_{f}
```

```{math}
v_{1i}=\frac{(m+M)}{m}v_{f}
```

After the collision, the energy of the (bullet $+\mathrm {b}\mathrm {l}\mathrm {o}\mathrm {c}\mathrm {k}+$earth) system is conserved since the gravitational force is the only force acting in the system.

```{math}
E_{i}=E_{f}
```

```{math}
\frac{1}{2}(m+M)v_{f}^{2}=(m+M)gh
```

```{math}
v_{f}=\sqrt{2gh}
```

That gives

```{math}
v_{1i}=\frac{(m+M)}{m}\sqrt{2gh}=\frac{(3.005 \; \mathrm {k}\mathrm {g})}{(0.005\,\mathrm {k}\mathrm {g})}\sqrt{2(9.8 \,\mathrm {m}/\mathrm {s}^{2})(0.05\,\mathrm {m})}=595 \; \mathrm {m}/\mathrm {s}
```

(b) The kinetic energy of the bullet before collision is

```{math}
\displaystyle \frac{1}{2}mv_{1i}^{2}=\frac{1}{2}(0.005 \; \mathrm {k}\mathrm {g})(595\,\mathrm {m}/\mathrm {s})^{2}=885 \; \mathrm {J}
```

After collision, the kinetic energy of the (bullet$+$block) is

```{math}
\frac{1}{2}(m+M)v_{f}^{2}=(m+M)\ (gh)=(3.005\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.05\,\mathrm {m})=1.5 \; \mathrm {J}
```

therefore,

```{math}
\triangle E=(885 \; \mathrm {J})-(1.5 \; \mathrm {J})=883.5 \; \mathrm {J}
```

That is, nearly, all the mechanical energy is dissipated and converted into internal (thermal) energy of the (block$+$bullet) system.

:::

````

````{prf:example}

:label: example-5-9

:enumerator: 5.9

Two masses $m_{1}=0.8$ kg and $m_{2}=0.5$ kg are heading toward each other with speeds of 0.25 $\mathrm {m}/\mathrm {s}$ and $-0.5\,\mathrm {m}/\mathrm {s}$, respectively. If they have a perfectly inelastic collision, find the final velocity of the system just after the collision.

:::{admonition} Solution 5.9

:class: dropdown

```{math}
v_{f}=\displaystyle \frac{m_{1}v_{1i}+m_{2}v_{2i}}{(m_{1}+m_{2})}=\frac{(0.8\,\mathrm {k}\mathrm {g})(0.25\,\mathrm {m}/\mathrm {s})-(0.5\,\mathrm {k}\mathrm {g})(0.5\,\mathrm {m}/\mathrm {s})}{(1.3\,\mathrm {k}\mathrm {g})}=-0.04\,\mathrm {m}/\mathrm {s}
```

:::

````

````{prf:example}

:label: example-5-10

:enumerator: 5.10

Two blocks $m_{1}=2$ kg and $m_{2}=1$ kg collide head-on with each other on a frictionless surface (see [](#fig-5-7)). If $v_{1i}=-10\,\mathrm {m}/\mathrm {s}$ and $v_{2i}=15\,\mathrm {m}/\mathrm {s}$ and the coefficient of restitution is $e=1/4$, determine the final velocities of the masses just after the collision.

```{figure} ../images/ch-05/459974_1_En_5_Fig7_HTML.png
:name: fig-5-7

Two blocks colliding head-on on a frictionless surface
```

:::{admonition} Solution 5.10

:class: dropdown

```{math}
e=\frac{v_{2f}-v_{1f}}{v_{1i}-v_{2i}}
```

```{math}
\frac{1}{4}=\frac{v_{2f}-v_{1f}}{(-25\mathrm {m}/\mathrm {s})}
```

```{math}
:label: eq-5-6

\begin{aligned} v_{2f}-v_{1f}=-6.25\,\mathrm {m}/\mathrm {s} \end{aligned}
```

From the conservation of momentum, we have

```{math}
m_{1}v_{1i}+m_{2}v_{2i}=m_{1}v_{1f}+m_{2}v_{2f}
```

```{math}
(2\,\mathrm {k}\mathrm {g})(-10\,\mathrm {m}/\mathrm {s})+(1\,\mathrm {k}\mathrm {g})(15\,\mathrm {m}/\mathrm {s})=(2\,\mathrm {k}\mathrm {g})v_{1f}+(1\,\mathrm {k}\mathrm {g})v_{2f}
```

That gives

```{math}
:label: eq-5-7

\begin{aligned} v_{2f}+(2\,\mathrm {k}\mathrm {g})v_{1f}=-5\,\mathrm {m}/\mathrm {s} \end{aligned}
```

Solving Eqs. [](#eq-5-6) and [](#eq-5-7) gives $v_{1f}=0.42 \,\mathrm {m}/\mathrm {s}$ and $v_{2f}=-5.83 \; \mathrm {m}/\mathrm {s}.$

:::

````

````{prf:example}

:label: example-5-11

:enumerator: 5.11

A $m_{1}=5\,\mathrm {g}$ bullet is fired horizontally at the center of a wooden block with a mass of $m_{2}=2\,\mathrm {k}\mathrm {g}$. The bullet embeds itself in the block and the two slides a distance of 0.$5\,\mathrm {m}$ on a rough surface $(\mu _{k}=0.2)$ before coming to rest. Find the initial speed of the bullet.

:::{admonition} Solution 5.11

:class: dropdown

Applying the law of conservation of momentum immediately before and after the collision gives

```{math}
p_{ix}=p_{fx}
```

```{math}
m_{1}v_{1i}+0=(m_{1}+m_{2})v_{f}
```

```{math}
v_{1i}=\frac{(2.005\,\mathrm {k}\mathrm {g})}{(0.005 \; \mathrm {k}\mathrm {g})}v_{f}=(401)v_{f}
```

by taking the (block$+$bullet) as the system after the collision until it comes to rest, we have

```{math}
K_{f}+U_{f}=K_{i}+U_{i}+\triangle K_{ext}
```

that gives

```{math}
0=\frac{1}{2}(m_{1}+m_{2})v_{f}^{2}-\mu _{k}(m_{1}+m_{2})gd
```

```{math}
v_{f}=\sqrt{2\mu _{k}gd}=\sqrt{2(0.2)(9.8\,\mathrm {m}/\mathrm {s}^{2})(0.5\,\mathrm {m})}=1.4\,\mathrm {m}/\mathrm {s}
```

Hence,

```{math}
v_{1i}=(401)(1.4\,\mathrm {m}/\mathrm {s})=561.4\,\mathrm {m}/\mathrm {s}
```

:::

````

### 5.4.6 Collision in Two Dimension

When a collision takes place in space, the total linear momentum is conserved along each of the $x-, y$-, and *z*-directions. That is, $p_{ix}=p_{fx}, p_{iy}=p_{fy}$, and $p_{iz}=p_{fz}.$ Here, we will analyze a two-dimensional elastic collision between two particles where one particle is moving and the other is at rest as shown in [](#fig-5-8). This type of collision is known as a glancing collision. Since the collision is elastic, it follows that the total linear momentum as well as the kinetic energy of the system are conserved. Applying these laws immediately before and immediately after the collision, we have $p_{ix}=p_{fx}$ and $p_{iy}=p_{fy}$ or

```{math}
m_{1}v_{1ix}+m_{2}v_{2ix}=m_{1}v_{1fx}+m_{2}v_{2fx}
```

and

```{math}
m_{1}v_{1iy}+m_{2}v_{2iy}=m_{1}v_{1fy}+m_{2}v_{2fy}
```

From [](#fig-5-8), we have

```{math}
m_{1}v_{1i}=m_{1}v_{1f}\cos \alpha _{1}+m_{2}v_{2f}\cos \alpha _{2}
```

and

```{math}
0=m_{1}v_{1f}\sin \alpha _{1}+m_{2}v_{2f}\sin \alpha _{2}
```

Furthermore,

```{math}
\frac{1}{2}m_{1}v_{1i}^{2}=\frac{1}{2}m_{1}v_{1f}^{2}+\frac{1}{2}m_{2}v_{2f}^{2}
```

Therefore, we have three equations and seven unknown quantities. By knowing any four of these quantities, the three equations for the three variables can be solved.

```{figure} ../images/ch-05/459974_1_En_5_Fig8_HTML.png
:name: fig-5-8

A two dimensional elastic collision between two particles where one particle is moving and the other is at rest
```

````{prf:example}

:label: example-5-12

:enumerator: 5.12

A ball of mass of 2 kg is sliding along a horizontal frictionless surface at a speed of 3 $\mathrm {m}/\mathrm {s}$. It then collides with a second ball of mass of 5 kg that is initially at rest. After the collision, the second ball is deflected with a speed of 1 $\mathrm {m}/\mathrm {s}$ at an angle of $30^{\mathrm {o}}$ below the horizontal as shown in [](#fig-5-9). (a) Find the final velocity of the first ball; (b) show that the collision is inelastic; (c) suppose that the two balls have equal masses and the collision is perfectly elastic, show that $\theta _{1}+\theta _{2}=90^{\mathrm {o}}.$

```{figure} ../images/ch-05/459974_1_En_5_Fig9_HTML.png
:name: fig-5-9

A ball sliding along a horizontal frictionless surface collides with a second ball that is initially at rest
```

:::{admonition} Solution 5.12

:class: dropdown

Applying the law of conservation of momentum immediately before and after the collision in each direction gives $p_{ix}=p_{fx}$ and $p_{iy}=p_{fy}$. Thus,

```{math}
m_{1}v_{1ix}+m_{2}v_{2ix}=m_{1}v_{1fx}+m_{2}v_{2fx}
```

```{math}
v_{1fx}=\displaystyle \frac{m_{1}v_{1ix}+m_{2}v_{2ix}-m_{2}v_{2fx}}{m_{1}}=\frac{(2\,\mathrm {k}\mathrm {g})(3\,\mathrm {m}/\mathrm {s})+0-((5\,\mathrm {k}\mathrm {g})(1\,\mathrm {m}/\mathrm {s})\cos (-30))}{(2\,\mathrm {k}\mathrm {g})}
```

```{math}
v_{1fx}=0.84\,\mathrm {m}/\mathrm {s}
```

Along the $\mathrm {y}$-direction, we have

```{math}
m_{1}v_{1iy}+m_{2}v_{2iy}=m_{1}v_{1fy}+m_{2}v_{2fy}
```

```{math}
v_{1fy}=\frac{m_{1}v_{1iy}+m_{2}v_{2iy}-m_{2}v_{2fy}}{m_{1}}=\frac{0-((5\,\mathrm {k}\mathrm {g})(1\,\mathrm {m}/\mathrm {s})\sin (-30^{\mathrm {o}}))}{(2\,\mathrm {k}\mathrm {g})}
```

```{math}
v_{1fy}=1.25\,\mathrm {m}/\mathrm {s}
```

Thus, the final velocity of the first ball is

```{math}
v_{1f}=\sqrt{v_{1fx}^{2}+v_{1fy}^{2}}=\sqrt{(0.84\,\mathrm {m}/\mathrm {s})^{2}+(1.25\,\mathrm {m}/\mathrm {s})^{2}}=1.5\,\mathrm {m}/\mathrm {s}
```

The direction of the velocity is

```{math}
\tan \theta _{1}=\frac{v_{1fy}}{v_{1fx}}=\frac{(1.25\,\mathrm {m}/\mathrm {s})}{(0.84\,\mathrm {m}/\mathrm {s})}=1.5
```

```{math}
\theta _{1}=56^{\mathrm {o}}
```

(b) The total kinetic energy before the collision is

```{math}
K_{i}=\frac{1}{2}m_{1}v_{1i}^{2}=\frac{1}{2}(2\,\mathrm {k}\mathrm {g})(3\,\mathrm {m}/\mathrm {s})^{2}=9\,\mathrm {J}
```

The total kinetic energy after the collision is

```{math}
K_{f}=\displaystyle \frac{1}{2}m_{1}v_{1f}^{2}+\frac{1}{2}m_{2}v_{2f}^{2}=\frac{1}{2}(2\,\mathrm {k}\mathrm {g})(1.5\,\mathrm {m}/\mathrm {s})^{2}+\frac{1}{2}(5\,\mathrm {k}\mathrm {g})(1\,\mathrm {m}/\mathrm {s})^{2}=4.75 \; \mathrm {J}
```

That is, some of the energy of the system is lost and thus the collision is inelastic.

(c) In a perfectly elastic collision, both the total momentum and the total mechanical energy of the system are conserved. That is

```{math}
p_{ix}=p_{fx}
```

```{math}
m_{1}v_{1ix}+m_{2}v_{2ix}=m_{1}v_{1fx}+m_{2}v_{2fx}
```

```{math}
:label: eq-5-8

\begin{aligned} v_{1i}=v_{1f}\cos \theta _{1}+v_{2f}\cos \theta _{2} \end{aligned}
```

```{math}
p_{iy}=p_{fy}
```

```{math}
0=v_{1f}\sin \theta _{1}-v_{2f}\sin \theta _{2}
```

```{math}
:label: eq-5-9

\begin{aligned} v_{1f}\sin \theta _{1}=v_{2f}\sin \theta _{2} \end{aligned}
```

From the conservation of kinetic energy, we have

```{math}
\frac{1}{2}m_{1}v_{1i}^{2}=\frac{1}{2}m_{1}v_{1f}^{2}+\frac{1}{2}m_{2}v_{2f}^{2}
```

or

```{math}
:label: eq-5-10

\begin{aligned} v_{1i}^{2}=v_{1f}^{2}+v_{2f}^{2} \end{aligned}
```

Substituting Eq. [](#eq-5-8) into Eq. [](#eq-5-9) gives

```{math}
v_{1i}=v_{2f}\displaystyle \frac{\sin \theta _{2}}{\sin \theta _{1}} \cos \theta _{1}+v_{2f} \cos \theta _{2}
```

or

```{math}
:label: eq-5-11

\begin{aligned} v_{1i}=\displaystyle \frac{v_{2f}\sin (\theta _{1}+\theta _{2})}{\sin \theta _{1}} \end{aligned}
```

Substituting Eq. [](#eq-5-11) into Eq. [](#eq-5-10) gives

```{math}
\frac{v_{2f}^{2}\sin ^{2}(\theta _{1}+\theta _{2})}{\sin ^{2}\theta _{1}}=\frac{v_{2f}^{2}\sin ^{2}\theta _{2}}{\sin ^{2}\theta _{1}}+v_{2f}^{2}
```

Therefore,

```{math}
\sin ^{2}(\theta _{1}+\theta _{2})=\sin ^{2}\theta _{1}+\sin ^{2}\theta _{2}
```

This is satisfied only if $\theta _{1}+\theta _{2}=90^{\mathrm {o}}$.

```{figure} ../images/ch-05/459974_1_En_5_Fig10_HTML.png
:name: fig-5-10

A 1200 kg car traveling east at a speed of 18 collides with another car of mass of 2500 kg that is traveling north at a speed of 23
```

:::

````

````{prf:example}

:label: example-5-13

:enumerator: 5.13

A 1200 kg car traveling east at a speed of 18 $\mathrm {m}/\mathrm {s}$ collides with another car of mass of 2500 kg that is traveling north at a speed of 23 $\mathrm {m}/\mathrm {s}$ as shown in [](#fig-5-10). If the collision is perfectly inelastic, how much mechanical energy is lost due to the collision?

:::{admonition} Solution 5.13

:class: dropdown

```{math}
p_{ix}=p_{fx}
```

```{math}
m_{1}v_{1ix}=(m_{1}+m_{2})v_{fx}
```

```{math}
v_{fx}=\frac{m_{1}v_{1ix}}{(m_{1}+m_{2})}=\frac{(1200\,\mathrm {k}\mathrm {g})(18\,\mathrm {m}/\mathrm {s})}{(3700\,\mathrm {k}\mathrm {g})}=5.8\,\mathrm {m}/\mathrm {s}
```

```{math}
p_{iy}=p_{fy}
```

```{math}
m_{2}v_{2iy}=(m_{1}+m_{2})v_{fy}
```

```{math}
v_{fy}=\frac{m_{2}v_{2iy}}{(m_{1}+m_{2})}=\frac{(2500\,\mathrm {k}\mathrm {g})(23\,\mathrm {m}/\mathrm {s})}{(3700\,\mathrm {k}\mathrm {g})}=15.5\,\mathrm {m}/\mathrm {s}
```

```{math}
v_{f}=\sqrt{v_{fx}^{2}+v_{fy}^{2}}=\sqrt{(5.8\,\mathrm {m}/\mathrm {s})^{2}+(15.5\,\mathrm {m}/\mathrm {s})^{2}}=16.5\,\mathrm {m}/\mathrm {s}
```

The direction of $v_{f}$ is

```{math}
\theta =\tan ^{-1}\frac{v_{fy}}{v_{fx}}=\tan ^{-1}\frac{(15.5\,\mathrm {m}/\mathrm {s})}{(5.8\,\mathrm {m}/\mathrm {s})}=69.5^{\mathrm {o}}
```

from the positive $\mathrm {x}$-axis. The change in the kinetic energy of the system is

```{math}
\triangle K=K_{f}-K_{i}=\frac{1}{2}(m_{1}+m_{2})v_{f}^{2}-\bigg (\frac{1}{2}m_{1}v_{1i}^{2}+\frac{1}{2}m_{2}v_{2i}^{2}\bigg )
```

```{math}
=\displaystyle \frac{1}{2} (3700 \; \displaystyle \mathrm {k}\mathrm {g})(16.5\,\mathrm {m}/\mathrm {s})^{2}-\bigg (\frac{1}{2} (1200 \; \displaystyle \mathrm {k}\mathrm {g})(18\,\mathrm {m}/\mathrm {s})^{2}+\frac{1}{2} (2500\,\mathrm {k}\mathrm {g})(23\,\mathrm {m}/\mathrm {s})^{2}\bigg )
```

```{math}
\triangle K=-3.5\times 10^{5} \; \mathrm {J}
```

:::

````

## 5.5 Torque

Consider a force $\mathrm {F}$ acting on a particle that has a position vector $\mathrm {r}$ with respect to some origin $\mathrm {O}$ that is in an inertial frame. The torque is a vector quantity that measures the tendency of that force to rotate the particle about $\mathrm {O}$ and is defined as

```{math}
\boldsymbol{\tau }=\mathbf {r}\times \mathbf {F}
```

The direction of $\boldsymbol{\tau }$ is perpendicular to the plane formed by $\mathbf {r}$ and $\mathbf {F}$ and its sense is given by the right-hand rule or of advance of a right-handed screw rotating from $\mathbf {r}$ to $\mathbf {F}$. From the vector product definition, this quantity has a magnitude given by

```{math}
\tau =rF\sin \phi
```

where $\phi$ is the smaller angle between $\mathrm {r}$ and $\mathrm {F}, \tau$ is positive if the force tends to rotate the particle counterclockwise and negative if it tends to rotate it clockwise. If $\phi =0$ or $180^{\circ }$, the force is radial and thus it has no rotating tendency. In component form, we may write

```{math}
\boldsymbol{\tau }=\mathbf {r}\times \mathbf {F}=(x\mathbf {i}+y\mathbf {j}+z\mathbf {k})\times (F_{x}\mathbf {i}+F_{y}\mathbf {j}+F_{z}\mathbf {k})
```

```{math}
=(yF_{z}-zF_{y})\mathbf {i}+(zF_{x}-xF_{z})\mathbf {j}+(xF_{y}-yF_{x})\mathbf {k}
```

Let us consider a particle in the x–y plane exposed to a force that lies in that plane (see [](#fig-5-11)). The resulting torque is then perpendicular to the x–y plane parallel to the $\mathrm {z}$-axis. $\tau$ can also be written as

```{math}
\tau =Fd
```

where $d=r\sin \phi$ is called the moment arm of $\mathrm {F}$ where it represents the perpendicular distance from the axis of rotation to the line of action of $\mathrm {F}$ as shown in [](#fig-5-12). Note that because $\tau$ depends on $\mathrm {r}$, it follows that $\tau$ depends on the choice of the origin O. The force $\mathrm {F}$ can be resolved into two components $F_{t}=F\sin \phi$ and $F_{r}=F\cos \phi$. Since the line of action of $F_{r}$ passes through $\mathrm {O},$ it has no rotating effect. Hence, $F_{t}$ is the only component of $\mathrm {F}$ that causes rotation. The SI unit of torque is the Newton-metre (N m). This unit is the same unit of work, but they are different quantities and the torque should never be expressed in joules.

```{figure} ../images/ch-05/459974_1_En_5_Fig11_HTML.png
:name: fig-5-11

A particle in the x-y plane exposed to a force that lies in that plane. The resulting torque is then perpendicular to the x-y plane parallel to the -axis
```

```{figure} ../images/ch-05/459974_1_En_5_Fig12_HTML.png
:name: fig-5-12

is called the moment arm of and it represents the perpendicular distance from the axis of rotation to the line of action of
```

````{prf:example}

:label: example-5-14

:enumerator: 5.14

A force $\mathbf {F}=(-2t\mathbf {i}-(t^{2}-3)\mathbf {j}+4t^{5}\mathbf {k}) \; \mathrm {N}$ acts on a particle that has a position vector $\displaystyle \mathbf {r}=\bigg (-6\mathbf {i}+5t\mathbf {j}+(\frac{t}{2}-1) \; \mathbf {k}\bigg)\,\mathrm {m}$ find the torque of the particle about the origin at $t=1\,\mathrm {s}.$

:::{admonition} Solution 5.14

:class: dropdown

```{math}
\boldsymbol{\tau }=\mathbf {r}\times \mathbf {F}=\left| \begin{array}{lll} \mathbf {i} & \quad \mathbf {j} & \quad \mathbf {k}\\ -6 & \quad 5t & \quad ({\frac{t}{2}-1})\\ -2t & \quad -(t^{2}-3) &\quad 4t^{5} \end{array}\right|
```

Evaluating this at $t=1\,\mathrm {s}$ gives

```{math}
\boldsymbol{\tau }=(2\mathrm {l}\mathbf {i}+25\mathbf {j}-2\mathbf {k})\,\mathrm {N}/\mathrm {m}
```

:::

````

## 5.6 Angular Momentum

The angular momentum $\mathbf {L}$ of a particle of mass *m* and linear momentum $\mathbf {p}$ is a vector quantity defined as

```{math}
\mathbf {L}=\mathbf {r}\times \mathbf {p}
```

where $\mathrm {r}$ is the position vector of the particle relative to an origin $\mathrm {O}$ that is in an inertial frame. Therefore, as $\boldsymbol{\tau }, \mathbf {L}$ also depends on the choice of the origin. Suppose the particle moves in the x–y plane (see [](#fig-5-13)). The direction of $\mathrm {L}$ is then perpendicular to the plane containing $\mathrm {r}$ and $\mathrm {p}$ and its sense is found by the right-hand rule. The magnitude of $\mathbf {L}$ is given by

```{math}
L=mvr\sin \phi
```

where $\phi$ is the smaller angle between $\mathbf {r}$ and $\mathbf {p}$. This quantity is the rotational analog of linear momentum in translational motion. If $\phi =0$ or $180^{\circ }$ the particle will move along a line passing through $\mathrm {O}$ and its angular momentum is zero. The SI unit of angular momentum is $\mathrm {k}\mathrm {g}.\mathrm {m}^{2}/\mathrm {s}$. In terms of rectangular components, we have

```{math}
\mathbf {L}=\mathbf {r}\times \mathbf {p}=(x\mathbf {i}+y\mathbf {j}+z\mathbf {k})\times (p_{x}\mathbf {i}+p_{y}\mathbf {j}+p_{\mathbf {z}}\mathbf {k})
```

```{math}
= (yp_{\mathrm {z}} -\mathrm z \mathrm p_{\mathrm {y}})\mathbf {i}+ (zp_{\mathrm {x}} -\mathrm x \mathrm p_{\mathrm {z}})\mathbf {j}+(xp_{\mathrm {y}} -\mathrm y \mathrm p_{\mathrm {x}})\mathbf {k}
```

```{figure} ../images/ch-05/459974_1_En_5_Fig13_HTML.png
:name: fig-5-13

If the particle is moving in the x-y plane, then the direction of is perpendicular to the plane containing and and is found by the right-hand rule
```

### 5.6.1 Newton’s Second Law in Angular Form

From the definition of torque, we have

```{math}
\boldsymbol{\tau }=\mathbf {r}\times \mathbf {F}=\mathbf {r}\times \frac{d(m\mathbf {v})}{dt}
```

```{math}
\frac{d\mathbf {L}}{dt}=\frac{d(\mathbf {r}\times m\mathbf {v})}{dt}=\frac{d\mathbf {r}}{dt}\times (m\mathbf {v})+\mathbf {r}\times \frac{d(m\mathbf {v})}{dt}
```

```{math}
=\mathbf {v}\times (m\mathbf {v})+\mathbf {r}\times \frac{d(m\mathbf {v})}{dt}=\mathbf {0}+\mathbf {r}\times \mathbf {F}=\boldsymbol{\tau }
```

```{math}
:label: eq-5-12

\begin{aligned} \displaystyle \boldsymbol{\tau }=\frac{d\mathbf {L}}{dt} \end{aligned}
```

This implies that the torque acting on a particle is equal to the time rate of change of the angular momentum for that particle. This equation is valid only if $\boldsymbol{\tau }$ and $\mathbf {L}$ are evaluated with respect to the same origin or any other fixed point in an inertial frame. If several forces act on the particle, Eq. [](#eq-5-12) can be written as

```{math}
\Sigma {\boldsymbol{\tau }}=\frac{d\mathbf {L}}{dt}
```

where $\Sigma \boldsymbol{\tau }$ is the net torque on the particle. This is the rotational analog of Newton’s second law in linear form, which states that the net force acting on a particle is equal to the time rate of change of its linear momentum. In component form, we have $\Sigma {\tau _{x}}=dL_{x}/dt, \Sigma {\tau _{y}}=dL_{y}/dt$ and $\Sigma {\tau _{z}}=dL_{z}/dt.$

### 5.6.2 Conservation of Angular Momentum

The total angular momentum of a particle is constant if the net external torque acting on it is zero:

```{math}
\Sigma {{\boldsymbol{\tau }}_{ext}}=\frac{d\mathbf {L}}{dt}=\mathbf {0}
```

```{math}
\mathbf {L}=\text {constant}
```

```{math}
m(\mathbf {r}\times \mathbf {v})= \text {contant}
```

or

```{math}
\mathbf {L}_{i}=\mathbf {L}_{f}
```

The law of conservation of angular momentum is a fundamental law of physics and it holds in relativity and quantum mechanics. Thus, for an isolated system, the linear momentum and angular momentum are conserved.

````{prf:example}

:label: example-5-15

:enumerator: 5.15

A cat watches a mouse of mass *m* run by, as shown in [](#fig-5-14). Determine the mouse’s angular momentum relative to the cat as a function of time if the mouse has a constant acceleration *a* and if it starts from rest.

:::{admonition} Solution 5.15

:class: dropdown

Suppose the plane is the x–y plane. Since $v=at$, we have

```{math}
\mathbf {L}=m(\mathbf {r}\times \mathbf {v})=mrat\cos \theta \mathbf {k}
```

```{figure} ../images/ch-05/459974_1_En_5_Fig14_HTML.png
:name: fig-5-14

A cat watching a mouse run by
```

:::

````

````{prf:example}

:label: example-5-16

:enumerator: 5.16

A 0.2 kg particle is moving in the x–y plane. If at a certain instant $r=3\,\mathrm {m}$ and $v=10\,\mathrm {m}/\mathrm {s}$ (see [](#fig-5-15)), find the magnitude and direction of the angular momentum of the particle at that instant relative to the origin.

:::{admonition} Solution 5.16

:class: dropdown

```{math}
\mathbf {L}=m(\mathbf {r}\times \mathbf {v})=-(mvr\sin \phi )\mathbf {k}=-(0.2\,\mathrm {k}\mathrm {g})(10\,\mathrm {m}/\mathrm {s})(3\,\mathrm {m}) \sin 60^{\circ } \mathbf {k}=(-5.2\,\mathbf {k})\mathrm {k}\mathrm {g}.\mathrm {m}^{2}/\mathrm {s}
```

```{figure} ../images/ch-05/459974_1_En_5_Fig15_HTML.png
:name: fig-5-15

A particle moving in the x-y plane
```

:::

````

````{prf:example}

:label: example-5-17

:enumerator: 5.17

A particle is moving under the influence of a force given by $\mathbf {F}=-k\mathbf {r}$. Prove that the angular momentum of the particle is conserved.

:::{admonition} Solution 5.17

:class: dropdown

```{math}
\boldsymbol{\tau }=\mathbf {r}\times \mathbf {F}=-k(\mathbf {r}\times \mathbf {r})=\mathbf {0}
```

Since $\boldsymbol{\tau }=d\mathbf {L}/dt$, it follows that the total angular momentum of the particle is conserved. That is,

```{math}
\mathbf {L}=\text {constant}
```

:::

````

````{prf:example}

:label: example-5-18

:enumerator: 5.18

A particle is moving in a circle where its position as a function of time is given by the expression $\mathbf {r}=a(\cos \omega t\mathbf {i}+\sin \omega t\mathbf {j})$, where $\omega$ is a constant. Show that the total angular momentum of the particle is constant.

:::{admonition} Solution 5.18

:class: dropdown

```{math}
\mathbf {v}=\frac{d\mathbf {r}}{dt}=a(-\omega \sin \omega t\mathbf {i}+\omega \cos \omega t\mathbf {j})
```

```{math}
\mathbf {L}=m(\mathbf {r}\times \mathbf {v})=ma^{2}[(\cos \omega t\mathbf {i}+\sin \omega t\mathbf {j})\times (-\omega \sin \omega t\mathbf {i}+\omega \cos \omega t\mathbf {j})]
```

```{math}
=ma^{2}(\omega \cos ^{2}\omega t\mathbf {k}+\omega \sin ^{2}\omega t\mathbf {k})
```

```{math}
=m\omega a^{2}\mathbf {k}= constant
```

:::

````

## Problems

```{exercise}

:label: prob-5-1

:enumerator: 5.1

A tennis ball of mass of 0.06 kg is initially traveling at an angle of $47^{\mathrm {o}}$ to the horizontal at a speed of 45 $\mathrm {m}/\mathrm {s}$. It then was shot by the tennis player and return horizontally at a speed of 35 $\mathrm {m}/\mathrm {s}$. Find the impulse delivered to the ball.

```

```{exercise}

:label: prob-5-2

:enumerator: 5.2

A force on a 0.5 kg particle varies with time according to [](#fig-5-16). Find (a) the impulse delivered to the particle, (b) the average force exerted on the particle from $t=0$ to $t=6\,\mathrm {s}$, and (c) the final velocity of the particle if its initial velocity is $2\,\mathrm {m}/\mathrm {s}$.

```

```{exercise}

:label: prob-5-3

:enumerator: 5.3

A 1 kg particle moves in a force field given by $\mathbf {F}=(2t^{2}\mathbf {i}+(5t-3)\mathbf {j}-6t\mathbf {k})$ N. Find the impulse delivered to the particle during the time interval from $t=1\,\mathrm {s}$ to $t=3\,\mathrm {s}.$

```

```{exercise}

:label: prob-5-4

:enumerator: 5.4

A boy of mass 45 kg runs and jump with a horizontal speed of 4.5 $\mathrm {m}/\mathrm {s}$ into a 70 kg cart that is initially at rest (see [](#fig-5-17)). Find the final velocity of the boy and the cart.

```

```{exercise}

:label: prob-5-5

:enumerator: 5.5

A rubber ball of mass of 0.2 kg is dropped from a height of 2.2 $\mathrm {m}$. It re- bounds to a height of 1.1 $\mathrm {m}$. Find (a) the coefficient of restitution, (b) the energy lost due to impact.

```

```{exercise}

:label: prob-5-6

:enumerator: 5.6

A 1200 kg car initially traveling at 12 $\mathrm {m}/\mathrm {s}$ due east collides with another car of mass of 1600 kg that is initially at rest. If the cars become entangled after the collision, find the common final speed of the cars.

```

```{exercise}

:label: prob-5-7

:enumerator: 5.7

Figure [](#fig-5-18) shows a ball that strikes a smooth surface with a velocity of 20 $\mathrm {m}/\mathrm {s}$ at an angle of $45^{\mathrm {o}}$ with the horizontal. If the coefficient of restitution for the impact between the ball and the surface is $e=0.85$, find the magnitude and direction of the velocity in which the ball rebounds from the surface. (Hint: use the velocity components in the direction perpendicular to the surface for the coefficient of restitution).

```

```{exercise}

:label: prob-5-8

:enumerator: 5.8

Two gliders moving on a frictionless linear air track experience a perfectly elastic collision (see [](#fig-5-19)). Find the velocity of each glider after the collision.

```

```{exercise}

:label: prob-5-9

:enumerator: 5.9

A bullet of mass of *m* is fired with a horizontal velocity *v* into a block of mass *M*. The block is initially at rest on a frictionless surface and is connected to a spring of force constant of *k* (see [](#fig-5-20)). If the bullet embeds itself in the block causing the spring to compress to a maximum distance *d*, find the initial speed of the bullet.

```

```{exercise}

:label: prob-5-10

:enumerator: 5.10

A block moves along the $\mathrm {y}$-axis due to a force given by $\mathbf {F}=a\mathbf {i}$ (see [](#fig-5-21)). Find the torque on the block about (a) the origin (b) point A.

```

```{exercise}

:label: prob-5-11

:enumerator: 5.11

A conical pendulum of mass *m* and length *L* is in uniform circular motion with a velocity *v* (see [](#fig-5-22)). Find the angular momentum and torque on the mass about O.

```

```{figure} ../images/ch-05/459974_1_En_5_Fig16_HTML.png
:name: fig-5-16

A force acting on a particle varies with time
```

```{figure} ../images/ch-05/459974_1_En_5_Fig17_HTML.png
:name: fig-5-17

A boy jumps on a cart that is initially at rest
```

```{figure} ../images/ch-05/459974_1_En_5_Fig18_HTML.png
:name: fig-5-18

A ball bouncing off a smooth surface
```

```{figure} ../images/ch-05/459974_1_En_5_Fig19_HTML.png
:name: fig-5-19

Two gliders moving on a frictionless linear air track experience a perfectly elastic collision
```

```{figure} ../images/ch-05/459974_1_En_5_Fig20_HTML.png
:name: fig-5-20

A bullet of mass of m is fired with a horizontal velocity v into a block of mass M
```

```{figure} ../images/ch-05/459974_1_En_5_Fig21_HTML.png
:name: fig-5-21

A block moving along the y-axis subject to a force
```

```{figure} ../images/ch-05/459974_1_En_5_Fig22_HTML.png
:name: fig-5-22

A conical pendulum of mass m and length L is in uniform circular motion with a velocity v
```
