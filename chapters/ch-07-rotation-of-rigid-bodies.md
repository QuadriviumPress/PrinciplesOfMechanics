---
title: 7. Rotation of Rigid Bodies
short_title: "Ch. 7 — Rotation"
label: ch-7
doi: 10.1007/978-3-030-15195-9_7
---

(sec-7-1)=
## 7.1 Rotational Motion

Rotational motion exists everywhere in the universe. The motion of electrons about an atom and the motion of the moon about the earth are examples of rotational motion. Objects cannot be treated as particles when exhibiting rotational motion since different parts of the object move with different velocities and accelerations. Therefore, it is necessary to treat the object as a system of particles.

(sec-7-2)=
## 7.2 The Plane Motion of a Rigid Body

When all parts of a rigid body move parallel to a fixed plane, then the motion of the object is referred to as plane motion. There are two types of plane motion, which are given as follows:
1. The pure rotational motion: The rigid body in such a motion rotates about a fixed axis that is perpendicular to a fixed plane. In other words, the axis is fixed and does not move or change its direction relative to an inertial frame of reference.
2. The general plane motion: The motion here can be considered as a combination of pure translational motion parallel to a fixed plane in addition to a pure rotational motion about an axis that is perpendicular to that plane. This chapter discusses the kinematics and dynamics of pure rotational motion.

(sec-7-2-1)=
### 7.2.1 The Rotational Variables

Suppose a rigid body of an arbitrary shape is in pure rotational motion about the $\mathrm {z}$-axis (see Fig. [](#fig-7-1)). Let us analyze the motion of a particle that lies in a slice of the body in the x-y plane as in Fig. [](#fig-7-2). This particle (at point P) will rotate in a circle of fixed radius *r* which represents the perpendicular distance from $\mathrm {P}$ to the axis of rotation. If you look at any other particle in the object you will see that every particle will rotate in its own circle that has the axis of rotation at its center. In other words, different particles move in different circles but the center of all of these circles lies on the rotational axis. Suppose the particle moves through an arc length *s* starting at the positive $\mathrm {x}$-axis. Its angular position is then given by
```{math}
\theta =\frac{s}{r}
```
*r* and $\theta$ are the polar coordinates of a point in a plane (which was mentioned in Sect. 2.6) where $\theta$ is always measured from the positive $\mathrm {x}$-axis. Because $\theta$ is the ratio of the arc length to the radius, it is a pure (dimensionless) number. The unit usually used to measure $\theta$ is the radians (rad). One radian is defined as the angle subtended by an arc of length that is equal to the radius of the circle. Since one rotation ($360^{\circ }$) corresponds to $\theta =2\pi r/r=2\pi$ rad, it follows that:
```{math}
1 \; \text {rev} =360^{\circ }=2\pi \; \text {rad}
```
```{math}
1 \; \text {rad} =57.3^{\circ }=0.159 \; \text {rev}
```
Note that if the particle completes one revolution, $\theta$ will not become zero again, it is then equal to $2\pi \mathrm {r}\mathrm {a}\mathrm {d}$. Thus for example for three revolutions the angular position is given by
```{math}
\theta =(2\pi +2\pi +2\pi ) \; \text {rad} =6\pi \; \text {rad}
```
Suppose that the particle in Fig. [](#fig-7-2) is at point $P_{1}$ at $t_{1}$ and at point $P_{2}$ at $t_{2}$ where it changes its angular position from $\theta _{1}$ to $\theta _{2}$ (see Fig. [](#fig-7-3)). Its angular displacement is then given by
```{math}
\triangle \theta =\theta _{2}-\theta _{1}
```
$\triangle \theta$ is positive for counterclockwise rotations (increasing $\theta$) and negative for clockwise rotations (decreasing $\theta$). If the particle undergoes this angular displacement during a time interval $\triangle t$, the average angular velocity $\overline{\omega }$ is then defined as
```{math}
\overline{\omega }=\frac{\theta _{2}-\theta _{1}}{t_{2}-t_{1}}=\frac{\triangle \theta }{\triangle t}
```
The instantaneous angular velocity is
```{figure} ../images/ch-07/459974_1_En_7_Fig1_HTML.png
:name: fig-7-1

A rigid body of an arbitrary shape is in pure rotational motion about the $\mathrm {z}$-axis
```
```{figure} ../images/ch-07/459974_1_En_7_Fig2_HTML.png
:name: fig-7-2

The motion of a particle that lies in a slice of the body in the x-y plane
```
```{figure} ../images/ch-07/459974_1_En_7_Fig3_HTML.png
:name: fig-7-3

The particle is at point $P_{1}$ at $t_{1}$ and at $P_{2}$ at $t_{2}$, where it changes its angular position from $\theta _{1}$ to $\theta _{2}$
```
```{math}
\omega =\lim _{\triangle t\rightarrow 0}\frac{\triangle \theta }{\triangle t}=\frac{d\theta }{dt}
```
$\omega$ has units of $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$ or $\mathrm {s}^{-1}$. The average angular acceleration is defined as
```{math}
\overline{\alpha }=\frac{\omega _{2}-\omega _{1}}{t_{2}-t_{1}}=\frac{\triangle \omega }{\triangle t}
```
The instantaneous angular acceleration is
```{math}
\alpha =\lim _{\triangle t\rightarrow 0}\frac{\triangle \omega }{\triangle t}=\frac{d\omega }{dt}
```
where $\alpha$ is in $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}$ or $\mathrm {s}^{-2}$. Note that $\omega$ is positive for increasing $\theta$ and negative for decreasing $\theta$, while $\alpha$ is positive for increasing $\omega$ and negative for decreasing $\omega$. When a rigid body is in pure rotational motion, all particles in the body rotate through the same angle during the same time interval. Thus, all particles have the same angular velocity and the same angular acceleration. Therefore, $\omega$ and $\alpha$ describes the motion of the whole body In the case of pure rotational motion, the direction of $\omega$ is along the axis of rotation (also see Sect. [](#sec-7-4)), it can be determined by the right-hand rule or of advance of a right-handed screw as in Fig. [](#fig-7-4). The direction of $\alpha$ is in the same direction of $\omega$ if $\omega$ is increasing or in the opposite direction if $\omega$ is decreasing.
The quantities $\theta , \omega$ and $\alpha$ in pure rotational motion are the rotational analog of *x*, *v* and *a* in translational one-dimensional motion. The vectors $\omega$ and $\alpha$ are not used in the case of pure rotational motion, they are used in the general rotational motion when the axis of rotation changes its direction with time. Note that only the infinitesimal angular displacement $d\theta$ can be represented by a vector but not the finite angular displacement $\triangle \theta$. This is because the finite angular displacement $\triangle \theta$ does not obey the commutative law of vector addition (see Fig. [](#fig-7-5)) and therefore cannot be represented by a vector. Hence, the instantaneous angular velocity and acceleration ($\omega$ and $\alpha$) can be represented by vectors but not their average values ($\overline{\omega }$ and $\overline{\alpha }$).
```{figure} ../images/ch-07/459974_1_En_7_Fig4_HTML.png
:name: fig-7-4

The direction of $\omega$ is along the axis of rotation and can be determined by the right-hand rule or of advance of a right-handed screw
```
```{figure} ../images/ch-07/459974_1_En_7_Fig5_HTML.png
:name: fig-7-5

Changing the order of addition will change the final result
```
````{prf:example}
:label: example-7-1
:enumerator: 7.1

Convert each of the following into the other angular units: $15^\circ$, 0.25 $\mathrm {r}\mathrm {e}\mathrm {v}/\mathrm {s}^{2}$, 3 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}.$

:::{admonition} Solution 7.1
:class: dropdown

```{math}
15^{\mathrm {o}}=(15 \; \displaystyle \mathrm {deg})\bigg (\frac{1 \; \mathrm {r}\mathrm {e}\mathrm {v}}{360 \; \mathrm {deg}}\bigg )=0.042 \; \text {rev}

```

```{math}
15^{\mathrm {o}}=(15 \; \displaystyle \mathrm {deg})\bigg (\frac{2 \; \pi \mathrm {r}\mathrm {a}\mathrm {d}}{360 \; \mathrm {deg}}\bigg )=0.26 \; \text {rad}

```

```{math}
0.25 \; \displaystyle \mathrm {r}\mathrm {e}\mathrm {v}/\mathrm {s}^{2}=\bigg (0.25 \; \frac{\mathrm {r}\mathrm {e}\mathrm {v}}{\mathrm {s}^{2}}\bigg )\bigg (\frac{2\pi \; \mathrm {r}\mathrm {a}\mathrm {d}}{1\mathrm {r}\mathrm {e}\mathrm {v}}\bigg )=1.57 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}

```

```{math}
0.25 \; \displaystyle \mathrm {r}\mathrm {e}\mathrm {v}/\mathrm {s}^{2}=\bigg (0.25 \; \frac{\mathrm {r}\mathrm {e}\mathrm {v}}{\mathrm {s}^{2}}\bigg )\bigg (\frac{360 \; \mathrm {deg}}{1\,\mathrm {r}\mathrm {e}\mathrm {v}}\bigg )=90 \; \mathrm {deg}/\mathrm {s}^{2}

```

```{math}
3\ \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}=\bigg (3 \; \frac{\mathrm {r}\mathrm {a}\mathrm {d}}{\mathrm {s}}\bigg )\bigg (\frac{1 \; \mathrm {r}\mathrm {e}\mathrm {v}}{2\pi \; \mathrm {r}\mathrm {a}\mathrm {d}}\bigg )=0.48 \; \mathrm {r}\mathrm {e}\mathrm {v}/\mathrm {s}

```

```{math}
3 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}=\bigg (3 \; \frac{\mathrm {r}\mathrm {a}\mathrm {d}}{\mathrm {s}}\bigg )\bigg (\frac{360^{\mathrm {o}} \; \mathrm {deg}}{2\pi \; \mathrm {r}\mathrm {a}\mathrm {d}}\bigg )=172 \; \mathrm {deg}/\mathrm {s}

```
:::
````

````{prf:example}
:label: example-7-2
:enumerator: 7.2

A rotating rigid object has an angular position given by $\theta (t)=((0.3)t^{2}+(0.4)t^{3})$ rad. Determine: (a) the angular displacement of the object and the average angular velocity during the time interval from $t_{1}=1\mathrm {s}$ to $t_{2}=2 \; \mathrm {s}$. (b) the instantaneous angular velocity and the instantaneous angular acceleration at $t=5 \; \mathrm {s}$.

:::{admonition} Solution 7.2
:class: dropdown

(a)

```{math}
\triangle \theta =\theta _{2}-\theta _{1}

```

```{math}
\theta _{1}=((0.3)(1 \; \mathrm {s})^{2}+(0.4)(1 \; \mathrm {s})^{3})=0.7 \; \text {rad}

```
and

```{math}
\theta _{2}=((0.3)(2 \; \mathrm {s})^{2}+(0.4)(2 \; \mathrm {s})^{3})=4.4 \; \text {rad}

```

```{math}
\triangle \theta =( 4.4 \; \text {rad})-(0.7\,\text {rad}) =3.7 \; \text {rad}

```

```{math}
\overline{\omega }=\frac{\triangle \theta }{\triangle t}=\frac{(3.7 \; \mathrm {r}\mathrm {a}\mathrm {d})}{(1 \; \mathrm {s})}=3.7 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}

```
(b)

```{math}
\omega =\frac{d\theta }{dt}=((0.6)t+(1.2)t^{2}) \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}

```
at $t=5 \; \mathrm {s}$

```{math}
\omega =(0.6)(5 \; \mathrm {s})+(1.2)(5 \; \mathrm {s})^{2}=33 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}

```

```{math}
\alpha =\frac{d\omega }{dt}=((0.6)+(2.4)t) \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}

```
at $t=5\mathrm {s}$

```{math}
\alpha =(0.6)+(2.4)(5 \; \mathrm {s})=12.6 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}

```
:::
````

````{prf:example}
:label: example-7-3
:enumerator: 7.3

A wheel is rotating with an angular acceleration that is given by $\alpha =(9-2t) \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}$. (a) Find the angular velocity and displacement at any time if at $t=0$ the wheel has an angular velocity of 2 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$ and an (initial) angular displacement of 3 rad; (b) at what angular displacement will the wheel reach its maximum angular velocity

:::{admonition} Solution 7.3
:class: dropdown

(a)

```{math}
\omega =\int \alpha dt=\int (9-2t)dt=9t-t^{2}+c_{1}

```
Since at $t=0$ $\omega =2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$, we have $c_{1}=2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$ and hence

```{math}
\omega =(9t-t^{2}+2) \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}

```

```{math}
\theta =\int \omega dt=\int (9t-t^{2}+2)dt=\frac{9}{2}t^{2}-\frac{1}{3}t^{3}+2t+c_{2}

```
Since at $t=0, \theta =3 \; \mathrm {r}\mathrm {a}\mathrm {d}$, then $c_{2}=3$ rad and

```{math}
\displaystyle \theta =\bigg (\frac{9}{2}t^{2}-\frac{1}{3}t^{3}+2t+3 \bigg ) \; \text {rad}

```
(b) The maximum velocity is when $\alpha =d\omega /dt=0$, or $9-2t=0$, i.e. at $t=4.5 \; \mathrm {s}$ The angular displacement at that time is

```{math}
\displaystyle \theta =\frac{9}{2}(4.5 \; \mathrm {s})^{2}-\frac{1}{3}(4.5 \; \mathrm {s})^{3}+2(4.5 \; \mathrm {s})+3=72.8 \; \text {rad}

```
:::
````

A pure rotational motion with constant angular acceleration is the rotational analogue of the pure translational motion with constant acceleration. The corresponding kinematic equations of pure rotational motion can be obtained by using the same method that is used for obtaining the kinematic equations of pure translational motion. To show this, consider a rigid object rotating with a constant angular acceleration during a time interval from $t_{1}$ to $t_{2}$ through an angle from $\theta _{1}$ to $\theta _{2}$. Let $t_{1}=0, t_{2}=t, \omega _{1}=\omega _{\mathrm {o}}, \omega _{2}=\omega , \theta _{1}=\theta _{\mathrm {o}}$, and $\theta _{2}=\theta .$ Because the angular acceleration is constant it follows that the angular velocity changes linearly with time and the average angular velocity is given by
```{math}
\overline{\omega }=\frac{\omega _{0}+\omega }{2}
```
Since
```{math}
\alpha =\overline{\alpha }=\frac{\omega _{2}-\omega _{1}}{t_{2}-t_{1}}=\frac{\omega -\omega _{0}}{t}
```
we have
```{math}
\begin{aligned} \omega =\omega _{0}+\alpha t \end{aligned}
```
Furthermore
```{math}
\overline{\omega }=\frac{\theta _{2}-\theta _{1}}{t_{2}-t_{1}}=\frac{\theta -\theta _{0}}{t}=\frac{\omega _{0}+\omega }{2}
```
Hence
```{math}
\begin{aligned} \displaystyle \theta =\theta _{0}+\frac{1}{2}(\omega _{0}+\omega )t \end{aligned}
```
Substituting Eq. 7.1 into Eq. 7.2 gives
```{math}
\theta =\theta _{0}+\frac{1}{2}(\omega _{0}+\omega )t=\theta _{0}+\frac{1}{2}(\omega _{0}+\omega _{0}+\alpha t)t
```
or
```{math}
\begin{aligned} \displaystyle \theta =\theta _{0}+\omega _{0}t+\frac{1}{2}\alpha t^{2} \end{aligned}
```
Finally solving for *t* from Eq. 7.1 and substituting into Eq. 7.2 gives
```{math}
\theta =\theta _{0}+\frac{1}{2}(\omega _{0}+\omega )t=\theta _{0}+\frac{1}{2}(\omega _{0}+\omega )\left( \frac{\omega -\omega _{0}}{\alpha }\right)
```
or
```{math}
\begin{aligned} \omega ^{2}=\omega _{0}^{2}+2\alpha (\theta -\theta _{0}) \end{aligned}
```
Note that as mentioned earlier, if a rigid object is in pure rotational motion, all particles in the object have the same angular velocity and angular acceleration. Different particles move in different circles but the center of these circles lies at the axis of rotation. As the rigid body rotates, a particle in the body will move through a distance *s* along its circular path (see Fig. [](#fig-7-6)). The angular displacement of the particle is related to *s* by
```{math}
s=r\theta
```
where *r* is the radius of the circle in which the particle is moving along. Differentiating the above equation with respect to *t* gives
```{math}
\frac{ds}{dt}=r\frac{d\theta }{dt}
```
Since *ds* / *dt* is the magnitude of the linear velocity of the particle and $d\theta /dt$ is the angular velocity of the body we may write
```{math}
\begin{aligned} v=r\omega \end{aligned}
```
Therefore, the farther the particle is from the rotational axis the greater its linear speed. The direction of the linear speed of the particles is always tangent to the path (as mentioned in Sect. 2.2.3). In Sect. 2.4.6 we have seen that a particle in nonuniform circular motion has both tangential and radial components of acceleration. The radial component is due to the change in the direction of the velocity and is given by
```{math}
\begin{aligned} a_{r}=\displaystyle \frac{v^{2}}{r} \end{aligned}
```
Substituting Eq. 7.5 into Eq. 7.6 gives
```{math}
a_{r}=\frac{v^{2}}{r}=r\omega ^{2}
```
The tangential component of the acceleration is due to the change in the magnitude of the velocity and it is given by
```{math}
a_{t}=\frac{dv}{dt}=r\frac{d\omega }{dt}
```
or
```{math}
a_{t}=r\alpha
```
The total linear acceleration of the particle (see Fig. [](#fig-7-7)) is given by
```{math}
\mathbf {a}=\mathbf {a}_t+\mathbf {a}_r
```
It’s magnitude is given by
```{math}
a=\sqrt{{a_t}^2+{a_r}^2}=\sqrt{{r}^2{\alpha }^2+{r}^2{\omega }^4}=r\sqrt{{\alpha }^2+{\omega }^4}
```
Table. 7.1 shows the linear/rotational analogous equations.
```{figure} ../images/ch-07/459974_1_En_7_Fig6_HTML.png
:name: fig-7-6

As the rigid body rotates, a particle in the body will move through a distance *s* along its circular path
```
```{figure} ../images/ch-07/459974_1_En_7_Fig7_HTML.png
:name: fig-7-7

The total acceleration of the particle
```
| Rotational motion about a fixed axis with constant $\alpha$ | Linear motion with constant *a* |
| --- | --- |
| $\omega =\omega _{0}+\alpha t$ | $v=v_{0}+at$ |
| $\displaystyle \theta =\theta _{0}+\frac{1}{2}(\omega +\omega _{0})t^{}$ | $x=x_{0}+\displaystyle \frac{1}{2}(v+v)t_{}$ |
| $\displaystyle \theta =\theta _{0}^{}+\omega _{0}t+\frac{1}{2}\alpha t^{2}$ | $x=x_{0}+v_{0}t_{}+\displaystyle \frac{1}{2}at^{2}$ |
| $\omega ^{2}=\omega _{0}^{2}+2\alpha (\theta -\theta _{0})$ | $v^{2}=v_{0}^{2}+2a(x-x_{0})$ |

````{prf:example}
:label: example-7-4
:enumerator: 7.4

A disc of radius of 10 cm rotates from rest with a constant angular acceleration. If it requires 2 $\mathrm {s}$ for it to rotate through an angular displacement of $60^{\mathrm {o}}$: (a) find the angular acceleration of the disc; (b) its angular velocity at $t=2\mathrm {s}$ and at $t=6\mathrm {s}, (\mathrm {c})$ the linear speed at $t=2\mathrm {s}$ of a point that is at a distance of 7 cm from the center of the disc; (d) the distance that this point has moved during that time interval.

:::{admonition} Solution 7.4
:class: dropdown

(a) We have $\omega _{0}=0$ and $\theta =(60\;\mathrm {deg})(2\pi \mathrm {r}\mathrm {a}\mathrm {d}/360\;\mathrm {deg})=1.05$ rad. By choosing the reference position $\theta _{0}=0$ we have

```{math}
\theta =\theta _{0}+\omega _{0}t+\frac{1}{2}\alpha t^{2}
```

```{math}
\alpha =\frac{2\theta }{t^{2}}=\frac{2(1.05 \; \mathrm {r}\mathrm {a}\mathrm {d})}{(2 \; \mathrm {s})^{2}}=0.525 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}
```

(b)

```{math}
\omega =\omega _{0}+\alpha t=(0.525 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2})(2 \; \mathrm {s})=1.05 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

at $t=6 \; \mathrm {s}$

```{math}
\omega =(0.525 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2})(6\mathrm {s})=3.15 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

(c)

```{math}
v=r\omega =(0.07 \; \mathrm {m})(1.05 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})=0.074 \; \mathrm {m}/\mathrm {s}
```

(d)

```{math}
s=r\theta =(0.07 \; \mathrm {m})(1.05 \; \mathrm {rad} ) =0.074 \; \mathrm {m}
```
:::
````

````{prf:example}
:label: example-7-5
:enumerator: 7.5

Two sprockets are attached to each other as in Fig. [](#fig-7-8). There radii are $r_{1}= 2$ cm and $r_{2}=5$ cm. If the angular velocity of the smaller sprocket is 2 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s},$ find the angular velocity of the other.

:::{admonition} Solution 7.5
:class: dropdown

A point at the rim of one sprocket has the same linear speed as a point at the rim of the other sprocket since they are attached to each other, i.e.,

```{math}
r_{1}\omega _{1}=r_{2}\omega _{2}=v
```

hence

```{math}
\omega _{2}=\frac{r_{1}}{r_{2}}\omega _{1}=\frac{(2 \; \mathrm {c}\mathrm {m})}{(5 \; \mathrm {c}\mathrm {m})}(2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})=0.8 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```
:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig8_HTML.png
:name: fig-7-8

Two sprockets connected at the rim
```

````{prf:example}
:label: example-7-6
:enumerator: 7.6

Find the angular speed of the moon in its orbit about the earth in rev/day.

:::{admonition} Solution 7.6
:class: dropdown

Assuming that the moon’s orbit is circular, the linear speed of the moon is given by $v=2\pi r/T$, where *r* is the mean distance from the earth to the moon and *T* is its period. Thus, the angular velocity of the moon is

```{math}
\displaystyle \omega =rv=\frac{2\pi }{T}=\frac{2(3.14)}{(27.3 \; \mathrm {d}\mathrm {a}\mathrm {y})}=0.23 \; \text {rad/day}
```

or

```{math}
\displaystyle \omega = \bigg (0.23 \; \frac{\mathrm {r}\mathrm {a}\mathrm {d}}{\mathrm {d}\mathrm {a}\mathrm {y}}\bigg ) \bigg (\frac{1 \; \mathrm {r}\mathrm {e}\mathrm {v}}{2\pi \; \mathrm {r}\mathrm {a}\mathrm {d}}\bigg )=0.037 \; \text {rev/day}
```
:::
````

(sec-7-4)=
## 7.4 Vector Relationship Between Angular and Linear Variables

Consider a rigid body in pure rotational motion about a fixed axis (for example the $\mathrm {z}$-axis). For any particle in the object, its linear velocity is given by
```{math}
v=r\omega =R\sin \theta \omega
```
where $\mathrm {R}$ is the position vector of the particle from the origin (see Fig. [](#fig-7-9)) and $\theta$ is the angle between the position vector and the $\mathrm {z}$-axis. As shown in Fig. [](#fig-7-9), the direction of $\mathrm {y}$ is perpendicular to the plane formed by $\omega$ and $\mathrm {R}$ where it can be verified using the right-hand rule. Therefore, by using the definition of vector product we may write
```{math}
\begin{aligned} \mathbf {v}=\boldsymbol{\omega }\times \mathbf {R} \end{aligned}
```
The total linear acceleration is
```{math}
\mathbf {a}=\frac{d\mathbf {v}}{dt}=\frac{d}{dt}(\boldsymbol{\omega }\times \mathbf {R})
```
From Sect. 1.9.1 $(d/dt(\mathbf {A}\times \mathbf {B})=\mathbf {A}\times d\mathbf {B}/dt+d\mathbf {A}/dt\times \mathbf {B})$ we have
```{math}
\mathbf {a}=\frac{d \boldsymbol{\omega }}{dt}\times \mathbf {R}+\boldsymbol{\omega }\times \frac{d\mathbf {R}}{dt}
```
```{math}
=\boldsymbol{\alpha }\times \mathbf {R}+\boldsymbol{\omega }\times \mathbf {v}
```
```{math}
|\boldsymbol{\alpha }\times \mathbf {R}|=\alpha R\sin \theta =r\alpha =a_{t}
```
Furthermore, the direction of $\boldsymbol{\alpha }\times \mathbf {R}$ is tangent to the circular path of the particle at any instant (see Fig. [](#fig-7-9)). Thus the quantity $\boldsymbol{\alpha }\times \mathbf {R}$ is just the tangential component of the total acceleration
```{math}
\begin{aligned} \mathbf {a_{t}}=\boldsymbol{\alpha }\times \mathbf {R} \end{aligned}
```
In addition
```{math}
|\boldsymbol{\omega }\times \mathbf {v}|=\omega v\sin 90^{\mathrm {o}}=\omega v=r\omega ^{2}=a_{r}
```
The direction of $\boldsymbol{\omega }\times \mathbf {v}$ is along the direction of $\mathrm {r}$ (radial direction). Hence, the quantity $\boldsymbol{\omega }\times \mathbf {v}$ is the radial component of the total acceleration
```{math}
\begin{aligned} \mathbf {a}_{r}=\boldsymbol{\omega }\times \mathbf {v} \end{aligned}
```
Equations 7.7–7.9 are the vector relationship between angular and linear quantities.
```{figure} ../images/ch-07/459974_1_En_7_Fig9_HTML.png
:name: fig-7-9

A rigid body in pure rotational motion about a fixed axis (here the $\mathrm {z}$-axis)
```

(sec-7-5)=
## 7.5 Rotational Energy

In Chap. 6 we have seen that the kinetic energy of a discrete system of particles is $K=\displaystyle \frac{1}{2}\sum _{i}m_{i}v_{i}^{2}$ where $m_{i}$ and $v_{i}$ are the mass and linear velocity of the *i*th particle respectively (see Fig. [](#fig-7-10)). From Eq. 7.5, we have
```{math}
v_{i}=r_{i}\omega
```
where $r_{i}$ is the perpendicular distance from the particle to the axis of rotation. Therefore the total kinetic energy of the system is
```{math}
K_{R}=\frac{1}{2}\sum _{i}(m_{i}r_{i}^{2})\omega ^{2}
```
The quantity between brackets is known as the moment of inertia of the system
```{math}
I=\sum _{i}m_{i}r_{i}^{2}
```
This quantity shows how the mass of the system is distributed about the axis of rotation. Thus, to find the rotational inertia, the axis of rotation must be specified. If the rotational axis changes its position or direction, *I* changes as well. The SI unit of the moment of inertia is kg $\mathrm {m}^{2}$. The rotational kinetic energy can thus be written as
```{math}
K_{R}=\frac{1}{2}I\omega ^{2}
```
This quantity is the rotational analogue of the kinetic energy in translational motion. Note that this energy is not a new kind of energy; it is just the sum of the translational kinetic energies of the particles. For a rigid body which is a continuous system of particles, the sum is replaced by an integral
```{math}
I=\lim _{\triangle m_{\mathrm {i}\rightarrow 0}}\sum _{i}m_{i}r_{i}^{2}=\int r^{2}dm
```
In solving problems $\rho , \sigma$, and $\lambda$ (see Sect. 6.3.4) are often used to express *dm* in terms of its position coordinates.
```{figure} ../images/ch-07/459974_1_En_7_Fig10_HTML.png
:name: fig-7-10

A system of particles rotating about the z-axis
```

(sec-7-6)=
## 7.6 The Parallel-Axis Theorem

The parallel-axis theorem states that the moment of inertia *I* of a system about any axis that is parallel to an axis passing through the center of mass is
```{math}
I=I_{cm}+MD^{2}
```
where $I_{cm}$ is the moment of inertia about an axis passing through the center of mass, *M* is the total mass of the system, and *D* is the perpendicular distance between the two parallel axes.
```{figure} ../images/ch-07/459974_1_En_7_Fig11_HTML.png
:name: fig-7-11

The Parallel-axis Theorem
```

Proof
Consider an axis that is perpendicular to the page and passing through the center of mass of the object. Figure [](#fig-7-11) shows a thin slice of the object that lies in the x-y plane. Because the origin is taken at the center of mass we have
```{math}
z_{cm}=x_{cm}=y_{cm}=0
```
The moment of inertia of the object about the center of mass axis is
```{math}
I_{cm}=\int r^{2}dm=\int (x^{2}+y^{2})dm
```
where *x* and *y* are the coordinates of the mass element *dm* from the center of mass (the origin). Now consider another axis that is parallel to the first axis and that passes through a point $\mathrm {P}$ as shown in Fig. [](#fig-7-11). Suppose that the $\mathrm {x}$ and $\mathrm {y}$ coordinates of $\mathrm {P}$ from the center of mass are $x_{p}$ and $y_{p}$. The moment of inertia about an axis passing through $\mathrm {P}$ is
```{math}
I_{P}=\int [(x-x_{P})^{2}+(y-y_{P})^{2}]dm
```
where $(x-x_{P})$ and $(y-y_{P})$ are coordinates of *dm* from point P Expanding this equation gives
```{math}
I_{P}=\int (x^{2}+y^{2})dm-2x_{P}\int xdm-2y_{P}\int ydm+\int (x_{P}^{2}+y_{P}^{2})dm
```
Since $x_{cm}=y_{cm}=0$ and since
```{math}
x_{cm}=\frac{1}{M}\int xdm
```
and
```{math}
y_{cm}=\frac{1}{M}\int ydm
```
it follows that the second and third terms are zero. Thus
```{math}
I_{P}=I_{cm}+D^{2}\int dm
```
where
```{math}
D=\sqrt{(x_{P}^{2}+y_{P}^{2})}
```
is the perpendicular distance between the two parallel axes. Hence
```{math}
I_{P}=I_{cm}+MD^{2} \quad \text {(Parallel--Axis Theorem)}
```

**Special Moment of Inertia** Fig. [](#fig-7-12) gives the rotational inertia of various rigid bodies of uniform density.
```{figure} ../images/ch-07/459974_1_En_7_Fig12_HTML.png
:name: fig-7-12

The rotational inertia of various rigid bodies of uniform density
```

(sec-7-7)=
## 7.7 Angular Momentum of a Rigid Body Rotating about a Fixed Axis

Consider a rigid body rotating about a fixed axis (the $\mathrm {z}$-axis) with an angular speed $\omega$ as shown in Fig. [](#fig-7-13). The angular momentum of the ith particle with respect to the origin is given by
```{math}
\mathbf {L}_{i}=\mathbf {R}_{i}\times \mathbf {p}_{i}
```
```{figure} ../images/ch-07/459974_1_En_7_Fig13_HTML.png
:name: fig-7-13

A rigid body rotating about a fixed axis (the $\mathrm {z}$-axis) with an angular speed $\omega$
```

Since the angle between $\mathbf {R}_{i}$ and $\mathbf {p}_{i}$ is 90, then $L_{i}=R_{i}p_{i}$. As seen from Fig. [](#fig-7-13), $\mathbf {L}_{i}$ is not parallel to $\boldsymbol{\omega }$. $\mathbf {L}_{i}$ can be analyzed to two components, $\mathrm {a}$ component parallel to $\boldsymbol{\omega }$ written $(\mathbf {L}_{iz})$ and a component perpendicular to $\boldsymbol{\omega }$, $(\mathbf {L}_{i\perp })$. The magnitude of $\mathbf {L}_{iz}$ is given by
```{math}
L_{iz}=L_{i}\sin \theta =R_{i}p_{i}\sin \theta =R_{i} ({ m_{i} v_{i}}) \sin \theta
```
```{math}
=R_{i}m_{i}(r_{i}\omega )\sin \theta =m_{i}r_{i}^{2}\omega
```
where $r_{i}$ is the radius of the circle in which the particle is moving along and $R_{i}=r_{i}\sin \theta$. Therefore, the total angular momentum of the rigid body along the $\mathrm {z}$-direction is
```{math}
L_{z}=\sum _{i}m_{i}r_{i}^{2}\omega =\bigg (\sum _{i}m_{i}r_{i}^{2}\bigg )\omega
```
```{math}
L_{z}=I\omega
```
where *I* is the moment of inertia of the rigid body about the rotational axis (z-axis). This equation can also be written in component form since $\mathbf {L}_{z}$ is parallel to $\boldsymbol{\omega }$, that is,
```{math}
\begin{aligned} \mathbf {L}_{z}=I\boldsymbol{\omega } \end{aligned}
```
Therefore, if a rigid body is rotating about a fixed axis (say the $\mathrm {z}$-axis), the component of the angular momentum along that axis is given by Eq. 7.10. Now suppose that the rigid body is symmetric and homogeneous and that it is rotating about its symmetrical axis (see Fig. [](#fig-7-14)). For any two particles (1 and 2) opposing each other with an equal angular momenta $\mathbf {L}_{1}$ and $\mathbf {L}_{2}$, the perpendicular components, $\mathbf {L}_{1\perp }$ and $\mathbf {L}_{2\perp }$, of the angular momenta cancel each other out since they are in opposite directions. That leaves the parallel components $\mathbf {L}_{1z}$ and $\mathbf {L}_{2z}$ which add up since they have the same direction. For all particles in the object the total angular momentum is, therefore, given by
```{math}
\mathbf {L}=\sum _{i}\mathbf {L}_{iz}=\mathbf {L}_{z}=I\boldsymbol{\omega }
```
Hence, the total angular momentum of a symmetrical homogeneous body in pure rotation about its symmetrical axis is given by
```{math}
\begin{aligned} \mathbf {L}=I\boldsymbol{\omega } \end{aligned}
```
Note that Eq. 7.10 is valid for any rigid object in pure rotation where it only gives the component of the angular momentum that is parallel to the rotational axis. On the other hand, Eq. 7.11 is valid only for a symmetrical homogeneous rigid object rotating about its symmetrical axis, where the angular momentum in the equation is the total angular momentum and it is directed along the axis of rotation. The net external torque acing on the rigid object is equal to the rate of change of the total angular momentum of the object, i.e.,
```{math}
\Sigma {\boldsymbol{\tau }_{ext}}=\frac{d\mathbf {L}}{dt}
```
In the case of any rigid object symmetrical or not, the net external torque acting on the object about the axis of rotation (say the $\mathrm {z}$-axis) is equal to the rate of change of the component of angular momentum that is along that axis
```{math}
\Sigma {\boldsymbol{\tau }_{extz}}=\frac{d\mathbf {L}_{z}}{dt}=\frac{d(I\boldsymbol{\omega })}{dt}=I\boldsymbol{\alpha }
```
However, if the object is symmetric and homogeneous in pure rotation about its symmetrical axis we may write
```{math}
\Sigma {\boldsymbol{\tau }_{ext}}=\frac{d\mathbf {L}}{dt}=\frac{d(I\boldsymbol{\omega })}{dt}=I\boldsymbol{\alpha }
```
```{figure} ../images/ch-07/459974_1_En_7_Fig14_HTML.png
:name: fig-7-14

A homogenous symmetrical rigid body rotating about its symmetrical axis
```

````{prf:example}
:label: example-7-7
:enumerator: 7.7

A 5 kg wheel of radius of 0.1 $\mathrm {m}$ decelerates from an angular speed of 5 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$ to rest after going through an angular displacement of 10 rev If a frictional force causes the wheel to decelerate, find the torque due to this force.

:::{admonition} Solution 7.7
:class: dropdown

The angular displacement is

```{math}
\triangle \theta =( 10 \; \mathrm {rev}) \bigg (\displaystyle \frac{2\pi \; \mathrm {r}\mathrm {a}\mathrm {d}}{1 \; \mathrm {r}\mathrm {e}\mathrm {v}}\bigg )=62.8 \; \text {rad}
```

The angular acceleration of the wheel is

```{math}
\alpha =\frac{\omega ^{2}-\omega _{0}^{2}}{2\triangle \theta }=\frac{0-(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}}{2(62.8 \; \mathrm {r}\mathrm {a}\mathrm {d})}=-0.2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

The external torque is

```{math}
\tau =I\alpha =MR^{2}\alpha =(5 \; \mathrm {k}\mathrm {g})(0.1 \; \mathrm {m})^{2}(-0.2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2})=-0.01 \; \mathrm {N}\,\mathrm {m}
```
:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig15_HTML.png
:name: fig-7-15

Three masses connected by massless rods
```

````{prf:example}
:label: example-7-8
:enumerator: 7.8

Three masses are connected by massless rods as in Fig. [](#fig-7-15). If $m=0.1 \; \mathrm {k}\mathrm {g},$ find the moment of inertia of the system and the corresponding kinetic energy if it rotates with an angular speed of 5 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$ about: (a) the $\mathrm {z}$-axis; (b) the $\mathrm {y}$-axis and; (c) the $\mathrm {x}$-axis $(a=0.2 \; \mathrm {m})$.

:::{admonition} Solution 7.8
:class: dropdown

(a)

```{math}
\begin{aligned} I_{z}&amp;=\displaystyle \sum _{i}m_{i}r_{i}^{2}=2ma^{2}+\frac{m}{2}a^{2}+ma^{2}=\frac{7}{2}ma^{2}\\&amp;=\frac{7}{2}(0.1 \; \mathrm {k}\mathrm {g})(0.2 \; \mathrm {m})^{2}=0.014 \; \mathrm {kg\, m^2} \end{aligned}
```

```{math}
K_{R}=\frac{1}{2}I_{z}\omega ^{2}=\frac{1}{2}(0.014 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}=0.175 \; \mathrm {J}
```

(b)

```{math}
I_{y}=\displaystyle \frac{m}{2}a^{2}+2ma^{2}=\frac{5}{2}ma^{2}=\frac{5}{2}(0.1 \; \mathrm {k}\mathrm {g})(0.2 \; \mathrm {m})^{2}=0.01 \; \mathrm {kg\, m^2}
```

```{math}
K_{R}=\frac{1}{2}I_{y}\omega ^{2}=\frac{1}{2}(0.01 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}=0.125 \; \mathrm {J}
```

(c)

```{math}
I_{x}=ma^{2}=(0.1 \; \mathrm {k}\mathrm {g})(0.2 \; \mathrm {m})^{2}=4\times 10^{-3} \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}
```

```{math}
K_{R}=\frac{1}{2}I_{x}\omega ^{2}=\frac{1}{2}(4\times 10^{-3} \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}=0.05 \; \mathrm {J}
```
:::
````

````{prf:example}
:label: example-7-9
:enumerator: 7.9

Fig. [](#fig-7-16) shows a uniform thin rod of mass *M* and length *L*. Find the moment of inertia of the rod about an axis that is perpendicular to it and passing through: (a) the center of mass; (b) at one end; (c) at a distance of *L* / 6 from one end.

:::{admonition} Solution 7.9
:class: dropdown

(a) The mass *dm* of an element in the rod is

```{math}
dm=\lambda dx=\bigg (\frac{M}{L}\bigg )dx
```

```{math}
I_{cm}=I_{y}=\displaystyle \int r^{2}dm=\int _{x=-\frac{L}{2}}^{\frac{L}{2}}x^{2}\bigg (\frac{M}{L}\bigg )dx=\frac{M}{L}\bigg (\frac{x^{3}}{3}\bigg ) \bigg |_{-L/2}^{L/2}=\displaystyle \frac{1}{12}ML^{2}
```

(b)

```{math}
I_{y'}=I_{cm}+MD^{2}=\frac{1}{12}ML^{2}+M\bigg (\frac{L}{2}\bigg )^{2}=\frac{1}{3}ML^{2}
```

(c)

```{math}
I_{y''}=I_{cm}+MD^{2}=\frac{1}{12}ML^{2}+M\bigg (\frac{L}{2}-\frac{L}{6}\bigg )^{2}=\frac{7}{36}ML^{2}
```
:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig16_HTML.png
:name: fig-7-16

A uniform thin rod of mass *M* and length *L*
```

````{prf:example}
:label: example-7-10
:enumerator: 7.10

Fig. [](#fig-7-17) shows a uniform thin plate of mass *M* and surface density $\sigma$. Find the moment of inertia of the plate about an axis passing through its center of mass if its length is *b* and its width is *a* (the $\mathrm {z}$-axis).

:::{admonition} Solution 7.10
:class: dropdown

A mass element *dm* has an area *dxdy* and is at a distance $r=\sqrt{x^{2}+y^{2}}$ from the axis of rotation. Therefore, we have

```{math}
I_{cm}=\int r^{2}dm=\int r^{2}\sigma dA=\int _{y=-a/2}^{a/2}\int _{y=-b/2}^{b/2}{(x^{2}+y^{2})\bigg (\frac{M}{ab}\bigg )dxdy}
```

```{math}
=\displaystyle \frac{M}{ab} \int _{y=-a/2}^{a/2} {{\bigg (\frac{x^3}{3}+xy^2\bigg )|_{x=-b/2}^{b/2}}dy}=\frac{M}{ab} \int _{y=-a/2}^{a/2} {{\bigg (\frac{b^3}{12}+by^2\bigg )}dy}
```

```{math}
=\displaystyle \frac{M}{ab} \bigg (\frac{b^3y}{12}+\frac{y^3b}{3}\bigg ) \bigg |_{x=-a/2}^{a/2}=\frac{M}{ab} \bigg [\frac{ab^3}{12}+\frac{ab^3}{12}\bigg ]=\frac{1}{12}M\big (a^2+b^2\bigg )
```
:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig17_HTML.png
:name: fig-7-17

A uniform thin plate of mass *M* and surface density $\sigma$
```

````{prf:example}
:label: example-7-11
:enumerator: 7.11

Find the moment of inertia of a uniform solid cylinder of radius *R*, length *L* and mass *M* about its axis of symmetry.

:::{admonition} Solution 7.11
:class: dropdown

:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig18_HTML.png
:name: fig-7-18

Calculating the moment of inertia of a uniform solid cylinder with the volume element defined in different ways
```

````{prf:example}
:label: example-7-12
:enumerator: 7.12

Three rods of length *L* and mass *M* are connected together as in Fig. [](#fig-7-19). Determine the moment of inertia of the system about an axis passing through $\mathrm {O}$ and perpendicular to the page (the rods lie in the same plane).

:::{admonition} Solution 7.12
:class: dropdown

The moment of inertia of a thin rod about an axis that is perpendicular to it and passing through one end is $1/3ML^{2}$. The total moment of inertia at $\mathrm {O}$ is the sum of the moment of inertias of the rods, i.e.,

```{math}
I=I_{1}+I_{2}+I_{3}=3\bigg (\frac{1}{3}ML^{2}\bigg )=ML^{2}
```
:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig19_HTML.png
:name: fig-7-19

Three rods of length *L* and mass *M* are connected together
```

````{prf:example}
:label: example-7-13
:enumerator: 7.13

Find the moment of inertia of a spherical shell of radius *R* and mass *M* about an axis passing through its center of mass.

:::{admonition} Solution 7.13
:class: dropdown

Let us divide the spherical shell into thin rings each of area (see Fig. [](#fig-7-20)) given by

```{math}
dA=2\pi R\sin \theta Rd\theta =2\pi R^{2}\sin \theta d\theta
```

```{math}
I=\int r^{2}dm=\int R^{2}\sin ^{2}\theta \sigma 2\pi R^{2}\sin \theta d\theta
```

since $\sigma =M/4\pi R^{2}$, we have

```{math}
I=\frac{M}{2}R^{2}\int _{\theta =0}^{\pi }\sin ^{3}\theta d\theta =\frac{M}{2}R^{2}\int _{\theta =0}^{\pi }(1-\cos ^{2}\theta )\sin \theta d\theta
```

```{math}
=\frac{M}{2}R^{2}\bigg [-\cos \theta +\frac{\cos ^{3}\theta }{3}\bigg ]_{\theta =0}^{\pi }=\frac{2}{3}MR^{2}
```
:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig20_HTML.png
:name: fig-7-20

A spherical shell divided into thin rings
```

(sec-7-8)=
## 7.8 Conservation of Angular Momentum of a Rigid Body Rotating About a Fixed Axis

In Chap. 5 we have seen that if the net external torque acting on a system of particles relative to an origin is zero then the total angular momentum of the system about that origin is conserved
```{math}
\mathbf {L}_{i}=\mathbf {L}_{f}= \mathrm{constant~(isolated~system)}
```
In the case of a rigid object in pure rotational motion, if the component of the net external torque about the rotational axis (say the $\mathrm {z}$-axis) is zero then the component of angular momentum along that axis is conserved, i.e., if
```{math}
\tau _{z}=\frac{dL_{z}}{dt}=0
```
then
```{math}
I_{i}\omega _{i}=I_{f}\omega _{f}
```
That is, the angular momentum is not necessarily conserved in all directions. It is conserved in the direction where the net external torque is equal to zero.

(sec-7-9)=
## 7.9 Work and Rotational Energy

Consider a rigid body rotating about a fixed axis as in Fig. [](#fig-7-21). If a force that lies in the x-y plane is applied to the body at $\mathrm {P}$, then the work done on the body if it rotates through an angle $d\theta$ is
```{math}
dW=\mathbf {F}\cdot d\mathbf {s}=\mathbf {F}\cdot \frac{d\mathbf {s}}{dt}dt=\mathbf {F}\cdot \mathbf {v} dt=\mathbf {F}\cdot (\boldsymbol{\omega }\times \mathbf {r})dt
```
```{math}
=(\mathbf {r}\times \mathbf {F})\cdot \boldsymbol{\omega }dt=\boldsymbol{\tau }\cdot \boldsymbol{\omega }dt
```
Since $\boldsymbol{\tau }$ and $\boldsymbol{\omega }$ are parallel, (the force lies in the x-y plane therefore the total torque is parallel to the $\mathrm {z}$-axis) we have
```{math}
dW=\tau \omega dt=\tau \frac{d\theta }{dt}dt=\tau d\theta
```
Therefore, the total work done in displacing the body from $\theta _{1}$ to $\theta _{2}$ is
```{math}
\begin{aligned} W=\displaystyle \int _{\theta _{1}}^{\theta _{2}}\tau d\theta \end{aligned}
```
If this torque is constant we have
```{math}
W=\tau (\theta _{2}-\theta _{1})=\tau \triangle \theta
```
```{figure} ../images/ch-07/459974_1_En_7_Fig21_HTML.png
:name: fig-7-21

A rigid body rotating about a fixed axis
```

**The Work–Energy Theorem** The work–energy theorem states that the work done by an external force while a rigid object rotate from $\theta _{1}$ to $\theta _{2}$ is equal to the change in the rotational energy of the object. This follows from Eq. 7.12 and by using the fact that along the axis of rotation the torque is given by $\tau _{z}=I\alpha$ (see Sect. [](#sec-7-7)), thus
```{math}
W=\int _{\theta _{1}}^{\theta _{2}}\tau d\theta =\int _{\theta _{1}}^{\theta _{2}}I\alpha d\theta =\int _{\omega _{1}}^{\omega _{2}}I\omega \frac{d\omega }{dt}dt=\int _{\omega _{1}}^{\omega _{2}}I\omega d\omega =\frac{1}{2}I\omega _{2}^{2}-\frac{1}{2}I\omega _{1}^{2}
```
```{math}
W=\triangle K=\frac{1}{2}I\omega _{2}^{2}-\frac{1}{2}I\omega _{1}^{2}
```
| Rotational motion | Linear motion |
| --- | --- |
| $\tau =I\alpha$ | $F=ma$ |
| $W=\int _{\theta _{0}}^{\theta }\tau d\theta$ | $W=\int _{x_{0}}^{x}Fdx$ |
| $K_{R}=\frac{1}{2}I\omega ^{2}$ | $K=\frac{1}{2}mv^{2}$ |
| $P=\tau \omega$ | $P=Fv$ |

(sec-7-10)=
## 7.10 Power

The instantaneous power delivered to rotate an object about a fixed axis is found from
```{math}
P=\frac{dW}{dt}=\frac{\tau _{z}d\theta }{dt}=\tau _{z}\omega _{z}
```
Table. 7.2 shows analogous equations in linear motion and rotational motion about a fixed axis

````{prf:example}
:label: example-7-14
:enumerator: 7.14

A disc of radius $R=0.08 \; \mathrm {m}$ and mass of 5 kg is rotating about its central axis with an angular speed of 170 rev/min. Find: (a) the rotational kinetic energy of the disc; (b) Suppose that the same disc rotate using a motor that delivers an instantaneous of power 0. $2\mathrm {h}\mathrm {p}$, find in that case the torque applied to the disc.

:::{admonition} Solution 7.14
:class: dropdown

(a) Since the rotational axis is the axis of symmetry of the disc, then the moment of inertia is

```{math}
I=\displaystyle \frac{1}{2}MR^{2}=\frac{1}{2}(5 \; \mathrm {k}\mathrm {g})(0.08 \; \mathrm {m})^{2}=0.016 \; \mathrm {kg\, m^2}
```

The angular velocity of the disc is

```{math}
\omega =\bigg (\frac{170 \; \mathrm {r}\mathrm {e}\mathrm {v}}{\min }\bigg )\bigg (\frac{2\pi \; \mathrm {r}\mathrm {a}\mathrm {d}}{1 \; \mathrm {r}\mathrm {e}\mathrm {v}}\bigg )\bigg (\frac{1 \; \min }{60 \; \mathrm {s}}\bigg )=17.8 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

```{math}
K=\frac{1}{2}I\omega ^{2}=\frac{1}{2}(0.016 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(17.8 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}=2.5 \; \mathrm {J}
```

(b)

```{math}
P=(0.2 \; \mathrm {h}\mathrm {p}\ ) \bigg (\frac{746 \; \mathrm {W}}{1\mathrm {h}\mathrm {p}}\bigg )=149.2 \; \mathrm {W}
```

and

```{math}
\tau =\frac{P}{\omega }=\frac{(149.2 \; \mathrm {W})}{(17.8 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})}=8.4 \; \mathrm {N}\,\mathrm {m}
```
:::
````

````{prf:example}
:label: example-7-15
:enumerator: 7.15

Consider a light rope wrapped around a uniform cylindrical shell of mass 30 kg and radius of 0.2 $\mathrm {m}$ as in Fig. [](#fig-7-22). Suppose that the cylinder is free to rotate about its central axis and that the rope is pulled from rest with a constant force of magnitude of 35 N. Assuming that the rope does not slip, find: (a) the torque applied to the cylinder about its central axis; (b) the angular acceleration of the cylinder; (c) the acceleration of a point in the unwinding rope; (d) the number of revolutions made by the cylinder when it reaches an angular velocity of 12 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}, (\mathrm {e})$ the work done by the applied force when the rope is pulled a distance of $1\mathrm {m}, (\mathrm {f})$ the work done using the work–energy theorem.

:::{admonition} Solution 7.15
:class: dropdown

:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig22_HTML.png
:name: fig-7-22

A light rope wrapped around a uniform cylindrical shell
```

````{prf:example}
:label: example-7-16
:enumerator: 7.16

A uniform rod of mass $M=0.75$ kg and length $L=1\mathrm {m}$ is hinged at one end and is free to rotate in a vertical plane as in Fig. [](#fig-7-23). If the rod is released from rest at an angle $\theta =30^{\mathrm {o}}$ to the horizontal, find; (a) the initial angular acceleration of the rod when it is released; (b) the initial acceleration of a point at the end of the rod; (c) from conservation of energy find the angular speed of the rod at its lowest position (Neglect friction at the pivot).

:::{admonition} Solution 7.16
:class: dropdown

:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig23_HTML.png
:name: fig-7-23

A uniform rod free to rotate at one end
```

```{figure} ../images/ch-07/459974_1_En_7_Fig24_HTML.png
:name: fig-7-24

A cylinder with a core section is free to rotate about its center. Ropes wrapped around the inner and outer sections exert different forces
```
```{figure} ../images/ch-07/459974_1_En_7_Fig25_HTML.png
:name: fig-7-25

A block of mass *m* is attached to a light string that is wrapped around the rim of a uniform solid disk of radius *R* and mass *M*
```

````{prf:example}
:label: example-7-17
:enumerator: 7.17

Find the net torque on the system shown in Fig. [](#fig-7-24) where $r_{1}=5$ cm, $r_{2}=15$ cm, $F_{1}=10 \; \mathrm {N}, F_{2}=20 \; \mathrm {N}$ and $F_{3}=15 \; \mathrm {N}$. Neglect the mass and friction of the ropes and pulleys.

:::{admonition} Solution 7.17
:class: dropdown

Since all forces lie in the same plane the net torque is

```{math}
\begin{aligned} \tau _{\mathrm {n}\mathrm {e}\mathrm {t}}&amp;=\tau _{1}+\tau _{2}+\tau _{3}=(10 \; \mathrm {N})(0.05\;\mathrm {m})+(20 \; \mathrm {N})(0.05 \; \mathrm {m})\\&amp;-(15 \; \mathrm {N})(0.15 \; \mathrm {m})=-0.75 \; \mathrm {N\, m} \end{aligned}
```
:::
````

````{prf:example}
:label: example-7-18
:enumerator: 7.18

A block of mass *m* is attached to a light string that is wrapped around the rim of a uniform solid disc of radius *R* and mass *M* as in Fig. [](#fig-7-25). Assuming that the string does not slip and that the disc rotates without friction, find: (a) the acceleration of the block; (b) the angular acceleration of the disc, and; (c) the tension in the string when the system is released from rest.

:::{admonition} Solution 7.18
:class: dropdown

The free-body diagrams of the disc and the block are shown in Fig. [](#fig-7-25). Applying Newton’s second law to the block gives

```{math}
T-mg=-ma
```

or

```{math}
\begin{aligned} a=\frac{mg-T}{m} \end{aligned}
```

where positive $\mathrm {y}$ is chosen to be directed upwards. Applying Newton’s second law in angular form to the disc gives

```{math}
\tau =RT=I\alpha
```

or

```{math}
\alpha =\frac{RT}{I}
```

Since the acceleration of the block is equal to the (tangential) acceleration of a point at the rim of the disc we have

```{math}
\begin{aligned} a=R\displaystyle \alpha =\frac{TR^{2}}{I} \end{aligned}
```

Equating Eqs. 7.13 and 7.14 gives

```{math}
\frac{TR^{2}}{I}=\frac{mg-T}{m}
```

```{math}
T=\frac{g}{1/m+R^{2}/I}=\frac{g}{1/m+2R^{2}/MR^{2}}
```

that gives

```{math}
T=\frac{mg}{1+2m/M}
```

Substituting this into Eq. 7.14

```{math}
a=\frac{TR^{2}}{I}=\frac{2TR^{2}}{MR^{2}}
```

gives

```{math}
a=\frac{g}{1+M/2m}
```

Finally

```{math}
\alpha =\frac{a}{R}=\frac{g}{R(1+M/{2m})}
```
:::
````

````{prf:example}
:label: example-7-19
:enumerator: 7.19

A homogeneous solid sphere of mass 4.7 kg and radius of 0.05 $\mathrm {m}$ rotate from rest about its central axis with a constant angular acceleration of 3 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}$. Find: (a) the torque that produces this angular acceleration; (b) the work done on the sphere after 7 revolutions; (c) the work done after 7 revolutions using the work–energy theorem.

:::{admonition} Solution 7.19
:class: dropdown

(a)

```{math}
\displaystyle \tau =I\alpha =\frac{2}{5}MR^{2}\alpha =\frac{2}{5}(4.7 \; \mathrm {k}\mathrm {g})(0.05 \; \mathrm {m})^{2}(3\,\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2})=0.014 \; \mathrm {N\,}
```

(b)

```{math}
\theta =( 7 \; \mathrm {rev}) \bigg (\displaystyle \frac{2\pi \mathrm {r}\mathrm {a}\mathrm {d}}{1 \; \mathrm {r}\mathrm {e}\mathrm {v}}\bigg )=44 \; \text{ rad }
```

and

```{math}
W=\tau \triangle \theta = (0.014 \; \mathrm {N/m}) (44 \; \mathrm {rad}) =0.6 \; \mathrm {J}
```

assuming $\theta _{0}=0.$

(c) After seven revolutions the angular velocity is

```{math}
\omega ^{2}=\omega _{0}^{2}+2\alpha (\theta -\theta _{0})
```

Since $\omega _{0}=0$, we have

```{math}
\omega ^{2}=2\alpha \theta =2(3 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}) ( 44 \; \text {rad})
```

that gives $\omega =16.24 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$. Hence

```{math}
W=\frac{1}{2}I\omega ^{2}-\frac{1}{2}I\omega _{0}^{2}=\frac{1}{2}(4.7\times 10^{-3} \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(16.24 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2})^{2}-0=0.6 \; \mathrm {J}
```
:::
````

````{prf:example}
:label: example-7-20
:enumerator: 7.20

Fig. [](#fig-7-26) shows Atwood’s machine when the mass of the pulley is considered. If the system is released from rest (and assuming that the string does not stretch or slip) and that the friction of the pulley is negligible, find linear acceleration of the blocks and the angular acceleration of the pulley.

:::{admonition} Solution 7.20
:class: dropdown

:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig26_HTML.png
:name: fig-7-26

Atwood’s machine
```

````{prf:example}
:label: example-7-21
:enumerator: 7.21

A uniform solid cylinder of radius of 0.2 $\mathrm {m}$ and mass of 10 kg is rotating about its central axis. If the angular speed of the cylinder is 5 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}{:} (\mathrm {a})$ calculate the angular momentum of the cylinder about its central axis; (b) Suppose the cylinder accelerates at a constant rate of 0.5 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}$, find the angular momentum of the cylinder at $t=3\mathrm {s}(\mathrm {c})$ find the applied torque; (d) find the work done after $3\mathrm {s}.$

:::{admonition} Solution 7.21
:class: dropdown

(a) The moment of inertia of the cylinder is

```{math}
I=\displaystyle \frac{1}{2}MR^{2}=\frac{1}{2}(10 \; \mathrm {k}\mathrm {g})(0.2 \; \mathrm {m})^{2}=0.2 \; \mathrm {kg\, m^2}
```

for homogeneous symmetrical objects the total angular momentum is

```{math}
L=I\omega =(0.2 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})=1 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}/\mathrm {s}
```

(b) At $t=3 \; \mathrm {s}$

```{math}
\omega =\omega _{0}+\alpha t=(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})+(0.5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2})(3 \; \mathrm {s})=6.5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

at that instant

```{math}
L=I\omega =(0.2 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(6.5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})=1.3 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}/\mathrm {s}
```

(c)

```{math}
\tau =I\alpha =(0.2 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(0.5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2})=0.1 \; \mathrm {N\, m}
```

(d)

```{math}
W=\frac{1}{2}I\omega ^{2}-\frac{1}{2}I\omega _{0}^{2}=\frac{1}{2}(0.2\,\mathrm {k}\mathrm {g}\,\mathrm {m}^{2})((6.5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}-(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2})=1.72 \; \mathrm {J}
```
:::
````

````{prf:example}
:label: example-7-22
:enumerator: 7.22

A uniform solid sphere of radius of 5 cm and mass of 4.7 kg is rotating about an axis that is tangent to the sphere (see Fig. [](#fig-7-27)). If its angular acceleration is given by $\alpha =(4t)\,\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}$ and if at $t=0, \omega _{0}=0$, find the angular momentum of the sphere and the applied torque as a function of time.

:::{admonition} Solution 7.22
:class: dropdown

```{math}
\omega =\int \alpha dt=\int 4tdt=2t^{2}+c
```

since at $t=0, \omega _{0}=0$ then $c=0$ and

```{math}
\omega =(2t^{2}) \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

The moment of inertia of the sphere is

```{math}
I=\displaystyle \frac{2}{5}MR^{2}+MR^{2}=\frac{7}{5}MR^{2}=\frac{7}{5}(4.7 \; \mathrm {k}\mathrm {g})(0.05 \; \mathrm {m})^{2}=0.016 \; \mathrm {kg\, m^2}
```

and

```{math}
L=I\omega =(0.016 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})((2t^{2}) \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})=(0.03t^{2}) \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}/\mathrm {s}
```

```{math}
\displaystyle \tau =\frac{dL}{dt}=(0.06t) \mathrm {N\, m}
```
:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig27_HTML.png
:name: fig-7-27

A uniform solid sphere rotating about an axis tangent to the sphere
```

````{prf:example}
:label: example-7-23
:enumerator: 7.23

In Example 7.8 find the angular momentum in each case.

:::{admonition} Solution 7.23
:class: dropdown

(a)

```{math}
L=I_{z}\omega =(0.014 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})=0.07 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}/\mathrm {s}
```

(b)

```{math}
L=I_{y}\omega =(0.01 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})=0.05 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}/\mathrm {s}
```

(c)

```{math}
L=I_{x}\omega =(4\times 10^{-3} \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})=0.02 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}/\mathrm {s}
```
:::
````

````{prf:example}
:label: example-7-24
:enumerator: 7.24

A uniform solid sphere of radius of 0.2 $\mathrm {m}$ is rotating about its central axis with an angular speed of 5 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$. If an impulsive force that has an average value of 100 $\mathrm {N}$ acts at the rim of the sphere at the center level for a short time of 2 $\mathrm {m}\mathrm {s}$:$(\mathrm {a})$ find the angular impulse of the force; (b) the final angular speed of the sphere.

:::{admonition} Solution 7.24
:class: dropdown

(a)

$\displaystyle \triangle L=\int _{t_{1}}^{t_{2}}\tau dt=\tau _{ave}\triangle t=\overline{F}Rt=(100 \; \mathrm {N})(0.2 \; \mathrm {m})(2\times 10^{-3} \; \mathrm {s})=0.04 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}/\mathrm {s}$

(b)

```{math}
\triangle L=I(\omega _{f}-\omega _{i})
```

```{math}
(0.04 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}/\mathrm {s})=(0.2 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})(\omega _{f}-(5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}))
```

That gives $\omega _{f}=5.2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}.$
:::
````

````{prf:example}
:label: example-7-25
:enumerator: 7.25

A man stands on a platform that is free to rotate without friction about a vertical axis as in Fig. [](#fig-7-28). If the system is initially rotating with an angular speed of 0.3 $\mathrm {r}\mathrm {e}\mathrm {v}/\mathrm {s}{:}\,(\mathrm {a})$ find the final angular speed of the system if the man draws the weights in; (b) find the increase in the kinetic energy of the system and its source. $(I_{i}=15 \; \mathrm {kg\, m^2}$ And $I_{f}=3 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})$.

:::{admonition} Solution 7.25
:class: dropdown

:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig28_HTML.png
:name: fig-7-28

A man stands on a platform that is free to rotate without friction about a vertical axis
```

````{prf:example}
:label: example-7-26
:enumerator: 7.26

A uniform disc of moment of inertia of 0.1 kg m$^{2}$ is rotating without friction with an angular speed of 3 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$ about an axle passing through its center of mass as in Fig. [](#fig-7-29). When another disc of moment of inertia of 0.05 kg m$^{2}$ that is initially at rest is dropped on the first, the two will eventually rotate with the same angular speed due to friction between them. Determine (a) the final angular speed; (b) the change in the kinetic energy of the system.

:::{admonition} Solution 7.26
:class: dropdown

:::
````

```{figure} ../images/ch-07/459974_1_En_7_Fig29_HTML.png
:name: fig-7-29

A uniform disc rotating without friction. Another disc that is initially at rest is dropped on the first, the two will eventually rotate with the same angular speed due to friction between them
```

## Problems

```{exercise}
:label: prob-7-1
:enumerator: 7.1

A wheel is initially rotating at 60 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$ in the clockwise direction. If a counterclockwise torque acts on the wheel producing a counterclockwise angular acceleration $\alpha =2t \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}$, find the time required for the wheel to reverse its direction of motion.
```

```{exercise}
:label: prob-7-2
:enumerator: 7.2

If the angular position of a point on a rotating wheel is given by $\theta =2t+ 5t^{2}$ rad, find the angular speed and angular acceleration of the point at $t=2 \; \mathrm {s}.$
```

```{exercise}
:label: prob-7-3
:enumerator: 7.3

A wheel of radius of 0.5 $\mathrm {m}$ rotates from rest at a constant angular acceleration of 2.5 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}$. At $t=2 \; \mathrm {s}$ Find (a) the angular speed of the wheel (b) the angle in radians through which the wheel rotates (c) the tangential and radial acceleration of a point at the rim of the wheel.
```

```{exercise}
:label: prob-7-4
:enumerator: 7.4

Find the angular speed in radians per second of the earth about (a) its axis (b) the sun.
```

```{exercise}
:label: prob-7-5
:enumerator: 7.5

An $\mathrm {L}$-shaped bar rotates counterclockwise with an angular acceleration of $\omega$ (see Fig. [](#fig-7-30)). Find (in vector form) the linear velocity and acceleration of the point $\mathrm {P}$ on the bar.
```

```{exercise}
:label: prob-7-6
:enumerator: 7.6

Four masses are connected by light rigid rods as in Fig. [](#fig-7-31). Calculate the moment of inertia of the system about (a) the $\mathrm {x}$-axis (b) the $\mathrm {y}$-axis (c) the $\mathrm {z}$-axis.
```

```{exercise}
:label: prob-7-7
:enumerator: 7.7

Find the moment of inertia of a uniform solid sphere of radius *R* and mass *M* about an axis passing through its center of mass.
```

```{exercise}
:label: prob-7-8
:enumerator: 7.8

Find the moment of inertia of an elliptical quadrant about the $\mathrm {y}$-axis (see Fig. [](#fig-7-32)).
```

```{exercise}
:label: prob-7-9
:enumerator: 7.9

A 5 kg uniform solid cylinder of radius 0.2 $\mathrm {m}$ rotate about its center of mass axis with an angular speed of 10 rev/min. Find (a) its rotational kinetic energy (b) its angular momentum.
```

```{exercise}
:label: prob-7-10
:enumerator: 7.10

A wheel of mass of 20 kg and radius of 0.75 $\mathrm {m}$ is initially rotating at 120 rev/min. If its angular speed is increased to 300 rev/min in 20 $\mathrm {s}$, find (a) the work done on the wheel (b) the average power delivered to the wheel.
```

```{exercise}
:label: prob-7-11
:enumerator: 7.11

A wheel of mass 10 kg and radius 0.4 $\mathrm {m}$ accelerates uniformly from rest to an angular speed of 800 rev/min in 20 $\mathrm {s}$. Find (a) the torque applied to the wheel (b) the work done on the wheel (c) the work done using the work–energy theorem.
```

```{exercise}
:label: prob-7-12
:enumerator: 7.12

A uniform rod of length *L* and mass *M* is pivoted at $\mathrm {O}$ (see Fig. [](#fig-7-33)). If a projectile of mass *m* moving at velocity *v* collide with the rod and stick to it, find the angular momentum of the system immediately before and immediately after the collision.
```

```{exercise}
:label: prob-7-13
:enumerator: 7.13

A disc of radius 2.2 $\mathrm {m}$ and mass of 120 kg rotate about a frictionless vertical axle that passes through its center. A man of mass 65 kg walks slowly from the rim of the disc towards the center. Find the angular speed of the disc when the man is at a distance of 0.7 $\mathrm {m}$ from the center if its angular speed when the man starts walking is 1.6 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}.$
```

```{figure} ../images/ch-07/459974_1_En_7_Fig30_HTML.png
:name: fig-7-30

An L-shaped bar rotating counterclockwise
```

```{figure} ../images/ch-07/459974_1_En_7_Fig31_HTML.png
:name: fig-7-31

Four masses connected by light rigid rods
```

```{figure} ../images/ch-07/459974_1_En_7_Fig32_HTML.png
:name: fig-7-32

An elliptical quadrant
```

```{figure} ../images/ch-07/459974_1_En_7_Fig33_HTML.png
:name: fig-7-33

A uniform rod of length L and mass M is pivoted at $\mathrm {O}$. A projectile of mass m moving at velocity v collides with the rod and sticks to it
```
