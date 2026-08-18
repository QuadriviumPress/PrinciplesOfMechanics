---
title: 10. Oscillatory Motion
short_title: "Ch. 10 — Oscillatory Motion"
label: ch-10
doi: 10.1007/978-3-030-15195-9_10
---

(sec-10-1)=
## 10.1 Oscillatory Motion

A motion repeating itself is referred to as periodic or oscillatory motion. An object in such motion oscillates about an equilibrium position due to a restoring force or torque. Such force or torque tends to restore (return) the system toward its equilibrium position no matter in which direction the system is displaced. This motion is important to study many phenomena including electromagnetic waves, alternating current circuits, and molecules. For a vibration to occur, two quantities are necessary to be present—stiffness and inertia.

(sec-10-2)=
## 10.2 Free Vibrations

When a system vibrates, a restoring force must be present. In addition to that force, there is always a retarding or damping force such as friction. If the effect of the damping force is small and can be neglected, then the motion is classified as free and undamped motion. Otherwise, the motion is classified as free damped motion. In both cases, the motion is known as free vibration since no forces other than the restoring and damping forces exist during vibration. If a driving force that does positive work on the system exists, the motion is classified as forced vibration.

This force may be applied externally to the system or sometimes is produced within the system. In this chapter, the case in which a restoring force is directly proportional to the displacement is considered. The resulting motion is then known as a harmonic vibration and the system is said to be linear. If the restoring force depends on the displacement in some other way, the resulting motion is known as anharmonic vibration and the system is said to be nonlinear.

(sec-10-3)=
## 10.3 Free Undamped Vibrations

This kind of motion is known as the simple harmonic motion. Next, we will examine examples of such motion in physics.

(sec-10-3-1)=
### 10.3.1 Mass Attached to a Spring

Consider a block of mass *m* attached to a light spring of spring constant *k* that is fixed at the other end (see [](#fig-10-1)). Suppose that the system lies on a frictionless horizontal surface. For small displacements, the restoring force acting on the block by the spring is given by Hook’s law

```{math}
F_{s}=-kx
```

As we’ve mentioned in [](#sec-4-1), if the block is displaced slightly to the right (for example to $x=A$), the restoring spring force will accelerate the block to the left transferring its potential energy into kinetic energy As the block reaches its equilibrium position $x=0$, all of its potential energy will be transformed into kinetic energy and it will overshoot to the other side. Again, as it moves left, the spring force decelerates the block to the right, transferring its kinetic energy into potential energy until all of its energy is potential at $x= -A$ where it comes to rest. At that point, it accelerates back to $x=0$ and regains all of its kinetic energy where it overshoots again to $x=A$. Therefore, stiffness restores the mass where inertia is responsible for the mass to overshoot. From Newton’s second law we, have

```{math}
ma=-kx
```

or

```{math}
m\frac{d^{2}x}{dt^{2}}+kx=0
```

or

```{math}
:label: eq-10-1

\begin{aligned} \frac{d^{2}x}{dt^{2}}+\omega _{n}^{2}x=0 \end{aligned}
```

where $\omega _{n}=\sqrt{k/m}$ is called the natural angular frequency of the system. The general solution of this equation is of the form

```{math}
:label: eq-10-2

\begin{aligned} x(t)=A_{1}\cos \omega _{n}t+A_{2}\sin \omega _{n}t \end{aligned}
```

where $A_{1}$ and $A_{2}$ are arbitrary constants that can be found from the initial conditions. Therefore, there are many possible motions with the same angular frequency $\omega _{n}$. By multiplying and dividing [](#eq-10-2) by $\sqrt{A_{1}^{2}+A_{2}^{2}}$, you can show that the solution may be written as

```{math}
:label: eq-10-3

\begin{aligned} x(t)=A\cos (\omega _{n}t-\phi ) \end{aligned}
```

where $A=\sqrt{A_{1}^{2}+A_{2}^{2}}$ is called the amplitude of motion and $\phi =\tan ^{-1}A_{2}/A_{1}$ is called the phase constant. In general, $\phi$ is chosen such that $0\le \phi \le \pi. A$ and $\phi$ can be determined from the initial conditions, i.e., from the values of the displacement and velocity when the motion starts. The mass therefore oscillates between *A* and $-A$. The quantity $(\omega _{n}t-\phi )$ is called the phase angle. If this angle is increased by $2\pi$, all physical quantities such as the displacement, velocity, and acceleration repeat themselves. The plot of *x* versus *t* is shown in [](#fig-10-2). If *A* is fixed and $\phi$ is changed the motion will be the same except that the same physical quantities will appear either earlier or later than the preceding motion.

```{figure} ../images/ch-10/459974_1_En_10_Fig1_HTML.png
:name: fig-10-1

A block of mass *m* attached to a light spring of spring constant *k* that is fixed at the other end
```

```{figure} ../images/ch-10/459974_1_En_10_Fig2_HTML.png
:name: fig-10-2

Plot of *x* versus *t* for a simple harmonic oscillator
```

(sec-10-3-1-1)=
#### 10.3.1.1 The Period and Frequency of Motion

The period of motion is the time required for one complete cycle or oscillation. Since the phase angle is changed by $2\pi$ after one complete cycle, we have for the mass–spring system,

```{math}
\omega _{n}t+2\pi =\omega _{n}(t+T)
```

or

```{math}
T=\frac{2\pi }{\omega _{n}}=2\pi \sqrt{\frac{m}{k}}
```

The frequency is defined as the number of complete cycles per unit time

```{math}
f_{n}=\frac{1}{T}=\frac{\omega _{n}}{2\pi }
```

This frequency is called the natural frequency of the motion. The unit of the frequency is cycles/s or hertz (Hz).

(sec-10-3-1-2)=
#### 10.3.1.2 The Phase Difference

The phase constant $\phi$ is important when comparing two or more oscillations of the same frequency Suppose a certain vibration has $\phi =0$, this means that at $t=0$ the displacement is maximum $x=A$. If a second vibration has also $\phi =0$, then the two vibrations are said to be in phase (see [](#fig-10-3) part a). Otherwise, the two vibrations are out of phase. If the phase constant of the second vibration is $\phi >0$, then the second vibration is leading the first vibration in phase by $\phi$. If $\phi <0$, then the second vibration is lagging the first by $\phi$. If $\phi =\pm \pi$, the two vibrations are said to be in antiphase with each other (see [](#fig-10-3) part b).

```{figure} ../images/ch-10/459974_1_En_10_Fig3_HTML.png
:name: fig-10-3

**a** Two simple harmonic motions of the same frequency and same phase constant $\pi =0$ but differing in amplitude. **b** Two simple harmonic motions of the same frequency and amplitude but differing in phase by $\phi =\pm \pi$
```

(sec-10-3-1-3)=
#### 10.3.1.3 The Velocity and Acceleration

The velocity of the mass is

```{math}
:label: eq-10-4

\begin{aligned} v(t)=\frac{dx}{dt}=-\omega _{n}A\sin (\omega _{n}t-\phi ) \end{aligned}
```

This can also be written as

```{math}
:label: eq-10-5

\begin{aligned} v(t)=\omega _{n}A\cos \bigg (\omega _{n}t-\phi +\frac{\pi }{2}\bigg ) \end{aligned}
```

The acceleration of the mass is

```{math}
:label: eq-10-6

\begin{aligned} a(t)=\frac{dv}{dt}=-\omega _{n}^{2}A\cos (\omega _{n}t-\phi ) \end{aligned}
```

or

```{math}
:label: eq-10-7

\begin{aligned} a(t)=\frac{dv}{dt}=\omega _{n}^{2}A\cos (\omega _{n}t-\phi +\pi ) \end{aligned}
```

Hence, the velocity and acceleration also vary harmonically with time with amplitudes $\omega _{n}A$ and $\omega _{n}^{2}A$, respectively, but they all have the same angular frequency From Eqs. 10.5 and 10.7 you can see that the velocity leads the displacement by $\pi /2$ or 90. The acceleration on the other hand leads the velocity by $\pi /2$ and the displacement by $\pi$ or 180. Figure 10.4 shows the displacement, velocity, and acceleration versus time.

```{figure} ../images/ch-10/459974_1_En_10_Fig4_HTML.png
:name: fig-10-4

The displacement, velocity and acceleration versus time
```

(sec-10-3-1-4)=
#### 10.3.1.4 Boundary Conditions

Boundary conditions are used to find *A* and $\phi$ for a specific vibration. Suppose that the vibration is measured when the stopwatch is set to zero, i.e., at $t=0$ and that at that instant the mass is released from rest at a distance of $x=A_{1}$ from its equilibrium position. Substituting these conditions into Eqs. 10.3 and 10.4, we have

```{math}
:label: eq-10-8

\begin{aligned} x=A\cos \phi =A_{1} \end{aligned}
```

```{math}
:label: eq-10-9

\begin{aligned} v=v_{0}=-\omega _{n}A\sin \phi \end{aligned}
```

Dividing [](#eq-10-9) by [](#eq-10-8) gives

```{math}
\tan \phi =\frac{-v_{0}}{\omega _{n}A_{1}}
```

Squaring and adding Eqs. 10.9 and 10.8 gives

```{math}
A_{1}^{2}+\bigg (\frac{v_{0}}{\omega _{n}}\bigg )^{2}=A^{2}\cos ^{2}\phi +A^{2}\sin ^{2}\phi
```

or

```{math}
A=\sqrt{A_{1}^{2}+\bigg (\frac{v_{0}}{\omega _{n}}\bigg )^{2}}
```

````{prf:example}
:label: example-10-1
:enumerator: 10.1

An object oscillates in simple harmonic motion according to the expression $x=(3\mathrm {m})\cos (\pi t+\pi /3)$. Find (a) the amplitude, phase constant, period, and frequency of motion; (b) the displacement, velocity, and acceleration of the object at $t=0.5\mathrm {s}(\mathrm {c})$ the time when the object first reach $x=-1.5 \; \mathrm {m}.$


:::{admonition} Solution 10.1
:class: dropdown

(a)

```{math}
A=3\,\mathrm {m}
```

```{math}
\phi =\frac{\pi }{3}
```

```{math}
T=\frac{2\pi }{\omega _{n}}=\frac{(2\pi )}{\pi }=2 \; \mathrm {s}
```

and

```{math}
f_{n}=\frac{1}{T}=\frac{1}{(2\mathrm {s})}=0.5 \; \text {Hz}
```

(b) At $t=0.5\,\mathrm {s}$

```{math}
x=(3 \; \mathrm {m})\cos \bigg (\pi (0.5 \; \mathrm {s})+\frac{\pi }{3}\bigg )=-2.6 \; \mathrm {m}
```

```{math}
v=-(3\pi \; \mathrm {m}/\mathrm {s})\sin \bigg (\pi t+\frac{\pi }{3}\bigg )
```

At $t=0.5\,\mathrm {s}$

```{math}
v=(-3\pi \; \mathrm {m}/\mathrm {s})\sin \bigg (\pi (0.5 \; \mathrm {s})+\frac{\pi }{3}\bigg )=-4.7 \; \mathrm {m}/\mathrm {s}
```

```{math}
a=(-3\pi ^{2} \; \mathrm {m}/\mathrm {s}^{2})\cos \bigg (\pi t+\frac{\pi }{3}\bigg )
```

at $t=0.5 \; \mathrm {s}$

```{math}
a=(-3\pi ^{2} \; \mathrm {m}/\mathrm {s}^{2})\cos \bigg (\pi (0.5 \; \mathrm {s})+\frac{\pi }{3}\bigg )=25.6 \; \mathrm {m}/\mathrm {s}^{2}
```

(c) at $x=-1.5 \; \mathrm {m}$

```{math}
(-1.5 \; \mathrm {m})=(3 \; \mathrm {m})\cos \bigg (\pi t+\frac{\pi }{3}\bigg )
```

or

```{math}
\frac{2\pi }{3}=\pi t+\frac{\pi }{3}
```

that gives $t=0.3 \; \mathrm {s}.$

:::
````
````{prf:example}
:label: example-10-2
:enumerator: 10.2

A 9 kg object is moving along the $\mathrm {x}$-axis under the influence of a force given by $F=(-3x)$ N. Find (a) the equation of motion; (b) the displacement of the mass at any time if at $t=0, x=5 \; \mathrm {m}$ and $v=0.$


:::{admonition} Solution 10.2
:class: dropdown

(a)

```{math}
F=-3x=ma=m\frac{d^{2}x}{dt^{2}}
```

hence,

```{math}
\frac{d^{2}x}{dt^{2}}+3x=0
```

(b) The general solution of this equation is

```{math}
x=A\cos \sqrt{3}t+B\sin \sqrt{3}t
```

Since at $t=0, \; x=5 \; \mathrm {m}$, then $A=5 \; \mathrm {m}$ and

```{math}
x=(5\mathrm {m})\cos \sqrt{3}t+B\sin \sqrt{3}t
```

also we have at $t=0, dx/dt=0$, or

```{math}
-5\sqrt{3}\sin \sqrt{3}t+\sqrt{3}B\cos \sqrt{3}t=0
```

and therefore $B=0$. Thus,

```{math}
x=(5\mathrm {m})\cos \sqrt{3}t
```

:::
````
````{prf:example}
:label: example-10-3
:enumerator: 10.3

A 0.3 kg block is attached to a spring of force constant 20 $\mathrm {N}/\mathrm {m}$ on a frictionless horizontal surface. If the initial displacement and velocity of the system is 0.02 $\mathrm {m}$ and 0.2 $\mathrm {m}/\mathrm {s}$, respectively, find the period, amplitude, and phase constant of motion.


:::{admonition} Solution 10.3
:class: dropdown

```{math}
\omega _{n}=\sqrt{\frac{k}{m}}=\sqrt{\frac{(20 \; \mathrm {N}/\mathrm {m})}{(0.3 \; \mathrm {k}\mathrm {g})}}=8.2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

```{math}
A=\sqrt{A_{1}^{2}+\bigg (\frac{v_{0}}{\omega _{n}}\bigg )^{2}}=\sqrt{(0.02 \; \mathrm {m})^{2}+\bigg (\frac{(0.2 \; \mathrm {m}/\mathrm {s})}{(82 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})}\bigg )^{2}}=0.03 \; \mathrm {m}
```

```{math}
\tan \phi =\frac{-v_{0}}{\omega _{n}A_{1}}=\frac{-(0.2 \; \mathrm {m}/.\mathrm {s})}{(8.2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})(0.03 \; \mathrm {m})}=-0.8
```

```{math}
\phi =-38.7^{\circ }
```

:::
````
````{prf:example}
:label: example-10-4
:enumerator: 10.4

A particle of mass *m* is dropped in a straight tunnel that is drilled through the earth and which passes through the center of earth as shown in [](#fig-10-5). Show that the motion of the particle is simple harmonic motion and find its period.


:::{admonition} Solution 10.4
:class: dropdown

Assuming that the earth is a perfect sphere of uniform density and since the particle is inside the earth, then from [](#sec-9-2), the gravitational force exerted on the particle by the earth is

```{math}
F=-\left( \frac{GmM_{E}}{R_{E}^{3}}\right) r=-kr
```

Because this force is directly proportional to the displacement and is opposite to it, then the particle will move in simple harmonic motion about the center of the earth. The equation of motion is

```{math}
\frac{dr^{2}}{dt^{2}}+\bigg (\frac{GM_{E}}{R_{E}^{3}}\bigg )r=0
```

hence,

```{math}
\omega _{n}=\sqrt{\frac{GM_{E}}{R_{E}^{3}}}=\sqrt{\frac{(6.67\times 10^{-11} \; \mathrm {N}\mathrm {m}^{2}/\mathrm {k}\mathrm {g}^{2})(5.98\times 10^{24} \; \mathrm {k}\mathrm {g})}{(6.37\times \mathrm {l0}^{6} \; \mathrm {m})^{3}}}=1.24\times 10^{-3} \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

```{math}
T=\frac{2\pi }{\omega _{n}}=\frac{2(3.14)}{(1.24\times 10^{-3} \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})}=5055.4 \; \mathrm {s}=84.25 \; \min
```

:::
````
```{figure} ../images/ch-10/459974_1_En_10_Fig5_HTML.png
:name: fig-10-5

A particle of mass *m* is dropped in a straight tunnel that is drilled through the earth and which passes through the center of earth
```

````{prf:example}
:label: example-10-5
:enumerator: 10.5

A 0.4 kg block is connected to two springs of force constants $k_{1}=20 \; \mathrm {N}/\mathrm {m}$ and $k_{2}=50 \; \mathrm {N}/\mathrm {m}$ as in [](#fig-10-6). Find (a) the total force acting on the block; (b) the period of motion.


:::{admonition} Solution 10.5
:class: dropdown

The force that each spring exerts on the block acts in the opposite direction of the displacement, therefore we have

```{math}
\sum F=-k_{1}x-k_{2}x=-(k_{1}+k_{2})x=-(70 \; \mathrm {N}/\mathrm {m})x
```

Thus the two springs can be considered as one spring of a force constant of $(k_{1}+k_{2})$. The period of motion is therefore

```{math}
T=2\pi \sqrt{\frac{m}{k_{1}+k_{2}}}=2(3.14)\sqrt{\frac{(0.4 \; \mathrm {k}\mathrm {g})}{(70 \; \mathrm {N}/\mathrm {m})}}=0.5 \; \mathrm {s}
```

:::
````
```{figure} ../images/ch-10/459974_1_En_10_Fig6_HTML.png
:name: fig-10-6

A block connected to two springs
```

```{figure} ../images/ch-10/459974_1_En_10_Fig7_HTML.png
:name: fig-10-7

A second block on top of a block connected to a spring
```

````{prf:example}
:label: example-10-6
:enumerator: 10.6

A 6 kg block is connected to a light spring of force constant of 300 $\mathrm {N}/\mathrm {m}$ on a frictionless horizontal surface. On top of it a second block of mass of 2 kg is placed. If the coefficient of static friction between the two blocks is 0.4 (see [](#fig-10-7)), find the maximum amplitude the system can have when it is in simple harmonic motion such that there is no slipping between the blocks.


:::{admonition} Solution 10.6
:class: dropdown

The maximum acceleration of the lower block is $a_{\max }=\omega _{n}^{2}A$. In order for the upper block not to slip, the force of static friction between the two blocks must produce the same acceleration as the lower block. The maximum statistical frictional force that can be exerted on the upper block is $\mu _{s}mg$ and hence, the maximum acceleration that the force of static friction can produce is $\mu _{s}g$. Therefore, $\mu _{s}g=a_{\max }=\omega _{n}^{2}A$. Since

```{math}
\omega _{n}=\sqrt{\frac{k}{(m+M)}}
```

we have

```{math}
A=\frac{\mu _{s}g}{\omega _{n}^{2}}=\frac{\mu _{s}g(m+M)}{k}=\frac{(0.4)(9.8 \; \mathrm {m}/\mathrm {s}^{2})(8 \; \mathrm {k}\mathrm {g})}{(300 \; \mathrm {N}/\mathrm {m})}=0.1 \; \mathrm {m}
```

:::
````
```{figure} ../images/ch-10/459974_1_En_10_Fig8_HTML.png
:name: fig-10-8

A particle in uniform circular motion
```

(sec-10-3-2)=
### 10.3.2 Simple Harmonic Motion and Uniform Circular Motion

Consider a circle of radius *A* centered at the $\mathrm {x}$ and $\mathrm {y}$ axes as shown in [](#fig-10-8). Let A be the position vector of a particle $\mathrm {P}$ rotating with a constant angular speed $\omega _{n}$ in the anticlockwise direction. The particle is thus in uniform circular motion. Suppose $\mathrm {P}$ starts the rotation at $t=0$ at an angle of $\phi$ measured from the positive $\mathrm {x}$-axis. At any time, the angular position of the particle is given by $(\omega _{n}t+\phi )$, therefore the vector position of the particle at any time is

```{math}
\mathbf {A}=x\mathbf {i}+y\mathbf {j}=A\cos (\omega _{n}t+\phi )\mathbf {i}+A\sin (\omega _{n}t+\phi )\mathbf {j}
```

Hence,

```{math}
x=A\cos (\omega _{n}t+\phi )
```

and

```{math}
y=A\sin (\omega _{n}t+\phi )
```

That is, as $\mathrm {P}$ moves in uniform circular motion, its projection $\mathrm {P}'$ on the x-axis moves in simple harmonic motion where the radius of the circle is equal to the amplitude of motion. The projection of $\mathrm {P}$ along the $\mathrm {y}$-axis also undergoes simple harmonic motion. Thus, uniform circular motion may be considered as a combination of the simple harmonic motions of the projections of $\mathrm {P}$ on each axis. These two simple harmonic motions have equal amplitudes and angular frequencies but are in quadrature with each other (they differ in phase by $\pi /2$). The linear tangential velocity of the particle in this uniform circular motion is given by

```{math}
v=A\omega _{n}
```

The $\mathrm {x}$ component of the velocity is from [](#fig-10-9) given by

```{math}
v_{x}=-\omega _{n}A\sin (\omega _{n}t+\phi )
```

The acceleration of the particle in uniform circular motion is just the radial (centripetal) acceleration that is given by

```{math}
a=\frac{v^{2}}{A}=A\omega _{n}^{2}
```

The $\mathrm {x}$ components of the acceleration (see [](#fig-10-10)) is

```{math}
a_{x}=-\omega _{n}^{2}A\cos (\omega _{n}t+\phi )
```

Hence as you can see, the displacement, velocity, and acceleration of the projection of $\mathrm {P}$ onto the $\mathrm {x}$ (or $\mathrm {y}$ axis) are the same as that of a simple harmonic motion. From this, we conclude that the simple harmonic motion can be represented as the projection of uniform circular motion along a diameter of the circle.

```{figure} ../images/ch-10/459974_1_En_10_Fig9_HTML.png
:name: fig-10-9

The velocity components of the particle
```

```{figure} ../images/ch-10/459974_1_En_10_Fig10_HTML.png
:name: fig-10-10

The acceleration components of the particle
```

(sec-10-3-3)=
### 10.3.3 Energy of a Simple Harmonic Oscillator

Since in a simple harmonic oscillator, there aren’t any dissipative forces, the total mechanical energy of the system is conserved and is equal to the sum of its kinetic and potential energies, that is

```{math}
E=K+U
```

```{math}
K=\frac{1}{2}mv^{2}=\frac{1}{2}m\omega _{n}^{2}A^{2}\sin ^{2}(\omega _{n}t+\phi )
```

```{math}
U=\frac{1}{2}kx^{2}=\frac{1}{2}kA^{2}\cos ^{2}(\omega _{n}t+\phi )
```

Thus,

```{math}
E=\frac{1}{2}kA^{2}[\sin ^{2}(\omega _{n}t+\phi )+\cos ^{2}(\omega _{n}t+\phi )]
```

or

```{math}
E=\frac{1}{2}kA^{2}= \text {constant}
```

The equation of motion of a simple harmonic oscillator can be obtained from the total mechanical energy of the system as follows:

```{math}
:label: eq-10-10

\begin{aligned} E=\frac{1}{2}m\dot{x}^{2}+\frac{1}{2}kx^{2}=\frac{1}{2}kA^{2} \end{aligned}
```

```{math}
\frac{dE}{dt}=m\dot{x}\ddot{x}+kx\dot{x}=0
```

or

```{math}
m\ddot{x}+kx=0
```

Hence

```{math}
\ddot{x}+\omega _{n}^{2}x=0
```

where $\omega _{n}=\sqrt{k/m}$. As the mass moves, its kinetic energy is transformed into potential energy and vice versa. Figure 10.11 shows the kinetic energy and potential energy of the system as a function of time and as a function of the displacement respectively Note that the variation of *U* and *K* with time is at twice the angular frequency of the variation of *x*, *v*, and *a* with time. This is because the potential energy is converted to kinetic energy twice in each cycle. The velocity of the simple harmonic oscillator can be obtained from the total energy of the system. From [](#eq-10-10), we have

```{math}
v=\pm \sqrt{\frac{k}{m}(A^{2}-x^{2})}
```

Hence, the maximum speed is at $x=0$ and is zero at $x=\pm A$ which are called the turning points as discussed in Chap. chap444.

```{figure} ../images/ch-10/459974_1_En_10_Fig11_HTML.png
:name: fig-10-11

As the mass moves, its kinetic energy is transformed into potential energy and vice versa
```

````{prf:example}
:label: example-10-7
:enumerator: 10.7

A 0.3 kg mass is attached to a light spring. If the total energy of the system is 0.025 $\mathrm {J}$ and the amplitude of motion is 5 cm, find the period and frequency of motion.


:::{admonition} Solution 10.7
:class: dropdown

```{math}
E= (0.025\,\mathrm {J})=\frac{1}{2}kA^{2}=\frac{1}{2}k(0.05 \; \mathrm {m})^{2}
```

hence

```{math}
k=20 \; \mathrm {N}/\mathrm {m}
```

The period of motion is therefore

```{math}
T=2\pi \sqrt{\frac{m}{k}}=2(3.14)\sqrt{\frac{(0.3 \; \mathrm {k}\mathrm {g})}{(20 \; \mathrm {N}/\mathrm {m})}}=0.8 \; \mathrm {s}
```

and the frequency is

```{math}
f_{n}=\frac{1}{T}=\frac{1}{(0.8 \; \mathrm {s})}=1.25 \; \mathrm {Hz}
```

:::
````
````{prf:example}
:label: example-10-8
:enumerator: 10.8

A 0.2 kg block is attached to a light spring of force constant of 11 $\mathrm {N}/\mathrm {m}$ on a horizontal frictionless surface. If the block is displaced a distance of 8 cm from its equilibrium position, find (a) the amplitude, the angular frequency, the period and the frequency of motion when the block is released; (b) the maximum force exerted on the block; (c) the total mechanical energy of the system; (d) the maximum speed and maximum acceleration of the block; (e) the velocity of the block when its displacement is 2 cm; (f) the acceleration of the block when its displacement is 3 cm.


:::{admonition} Solution 10.8
:class: dropdown

(a)

```{math}
A=8\,\mathrm {c}\mathrm {m}
```

```{math}
\omega _{n}=\sqrt{\frac{k}{m}}=\sqrt{\frac{(11 \; \mathrm {N}/\mathrm {m})}{(0.2 \; \mathrm {k}\mathrm {g})}}=7.4 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

```{math}
T=\frac{2\pi }{\omega _{n}}=\frac{2(3.14)}{(7.4 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})}=0.85 \; \mathrm {s}
```

```{math}
f_{n}=\frac{1}{T}=\frac{1}{(0.85 \; \mathrm {s})}=1.2 \; \mathrm {Hz}
```

(b)

```{math}
|F|=kA=(11\,\mathrm {N}/\mathrm {m})(0.08\,\mathrm {m})=0.9\,\mathrm {N}
```

(c)

```{math}
E=\frac{1}{2}kA^{2}=\frac{1}{2}(11 \; \mathrm {N}/\mathrm {m})(0.08 \; \mathrm {m})^{2}=0.035 \; \mathrm {J}
```

(d)

```{math}
v_{\max }=\omega _{n}A=( 7.4 \; \mathrm {rad/s}) (0.08 \; \mathrm {m})=0.6 \; \mathrm {m}/\mathrm {s}
```

```{math}
a_{\max }=\omega _{n}^{2}A=(7.4 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}(0.08 \; \mathrm {m})=4.4 \; \mathrm {m}/\mathrm {s}^{2}
```

(e)

```{math}
v=\pm \sqrt{\frac{k}{m}(A^{2}-x^{2})}=\sqrt{\frac{(11 \; \mathrm {N}/\mathrm {m})}{(0.2 \; \mathrm {k}\mathrm {g})}((0.08 \; \mathrm {m})^2-(0.02 \; \mathrm {m})^2)}=1.8 \; \mathrm {m}/\mathrm {s}
```

(f)

```{math}
a=-\omega _{n}^{2}x=-(7.4 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}(0.03 \; \mathrm {m})=-1.6 \; \mathrm {m}/\mathrm {s}^{2}
```

:::
````
````{prf:example}
:label: example-10-9
:enumerator: 10.9

An object connected to a spring is in simple harmonic motion on a frictionless surface. If the object’s displacement when $(2v_{\max }/3)$ is $\pm 0.015 \; \mathrm {m}$, find the amplitude of motion.


:::{admonition} Solution 10.9
:class: dropdown

```{math}
\frac{1}{2}kA^{2}=\frac{1}{2}mv^{2}+\frac{1}{2}kx^{2}=\frac{1}{2}m\frac{4\omega _{n}^{2}A^{2}}{9}+\frac{1}{2}kx^{2}
```

therefore

```{math}
A^{2}=\frac{9}{5}x^{2}=\frac{9}{5} (0.015 \; \mathrm {m})^{2}
```

```{math}
A=0.02 \; \mathrm {m}
```

:::
````
````{prf:example}
:label: example-10-10
:enumerator: 10.10

A solid cylinder is connected to a light spring as in [](#fig-10-12). If the cylinder rolls without slipping along the surface, show that the motion of the cylinder is simple harmonic motion and find its frequency.


:::{admonition} Solution 10.10
:class: dropdown

At any instant the total mechanical energy is

```{math}
E=\frac{1}{2}kx^{2}+\frac{1}{2}I_{cm}\omega ^{2}+\frac{1}{2}Mv_{cm}^{2}=\frac{1}{2}kx^{2}+\frac{1}{2}I_{cm}\frac{v_{cm}^{2}}{R^{2}}+\frac{1}{2}Mv_{cm}^{2}
```

```{math}
=\frac{1}{2}kx^{2}+\frac{1}{2}\left( \frac{1}{2}MR^{2}\right) \frac{v_{cm}^{2}}{R^{2}}+\frac{1}{2}Mv_{cm}^{2}
```

Since the total mechanical energy is conserved

```{math}
\frac{dE}{dt}=kv_{cm}x+\frac{1}{2}Mv_{cm}a_{cm}+Mv_{cm}a_{cm}=0
```

```{math}
kv_{cm}x=\frac{-3}{2}Mv_{cm}a_{cm}
```

or

```{math}
a_{cm}=\frac{-2}{3}\frac{k}{M}x
```

```{math}
\frac{d^{2}x}{dt^{2}}+\frac{2}{3}\frac{k}{M}x=0
```

this equation is of a simple harmonic motion with

```{math}
\omega _{n}=\sqrt{\frac{2}{3}\frac{k}{M}}
```

:::
````
```{figure} ../images/ch-10/459974_1_En_10_Fig12_HTML.png
:name: fig-10-12

A solid cylinder connected to a light spring
```

(sec-10-3-4)=
### 10.3.4 The Simple Pendulum

The simple pendulum is an example of an angular vibration in which the restoring effect is due to a restoring torque. A simple pendulum consists of a mass (called the bob) suspended by a light string of length *L* that is fixed at the other end (see [](#fig-10-13)). If the mass is pulled to the right or left from its equilibrium position and released, then the pendulum will swing in a vertical plane about an axis passing through O. The resulting motion is then a periodic or oscillatory motion. The restoring torque is due to gravity and is given by

```{math}
\tau =-(mg\sin \theta )L
```

The minus sign indicates that the torque is a restoring torque, since it always tends to decrease $\theta$. The moment of inertia of the bob about an axis passing through $\mathrm {O}$ is

```{math}
I=mL^{2}
```

From Newton’s second law in angular form, we have

```{math}
\tau =I\alpha =I\ddot{\theta }
```

Hence,

```{math}
-mg\sin \theta L=mL^{2}\ddot{\theta }
```

or

```{math}
:label: eq-10-11

\begin{aligned} \ddot{\theta }+\bigg (\frac{g}{L}\bigg )\sin \theta =0 \end{aligned}
```

This equation does not represent a harmonic motion. That is because the torque is not directly proportional to the angular displacement. Thus, the system is nonlinear. However for small angular displacements, we have $\sin \theta \approx \theta ($since $\sin \theta =\theta -\theta ^{3}/3!+\theta ^{5}/5!\ldots )$ and [](#eq-10-11) becomes

```{math}
\ddot{\theta }+\bigg (\frac{g}{L}\bigg )\theta =0
```

or

```{math}
:label: eq-10-12

\begin{aligned} \ddot{\theta }+\omega _{n}^{2}\theta =0 \end{aligned}
```

where $\omega _{n}=\sqrt{g/L}$. Hence for small angular displacements, the motion is a simple harmonic motion. The solution of [](#eq-10-12) is of the form

```{math}
\theta =\theta _{m}\cos (\omega _{n}t-\phi )
```

where $\theta _{m}$ is the maximum angular displacement and $\phi$ is the phase constant. The plot of this equation is shown in [](#fig-10-14). The period of the simple pendulum is therefore given by

```{math}
T=\frac{2\pi }{\omega _{n}}=2\pi \sqrt{\frac{L}{g}}
```

```{figure} ../images/ch-10/459974_1_En_10_Fig13_HTML.png
:name: fig-10-13

The simple pendulum
```

```{figure} ../images/ch-10/459974_1_En_10_Fig14_HTML.png
:name: fig-10-14

The displacement versus time of a simple pendulum
```

(sec-10-3-4-1)=
#### 10.3.4.1 Energy

The kinetic energy of the simple pendulum is

```{math}
K=\frac{1}{2}mv^{2}=\frac{1}{2}mL^{2}\omega _{n}^{2}=\frac{1}{2}mL\dot{\theta }^{2}
```

Taking the reference point of potential energy of the system to be zero when the bob is at the bottom, we have

```{math}
U=MgL(1-\cos \theta )
```

The total energy is therefore given by

```{math}
E=K+U=\frac{1}{2}ML^{2}\dot{\theta }^{2}+MgL(1-\cos \theta )
```

For small $\theta$, we have $\cos \theta \approx 1-\frac{\theta ^{2}}{2}$since $\cos \theta =1-\theta ^{2}/2!+\theta ^{4}/4!\ldots )$ thus

```{math}
E=\frac{1}{2}ML^{2}\dot{\theta }^{2}+\frac{1}{2}MgL\theta ^{2}
```

Since

```{math}
\dot{\theta }=-\theta _{m}\omega _{n}\sin (\omega _{n}t-\phi )
```

we have

```{math}
E=\frac{1}{2}ML^{2}\theta _{m}^{2}\omega _{n}^{2}\sin ^{2}(\omega _{n}t-\phi )+\frac{1}{2}MgL\theta _{m}^{2}\cos ^{2}(\omega _{n}t-\phi )
```

or

```{math}
E=\frac{1}{2}MgL\theta _{m}^{2}
```

Therefore, the total energy of the system is constant. Figure 10.15 shows the variation of the kinetic and potential energies with the displacement.

```{figure} ../images/ch-10/459974_1_En_10_Fig15_HTML.png
:name: fig-10-15

The total energy of a simple pendulum
```

The equation of motion may also be obtained from energy as follows:

```{math}
\frac{dE}{dt}=ML^{2}\dot{\theta }\ddot{\theta }+MgL\theta \dot{\theta }=0
```

or

```{math}
\ddot{\theta }+\bigg (\frac{g}{L}\bigg )\theta =0
```

````{prf:example}
:label: example-10-11
:enumerator: 10.11

A simple pendulum is 0.5 $\mathrm {m}$ long. Find its period at the surface of Mars and compare it to its period at the earth’s surface.


:::{admonition} Solution 10.11
:class: dropdown

At Mars’s surface, the gravitational acceleration is

```{math}
g_{M}=\frac{GM_{M}}{R_{M}^{2}}=\frac{(6.67\times 10^{-11} \; \mathrm {N}\, mathrm{m}^{2}/\mathrm {k}\mathrm {g}^{2})(6.42\times 10^{23} \; \mathrm {k}\mathrm {g})}{(3.37\times \mathrm {l}0^{6} \; \mathrm {m})^{2}}=3.8 \; \mathrm {m}/\mathrm {s}^{2}
```

The period at Mars is therefore

```{math}
T_{M}=2\pi \sqrt{\frac{L}{g_{M}}}=2(3.14)\sqrt{\frac{(0.5 \; \mathrm {m})}{(3.8 \; \mathrm {m}/\mathrm {s}^{2})}}=2.3 \; \mathrm {s}
```

At the earth’s surface,

```{math}
T_{E}=2\pi \sqrt{\frac{L}{g_{E}}}=2(3.14)\sqrt{\frac{(0.5 \; \mathrm {m})}{(9.8 \; \mathrm {m}/\mathrm {s}^{2})}}=1.4 \; \mathrm {s}
```

Thus, $T_{M}=1.6T_{E}.$

:::
````
````{prf:example}
:label: example-10-12
:enumerator: 10.12

A simple pendulum of length of 2 $\mathrm {m}$ is displaced through an angle of $12^{\circ }$ and released. Find (a) the angular frequency of motion; (b) the maximum angular speed and maximum angular acceleration.


:::{admonition} Solution 10.12
:class: dropdown

(a) The amplitude of motion is

```{math}
\theta _{\max }=(12^{\circ })\bigg (\frac{2\pi \; \mathrm {r}\mathrm {a}\mathrm {d}}{360^{\circ } \; \deg }\bigg )=0.21 \; \text {rad}
```

The angular frequency is

```{math}
\omega _{n}=\sqrt{\frac{g}{L}}=\sqrt{\frac{(9.8 \; \mathrm {m}/\mathrm {s}^{2})}{(2 \; \mathrm {m})}}=2.2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

(b) The maximum angular speed is

```{math}
\dot{\theta }_{\max }=\omega _{n}A=( 2.2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})(0.21 \; \mathrm {r}\mathrm {a}\mathrm {d}) =0.5 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

The maximum angular acceleration is

```{math}
\ddot{\theta }_{\max }=\omega _{n}^{2}A=(2.2 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}(0.21 \; \mathrm {r}\mathrm {a}\mathrm {d} )=1 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}^{2}
```

:::
````
````{prf:example}
:label: example-10-13
:enumerator: 10.13

A simple pendulum 1.4 $\mathrm {m}$ in length is displaced through an angle of $10^{\circ }$ and released. Find the velocity of the bob when it reaches the bottom.


:::{admonition} Solution 10.13
:class: dropdown

```{math}
\theta =(10^{\circ })\bigg (\frac{2\pi \; \mathrm {r}\mathrm {a}\mathrm {d}}{360^{\circ } \; \deg }\bigg )=0.17 \; \text {rad}
```

Taking the potential energy to be zero at the bottom, we have

```{math}
mgL(1-\cos \theta )=\frac{1}{2}mv^{2}
```

Since $\theta$ is small, $\cos \theta \approx 1-\theta ^{2}/2$ and therefore

```{math}
mgL\frac{\theta ^{2}}{2}=\frac{1}{2}mv^{2}
```

and

```{math}
v=\sqrt{gL}\theta =\sqrt{(9.8 \; \mathrm {m}/\mathrm {s}^{2})(14 \; \mathrm {m})} (0.17 \; \mathrm {rad}) = \; 0.63\mathrm {m}/\mathrm {s}
```

:::
````
```{figure} ../images/ch-10/459974_1_En_10_Fig16_HTML.png
:name: fig-10-16

The physical pendulum
```

(sec-10-3-5)=
### 10.3.5 The Physical Pendulum

The physical pendulum is a rigid body that oscillates about an axis passing through a point in the body other than its center of mass (the center of mass is assumed to be located at the center of gravity). Figure 10.16 shows a rigid body pivoted at point $\mathrm {O}$ that is at a distance *d* from the center of mass. The equilibrium position of the body is when its center of mass is directly below the pivot O. If the body is displaced either to the right or left from the equilibrium position, a restoring torque due to gravity will act on it. As a result, the body will oscillate in a vertical plane where the axis of rotation is perpendicular to the page. The restoring torque is given by

```{math}
\tau =-Mgd\ \sin \theta
```

where *M* is the mass of the body and *d* is the moment arm of the tangential component of the weight $(Mg\ \sin \theta )$. From Newton’s second law, we have

```{math}
\tau =I\alpha
```

```{math}
-Mgd\sin \theta =I\ddot{\theta }
```

For small angular displacements $\sin \theta \approx \theta$ and hence

```{math}
\ddot{\theta }+\bigg (\frac{Mgd}{I}\bigg )\theta =0
```

or

```{math}
\ddot{\theta }+\omega _{n}^{2}\theta =0
```

This equation is of a simple harmonic motion with an angular frequency of

```{math}
\omega _{n}=\sqrt{\frac{Mgd}{I}}
```

and a period of motion of

```{math}
T=\frac{2\pi }{\omega _{n}}=2\pi \sqrt{\frac{I}{Mgd}}
```

Thus,

```{math}
I=\frac{T^{2}Mgd}{4\pi ^{2}}
```

Therefore, the moment of inertia of a body can be found by measuring its period when it is in simple harmonic motion as a physical pendulum. Note that, the simple pendulum is a special case of the physical pendulum since for a simple pendulum of mass *m*, the moment of inertia is

```{math}
I=md^{2}
```

and thus, the angular frequency is

```{math}
\omega _{n}=\sqrt{\frac{mgd}{md^{2}}}=\sqrt{\frac{g}{d}}
```

This angular frequency is of a simple pendulum where *d* represents the length of the string.

````{prf:example}
:label: example-10-14
:enumerator: 10.14

A uniform rod of length of 0.6 $\mathrm {m}$ that is suspended at one end oscillates with a small amplitude as in [](#fig-10-17). Find the frequency of motion.


:::{admonition} Solution 10.14
:class: dropdown

```{math}
f_{n}=\frac{1}{2\pi }\sqrt{\frac{Mgd}{I}}=\frac{1}{2\pi }\sqrt{\frac{Mg({L}/{2})}{(1/3){ML^{2}}}}=\frac{1}{2\pi }\sqrt{\frac{3g}{2L}}=\frac{1}{2(3.14)}\sqrt{\frac{3(9.8\mathrm {m}/\mathrm {s}^{2})}{2(0.6\mathrm {m})}}=0.8\,\text {Hz}
```

:::
````
```{figure} ../images/ch-10/459974_1_En_10_Fig17_HTML.png
:name: fig-10-17

A uniform rod suspended at one end oscillated with a small amplitude
```

```{figure} ../images/ch-10/459974_1_En_10_Fig18_HTML.png
:name: fig-10-18

A uniform square plate pivoted at one of its corners and oscillates in a vertical plane
```

````{prf:example}
:label: example-10-15
:enumerator: 10.15

A uniform square plate of length *a* is pivoted at one of its corners and oscillates in a vertical plane as in [](#fig-10-18). Find the period of motion if the amplitude is small.


:::{admonition} Solution 10.15
:class: dropdown

The moment of inertia of a uniform rectangular plate about its center of mass is

```{math}
I_{cm}=\frac{1}{12}M(a^{2}+b^{2})
```

Thus for a uniform square plate, we have

```{math}
I_{cm}=\frac{1}{6}Ma^{2}
```

From the parallel axis theorem, the moment of inertia of the plate about an axis that is parallel to the center of mass axis and passing through one corner $(D=\sqrt{2}a)$ is

```{math}
I=I_{cm}+MD^{2}=\frac{1}{6}\ Ma^{2}+2Ma^{2}=\frac{13}{6}Ma^{2}
```

and hence

```{math}
T=2\pi \sqrt{\frac{I}{Mgd}}=2\pi \sqrt{\frac{(13/6){Ma^{2}}}{Mg\sqrt{2}a}}=2\pi \sqrt{1.5\frac{a}{g}}
```

:::
````
```{figure} ../images/ch-10/459974_1_En_10_Fig19_HTML.png
:name: fig-10-19

The torsional pendulum
```

(sec-10-3-6)=
### 10.3.6 The Torsional Pendulum

The torsional pendulum consists of a rigid body suspended by a wire from its center of mass where the other end of the wire is fixed as shown in [](#fig-10-19). The body is in equilibrium if the wire is untwisted. If the body is rotated through an angle $\theta$ it will oscillate about its equilibrium position (the line OP) due to a restoring torque exerted by the twisted wire on the body. This torque is found to be directly proportional to the angular displacement of the body. That is

```{math}
\tau =-k\theta
```

where *k* is called the torsional constant. Its value depends on the property of the wire. Note that this equation is the rotational analogue of Hook’s law in linear form $(F=-kx)$. From Newton’s second law, we have

```{math}
\tau =I\alpha
```

or

```{math}
-k\theta =I\ddot{\theta }
```

That gives

```{math}
\ddot{\theta }+\bigg (\frac{k}{I}\bigg )\theta =0
```

or

```{math}
\ddot{\theta }+\omega _{n}^{2}\theta =0
```

where $\omega _{n}=\sqrt{k/I}$ and the period is $T=2\pi \sqrt{I/k}.$

````{prf:example}
:label: example-10-16
:enumerator: 10.16

A uniform solid sphere of mass of 4.7 kg and radius of 5 cm is suspended at its midpoint by a light string (see [](#fig-10-20)) where it oscillates as a torsional pendulum. If the period of motion is 3.5 $\mathrm {s}$, find the torsion constant.


:::{admonition} Solution 10.16
:class: dropdown

```{math}
T=2\pi \sqrt{\frac{I}{k}}
```

for a uniform solid sphere

```{math}
I_{cm}=\frac{2}{5}MR^{2}=\frac{2}{5}(4.7 \; \mathrm {k}\mathrm {g})(0.05 \; \mathrm {m})^{2}=4.7\times 10^{-3} \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}
```

hence,

```{math}
k=\frac{4\pi ^{2}I_{cm}}{T}=\frac{4(3.14)^{2}(4.7\times 10^{-3} \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2})}{(3.5 \; \mathrm {s})}=0.05 \; \mathrm {k}\mathrm {g}\,\mathrm {m}^{2}/\mathrm {s}^{2}
```

:::
````
```{figure} ../images/ch-10/459974_1_En_10_Fig20_HTML.png
:name: fig-10-20

A uniform solid sphere suspended at its midpoint by a light string
```

(sec-10-4)=
## 10.4 Damped Free Vibrations

In this section, we will discuss the case in which the effect of damping that is due to a nonconservative force cannot be neglected. An example of such a force in mechanical systems is the force of friction. In this case, the mechanical energy of the system will be lost, the amplitude of motion will decrease to zero, and the oscillation dies out eventually. Here, we will discuss damping due to friction in the simplest case, where the frictional force is proportional to the first power of the velocity of the oscillating body. An example of such a frictional force is the force that an object experience when moving in a fluid with a low speed and is given by

```{math}
F_{D}=-bv
```

where *b* is a positive constant called the damping coefficient. Its SI units is $\mathrm {N}(\mathrm {m}\,\mathrm {s}^{-1})=\mathrm {k}\mathrm {g}\,\mathrm {s}^{-1}$. The negative sign shows that the direction of the force is always opposite to the velocity. Now consider the spring–mass system as shown in [](#fig-10-21), the cylinder shown in the figure contains a viscous fluid and a piston moving in it. Such device is known as the viscous damper. The net force on the oscillating body is

```{figure} ../images/ch-10/459974_1_En_10_Fig21_HTML.png
:name: fig-10-21

A mass-spring system with damping
```

```{math}
\sum F=F_{s}+F_{D}=-kx-bv
```

hence

```{math}
m\ddot{x}+b\dot{x}+kx=0
```

or

```{math}
:label: eq-10-13

\begin{aligned} \ddot{x}+\gamma \dot{x}+\omega _{n}^{2}x=0 \end{aligned}
```

where $\gamma =b/m$ and $\omega _{n}=\sqrt{k/m}$. The units of $\gamma$ is $\mathrm {s}^{-1}$. This equation is a second order linear differential equation of constant coefficients. We may assume a solution of the form

```{math}
x=Ce^{\lambda t}
```

Substituting this solution into [](#eq-10-13) gives the characteristic (auxiliary) equation given by

```{math}
\lambda ^{2}+\gamma \lambda +\omega _{n}^{2}=0
```

The roots of this equation are given by

```{math}
\lambda _{1}=-\frac{\gamma }{2}+\sqrt{\bigg (\frac{\gamma ^{2}}{4}-\omega _{n}^{2}\bigg )}
```

and

```{math}
\lambda _{2}=-\frac{\gamma }{2}-\sqrt{\bigg (\frac{\gamma ^{2}}{4}-\omega _{n}^{2}\bigg )}
```

From superposition, the general solution is given by

```{math}
:label: eq-10-14

\begin{aligned} x=C_{1}e^{\lambda _{1}t}+C_{2}e^{\lambda _{2}t} \end{aligned}
```

Three possible solutions arise depending on whether the sign of the bracket $(\gamma ^{2}/4-\omega _{n}^{2})$ is positive, negative or zero, i.e., depending on the size of the damping force. The roots $\lambda _{1}$ and $\lambda _{2}$ are either distinct real roots, equal real roots or a conjugate complex roots. Therefore, there are three possible motions of the system.

(sec-10-4-1)=
### 10.4.1 Light Damping (Under-Damped) $(\gamma <2\omega _{n})$

If $\gamma <2\omega _{n}$ the resulting roots are complex roots given by

```{math}
\lambda _{1}=-\frac{\gamma }{2}+i\omega _{D}
```

and

```{math}
\lambda _{2}=-\frac{\gamma }{2}-i\omega _{D}
```

where

```{math}
\omega _{D}=\bigg (\omega _{n}^{2}-\frac{\gamma ^{2}}{4}\bigg )^{1_{/2}}
```

Hence, [](#eq-10-14) may be written as

```{math}
x=\bigg [C_{1}e^{i\omega _{D}t}+C_{2}e^{-i\omega _{D}t}\bigg ]e^{\frac{-\gamma }{2}t}
```

Since $e^{\pm ix}=\cos x\pm i\sin x$ we have

```{math}
x=[C_{1}(\cos \omega _{D}t+i\sin \omega _{D}t)+C_{2}(\cos \omega _{D}t-i\sin \omega _{D}t)]e^{\frac{-\gamma }{2}t}
```

```{math}
=[(C_{1}+C_{2})\cos \omega _{D}t+i(C_{1}-C_{2})\sin \omega _{D}t]e^{\frac{-\gamma }{2}t}
```

```{math}
:label: eq-10-15

\begin{aligned} =[A_{1}\cos \omega _{D}t+A_{2}\sin \omega _{D}t]e^{\frac{-\gamma }{2}t} \end{aligned}
```

where $A_{1}=C_{1}+C_{2}$ and $A_{2}=i(C_{1}-C_{2})$. As mentioned earlier [](#eq-10-15) can be written as

```{math}
:label: eq-10-16

\begin{aligned} x=A\cos (\omega _{D}t-\phi )e^{\frac{-\gamma }{2}t} \end{aligned}
```

where *A* is the initial amplitude of motion. $Ae^{\frac{-\gamma }{2}t}$ is called the amplitude of motion and $\phi$ is the phase constant and $\omega _{D}$ is the angular frequency of the damped motion. This equation shows that the system oscillates in a decreasing harmonic motion where the amplitude of motion decreases exponentially with time until eventually the oscillation dies out (see [](#fig-10-22)). The dashed lines in [](#fig-10-22) are called the envelope of the oscillation curve. The period of motion in light damping is therefore given by

```{math}
\tau _{D}=\frac{2\pi }{\omega _{D}}=\frac{2\pi }{\sqrt{\omega _{n}^{2}-\frac{\gamma ^{2}}{4}}}
```

If $b=0$ and thus $\gamma =0$ the period of motion is reduced to that of a simple harmonic oscillator. If $\gamma \ll \omega _{D}$, the situation is referred to as very light damping and $\omega _{D}\approx \omega _{n}$. Furthermore if there are two amplitudes $A_{a}$ and $A_{b}$ separated by the period of motion, then their ratio is given by

```{math}
\frac{A_{a}}{A_{b}}=\frac{Ae^{-\frac{\gamma }{2}t_{1}}}{Ae^{-\frac{\gamma }{2}(t_{1}+\tau _{D})}}=e^{\frac{\gamma }{2}\tau _{D}}
```

A quantity known as the logarithmic decrement is defined as

```{math}
\delta =\ln \bigg (\frac{A_{a}}{A_{b}}\bigg )=\frac{\gamma }{2}\tau _{D}
```

```{figure} ../images/ch-10/459974_1_En_10_Fig22_HTML.png
:name: fig-10-22

In A lightly damped oscillator, the system oscillates in a decreasing harmonic motion where the amplitude of motion decreases exponentially with time until eventually the oscillation dies out
```

````{prf:example}
:label: example-10-17
:enumerator: 10.17

An 8 kg block is attached to a light spring and a light viscous damper. If at $t=0, x=0.12 \; \mathrm {m}$ and $v=0$, find (a) the displacement at any time; (b) the logarithmic decrement. $(k=30 \; \mathrm {N}/\mathrm {m},\ b=20 \; \mathrm {N}\,\mathrm {s}/\mathrm {m})$.


:::{admonition} Solution 10.17
:class: dropdown

(a)

```{math}
\omega _{n}=\sqrt{\frac{k}{m}}=\sqrt{\frac{(30 \; \mathrm {N}/\mathrm {m})}{(8 \; \mathrm {k}\mathrm {g})}}=1.9 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

```{math}
\gamma =\frac{b}{m}=\frac{(20 \; \mathrm {N}\,\mathrm {s}/\mathrm {m})}{(8 \; \mathrm {k}\mathrm {g})}=2.5 \; \mathrm {s}^{-1}
```

and

```{math}
\omega _{D}=\bigg (\omega _{n}^{2}-\frac{\gamma ^{2}}{4}\bigg )^{1_{/2}}=((1.9 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})^{2}-(2.5 \; \mathrm {N} \mathrm {s}/\mathrm {m}\,\mathrm {k}\mathrm {g})^{2}4)^{1_{/2}}=1.43 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}
```

since $\gamma <2\omega _{\mathrm {n}}$, the damping is light. The displacement as a function of time is given by

```{math}
x=A\cos (\omega _{D}t-\phi )e^{\frac{-\gamma }{2}t}
```

or

```{math}
x=A\cos (1.43t-\phi )e^{-1.25t}
```

since at $t=0, x=0.12 \; \mathrm {m}$, then

```{math}
:label: eq-10-17

\begin{aligned} (0.12 \; \mathrm {m})=A\cos \phi \end{aligned}
```

the velocity of the block at any time is

```{math}
\dot{x}=-1.43A\sin (1.43t-\phi )e^{-1.25t}-1.25A\cos (1.43t-\phi )e^{-1.25t}
```

at $t=0, v=0$ and thus

```{math}
:label: eq-10-18

\begin{aligned} 0=-1.43A\sin \phi -1.25A\cos \phi \end{aligned}
```

Solving Eqs. 10.17 and 10.18 for *A* and $\phi$ gives $\phi =-0.7$ rad and $A=0.17 \; \mathrm {m}.$ Therefore,

```{math}
x=0.17\cos (1.43t-0.7)e^{-1.25t}
```

(b)

```{math}
\tau _{D}=\frac{2\pi }{\omega _{D}}=\frac{2\pi }{(1.43 \; \mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s})}=4.4 \; \mathrm {s}
```

```{math}
\delta =\frac{\gamma }{2}\tau _{D}=(1.25 \; \mathrm {s}^{-1})(4.4 \; \mathrm {s})=5.5
```

:::
````
(sec-10-4-2)=
### 10.4.2 Critically Damped Motion $(\gamma =2\omega _{n})$

If $\gamma =2\omega _{n}$, then the roots are equal real roots

```{math}
\lambda _{1}=\lambda _{2}=-\frac{\gamma }{2}=-\omega _{n}
```

In that case, the motion decays without oscillation (see [](#fig-10-23)) and the general solution of [](#eq-10-13) is

```{math}
x=(C_{1}+C_{2}\omega _{n}t)e^{-\omega _{n}t}
```

$C_{1}$ and $C_{2}$ are found from boundary conditions. If at $t=0, x=A$, and $v=0,$ then

```{math}
x(0)=C_{1}=A
```

and

```{math}
v(0)=\omega _{n}C_{2}-\omega _{n}C_{1}=0
```

or

```{math}
C_{1}=C_{2}=A
```

That gives

```{math}
x=A(1+\omega _{n}t)e^{-\omega _{n}t}
```

```{figure} ../images/ch-10/459974_1_En_10_Fig23_HTML.png
:name: fig-10-23

In a critically damped motion, the motion decays without oscillation
```

(sec-10-4-3)=
### 10.4.3 Over Damped Motion (Heavy Damping) $(\gamma >2\omega _{n})$

If $\gamma >2\omega _{n}$, the roots are distinct real roots given by

```{math}
\lambda _{1}=-\frac{\gamma }{2}+\sqrt{\bigg (\frac{\gamma ^{2}}{4}-\omega _{n}^{2}\bigg )}
```

and

```{math}
\lambda _{2}=-\frac{\gamma }{2}-\sqrt{\bigg (\frac{\gamma ^{2}}{4}-\omega _{n}^{2}\bigg )}
```

The general solution is given by

```{math}
x=C_{1}e^{\lambda _{1}t}+C_{2}e^{\lambda _{2}t}
```

or

```{math}
x=(C_{1}e^{\alpha t}+C_{2}e^{-\alpha t})e^{-\frac{\gamma }{2}t}
```

where

```{math}
\alpha =\sqrt{\bigg (\frac{\gamma ^{2}}{4}-\omega _{n}^{2}\bigg )}
```

$C_{1}$ and $C_{2}$ are found from boundary conditions. As critical damping, the resulting motion here is nonperiodic but the system returns to its equilibrium position at large values of *t* unlike critical damping (see [](#fig-10-24)).

```{figure} ../images/ch-10/459974_1_En_10_Fig24_HTML.png
:name: fig-10-24

As critical damping, the resulting motion here is non-periodic but the system returns to its equilibrium position at large values of *t* unlike critical damping
```

````{prf:example}
:label: example-10-18
:enumerator: 10.18

In [](#example-10-17), find the range of values of the damping coefficient for the system to be: (a) over damped; (b) critically damped.


:::{admonition} Solution 10.18
:class: dropdown

(a) over damped if $\gamma >2\omega _{n}$, i.e., if $\gamma >3.8\mathrm {s}^{-1}(\mathrm {b})$ critically damped if $\gamma =3.8\mathrm {s}^{-1}.$

:::
````
(sec-10-4-4)=
### 10.4.4 Energy Decay

In damped free vibrations, the total mechanical energy is not constant since the damping force opposes the motion and dissipates the energy of the system. Now, consider the mass–spring system, the total mechanical energy of the system is

```{math}
E=K+U=\frac{1}{2}m\dot{x}^{2}+\frac{1}{2}kx^{2}
```

The rate of change of energy is

```{math}
\frac{dE}{dt}=(m\ddot{x}+kx)\dot{x}
```

For damped vibrations in which the damping force is directly proportional to the velocity, we have

```{math}
m\ddot{x}+kx=-b\dot{x}
```

Hence,

```{math}
\frac{dE}{dt}=-b\dot{x}^{2}\le 0
```

Thus, the energy decreases with time in any damped motion and the rate in which it decreases is not uniform.

(sec-10-5)=
## 10.5 Forced Vibrations

In the previous sections, only free vibrations have been considered (i.e., vibrations in which only a restoring and damping force act within the system during motion). This section considers the case in which an external driving force is applied to the vibrator. This force is given as a function of time and we have

```{math}
:label: eq-10-19

\begin{aligned} m\ddot{x}+b\dot{x}+kx=F(t) \end{aligned}
```

Here, we will consider the case in which the force is a simple periodic force given by

```{math}
:label: eq-10-20

\begin{aligned} F(t)=F_{0}\cos \omega t \end{aligned}
```

where $F_{0}$ is the amplitude and $\omega$ is the driving frequency. This force does positive work on the system to balance the energy loss due to damping. Substituting [](#eq-10-20) into [](#eq-10-19) gives

```{math}
:label: eq-10-21

\begin{aligned} m\ddot{x}+b\dot{x}+kx=F_{0}\cos \omega t \end{aligned}
```

or

```{math}
\ddot{x}+\gamma \dot{x}+\omega _{n}^{2}x=\frac{F_{0}\cos \omega t}{m}
```

Let us assume that the solution of [](#eq-10-19) is given by

```{math}
x=C_{1}\cos \omega t+C_{2}\sin \omega t
```

then, we have

```{math}
\dot{x}=-\omega C_{1}\sin \omega t+\omega C_{2}\cos \omega t
```

and

```{math}
\ddot{x}=-\omega ^{2}C_{1}\cos \omega t-\omega ^{2}C_{2}\sin \omega t
```

Substituting into [](#eq-10-19) gives

```{math}
\begin{aligned}&(-\omega ^{2}C_{1}\cos \omega t-\omega ^{2}C_{2}\sin \omega t)+\gamma (-\omega C_{1}\sin \omega t+\omega C_{2}\cos \omega t) \nonumber \\&+\omega _{n}^{2}(C_{1}\cos \omega t+C_{2}\sin \omega t)=\frac{F_{0}\cos \omega t}{m} \end{aligned}
```

That gives

```{math}
-\omega ^{2}C_{1}+\gamma \omega C_{2}+\omega _{n}^{2}C_{1}=\frac{F_{0}}{m}
```

and

```{math}
-\omega ^{2}C_{2}-\gamma \omega C_{1}+\omega _{n}^{2}C_{2}=0
```

Solving for $C_{1}$ and $C_{2}$ gives

```{math}
C_{1}=\frac{({F_{0}}/{m})(\omega _{n}^{2}-\omega ^{2})}{(\omega ^{2}-\omega _{n}^{2})^{2}+\gamma ^{2}\omega ^{2}}
```

and

```{math}
C_{2}=\frac{({F_{0}}/{m})\gamma \omega }{(\omega ^{2}-\omega _{n}^{2})^{2}+\gamma ^{2}\omega ^{2}}
```

Hence,

```{math}
x=\frac{({F_{0}}/{m})[(\omega _{n}^{2}-\omega ^{2})\cos \omega t+\gamma \omega \sin \omega t]}{(\omega ^{2}-\omega _{n}^{2})^{2}+\gamma ^{2}\omega ^{2}}
```

The term in brackets is of the form $A_{1}\cos \omega t+A_{2}\sin \omega t$ and thus it can be written as $A'\cos (\omega t-\phi )$ where

```{math}
A'=\sqrt{A_{1}^{2}+A_{2}^{2}}
```

i.e.,

```{math}
A'=((\omega _{n}^{2}-\omega ^{2})^{2}+\gamma ^{2}\omega ^{2})^{\frac{1}{2}}
```

and

```{math}
\phi =\tan ^{-1}\frac{A_{2}}{A_{1}}=\tan ^{-1}\frac{\gamma \omega }{(\omega ^{2}-\omega _{n}^{2})}
```

where $0\le \phi \le \pi$. Hence,

```{math}
:label: eq-10-22

\begin{aligned} x=\frac{(^{F_{0}}/_{m})}{\sqrt{(\omega ^{2}-\omega _{n}^{2})^{2}+\gamma ^{2}\omega ^{2}}}\cos (\omega t-\phi ) \end{aligned}
```

If the driving force is applied for a long time compared with the time that the damped vibration dies out, then the system will eventually vibrate at the same frequency of the deriving force. Therefore, the general solution of [](#eq-10-13) is called the transient solution since it approaches zero in a relativity short time whereas [](#eq-10-21) is called the steady-state solution where the system oscillates with the same frequency as the deriving force. Therefore, the amplitude of a steady-state vibration is

```{math}
A=\frac{({F_{0}}/_{m})}{\sqrt{(\omega ^{2}-\omega _{n}^{2})^{2}+\gamma ^{2}\omega ^{2}}}
```

When the deriving frequency $\omega$ approaches the natural frequency of the system $\omega _{D}$, the amplitude of the resulting forced oscillation will increase. This is known as resonance. If the damping is very light, the amplitude reaches its peak when the deriving frequency is nearly equal to the natural frequency $\omega _{n}$. As the damping becomes heavier, the maximum amplitude shifts to lower frequencies (see [](#fig-10-25)). In the case where there is no damping at all $(b=0)$, the amplitude of resonance is infinite at $\omega =\omega _{n}.$

```{figure} ../images/ch-10/459974_1_En_10_Fig25_HTML.png
:name: fig-10-25

When the deriving frequency $\omega$ approaches the natural frequency of the system $\omega _{D}$, the amplitude of the resulting forced oscillation will increase. This is known as resonance. If the damping is very light the amplitude reaches its peak when the deriving frequency is nearly equal to the natural frequency $\omega _{n}$. As the damping becomes heavier, the maximum amplitude shifts to lower frequencies
```

````{prf:example}
:label: example-10-19
:enumerator: 10.19

In [](#example-10-17), if a driving force of the form $F(t)=5\cos 4t$ is applied to the system, find the steady-state displacement as a function of time.


:::{admonition} Solution 10.19
:class: dropdown

```{math}
A=\frac{({F_{0}}/_{m})}{\sqrt{(\omega ^{2}-\omega _{n}^{2})^{2}+\gamma ^{2}\omega ^{2}}}=\frac{({5}/8)}{\sqrt{((4)^{2}-(1.9)^{2})^{2}+(2.5)^{2}(4)^{2}}}=0.04 \; \mathrm {m}
```

```{math}
\phi =\tan ^{-1}\frac{\gamma \omega }{(\omega ^{2}-\omega _{n}^{2})}=\tan ^{-1}\ \frac{(2.5)(4)}{((4)^{2}-(1.9)^{2})}=0.8^{\circ }
```

Hence,

```{math}
x=0.04\cos (4t-0.8)
```

Therefore, the forced vibration has the same frequency as the deriving force but lag in phase by $0.8^{\circ }$

:::
````
````{prf:example}
:label: example-10-20
:enumerator: 10.20

In Example (10.17), find the steady-state displacement as a function of time if there is no damping.


:::{admonition} Solution 10.20
:class: dropdown

The amplitude of the forced oscillation when the angular frequency $\omega$ of the deriving force is varied.

```{math}
A=\frac{({F_{0}}/_{m})}{\sqrt{(\omega ^{2}-\omega _{n}^{2})^{2}+\gamma ^{2}\omega ^{2}}}=\frac{({5}/{8})}{\sqrt{((4)^{2}-(1.9)^{2})^{2}}}=0.05 \; \mathrm {m}
```

$x=0.05\cos 4t,\; \phi =0.$

:::
````
**Problems**

```{exercise}
:label: prob-10-1
:enumerator: 10.1

A 2 kg block is fastened to a spring of force constant 98 $\mathrm {N}/\mathrm {m}$ on a horizontal frictionless surface. If the block is released a distance of 6 cm from its equilibrium position, find (a) the angular frequency, the frequency and the period of the resulting motion, (b) the time it takes the block to first reach $x=-5$ cm and its velocity at that time, (c) the maximum speed and maximum acceleration of the oscillating block, (d) the total mechanical energy of the oscillator.

```

```{exercise}
:label: prob-10-2
:enumerator: 10.2

A 10 kg block is attached to a light spring of force constant 200 $\mathrm {N}/\mathrm {m}$ on a smooth horizontal surface. Find the amplitude of motion if at $x=0.06 \; \mathrm {m}$ the velocity of the block is $v=0.5 \; \mathrm {m}/\mathrm {s}.$

```

```{exercise}
:label: prob-10-3
:enumerator: 10.3

A particle rotate counterclockwise in a circle of radius 0.2 $\mathrm {m}$ with a constant angular speed of 2 $\mathrm {r}\mathrm {a}\mathrm {d}/\mathrm {s}$. If at $t=0$ the $\mathrm {x}$-coordinate of the particle is 0.14 $\mathrm {m}$, find the displacement, velocity and acceleration of the particle at any time.

```

```{exercise}
:label: prob-10-4
:enumerator: 10.4

If a simple pendulum has a period of 2 $\mathrm {s}$, find its period when its length is increased by $20\%$.

```

```{exercise}
:label: prob-10-5
:enumerator: 10.5

A simple pendulum of length lm and mass of 0.4 kg oscillates in a region where $g=9.8 \; \mathrm {m}/\mathrm {s}^{2}$. If the amplitude of oscillation is $10^{\circ }$, find (a) the angular displacement, angular velocity and angular acceleration of the pendulum as a function of time.

```

```{exercise}
:label: prob-10-6
:enumerator: 10.6

A uniform solid cylinder of radius *R* and mass *M* rolls without slipping on a track of radius 4*R* as shown in [](#fig-10-26). Find the period of oscillation when the cylinder is displaced slightly from its equilibrium position.

```

```{exercise}
:label: prob-10-7
:enumerator: 10.7

A planer body of mass 3 kg oscillates as a physical pendulum. If the period of oscillation is 3 $\mathrm {s}$ and if the pivot point is at 0.2 $\mathrm {m}$ from the center of mass, find the moment of inertia of the body.

```

```{exercise}
:label: prob-10-8
:enumerator: 10.8

A uniform hollow cylinder of radius *R* and mass *M* is suspended at its midpoint from a wire and form a torsional pendulum. If the period of motion is *T*, find the torsion constant.

```

```{exercise}
:label: prob-10-9
:enumerator: 10.9

For the system shown in [](#fig-10-27), determine the displacement of the block at any time if at $t=0, x=0$ and $v=0.\,(k=200 \; \mathrm {N}/\mathrm {m},\ b=200 \; \mathrm {N}\,\mathrm {s}/\mathrm {m})$.

```

```{exercise}
:label: prob-10-10
:enumerator: 10.10

For the system shown in [](#fig-10-28), find the steady-state displacement as a function of time.

```

```{figure} ../images/ch-10/459974_1_En_10_Fig26_HTML.png
:name: fig-10-26

A uniform solid cylinder of radius *R* and mass *M* rolls without slipping on a track of radius 4*R*
```

```{figure} ../images/ch-10/459974_1_En_10_Fig27_HTML.png
:name: fig-10-27

A damped oscillator
```

```{figure} ../images/ch-10/459974_1_En_10_Fig28_HTML.png
:name: fig-10-28

A forced oscillator
```
