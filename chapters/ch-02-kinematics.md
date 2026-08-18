---
title: 2. Kinematics
short_title: "Ch. 2 — Kinematics"
label: ch-2
doi: 10.1007/978-3-030-15195-9_2
---

(sec-2-1)=
## 2.1 Introduction

Mechanics is the science that studies the motion of objects and can be divided into the following:

1. Kinematics: Describes how objects move in terms of space and time.
2. Dynamics: Describes the cause of the object’s motion.
3. Statics: Deals with the conditions under which an object subjected to various forces is in equilibrium.

This chapter is considered with kinematics which answers many questions such as: How long it takes for an apple to reach the ground when it falls from a tree? What is the maximum height reached by a baseball when thrown into air? What is the distance it takes an airplane to take off?

In physics, there are three types of motion: translational, rotational, and vibrational. A block sliding on a surface is in translational motion, a (Merry-go-Round) is an example of rotational motion, and a mass–spring system when stretched and released is in vibrational motion. From here until Chap. [](#ch-7), the object studied will be treated as a particle (i.e., a point mass with no size). This assumption is possible only if the object moves in translational motion without rotating and by neglecting any internal motions that might exist in the object.

That is, an object can be treated as a particle only if all of its parts move in exactly the same way.

For example, if a man jumps into a pool without rotating by doing a somersault (freezing his body), he can be treated as a particle since all particles in his body will move in exactly the same way. Another example of an object that can be treated as a particle is the Earth in its motion about the Sun. Since the dimensions of the Earth are small compared to the dimensions of its path, it can be considered as a particle. The motion of an object is described either by equations or by graphs. Both ways provide information about the motion; however, equations provide precise information while graphs give greater insight about the motion.

(sec-2-2)=
## 2.2 Displacement, Velocity, and Acceleration

This section will discuss the concepts of displacement, velocity, and acceleration in one dimension. These concepts are essential in analyzing the motion of an object.

### 2.2.1 Displacement

Consider a car that is treated as a particle moving along the straight-line path shown in [](#fig-2-1). The $\mathrm{x}$-axis of a coordinate system is used to describe the position of the car with respect to the origin $\mathrm{O}$, where the points $\mathrm{P}$ and $\mathrm{Q}$ correspond to the positions $x_{i}$ at $t_{i}$ and $x_{f}$ at $t_{f}$, respectively. The position–time graph of this motion is shown in [](#fig-2-2). The displacement of the truck is a vector quantity defined as the change in its position during the time interval from $t_{i}$ to $t_{f}$ and is given by

```{math}
\triangle x=x_{f}-x_{i}
```

Hence displacement is a quantity that depends only on the initial and final positions of the object. The direction of the displacement in one dimension is specified by a plus or minus sign. It is positive if the particle is moving in the positive $\mathrm{x}$ direction and negative if the particle is moving in the negative $\mathrm{x}$ direction. In two or three dimensions, the displacement is represented by a vector. The SI unit of the displacement is the meter (m).

```{figure} ../images/ch-02/459974_1_En_2_Fig1_HTML.png
:name: fig-2-1

A car that is treated as a particle moving along the straight-line path
```

```{figure} ../images/ch-02/459974_1_En_2_Fig2_HTML.png
:name: fig-2-2

The position time graph of the car's motion
```

### 2.2.2 Average Speed

The average speed of an object is a scalar quantity defined as the total distance traveled divided by the total time:

```{math}
\text{Average speed}=\frac{\text{Total distance traveled}}{\text{Total time}}
```

The SI unit of the average speed is meter per second $(\mathrm{m}/\mathrm{s})$.

### 2.2.3 Velocity

The average velocity $\overline{v}$ of an object is a vector quantity defined in terms of displacement rather than the total distance traveled:

```{math}
\overline{v}=\frac{\triangle x}{\triangle t}
```

$\overline{v}$ is positive if the motion is in the positive $\mathrm{x}$-direction and negative if it is in the negative $\mathrm{x}$-direction. On the position–time graph in [](#fig-2-2), $\overline{v}$ is the slope of the straight line connecting the points $\mathrm{P}$ and Q. The average velocity helps in describing the overall motion of the particle in a certain time interval. To describe the motion in more detail, the instantaneous velocity is defined. This velocity corresponds to the velocity of a particle at a particular time. That involves allowing $\triangle t$ to approach zero:

```{math}
v=\lim _{\triangle t\rightarrow \infty }\frac{\triangle x}{\triangle t}=\frac{dx}{dt}
```

Geometrically, the instantaneous velocity of a particle at a particular time on the position–time curve is the slope (the tangent) to the position–time curve at that point or instance (see [](#fig-2-3)). The SI unit of the velocity is $\mathrm{m}/\mathrm{s}$.

```{figure} ../images/ch-02/459974_1_En_2_Fig3_HTML.png
:name: fig-2-3

Geometrically, the instantaneous velocity of a particle at a particular time on the position-time curve is the slope (the tangent) to the position-time curve at that point or instance
```

### 2.2.4 Speed

The speed of the particle is defined as the magnitude of its velocity. Note that speed and average speed are different since speed is defined in terms of displacement, whereas average speed is defined in terms of the total distance traveled.

### 2.2.5 Acceleration

If the particle’s velocity changes with time, it is said to be accelerating. The average acceleration $\overline{a}$ of the particle is defined as the ratio of the change of its velocity $\triangle v$ to the time interval $\triangle t$:

```{math}
\overline{a}=\frac{\triangle v}{\triangle t}
```

The SI unit of acceleration is $\mathrm{m}/\mathrm{s}^{2}$. The instantaneous acceleration is defined as

```{math}
a=\lim _{\triangle t\rightarrow 0}\frac{\triangle v}{\triangle t}=\frac{dv}{dt}
```

The average acceleration is the slope of the line joining the points $\mathrm{P}$ and $\mathrm{Q}$ on the velocity–time graph, whereas the instantaneous acceleration is the slope of the curve at a particular point (see [](#fig-2-4)). [](#fig-2-5) shows the position, velocity, and acceleration for a particle simultaneously.

```{figure} ../images/ch-02/459974_1_En_2_Fig4_HTML.png
:name: fig-2-4

The average acceleration is the slope of the line joining the points $\mathrm{P}$ and $\mathrm{Q}$ on the velocity-time graph, whereas the instantaneous acceleration is the slope of the curve at a particular point
```

```{figure} ../images/ch-02/459974_1_En_2_Fig5_HTML.png
:name: fig-2-5

This figure shows the position, velocity and acceleration as a function of time of a particle moving in one direction. The particle starts from rest, accelerates to a certain speed, is maintained at that speed for some time, then it decelerates back to rest
```

```{figure} ../images/ch-02/459974_1_En_2_Fig6_HTML.png
:name: fig-2-6

A car moving along the curved path where it is located at $x_{i}=3$ km at $t_{i}=0$, and at $x_{f}=19$ km at $t_{f}=0.25$ hr
```

````{prf:example}
:label: example-2-1
:enumerator: 2.1

A car travels along the path shown in [](#fig-2-6), where it is located at $x_{i}=3$ km at $t_{i}=0$, and at $x_{f}=19$ km at $t_{f}=0.25$ h. Find the displacement, average velocity, and average speed of the car during this time interval if the total distance traveled is 20 km.

:::{admonition} Solution 2.1
:class: dropdown

The displacement of the car is

```{math}
\triangle x=x_{f}-x_{i}=(19\,\mathrm{km})-(3\,\mathrm{km})=16\,\mathrm{km}
```

Its average velocity is

```{math}
\overline{v}=\frac{\triangle x}{\triangle t}=\frac{x_{f}-x_{i}}{t_{f}-t_{i}}=\frac{(16\,\mathrm{km})}{(0.25\,\mathrm{h})}=64\,\mathrm{m}/\mathrm{s}
```

```{math}
\text{Average speed}=\frac{\text{Total distance traveled}}{\text{Total time}}=\frac{(2.0\,\mathrm{km})}{(0.25\,\mathrm{h})}=80\,\mathrm{km}/\mathrm{h}
```

:::
````

```{figure} ../images/ch-02/459974_1_En_2_Fig7_HTML.png
:name: fig-2-7

A particle moves along the $\mathrm{x}$-axis according to the expression $x=2t^{2}$
```

````{prf:example}
:label: example-2-2
:enumerator: 2.2

A particle moves along the $\mathrm{x}$-axis according to the expression $x=2t^{2}$. The plot of this equation is shown in [](#fig-2-7). Find: (a) the displacement and average velocity of the particle during the time interval between $t=1\,\mathrm{s}$ and $t=3\,\mathrm{s}$; (b) the instantaneous velocity of the particle as a function of time and at $t=1\,\mathrm{s}$ and $t=3\,\mathrm{s}$.

:::{admonition} Solution 2.2
:class: dropdown

(a)

```{math}
x_{i}=2t_{i}^{2}=2(1)^{2}=2\,\mathrm{m}
```

```{math}
x_{f}=2t_{f}^{2}=2(3)^{2}=18\,\mathrm{m}
```

The displacement of the particle is

```{math}
\triangle x=x_{f}-x_{i}=(18\,\mathrm{m})-(2\,\mathrm{m})=16\,\mathrm{m}
```

The average velocity is

```{math}
\overline{v}=\frac{\triangle x}{\triangle t}=\frac{(16\,\mathrm{m})}{(2\,\mathrm{s})}=8\,\mathrm{m}/\mathrm{s}
```

(b) The instantaneous velocity is given by

```{math}
v=\frac{dx}{dt}=(4t)\,\mathrm{m}/\mathrm{s}
```

at $t=1\,\mathrm{s}$, $v=2\,\mathrm{m}/\mathrm{s}$, and at $t=3\,\mathrm{s}$, $v=12\,\mathrm{m}/\mathrm{s}$.

:::
````

````{prf:example}
:label: example-2-3
:enumerator: 2.3

A particle is moving along the $\mathrm{x}$-axis. The position–time graph of its motion is shown in [](#fig-2-8). Find: (a) the average velocity between $\mathrm{a}$ and $\mathrm{b}$; (b) the instantaneous velocity at the points $\mathrm{a}$, $\mathrm{c}$ and $\mathrm{d}$.

:::{admonition} Solution 2.3
:class: dropdown

(a)

```{math}
\overline{v}_{ab}=\frac{\triangle x}{\triangle t}=\frac{(2\,\mathrm{m})-(-1.8\,\mathrm{m})}{(3\,\mathrm{s})-(1\,\mathrm{s})}=1.9\,\mathrm{m}/\mathrm{s}
```

(b)

```{math}
v_{a}=\frac{\triangle x}{\triangle t}=\frac{0-(-2.5\,\mathrm{m})}{(3\,\mathrm{s})-0}=0.83\,\mathrm{m}/\mathrm{s}
```

```{math}
v_{c}=0
```

```{math}
v_{d}=\frac{\triangle x}{\triangle t}=\frac{0-(3\,\mathrm{m})}{(8.5\,\mathrm{s})-(4\,\mathrm{s})}=-0.67\,\mathrm{m}/\mathrm{s}
```

:::
````

```{figure} ../images/ch-02/459974_1_En_2_Fig8_HTML.png
:name: fig-2-8

The position-time graph of a particle moving along the x-axis
```

````{prf:example}
:label: example-2-4
:enumerator: 2.4

The acceleration of an object is given by $a=(1-4t)\,\mathrm{m}/\mathrm{s}^{2}$. If the object has an initial velocity of $3\,\mathrm{m}/\mathrm{s}$ and an initial displacement of $2\,\mathrm{m}$, determine (a) its velocity and displacement at any time; (b) the displacement of the object when it reaches its maximum speed.

:::{admonition} Solution 2.4
:class: dropdown

(a)

```{math}
v=\int adt=\int (1-4t)dt=t-2t^{2}+c_{1}
```

At $t=0$, $v=3\,\mathrm{m}/\mathrm{s}$ and therefore $c_{1}=3\,\mathrm{m}/\mathrm{s}$. Thus

```{math}
v=(t-2t^{2}+3)\,\mathrm{m}/\mathrm{s}
```

```{math}
x=\int vdt=\int (t-2t^{2}+3)dt=0.5t^{2}-0.66t^{3}+3t+c_{2}
```

At $t=0$, $x=2\,\mathrm{m}$ and $c_{2}=2\,\mathrm{m}$. Therefore

```{math}
:label: eq-2-1

x=(0.5t^{2}-0.66t^{3}+3t+2)\,\mathrm{m}
```

(b) When the object reaches its maximum speed $\frac{dv}{dt}=0$ and hence $1-4t=0$, that gives $t=0.25\,\mathrm{s}$. Substituting into Eq. [](#eq-2-1) gives

```{math}
x=1/2(0.25\,\mathrm{s})^{2}-2/3(0.25\,\mathrm{s})^{3}+3(0.25\,\mathrm{s})+2=2.8\,\mathrm{m}
```

:::
````

(sec-2-3)=
## 2.3 Motion in Three Dimensions

Consider the particle moving from point $\mathrm{P}$ to point $\mathrm{Q}$ along a path or curve $\mathrm{C}$ during a time interval $\triangle t=t_{f}-t_{i}$ as shown in [](#fig-2-9). To locate the particle at any point the position vector $\mathbf{r}=x\mathbf{i}+y\mathbf{j}+z\mathbf{k}$ is used. $\mathbf{r}_{\mathrm{i}}$ and $\mathbf{r}_{\mathrm{f}}$ corresponds to the position vectors of the particle at $t_{i}$ and $t_{f}$ respectively. A position vector should be drawn from a reference point (usually the origin of the coordinate system).

```{figure} ../images/ch-02/459974_1_En_2_Fig9_HTML.png
:name: fig-2-9

A particle moving from point $\mathrm{P}$ to point $\mathrm{Q}$ along a path or curve $\mathrm{C}$ during a time interval $\triangle t=t_{f}-t_{i}$
```

The displacement vector is then given by

```{math}
\triangle \mathbf{r}=\mathbf{r}_{f}-\mathbf{r}_{i}
```

The average velocity is

```{math}
\overline{\mathbf{v}}=\frac{\triangle \mathbf{r}}{\triangle t}=\frac{\mathbf{r}_{f}-\mathbf{r}_{i}}{t_{f}-t_{i}}
```

The instantaneous velocity at a particular time is defined as

```{math}
\mathbf{v}=\lim _{\triangle t\rightarrow 0}\frac{\triangle \mathbf{r}}{\triangle t}=\frac{d\mathbf{r}}{dt}
```

As $\triangle t$ approaches zero, $\triangle \mathbf{r}$ becomes tangent to the path and it is replaced by $d\mathbf{r}$. The direction of $\mathrm{y}$ is in the direction of $dr$, hence, $\mathrm{y}$ is always tangent to the path at any point. In terms of components $\mathrm{y}$ is given by

```{math}
\mathbf{v}=\frac{dx}{dt}\mathbf{i}+\frac{dy}{dt}\mathbf{j}+\frac{dz}{dt}\mathbf{k}=v_{x}\mathbf{i}+v_{y}\mathbf{j}+v_{z}\mathbf{k}
```

The magnitude of the instantaneous velocity is

```{math}
|\mathbf{v}|=|\frac{d\mathbf{r}}{dt}|=v=\sqrt{\left( \frac{dx}{dt}\right) ^{2}+\left( \frac{dy}{dt}\right) ^{2}+\left( \frac{dz}{dt}\right) ^{2}}=\frac{ds}{dt}
```

```{figure} ../images/ch-02/459974_1_En_2_Fig10_HTML.png
:name: fig-2-10

The instantaneous velocity vectors along the path
```

where $ds$ is the infinitesimal arc length along the path and comes from the fact that as $\triangle t$ approaches zero, the distance traveled by the particle along the path becomes equal to the vector displacement $|\triangle \mathbf{r}|$. [](#fig-2-10) shows the instantaneous velocities along the path. The average acceleration is

```{math}
\overline{\mathbf{a}}=\frac{\triangle \mathbf{v}}{\triangle t}=\frac{\mathbf{v}_{f}-\mathbf{v}_{i}}{t_{f}-t_{i}}
```

The direction of $\overline{\mathbf{a}}$ is of the same direction as $\triangle \mathbf{v}$. The instantaneous acceleration is then

```{math}
\mathbf{a}=\lim _{\triangle t\rightarrow 0}\frac{\triangle \mathbf{v}}{\triangle t}=\frac{d\mathbf{v}}{dt}
```

In terms of components

```{math}
\mathbf{a}=\frac{dv_{x}}{dt}\mathbf{i}+\frac{dv_{y}}{dt}\mathbf{j}+\frac{dv_{z}}{dt}\mathbf{k}=a_{x}\mathbf{i}+a_{y}\mathbf{j}+a_{z}\mathbf{k}
```

Another way to describe motion in three dimensions is by using spherical or cylindrical coordinates. In this book, we will only use rectangular coordinates for three-dimensional motion.

(sec-2-3-1)=
### 2.3.1 Normal and Tangential Components of Acceleration

The acceleration describes the change in both the magnitude and direction of the velocity. That is, the acceleration is not necessarily produced due to the change in the magnitude of the velocity only. Sometimes, it is produced due to the change in the direction of the velocity even if its magnitude is unchanged, and sometimes due to the change in both the magnitude and direction. Furthermore, the direction of $\mathbf{a}$ is not necessarily in the direction of $\mathbf{v}$. If $\mathbf{v}$ is changed in magnitude only (motion along a straight line) then $\mathbf{a}$ is parallel to $\mathbf{v}$ if $\mathbf{v}$ is increasing, and antiparallel if $\mathbf{v}$ is decreasing. If $\mathbf{v}$ is changed in direction only (motion along a curved path with constant speed), then $\mathbf{a}$ is always perpendicular to $\mathbf{v}$ at any point (see [](#fig-2-11)). Finally, if $\mathbf{v}$ is changed in both magnitude and direction then $\mathbf{a}$ will be directed at some angle to $\mathbf{v}$ as in [](#fig-2-12).

```{figure} ../images/ch-02/459974_1_En_2_Fig11_HTML.png
:name: fig-2-11

If $\mathbf{v}$ is changed in magnitude only (motion along a straight line) then $\mathbf{a}$ is parallel to $\mathbf{v}$ if $\mathbf{v}$ is increasing, and antiparallel if $\mathbf{v}$ is decreasing. If $\mathbf{v}$ is changed in direction only (motion along a curved path with constant speed) then $\mathbf{a}$ is always perpendicular to $\mathbf{v}$ at any point
```

In this case, the acceleration can be resolved into parallel and perpendicular components. The parallel component corresponds to the change in the magnitude of $\mathbf{v}$, while the perpendicular component corresponds to the change in the direction of $\mathbf{v}$. These components can be viewed to be directed along a rectangular coordinate system that moves with the particle (as it moves in space), where the particle is located at the origin of this coordinate system. The parallel (or tangential) component of the acceleration is always tangent to the path while the perpendicular (or normal) component is normal to the path at each point as shown in [](#fig-2-13).

[](#fig-2-14) shows the direction of the acceleration of a car moving down a ramp under the influence of gravity.

In terms of unit vectors, let $\mathbf{T}$ be the unit vector along the tangent axis, $\mathbf{N}$ is the unit vector along the normal axis (also called the principal unit normal vector) and $\mathbf{B}$ a third unit vector called the binormal vector defined by $\mathbf{B}= \mathbf{T}\times \mathbf{N}$. These unit vectors form a frame called the TNB frame, where it moves with the particle (see [](#fig-2-15)). Since $\mathbf{v}$ is always tangent to the path we may write

```{math}
\mathbf{T}=\frac{\mathbf{v}}{|\mathbf{v}|}=\frac{d\mathbf{r}/dt}{|d\mathbf{r}/dt|}=\frac{d\mathbf{r}/dt}{ds/dt}
```

```{figure} ../images/ch-02/459974_1_En_2_Fig12_HTML.png
:name: fig-2-12

If $\mathbf{v}$ is changed in both magnitude and direction then $\mathbf{a}$ will be directed at some angle to $\mathbf{v}$
```

```{figure} ../images/ch-02/459974_1_En_2_Fig13_HTML.png
:name: fig-2-13

The parallel (or tangential) component of the acceleration is always tangent to the path while the perpendicular (or normal) component is normal to the path at each point
```

```{figure} ../images/ch-02/459974_1_En_2_Fig14_HTML.png
:name: fig-2-14

At $\mathrm{A}$ the acceleration of a car is in the same direction of the velocity since the latter changes only in magnitude. As it moves its velocity is changed in both magnitude and direction. Therefore at $\mathrm{B}$ the direction of the acceleration is at some angle to the velocity. At $\mathrm{C}$ the speed reaches a maximum and therefore the instantaneous change of speed is zero at this point and the acceleration has only a perpendicular component. As the car moves up its velocity decreases and changes in direction also, thus the acceleration has both parallel and perpendicular components. Finally at $\mathrm{E}$, the acceleration is in the opposite direction of the velocity since the velocity is decreasing but its direction is the same
```

```{figure} ../images/ch-02/459974_1_En_2_Fig15_HTML.png
:name: fig-2-15

The TNB frame moves with the particle
```

Because $\mathbf{T}$ is a unit vector we have $\mathbf{T}\cdot \mathbf{T}=1$, differentiating this with respect to $s$ gives

```{math}
\mathbf{T}\cdot \frac{d\mathbf{T}}{ds}+\frac{d\mathbf{T}}{ds}\cdot \mathbf{T}=2\mathbf{T}\cdot \frac{d\mathbf{T}}{ds}=0
```

or

```{math}
\mathbf{T}\cdot \frac{d\mathbf{T}}{ds}=0
```

Hence, $\mathbf{T}$ is perpendicular to $d\mathbf{T}/ds$. Since $\mathbf{N}$ is also perpendicular to $\mathbf{T}$, then we have

```{math}
\mathbf{N}=\frac{d\mathbf{T}/ds}{|d\mathbf{T}/ds|}=\frac{1}{k}\frac{d\mathbf{T}}{ds}
```

$k$ is called the curvature of $\mathrm{C}$ at a certain point and it has the value $k= |d\mathbf{T}/ds|$. The quantity $R=1/k$ is the radius of curvature at that point. Thus, $\mathbf{N}=R(d\mathbf{T}/ds)$. The total acceleration of the particle in terms of the unit tangent $\mathbf{T}$ vector and the principal unit normal vector $\mathbf{N}$ can be written as

```{math}
:label: eq-2-2

\mathbf{a}=\frac{d\mathbf{v}}{dt}=\frac{d}{dt}(v\mathbf{T})=\frac{dv}{dt}\mathbf{T}+v\frac{d\mathbf{T}}{dt}
```

Furthermore,

```{math}
:label: eq-2-3

\frac{d\mathbf{T}}{dt}=\frac{d\mathbf{T}}{ds}\frac{ds}{dt}=\frac{\mathbf{N}}{R}\frac{ds}{dt}=\frac{v\mathbf{N}}{R}
```

Substituting Eq. [](#eq-2-2) into Eq. [](#eq-2-3) gives

```{math}
\mathbf{a}=\frac{dv}{dt}\mathbf{T}+\frac{v^{2}}{R}\mathbf{N}
```

Therefore, $a_{n}=v^{2}/R$ and $a_{t}=dv/dt$. Note that unlike $d|\mathbf{v}|/dt$, $|d\mathbf{v}/dt|$ corresponds to the change in the magnitude of the velocity or in its direction or in both (as it represents the magnitude of the total acceleration vector), whereas $d|\mathbf{v}|/dt$ corresponds to the change in the magnitude only.

````{prf:example}
:label: example-2-5
:enumerator: 2.5

A particle is moving in space according to the expression

```{math}
\mathbf{r}=(5\cos t\,\mathbf{i}+5\sin t\,\mathbf{j}+7t\,\mathbf{k})\,\mathrm{m}
```

Find the radius of curvature at any point on the space curve.

:::{admonition} Solution 2.5
:class: dropdown

```{math}
\frac{d\mathbf{r}}{dt}=(-5\sin t\,\mathbf{i}+5\cos t\,\mathbf{j}+7\mathbf{k})\,\mathrm{m}/\mathrm{s}
```

```{math}
\frac{ds}{dt}=\bigg |\frac{d\mathbf{r}}{dt}\bigg |=\sqrt{(-5\sin t)^{2}+(5\cos t)^{2}+(7)^{2}}=10\,\mathrm{m}/\mathrm{s}
```

Hence

```{math}
\mathbf{T}=\frac{d\mathbf{r}/dt}{ds/dt}=\frac{(-5\sin t\,\mathbf{i}+5\cos t\,\mathbf{j}+7\mathbf{k})}{10}=-0.5\sin t\,\mathbf{i}+0.5\cos t\,\mathbf{j}+0.7\mathbf{k}
```

The radius of curvature is

```{math}
R=\frac{1}{k}=\frac{1}{|d\mathbf{T}/ds|}
```

```{math}
\frac{d\mathbf{T}}{ds}=\frac{d\mathbf{T}}{dt}\frac{dt}{ds}=\frac{d\mathbf{T}/dt}{ds/dt}=\frac{-0.5\cos t\,\mathbf{i}-0.5\sin t\,\mathbf{j}}{10}=-0.05\cos t\,\mathbf{i}-0.05\sin t\,\mathbf{j}
```

```{math}
\bigg |\frac{d\mathbf{T}}{ds}\bigg |=\sqrt{(-0.05\cos t)^{2}+(-0.05\sin t)^{2}}=0.07
```

```{math}
R=\frac{1}{0.07}=14.3\,\mathrm{m}
```

:::
````

````{prf:example}
:label: example-2-6
:enumerator: 2.6

A car moves with constant tangential acceleration down a ramp as shown in [](#fig-2-16). If it starts from rest at A and reaches $\mathrm{B}$ after 4 s with a speed of $10\,\mathrm{m}/\mathrm{s}$, find the radius of curvature at $\mathrm{B}$ if the total acceleration of the car at that point is $3.2\,\mathrm{m}/\mathrm{s}^{2}$.

```{figure} ../images/ch-02/459974_1_En_2_Fig16_HTML.png
:name: fig-2-16

A car moving with a constant tangential acceleration down a ramp
```

:::{admonition} Solution 2.6
:class: dropdown

Since the tangential acceleration of the car is constant, it can be found from

```{math}
a_{t}=\frac{v_{B}-v_{A}}{t}=\frac{(10\,\mathrm{m}/\mathrm{s})-0}{4\,\mathrm{s}}=2.5\,\mathrm{m}/\mathrm{s}^{2}
```

Since the total acceleration of the car at $\mathrm{B}$ is 2 $\mathrm{m}/\mathrm{s}^{2}$ then the normal acceleration is

```{math}
a_{n}^{2}=a^{2}-a_{t}^{2}=(3.2\,\mathrm{m}/\mathrm{s}^{2})^{2}-(2.5\,\mathrm{m}/\mathrm{s}^{2})^{2}=4\,(\mathrm{m}/\mathrm{s}^{2})^{2}
```

```{math}
a_{n}=2\,\mathrm{m}/\mathrm{s}^{2}
```

The radius of curvature is

```{math}
R=\frac{v^{2}}{a_{n}}=\frac{(10\,\mathrm{m}/\mathrm{s})^{2}}{(2\,\mathrm{m}/\mathrm{s}^{2})}=50\,\mathrm{m}
```

:::
````

(sec-2-4)=
## 2.4 Some Applications

(sec-2-4-1)=
### 2.4.1 One-Dimensional Motion with Constant Acceleration

An acceleration that does not change with time is said to be a constant or uniform acceleration. In that case, the average and instantaneous accelerations are equal. This type of motion is more easily analyzed than when the acceleration is varied. Since the motion is in one dimension, it follows that the $y$ and $z$ components are zero. That is,

```{math}
\mathbf{r}=x\mathbf{i}
```

```{math}
\triangle \mathbf{r}=(x_{f}-x_{i})\mathbf{i}
```

Hence, as we’ve mentioned earlier, the direction of the displacement can be specified with a plus or minus sign, as well as the directions of the velocity and acceleration. Let us assume that $t_{i}=0$, $t_{f}=t$, $v_{xf}=v$, $v_{xi}=v_{0}$, $x_{i}=x_{0}$ and $x_{f}=x$. Since the acceleration is constant, the velocity will vary linearly with time, and thus the average velocity can be expressed as

```{math}
\overline{v}=\frac{v_{0}+v}{2}
```

```{math}
a=\overline{a}=\frac{v_{f}-v_{i}}{t_{f}-t_{i}}=\frac{v-v_{0}}{t}
```

```{math}
:label: eq-2-4

v=v_{0}+at
```

```{math}
\overline{v}=\frac{\triangle x}{\triangle t}=\frac{(v+v_{0})}{2}
```

```{math}
:label: eq-2-5

x-x_{0}=\frac{1}{2}(v+v_{0})t
```

Furthermore,

```{math}
x-x_{0}=\frac{1}{2}(v+v_{0})t=\frac{1}{2}(v_{0}+v_{0}+at)t
```

```{math}
:label: eq-2-6

x-x_{0}=v_{0}t+\frac{1}{2}at^{2}
```

Finally,

```{math}
x-x_{0}=\frac{1}{2}(v+v_{0})t=\frac{1}{2}(v+v_{0})\left( \frac{v-v_{0}}{a}\right)
```

```{math}
:label: eq-2-7

v^{2}=v_{0}^{2}+2a(x-x_{0})
```

Equations [](#eq-2-4), [](#eq-2-5), [](#eq-2-6), and [](#eq-2-7) are called the kinematic equations for motion in a straight line under constant acceleration. The motion graphs for an object moving with constant acceleration in the positive $\mathrm{x}$-direction are shown in [](#fig-2-17).

```{figure} ../images/ch-02/459974_1_En_2_Fig17_HTML.png
:name: fig-2-17

The motion graphs for an object moving with constant acceleration in the positive $\mathrm{x}$-direction
```

````{prf:example}
:label: example-2-7
:enumerator: 2.7

A train accelerates uniformly from rest and travels a distance of 200 $\mathrm{m}$ in the first 8 s. Determine: (a) the acceleration of the train; (b) the time it takes the train to reach a velocity of 70 $\mathrm{m}/\mathrm{s}$, (c) the distance traveled during that time; (d) the velocity of the train 5 s later from the time calculated in (b).

:::{admonition} Solution 2.7
:class: dropdown

(a)

```{math}
x-x_{0}=v_{0}t-\frac{1}{2}at^{2}
```

Since $v_{0}=0$, we have

```{math}
a=\frac{2(x-x_{0})}{t^{2}}=\frac{2(200\,\mathrm{m})}{(8\,\mathrm{s})^{2}}=6.25\,\mathrm{m}/\mathrm{s}^{2}
```

(b)

```{math}
v=v_{0}+at
```

$v_{0}=0$ and therefore

```{math}
t=\frac{v}{a}=\frac{(70\,\mathrm{m}/\mathrm{s})}{(6.25\,\mathrm{m}/\mathrm{s}^{2})}=11.2\,\mathrm{s}
```

(c)

```{math}
x-x_{0}=\frac{1}{2}at^{2}=\frac{1}{2}(6.25)(11.2)^{2}=392\,\mathrm{m}
```

(d)

```{math}
v=v_{0}+at=(70\,\mathrm{m}/\mathrm{s})+(6.25\,\mathrm{m}/\mathrm{s}^{2})(5\,\mathrm{s})=101.25\,\mathrm{m}/\mathrm{s}
```

:::
````

````{prf:example}
:label: example-2-8
:enumerator: 2.8

An airplane accelerates uniformly from rest at a rate of 3 $\mathrm{m}/\mathrm{s}^{2}$ before taking off. If it is to take off at a speed of 100 $\mathrm{m}/\mathrm{s}$: (a) how much time is required for it to take off; (b) what distance will it have traveled before taking off?

:::{admonition} Solution 2.8
:class: dropdown

(a)

```{math}
v=v_{0}+at
```

We have $v_{0}=0$, this gives

```{math}
t=\frac{v}{a}=\frac{(100\,\mathrm{m}/\mathrm{s})}{(3\,\mathrm{m}/\mathrm{s}^{2})}=33.3\,\mathrm{s}
```

(b)

```{math}
x=\frac{1}{2}at^{2}=\frac{1}{2}(3\,\mathrm{m}/\mathrm{s}^{2})(33.3\,\mathrm{s})^{2}=1.7\times 10^{3}\,\mathrm{m}
```

:::
````

````{prf:example}
:label: example-2-9
:enumerator: 2.9

A car moving at a constant velocity of 140 $\mathrm{km}/\mathrm{h}$ passed a police car moving at a constant velocity of 80 $\mathrm{km}/\mathrm{h}$. 5 s after the car had passed the police car, the police vehicle begins to accelerate toward the car at a constant rate of $1.4\times 10^{4}\,\mathrm{km}/\mathrm{h}^{2}$ (a) How much time will it take the police car to catch the other car? (b) What is the distance traveled by both during that time? (c) How much time has passed from where the car passed the police car to where it was caught?

:::{admonition} Solution 2.9
:class: dropdown

Let’s assume that $x=0$ at where the car passed the police car and that $t=0$ at the instant the police car begins to accelerate. The velocity of the car is equal to 38.9 $\mathrm{m}/\mathrm{s}$, and the initial velocity and acceleration of the police car are 22.2 $\mathrm{m}/\mathrm{s}$ and 1.1 $\mathrm{m}/\mathrm{s}^{2}$, respectively The police will catch the car when both their displacements from $x=0$ are equal. (a) From the expression $x= x_{0}+v_{0}t+\frac{1}{2}at^{2}$, the displacement of the car at any time is

```{math}
x_{c}=x_{0c}+v_{0c}t=(194.5\,\mathrm{m})+(38.9\,\mathrm{m}/\mathrm{s})t
```

The displacement of the police car at any time is

```{math}
x_{p}=x_{0p}+v_{0p}t+\frac{1}{2}a_{p}t^{2}=(111\,\mathrm{m})+(22.2\,\mathrm{m}/\mathrm{s})t+\frac{1}{2}(1.1\,\mathrm{m}/\mathrm{s}^{2})t^{2}
```

The police will catch the car when $x_{c}=x_{p}$, and therefore if $(194.5\,\mathrm{m})+(38.9\,\mathrm{m}/\mathrm{s})t=(111\,\mathrm{m})+(22.2\,\mathrm{m}/\mathrm{s})t+\frac{1}{2}(1.1\,\mathrm{m}/\mathrm{s}^{2})t^{2}$ or

```{math}
t^{2}-30.4t-151.8=0
```

Thus

```{math}
t=\frac{(30.4)\pm \sqrt{(304)^{2}+(4)(1518)}}{2}
```

That gives $t=34.8\,\mathrm{s}$.

(b)

```{math}
x_{p}=x_{c}=(111\,\mathrm{m})+(22.2\,\mathrm{m}/\mathrm{s})(34.8\,\mathrm{s})+\frac{1}{2}(1.1\,\mathrm{m}/\mathrm{s}^{2})(34.8\,\mathrm{s})^{2}=1.55\times 10^{3}\,\mathrm{m}
```

(c)

```{math}
t=(5\,\mathrm{s})+(34.8\,\mathrm{s})=39.8\,\mathrm{s}
```

:::
````

(sec-2-4-2)=
### 2.4.2 Free-Falling Objects

Galileo Galilei (1564–1642) was an Italian scientist, who studied and experimented the acceleration of falling objects. By dropping various objects from the Leaning Tower of Pisa (or by releasing objects from inclined planes according to another story), Galileo discovered that when air resistance is neglected then all objects would fall with the same constant acceleration regardless of their mass or size. This acceleration, denoted by *g*, is known as the free-fall acceleration since air resistance is neglected and the object is assumed to be moving freely under gravity alone. The direction of the vector $\mathbf{g}$ is downwards toward the earth’s center. However, *g* varies with altitude as well as other factors which will be discussed in Chap. [](#ch-9).

In solving problems involving objects falling near the surface of the earth, $g$ can be assumed to be constant with a value of 9.8 $\mathrm{m}/\mathrm{s}^{2}$ and air resistance can be neglected. A free-falling motion is a motion along a straight line (for example along the $\mathrm{y}$-axis) where objects may move upwards or downwards. The kinematics equations of the free-falling motion with constant acceleration can be found from Eqs. ([](#eq-2-4)), ([](#eq-2-5)), ([](#eq-2-6)), and ([](#eq-2-7)) by simply replacing $x$ with $y$ and $a$ with $g$. If the positive direction of $y$ is chosen to be upwards, then the acceleration is negative (downwards) and is given by $(a=-g)$. These substitutions give

```{math}
v=v_{0}-gt
```

```{math}
y-y_{0}=\frac{1}{2}(v+v_{0})t
```

```{math}
y-y_{0}=v_{0}t-\frac{1}{2}gt^{2}
```

```{math}
v^{2}=v_{0}^{2}-2g(y-y_{0})
```

The displacement and velocity graphs are shown in [](#fig-2-18). Note that it does not matter whether the object is falling or moving upward, it will experience the same acceleration $g$ which is directed downwards. [](#fig-2-19) shows the important features of a free-falling object that is dropped from rest.

```{figure} ../images/ch-02/459974_1_En_2_Fig18_HTML.png
:name: fig-2-18

The displacement and velocity graph for a free-falling object
```

```{figure} ../images/ch-02/459974_1_En_2_Fig19_HTML.png
:name: fig-2-19

The important features of a free falling object that is dropped from rest
```

````{prf:example}
:label: example-2-10
:enumerator: 2.10

A ball is thrown directly upwards with an initial velocity of 15 $\mathrm{m}/\mathrm{s}$. On its way down, it was caught at a distance of 1 m below the point from where it was thrown. Determine (a) the maximum height reached by the ball; (b) the time it takes the ball to reach that height; (c) the velocity of the ball when it is caught; (d) the total time elapsed from where the ball was thrown to where it was caught.

:::{admonition} Solution 2.10
:class: dropdown

(a) First we take $y=0$ at the position where the ball is thrown and positive $y$ to be upwards. At the maximum height the velocity of the ball is zero,

```{math}
v^{2}=v_{0}^{2}-2g(y-y_{0})
```

```{math}
0=(15\,\mathrm{m}/\mathrm{s})^{2}-2(9.8\,\mathrm{m}/\mathrm{s}^{2})h_{\max }
```

```{math}
h_{\max }=11.5\,\mathrm{m}
```

(b) Using the expression $v=v_{0}-gt$ we have

```{math}
0=(15\,\mathrm{m}/\mathrm{s})-(9.8\,\mathrm{m}/\mathrm{s}^{2})t
```

```{math}
t=1.5\,\mathrm{s}
```

(c) When the ball is caught its position is $y=-1\,\mathrm{m}$,

```{math}
v^{2}=v_{0}^{2}-2g(y-y_{0})
```

taking the initial position of the ball at $y=0$, we get

```{math}
v^{2}=(15\,\mathrm{m}/\mathrm{s})^{2}-2(9.8\,\mathrm{m}/\mathrm{s}^{2})((-1\,\mathrm{m})-0)
```

and

```{math}
v=-15.6\,\mathrm{m}/\mathrm{s}
```

or if we take the initial position at $y=11.5\,\mathrm{m}$ we have

```{math}
v^{2}=0-2(9.8\,\mathrm{m}/\mathrm{s}^{2})((-1\,\mathrm{m})-(11.5\,\mathrm{m}))
```

and

```{math}
v=-15.6\,\mathrm{m}/\mathrm{s}.
```

(d) $v=v_{0}-gt$, substituting for $v$ and $v_{0}$ we have

```{math}
(-15.6\,\mathrm{m}/\mathrm{s})=(15\,\mathrm{m}/\mathrm{s})-(9.8\,\mathrm{m}/\mathrm{s}^{2})t
```

```{math}
t=3.1\,\mathrm{s}
```

:::
````

````{prf:example}
:label: example-2-11
:enumerator: 2.11

A tennis ball is dropped from a building that is $30\,\mathrm{m}$ high. Find (a) its position and velocity 2 s later; (b) the total time it takes the ball to fall to the ground; (c) its velocity just before it hits the ground.

:::{admonition} Solution 2.11
:class: dropdown

(a) Taking $y_{0}=0$ and $v_{0}=0$ at $t=0$ we have

```{math}
y-y_{0}=v_{0}t-\frac{1}{2}gt^{2}
```

at $t=2\,\mathrm{s}$

```{math}
y-0=0-\frac{1}{2}(9.8\,\mathrm{m}/\mathrm{s}^{2})(2\,\mathrm{s})^{2}=-19.6\,\mathrm{m}
```

```{math}
v=v_{0}-gt=0-(9.8\,\mathrm{m}/\mathrm{s}^{2})(2\,\mathrm{s})=-19.6\,\mathrm{m}/\mathrm{s}
```

(b)

```{math}
y-y_{0}=v_{0}t-\frac{1}{2}gt^{2}
```

```{math}
(-30\,\mathrm{m})-0=0-\frac{1}{2}(9.8\,\mathrm{m}/\mathrm{s}^{2})t^{2}
```

```{math}
t=2.5\,\mathrm{s}
```

(c)

```{math}
v=v_{0}-gt=0-(9.8\,\mathrm{m}/\mathrm{s}^{2})(2.5\,\mathrm{s})
```

```{math}
v=-24.5\,\mathrm{m}/\mathrm{s}
```

:::
````

````{prf:example}
:label: example-2-12
:enumerator: 2.12

A ball is thrown vertically downwards from a 100 $\mathrm{m}$ high building with an initial speed of 1 $\mathrm{m}/\mathrm{s}$. 3 s later a second ball is thrown. What initial speed must the second ball have so that the two balls hit the ground at the same time?

:::{admonition} Solution 2.12
:class: dropdown

The time it takes the first ball to hit the ground is found from

```{math}
y-y_{0}=v_{0}t-\frac{1}{2}gt^{2}
```

```{math}
0-(100\,\mathrm{m})=(-1\,\mathrm{m}/\mathrm{s})t_{1}-\frac{1}{2}(9.8\,\mathrm{m}/\mathrm{s}^{2})t_{1}^{2}
```

```{math}
t_{1}=6.4\,\mathrm{s}
```

The second ball must fall the same distance during a time of

```{math}
t_{1}-(3\,\mathrm{s})=(6.4\,\mathrm{s})-(3\,\mathrm{s})=3.4\,\mathrm{s}
```

and therefore

```{math}
y-y_{0}=v_{0}t-\frac{1}{2}gt^{2}
```

```{math}
0-(100\,\mathrm{m})=v_{0}(3.4\,\mathrm{s})-\frac{1}{2}(9.8\,\mathrm{m}/\mathrm{s}^{2})(3.4\,\mathrm{s})^{2}
```

```{math}
v_{0}=-12.6\,\mathrm{m}/\mathrm{s}
```

:::
````

### 2.4.3 Motion in Two Dimensions with Constant Acceleration

The position vector can be written as

```{math}
\mathbf{r}=x\mathbf{i}+y\mathbf{j}
```

```{math}
\mathbf{v}=v_{x}\mathbf{i}+v_{y}\mathbf{j}
```

```{math}
\mathbf{a}=a_{x}\mathbf{i}+a_{y}\mathbf{j}
```

Because $a$ is a constant both $a_{x}$ and $a_{y}$ are constants. Therefore, the kinematic in Sect. [](#sec-2-4-1) applies in each direction:

```{math}
:label: eq-2-8

v_{x}=v_{0x}+a_{x}t
```

```{math}
:label: eq-2-9

x=x_{0}+v_{0x}t+\frac{1}{2}a_{x}t^{2}
```

```{math}
:label: eq-2-10

v_{y}=v_{0y}+a_{y}t
```

```{math}
:label: eq-2-11

y=y_{0}+v_{0y}t+\frac{1}{2}a_{y}t^{2}
```

```{math}
\mathbf{r}=x\mathbf{i}\ +y\mathbf{j}=(x_{0}+v_{0x}t+\frac{1}{2}a_{x}t^{2})\mathbf{i}+(y_{0}+v_{0y}t+\frac{1}{2}a_{y}t^{2})\mathbf{j}
```

```{math}
:label: eq-2-12

\mathbf{r}=\mathbf{r}_{0}+\mathbf{v}_{0}t+\frac{1}{2}\mathbf{a}t^{2}
```

```{math}
\mathbf{v}=v_{x}\mathbf{i}+v_{y}\mathbf{j}=(v_{0x}+a_{x}t)\mathbf{i}+(v_{0y}+a_{y}t)\mathbf{j}=(v_{0x}\mathbf{i}+v_{0y}\mathbf{j})+(a_{x}\mathbf{i}+a_{y}\mathbf{j})t
```

```{math}
:label: eq-2-13

\mathbf{v}=\mathbf{v}_{0}+\mathbf{a}t
```

````{prf:example}
:label: example-2-13
:enumerator: 2.13

If the motion of a particle in a plane is described by $v_{y}=(-8t)\,\mathrm{m}/\mathrm{s}$ and $x= (5-2t^{2})\,\mathrm{m}$: (a) plot the $\mathrm{y}$ component of the particle as a function of time if at $t=0$, $y=0$; (b) find the total speed and magnitude of the acceleration of the particle at $t=2\,\mathrm{s}$.

```{figure} ../images/ch-02/459974_1_En_2_Fig20_HTML.png
:name: fig-2-20

The $\mathrm{y}$ component of the particle as a function of time
```

:::{admonition} Solution 2.13
:class: dropdown

(a) The $\mathrm{y}$-component of position is

```{math}
y=\int v_{y}dt=\int (-8t)dt=-4t^{2}+c
```

since at $t=0$, $y=0$, then

```{math}
y=(-4t^{2})\,\mathrm{m}
```

The plot of $y$ against $t$ is shown in [](#fig-2-20).

(b) The $\mathrm{x}$-components of velocity and acceleration is

```{math}
v_{x}=\frac{dx}{dt}=\frac{d(5-2t^{2})}{dt}
```

```{math}
v_{x}=(-4t)\,\mathrm{m}/\mathrm{s}
```

```{math}
a_{x}=\frac{dv_{x}}{dt}=\frac{d(-4t)}{dt}
```

```{math}
a_{x}=-4\,\mathrm{m}/\mathrm{s}^{2}
```

The $\mathrm{y}$-component of acceleration is

```{math}
a_{y}=\frac{dv_{y}}{dt}=\frac{d(-8t)}{dt}
```

or

```{math}
a_{y}=(-8)\,\mathrm{m}/\mathrm{s}^{2}
```

at $t=2\,\mathrm{s}$, $v_{x}=-8\,\mathrm{m}/\mathrm{s}$, $v_{y}=-16\,\mathrm{m}/\mathrm{s}$ and the velocity is

```{math}
v=\sqrt{v_{x}+v_{y}}=\sqrt{(-8\,\mathrm{m}/\mathrm{s})^{2}+(-16\,\mathrm{m}/\mathrm{s})^{2}}=17.9\,\mathrm{m}/\mathrm{s}
```

```{math}
a_{x}=-4\,\mathrm{m}/\mathrm{s}^{2}
```

and

```{math}
a_{y}=(-8)\,\mathrm{m}/\mathrm{s}^{2}
```

Therefore, the acceleration of the particle is constant at any time and is given by

```{math}
a=\sqrt{a_{x}+a_{y}}=\sqrt{(-4\,\mathrm{m}/\mathrm{s}^{2})^{2}+(-8\,\mathrm{m}/\mathrm{s}^{2})^{2}}=8.9\,\mathrm{m}/\mathrm{s}^{2}
```

:::
````

### 2.4.4 Projectile Motion

Projectile motion is the motion of an object thrown (projected) into the air at some angle with respect to the surface of the earth, such as the motion of a baseball thrown into the air or an object dropped from a moving airplane. In the simplified model where air resistance as well as other factors such as the Earth’s curvature and rotation are neglected, and if the free-fall acceleration $\mathbf{g}$ is assumed constant in magnitude and direction throughout the motion of the object, then the path of the projectile is always a parabola that depends on the magnitude and direction of its initial velocity. Therefore, the projectile can be considered as a combination of a vertical motion with a constant acceleration directed downwards and a horizontal motion with zero acceleration (constant velocity). We can see from [](#fig-2-21) that

```{figure} ../images/ch-02/459974_1_En_2_Fig21_HTML.png
:name: fig-2-21

The projectile motion
```

```{math}
\cos \theta _{0}={v_{0x}}/v_{o}
```

```{math}
\sin \theta _{0}={v_{0y}}/v_{o}
```

At $t=0$, we have $x_{0}=y_{0}=0$ and $v_{i}=v_{0}$. Because $a_{y}=-g$ and $a_{x}=0$ and by substituting in Eqs. [](#eq-2-8), [](#eq-2-9), [](#eq-2-10), and [](#eq-2-11) gives

```{math}
:label: eq-2-14

v_{x}=v_{0x}=v_{0}\cos \theta _{0}= \text {constant}
```

```{math}
:label: eq-2-15

v_{y}=v_{y0}-gt=v_{0}\sin \theta _{0}-gt
```

```{math}
:label: eq-2-16

x=v_{x0}t=(v_{0}\cos \theta _{0})t
```

```{math}
:label: eq-2-17

y=v_{y0}t-\frac{1}{2}gt^{2}=(v_{0}\sin \theta _{0})t-\frac{1}{2}gt^{2}
```

Combining and eliminating $t$ from Eqs. [](#eq-2-16) and [](#eq-2-17) we find that

```{math}
y=(\tan \theta _{0})x-\bigg (\frac{g}{2v_{0}^{2}\cos ^{2}\theta _{0}}\bigg )x^{2} \quad \left(0<\theta _{0}<\frac{\pi }{2}\right)
```

This equation which is of the form $y=ax-bx^{2}$ ($a$ and $b$ are constants), is the equation of a parabola. Therefore, when air resistance is neglected (when using the simplified model of the system), the trajectory of the projectile is always a parabola. At any instant, the velocity of the object is tangent to its trajectory Its magnitude and direction with respect to the positive $\mathrm{x}$-direction are given by

```{math}
v=\sqrt{v_{x}^{2}+v_{y}^{2}}
```

and

```{math}
\theta =\tan ^{-1} {(v_{y}/v_{x})}
```

respectively The maximum height $h$ of the projectile, as in [](#fig-2-22), is found at $t=t_{1}$ by noting that at the peak $h$, $v_{y}=0$. Substituting this in Eq. [](#eq-2-15) gives

```{math}
v_{0}\sin \theta _{0}=gt_{1}
```

```{math}
t_{1}=\frac{v_{0}\sin \theta _{0}}{g}
```

Substituting $t_{1}$ into Eq. [](#eq-2-17) we get

```{math}
y_{\max }=h=(v_{0}\sin \theta _{0})t_{1}-\frac{1}{2}gt_{1}^{2}
```

```{math}
h=(v_{0}\sin \theta _{0})\bigg (\frac{v_{0}\sin \theta _{0}}{g}\bigg )-\frac{1}{2}g\bigg (\frac{v_{0}\sin \theta _{0}}{g}\bigg )^{2}
```

```{math}
h=\frac{v_{0}^{2}\sin ^{2}\theta _{0}}{2g}
```

The maximum range $R$ is at $t=2t_{1}$. Substituting $t$ into Eq. [](#eq-2-16) gives

```{math}
x=R=(v_{0}\cos \theta _{0})2t_{1}=(v_{0}\cos \theta _{0})\frac{2v_{0}\sin \theta _{0}}{g}=\frac{2v_{0}^{2}\sin \theta _{0}\cos \theta _{0}}{g}
```

```{math}
R=\frac{v_{0}^{2}\sin 2\theta _{0}}{g}
```

```{figure} ../images/ch-02/459974_1_En_2_Fig22_HTML.png
:name: fig-2-22

The maximum height of a projectile
```

````{prf:example}
:label: example-2-14
:enumerator: 2.14

A baseball is thrown at angle of $35^{\circ}$ to the horizontal with an initial speed of 20 $\mathrm{m}/\mathrm{s}$. Neglecting air resistance, find: (a) the maximum height reached by the ball; (b) the time it takes the ball to hit the ground; (c) the range; and (d) the speed of the ball just before it strikes the ground.

:::{admonition} Solution 2.14
:class: dropdown

(a) The maximum height reached by the ball is

```{math}
h=\frac{v_{0}^{2}\sin ^{2}\theta _{0}}{2g}=\frac{(20\,\mathrm{m}/\mathrm{s})^{2}\sin ^{2}(35^{\circ})}{2(9.8\,\mathrm{m}/\mathrm{s}^{2})}=6.7\,\mathrm{m}
```

(b) The time it takes the ball to hit the ground is

```{math}
t=2t_{1}=\frac{2v_{0}\sin \theta _{0}}{g}=\frac{2(20\,\mathrm{m}/\mathrm{s})\sin (35^{\circ})}{(9.8\,\mathrm{m}/\mathrm{s}^{2})}=2.34\,\mathrm{s}
```

(c) The range is

```{math}
R=\frac{v_{0}^{2}\sin 2\theta _{0}}{g}=\frac{(20\,\mathrm{m}/\mathrm{s})^{2}\sin (70^{\circ})}{(9.8\,\mathrm{m}/\mathrm{s}^{2})}=38.4\,\mathrm{m}
```

(d) The $\mathrm{x}$-component of the velocity of the ball just before it hits the ground is

```{math}
v_{x}=v_{0x}=v_{0}\cos \theta _{0}=(20\,\mathrm{m}/\mathrm{s})\cos (35^{\circ})=16.4\,\mathrm{m}/\mathrm{s}
```

The $\mathrm{y}$-component is

```{math}
v_{y}=v_{0y}-gt=v_{0}\sin \theta _{0}-gt=(20\,\mathrm{m}/\mathrm{s})\sin (35^{\circ})-(9.8\,\mathrm{m}/\mathrm{s}^{2})(2.34\,\mathrm{s})=-11.5\,\mathrm{m}/\mathrm{s}
```

Hence, the speed is

```{math}
v=\sqrt{v_{x}^{2}+v_{y}^{2}}=\sqrt{(164\,\mathrm{m}/\mathrm{s})^{2}+(-11.5\,\mathrm{m}/\mathrm{s})^{2}}=20\,\mathrm{m}/\mathrm{s}
```

:::
````

````{prf:example}
:label: example-2-15
:enumerator: 2.15

A boy throws a ball with a constant horizontal velocity of 1 $\mathrm{m}/\mathrm{s}$ at an altitude of 0.6 $\mathrm{m}$. Find the horizontal distance between the releasing point to the point where the ball hits the ground.

:::{admonition} Solution 2.15
:class: dropdown

Let the origin of the reference frame be the releasing point. Since $v_{0y}=0$ we have

```{math}
y=-\frac{1}{2}gt^{2}
```

and

```{math}
x=v_{0x}t
```

Hence, when the ball reaches the ground, the elapsed time is

```{math}
t=\sqrt{\frac{-2y}{g}}=\sqrt{\frac{-2(0.6\,\mathrm{m})}{(-9.8\,\mathrm{m}/\mathrm{s}^{2})}}=0.34\,\mathrm{s}
```

and

```{math}
x=(1\,\mathrm{m}/\mathrm{s})(0.34\,\mathrm{s})=0.34\,\mathrm{m}
```

:::
````

(sec-2-4-5)=
### 2.4.5 Uniform Circular Motion

A particle moving in a circular path with constant speed is said to be in uniform circular motion. The motion of the moon about earth, and the motion of clothes in a washing machine are examples of uniform circular motion. In this motion, the direction of the velocity of the particle is continuously changing but its magnitude is constant. As we have mentioned in Sect. [](#sec-2-3-1), when only the direction of the velocity changes, the acceleration is then always perpendicular to the velocity at any time. Therefore, we have only the normal component of the acceleration $a_{n}=v^{2}/R$, and the tangential component of the acceleration $a_{t}=dv/dt$ is zero. In the case of the circular path the radius of curvature $R$ is constant, denoted by $r$, and the normal acceleration is directed along the radius of the circle

```{math}
a_{rad}=\frac{v^{2}}{r}
```

The subscript rad is for radial. Thus, this radial or centripetal acceleration $a_{rad}$ is always directed toward the center of the circle. Therefore, the directions of $\mathbf{v}$ and a change continuously with time but their magnitudes are constant (see [](#fig-2-23)). The time required for the particle to complete one revolution around the circle is called the period of revolution and is given by

```{math}
T=\frac{2\pi r}{v}
```

Thus

```{math}
a_{rad}=\frac{4\pi ^{2}r}{T^{2}}
```

```{figure} ../images/ch-02/459974_1_En_2_Fig23_HTML.png
:name: fig-2-23

The directions of $\mathrm{y}$ and a change continuously with time but their magnitudes are constant
```

````{prf:example}
:label: example-2-16
:enumerator: 2.16

In a fun fair ride, the passengers rotate in a circle with a constant speed of 3 $\mathrm{m}/\mathrm{s}$. If the period of revolution is 1.5 $\mathrm{s}$, find the total acceleration of the passenger.

:::{admonition} Solution 2.16
:class: dropdown

Since the speed of the passenger is constant, it follows that the passenger’s total acceleration is just the centripetal acceleration given by

```{math}
a_{rad}=\frac{v^{2}}{r}
```

The radius of the circular path is

```{math}
r=\frac{vT}{2\pi }=\frac{(3\,\mathrm{m}/\mathrm{s})(1.5\,\mathrm{s})}{2(3.14)}=0.7\,\mathrm{m}
```

```{math}
a_{rad}=\frac{v^{2}}{r}=\frac{(3\,\mathrm{m}/\mathrm{s})^{2}}{(0.7\,\mathrm{m})}=12.86\,\mathrm{m}/\mathrm{s}^{2}
```

:::
````

(sec-2-4-6)=
### 2.4.6 Nonuniform Circular Motion

In nonuniform circular motion, the velocity of the particle varies in both magnitude and direction. As mentioned in Sect. [](#sec-2-3-1), when both the magnitude and direction of the particle’s velocity change then its acceleration is directed at some angle to $\mathbf{v}$. Thus, in addition to the normal acceleration in uniform circular motion that corresponds to the change in the direction of $\mathbf{v}$, there is a tangential component that corresponds to the change in the magnitude of $\mathbf{v}$. Furthermore $a_{rad}$ is not constant since $\mathbf{v}$ changes with time. Therefore, the resultant acceleration is

```{math}
\mathbf{a}=\mathbf{a}_{n}+\mathbf{a}_{t}=\frac{v^{2}}{r}\mathbf{N}+\frac{d|\mathbf{v}|}{dt}\mathbf{T}
```

In Chap. [](#ch-8), the concepts of angular velocity and acceleration and their vector relationship with the normal and tangential accelerations are introduced. [](#fig-2-24) shows the velocity and total acceleration vectors of a particle moving in a circular path with increasing speed (clockwise) until it reaches the maximum speed at the bottom, and then slows down as it goes back up. An example of this motion is in a roller coaster ride in a vertical circle.

```{figure} ../images/ch-02/459974_1_En_2_Fig24_HTML.png
:name: fig-2-24

The velocity and total acceleration vectors of a particle moving in a circular path with increasing speed (clockwise) until it reaches the maximum speed at the bottom, and then slows down as it goes back up. An example of this motion is in a roller coaster ride in a vertical circle
```

````{prf:example}
:label: example-2-17
:enumerator: 2.17

A car moving on a circular track of a 20 $\mathrm{m}$ radius accelerates uniformly from a speed of 30 $\mathrm{km}/\mathrm{h}$ to a speed of 50 $\mathrm{km}/\mathrm{h}$ in 3 $\mathrm{s}$. Find the total acceleration of the car at the instant its speed is 40 $\mathrm{km}/\mathrm{s}$.

:::{admonition} Solution 2.17
:class: dropdown

Since both the direction and the magnitude of the car’s velocity change, its total acceleration is the vector sum of its tangential and radial accelerations. The tangential acceleration is

```{math}
a_{t}=\frac{v-v_{0}}{t}=\frac{(13.8\,\mathrm{m}/\mathrm{s})-(8.3\,\mathrm{m}/\mathrm{s})}{(3\,\mathrm{s})}=1.83\,\mathrm{m}/\mathrm{s}^{2}
```

When $v=40\,\mathrm{km}/\mathrm{h}=11.1\,\mathrm{m}/\mathrm{s}$ the radial acceleration is

```{math}
a_{rad}=\frac{v^{2}}{r}=\frac{(11.1\,\mathrm{m}/\mathrm{s})^{2}}{(20\,\mathrm{m})}=6.2\,\mathrm{m}/\mathrm{s}^{2}
```

And the total acceleration is

```{math}
a=\sqrt{(1.83\,\mathrm{m}/\mathrm{s}^{2})^{2}+(6.2\,\mathrm{m}/\mathrm{s}^{2})^{2}}=6.5\,\mathrm{m}/\mathrm{s}^{2}
```

:::
````

(sec-2-5)=
## 2.5 Relative Velocity

In this section, we will see how observers moving relative to each other obtain different results when measuring the velocity of a moving body. Suppose two cars are moving besides each other at the same speed of 120 $\mathrm{km}/\mathrm{h}$ with respect to earth. In this case, any of the two cars is at rest relative to the other. According to an observer who is stationary with respect to earth, each car is moving with a speed of 120 $\mathrm{km}/\mathrm{s}$. A second observer, in any of the cars, will see the stationary observer moving backwards at a speed of 120 $\mathrm{km}/\mathrm{h}$. In addition, if a third car is moving ahead of the two cars at a speed of 140 $\mathrm{km}/\mathrm{h}$ relative to earth, then its speed relative to an observer in any of the two cars is 20 $\mathrm{km}/\mathrm{s}$. Thus, the displacement and velocities may have different values when measured relative to different observers. Therefore, the description of motion depends on the observer. By attaching a coordinate system to an observer together with an appropriate time scale, he or she are then said to be in a reference frame. In measuring quantities, it is essential to specify the reference frame. In most situations, the earth (the lab) is used as our frame of reference. To understand this, consider a particle moving in one dimension in the positive $\mathrm{x}$-direction. Suppose two observers want to describe its motion, one is observer $\mathrm{S}$ who is stationary relative to the ground, and the other is observer $\mathrm{S}'$, who is moving in the positive $\mathrm{x}$-direction with a constant velocity relative to the ground (see [](#fig-2-25)). At any instant, the position of the particle relative to $\mathrm{S}$ is $x_{PS}$, and its position relative to $\mathrm{S}'$ is $x_{PS'}$. The relation between these two observations is

```{math}
:label: eq-2-18

x_{PS}=x_{PS'}+x_{S'S}
```

Therefore, the position of $\mathrm{P}$ relative to $\mathrm{O}_{\mathrm{S}}$ is equal to the position of $\mathrm{P}$ relative to $\mathrm{O}_{\mathrm{S}'}$ plus the distance between $\mathrm{O}_{\mathrm{S}}$ and $\mathrm{O}_{\mathrm{S}'}$. Differentiating Eq. [](#eq-2-18) with respect to time we get

```{math}
\frac{dx_{PS}}{dt}=\frac{dx_{PS'}}{dt}+\frac{dx_{S'S}}{dt}
```

or

```{math}
v_{PS}=v_{PS'}+v_{S'S}
```

We will extend this to three dimensions in the case where the velocity of $\mathrm{S}'$ with respect to $\mathrm{S}(v_{S'S})$ is constant in both magnitude and direction (see [](#fig-2-26)). The position vector of the particle $\mathrm{P}$ relative to $\mathrm{S}$ is given by

```{math}
:label: eq-2-19

\mathbf{r}_{PS}=\mathbf{r}_{PS'}+\mathbf{r}_{S'S}
```

Differentiating this with respect to time gives

```{math}
:label: eq-2-20

\mathbf{v}_{PS}=\mathbf{v}_{PS'}+\mathbf{v}_{S'S}
```

Equations [](#eq-2-19) and [](#eq-2-20) are called the Galilean transformation equations. In addition, for any two frames of reference $\mathrm{S}$ and $\mathrm{S}$ we have

```{math}
\mathbf{v}_{SS'}=-\mathbf{v}_{S'S}
```

```{figure} ../images/ch-02/459974_1_En_2_Fig25_HTML.png
:name: fig-2-25

Observer $\mathrm{S}$ is stationary relative to the ground, and observer $\mathrm{S}'$ is moving in the positive $\mathrm{x}$-direction with a constant velocity relative to the ground
```

```{figure} ../images/ch-02/459974_1_En_2_Fig26_HTML.png
:name: fig-2-26

The velocity of $\mathrm{S}'$ with respect to $\mathrm{S}(v_{S'S})$ is constant in both magnitude and direction
```

````{prf:example}
:label: example-2-18
:enumerator: 2.18

Two motor cyclists $\mathrm{A}$ and $\mathrm{B}$ are driving along the same road (See [](#fig-2-27)) with speeds 90 $\mathrm{km}/\mathrm{h}$ and 50 $\mathrm{km}/\mathrm{s}$, respectively. Determine: (a) the velocity of motorcyclist A relative to $\mathrm{B}$ and of $\mathrm{B}$ relative to $\mathrm{A}$?, and (b) if the two motor cyclists approach each other along two parallel roads, (See [](#fig-2-28)), A moving at 80 $\mathrm{km}/\mathrm{s}$, and $\mathrm{B}$ moving at 60 $\mathrm{km}/\mathrm{s}$, what is the velocity of motorcyclist A relative to $\mathrm{B}$ and of $\mathrm{B}$ relative to A.

```{figure} ../images/ch-02/459974_1_En_2_Fig27_HTML.png
:name: fig-2-27

Two motor cyclists $\mathrm{A}$ and $\mathrm{B}$ driving with speeds 90 $\mathrm{km}/\mathrm{h}$ and 50 $\mathrm{km}/\mathrm{s}$ respectively
```

```{figure} ../images/ch-02/459974_1_En_2_Fig28_HTML.png
:name: fig-2-28

A is moving at 80 $\mathrm{km}/\mathrm{s}$, and $\mathrm{B}$ moving at 60 $\mathrm{km}/\mathrm{s}$
```

:::{admonition} Solution 2.18
:class: dropdown

Using the above discussion, consider $\mathrm{S}$ as the Earth’s frame of reference denoted E, $\mathrm{S}'$ as the frame of reference of motorcyclist B and the point P as the motor cyclist A

(a) The velocity of A relative to $\mathrm{B}$ is found from

```{math}
v_{AB}=v_{AE}-v_{BE}=( 90\,\mathrm{km}/\mathrm{h})-(50\,\mathrm{km}/\mathrm{h})=40\,\mathrm{km}/\mathrm{h}
```

The velocity of $\mathrm{B}$ relative to A is

```{math}
v_{BA}=-40\,\mathrm{km}/\mathrm{h}
```

(b)

```{math}
v_{AB}=v_{AE}-v_{BE}=( 80\,\mathrm{km})-(-60\,\mathrm{km}/\mathrm{h})=140\,\mathrm{km}/\mathrm{h}
```

```{math}
v_{BA}=-140\,\mathrm{km}/\mathrm{h}
```

:::
````

````{prf:example}
:label: example-2-19
:enumerator: 2.19

A boat is traveling at sea at 8 $\mathrm{km}/\mathrm{h}$ north relative to the sea’s waves, and the waves are traveling northeast relative to the earth at a constant speed of 4 $\mathrm{km}/\mathrm{h}$. What is the velocity of the boat relative to the earth?

:::{admonition} Solution 2.19
:class: dropdown

Using [](#fig-2-26), consider the Earth as S (denoted E), the waves as $\mathrm{S}'$, and the boat as the point P. As we can see from [](#fig-2-29), the velocity of the boat relative to the earth is given by $\mathbf{v}_{bE}=\mathbf{v}_{bw}+\mathbf{v}_{wE}$, where $\mathbf{v}_{bw}$ and $\mathbf{v}_{wE}$ are the velocities of the boat relative to the waves and the velocity of the waves relative to the earth respectively With the east as the direction of the positive $\mathrm{x}$-axis we get

```{math}
v_{(bE)y}=v_{(bw)y}+v_{(wE)y}=(8\,\mathrm{km}/\mathrm{h})+(4\,\mathrm{km}/\mathrm{h}) \sin 45^{\circ } =10.83\,\mathrm{km}/\mathrm{h}
```

```{math}
v_{(bE)x}=v_{(wE)x}=(4\,\mathrm{km}/\mathrm{h}) \cos 45^{\circ } =2.83\,\mathrm{km}/\mathrm{h}
```

Hence

```{math}
v_{bE}=\sqrt{(v_{(bE)x})^{2}+(v_{(bE)y})^{2}}=\sqrt{(10.83\,\mathrm{km}/\mathrm{h})^{2}+(2.83\,\mathrm{km}/\mathrm{h})^{2}}=11.2\,\mathrm{km}/\mathrm{h}
```

The direction of $\mathbf{v}_{bE}$ is

```{math}
\theta =\tan ^{-1}\frac{(v_{bE})_{y}}{(v_{bE})_{x}}=\tan ^{-1}\frac{(10.83\,\mathrm{km}/\mathrm{h})}{(2.83\,\mathrm{km}/\mathrm{h})}=75.35^{\circ}
```

:::
````

```{figure} ../images/ch-02/459974_1_En_2_Fig29_HTML.png
:name: fig-2-29

A boat is traveling at 8 $\mathrm{km}/\mathrm{h}$ north relative to the sea’s waves, and the waves are traveling northeast relative to the earth at a constant speed of 4 $\mathrm{km}/\mathrm{h}$
```

```{figure} ../images/ch-02/459974_1_En_2_Fig30_HTML.png
:name: fig-2-30

$\mathrm{r}_{1}$ is a unit vector along the increasing r direction and $\theta _{1}$ is a unit vector in the direction of increasing $\theta$ (anticlockwise direction)
```

(sec-2-6)=
## 2.6 Motion in a Plane Using Polar Coordinates

Consider a particle moving in the x–y plane. A useful way to describe the position, velocity, and acceleration of the particle is by using its polar coordinates $(r,\theta )$. The relationship between the polar and rectangular coordinates is

```{math}
x=r\cos \theta
```

```{math}
y=r\sin \theta
```

where $\theta$ is measured from the positive $\mathrm{x}$- axis. Suppose a particle is located at $(r,\theta )$. If the particle moves in a straight line along the $r$ direction, then $\theta$ is constant through the motion of the particle. If the particle moves in a circle, then $r$ is constant. Let $\mathrm{r}_{1}$ be a unit vector along the increasing $r$ direction and $\theta _{1}$ to be a unit vector in the direction of increasing $\theta$ (anticlockwise direction). From [](#fig-2-30), we have

```{math}
\mathbf{r}_{1}=\cos \theta \mathbf{i}+\sin \theta \mathbf{j}
```

and

```{math}
\boldsymbol{\theta _{1}}=-\sin \theta \mathbf{i}+\cos \theta \mathbf{j}
```

Unlike the rectangular unit vectors, the polar unit vectors are not fixed in direction. Their direction changes as the particle moves along some path. Therefore, when finding the velocity and acceleration of a particle the derivatives of the polar unit vectors must be considered. The position vector of the particle is given by

```{math}
\mathbf{r}=r\mathbf{r}_{1}
```

To find the velocity in terms of the polar unit vectors let us differentiate $\mathbf{r}_{1}$ and $\boldsymbol{\theta _{1}}$ with respect to time. That gives

```{math}
\dot{\mathbf{r}}_{1}=\frac{d\mathbf{r}_{1}}{dt}=-\sin \theta \frac{d\theta }{dt}\mathbf{i}+\cos \theta \frac{d\theta }{dt}\mathbf{j}=\boldsymbol{\theta _{1}}\frac{d\theta }{dt}=\dot{\theta }\boldsymbol{\theta _{1}}
```

```{math}
\dot{\boldsymbol{\theta _{1}}}=\frac{d{\boldsymbol{\theta _{1}}}}{dt}=-\cos \theta \frac{d\theta }{dt} \mathbf{i}-\sin \theta \frac{d\theta }{dt}\mathbf{j}=-\mathbf{r}_{1}\frac{d\theta }{dt}=-\dot{\theta }\mathbf{r}_{1}
```

The velocity of the particle is given by

```{math}
\mathbf{v}=\frac{d\mathbf{r}}{dt}=\frac{d}{dt}(r\mathbf{r}_{1})=\frac{dr}{dt}\mathbf{r}_{1}+r\frac{d\mathbf{r}_{1}}{dt}=\dot{r}\mathbf{r}_{1}+r\dot{\mathbf{r}}_{1}=\dot{r}\mathbf{r}_{1}+r\dot{\theta }{\boldsymbol{\theta _{1}}}
```

Hence, the velocity is ([](#fig-2-31))

```{math}
:label: eq-2-21

\mathbf{v}=\dot{r}\mathbf{r}_{1}+r\dot{\theta }{\boldsymbol{\theta _{1}}}
```

We may write

```{math}
\mathbf{v}=v_{r}\mathbf{r}_{1}+v_{\theta }{\boldsymbol{\theta _{1}}}
```

```{figure} ../images/ch-02/459974_1_En_2_Fig31_HTML.png
:name: fig-2-31

Unlike the rectangular unit vectors, the polar unit vectors are not fixed in direction. Their direction changes as the particle moves along some path
```

where $v_{r}=\dot{r}$ and $v_{\theta }=r\dot{\theta }$ and $v=\sqrt{v_{r}^{2}+v_{\theta }^{2}}$. The total acceleration is

```{math}
\mathbf{a}=\frac{d\mathbf{v}}{dt}=\frac{d}{dt}(\dot{r}\mathbf{r}_{1}+r\dot{\theta }{\boldsymbol{\theta }_{1}})=\ddot{r}\mathbf{r}_{1}+\dot{r}\dot{\mathbf{r}}_{1}+\dot{r}\dot{\theta }{\boldsymbol{\theta }_{1}}+r\ddot{\theta }{\boldsymbol{\theta }_{1}}+r\dot{\theta }\dot{\boldsymbol{\theta }_{1}}
```

```{math}
=\ddot{r}\mathbf{r}_{1}+\dot{r}(\dot{\theta }\boldsymbol{\theta _{1}})+\dot{r}\dot{\theta }\boldsymbol{\theta _{1}}+r\ddot{\theta }\boldsymbol{\theta _{1}}+r\dot{\theta }(-\dot{\theta }\mathbf{r}_{1})
```

```{math}
:label: eq-2-22

\mathbf{a}=(\ddot{r}-r\dot{\theta }^{2})\mathbf{r}_{1}+(r\ddot{\theta }+2\dot{r}\dot{\theta })\boldsymbol{\theta _{1}}
```

or

```{math}
\mathbf{a}=a_{r}\mathbf{r}_{1}+a_{\theta }\boldsymbol{\theta _{1}}
```

where

```{math}
a_{r}=(\ddot{r}-r\dot{\theta }^{2})
```

and

```{math}
a_{\theta }=(r\ddot{\theta }+2\dot{r}\dot{\theta })
```

and

```{math}
a=\sqrt{a_{r}^{2}+a_{\theta }^{2}}
```

````{prf:example}
:label: example-2-20
:enumerator: 2.20

If a particle moves in a plane according to the expressions $\theta =0.3t+0.2t^{2}$ and $r=0.5t+0.4t^{2}$. Find its velocity and acceleration at $t=2\,\mathrm{s}$

:::{admonition} Solution 2.20
:class: dropdown

At $t=2\,\mathrm{s}$, $\theta =0.3t+0.2t^{2}=1.4$ rad, $\dot{\theta }=0.3+0.4t=1.1\,\mathrm{rad}/\mathrm{s}$ and $\ddot{\theta }=0.4\,\mathrm{rad}/\mathrm{s}^{2}$. Also $r=0.5t+0.4t^{2}=2.6\,\mathrm{m}$, $\dot{r}=0.5+0.8 t=2.1\,\mathrm{m}/\mathrm{s}$ and $\ddot{r}=0.8\,\mathrm{m}/\mathrm{s}^{2}$. Therefore

```{math}
v_{r}=\dot{r}=2.1\,\mathrm{m}/\mathrm{s}
```

```{math}
v_{\theta }=r\dot{\theta }=(2.6\,\mathrm{m})(1.1\,\mathrm{rad}/\mathrm{s})=2.9\,\mathrm{m}/\mathrm{s}
```

```{math}
v=\sqrt{v_{r}^{2}+v_{\theta }^{2}}=\sqrt{(2.1\,\mathrm{m}/\mathrm{s})^{2}+(2.9\,\mathrm{m}/\mathrm{s})^{2}}=3.6\,\mathrm{m}/\mathrm{s}
```

and

```{math}
a_{r}=\ddot{r}-r\dot{\theta }^{2}=(0.8\,\mathrm{m}/\mathrm{s}^{2})-(2.6\,\mathrm{m})(1.1\,\mathrm{rad}/\mathrm{s})^{2}=-2.35\,\mathrm{m}/\mathrm{s}^{2}
```

```{math}
a_{\theta }=r\ddot{\theta }+2\dot{r}\dot{\theta }=(2.6\,\mathrm{m})(0.4\,\mathrm{rad}/\mathrm{s}^{2})+2(2.1\,\mathrm{m}/\mathrm{s})(1.1\,\mathrm{rad}/\mathrm{s})=5.7\,\mathrm{m}/\mathrm{s}^{2}
```

```{math}
a=\sqrt{a_{r}^{2}+a_{\theta }^{2}}=\sqrt{(-2.35\,\mathrm{m}/\mathrm{s}^{2})^{2}+(5.7\,\mathrm{m}/\mathrm{s}^{2})^{2}}=6.2\,\mathrm{m}/\mathrm{s}^{2}
```

:::
````

```{figure} ../images/ch-02/459974_1_En_2_Fig32_HTML.png
:name: fig-2-32

An object moving in one dimension along the $\mathrm{x}$-axis
```

```{figure} ../images/ch-02/459974_1_En_2_Fig33_HTML.png
:name: fig-2-33

The position-time graph of a particle moving along the $\mathrm{x}$-axis
```

## Problems

```{exercise}
:label: prob-2-1
:enumerator: 2.1

A sports car moves around a circular track of radius of 100 $\mathrm{m}$. If the car makes one round in 75 $\mathrm{s}$, find the car’s (a) average speed (b) average velocity.
```

```{exercise}
:label: prob-2-2
:enumerator: 2.2

An object is moving in one dimension along the $\mathrm{x}$-axis according to [](#fig-2-32). Describe the motion of the object.
```

```{exercise}
:label: prob-2-3
:enumerator: 2.3

The position–time graph of a particle moving along the $\mathrm{x}$-axis is shown in [](#fig-2-33). Find (a) the average velocity between $\mathrm{a}$ and $\mathrm{b}$; (b) the instantaneous velocity at $\mathrm{a}$, $\mathrm{b}$, and $\mathrm{c}$.
```

```{exercise}
:label: prob-2-4
:enumerator: 2.4

A motorist drives along a straight-line road. His speed varies with time according to [](#fig-2-34). Sketch the position versus time and acceleration versus time graphs of the motorist.
```

```{exercise}
:label: prob-2-5
:enumerator: 2.5

A particle moves along the curve defined by $x=5e^{-t}$ and $y=\sin 5t$. Find the position, velocity and acceleration of the particle at any time.
```

```{exercise}
:label: prob-2-6
:enumerator: 2.6

A car moves at constant speed of 40 $\mathrm{km}/\mathrm{h}$ along the road shown in [](#fig-2-35). If the radius of curvature at A is 350 $\mathrm{m}$ and the total acceleration of the car at $\mathrm{B}$ is $1\,\mathrm{m}/\mathrm{s}^{2}$, find (a) the total acceleration of the car at A and $\mathrm{C}$; (b) the radius of curvature at B.(Hint: the radius of curvature at C is infinite).
```

```{exercise}
:label: prob-2-7
:enumerator: 2.7

A body with initial speed of 15 $\mathrm{m}/\mathrm{s}$ undergoes a uniform acceleration of $-2\,\mathrm{m}/\mathrm{s}^{2}$. Find the elapsed time and the distance it traveled when it reaches a speed of 3 $\mathrm{m}/\mathrm{s}$.
```

```{exercise}
:label: prob-2-8
:enumerator: 2.8

A stone is thrown downwards from a height of 10 $\mathrm{m}$. Find its initial speed if it reaches the ground after 1 s.
```

```{exercise}
:label: prob-2-9
:enumerator: 2.9

A block is thrown horizontally from the top of a cliff that is 30 $\mathrm{m}$ high with a speed of 10 $\mathrm{m}/\mathrm{s}$. Find (a) the block’s magnitude of displacement from the origin and its velocity after 1.5 $\mathrm{s}$; (b) the horizontal distance from the releasing point to where the block hits the ground.(Hint: the magnitude of displacement from the origin is $d=\sqrt{x^{2}+y^{2}}$).
```

```{exercise}
:label: prob-2-10
:enumerator: 2.10

A river has a uniform speed of 0.5 $\mathrm{m}/\mathrm{s}$ due east. If a boat travels east at a speed of 3 $\mathrm{m}/\mathrm{s}$ relative to the water, find the time it takes the boat to travel a distance of 1100 km and return to its starting point.
```

```{exercise}
:label: prob-2-11
:enumerator: 2.11

An aircraft is tracked by a radar (see [](#fig-2-36)). If at a certain instant the radar measurements give $r=7 \times 10^4 \,\mathrm{m}$, $\dot{r}=1000 \,\mathrm{m}/\mathrm{s}$, $\ddot{r}=7 \,\mathrm{m}/\mathrm{s}^{2}$, $\theta =45^{\circ}$, $\dot{\theta }=0.6 \,\mathrm{deg}/\mathrm{s}$, and $\ddot{\theta }=0.02 \,\mathrm{deg}/\mathrm{s}^{2}$. Find the velocity and acceleration of the airplane at that instant.
```

```{figure} ../images/ch-02/459974_1_En_2_Fig34_HTML.png
:name: fig-2-34

The speed of a motorcyclist varying with time
```

```{figure} ../images/ch-02/459974_1_En_2_Fig35_HTML.png
:name: fig-2-35

A car moves at a constant speed of 40 $\mathrm{km}/\mathrm{h}$ along curved path
```

```{figure} ../images/ch-02/459974_1_En_2_Fig36_HTML.png
:name: fig-2-36

An aircraft tracked by a radar coordinates
```
