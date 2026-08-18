---
title: 3. Newton’s Laws
short_title: "Ch. 3 — Newton's Laws"
label: ch-3
doi: 10.1007/978-3-030-15195-9_3
---

(sec-3-1)=
## 3.1 Introduction

In this chapter, dynamics which is a branch of mechanics will be discussed. Dynamics is concerned with the cause behind the motion of objects and answers questions such as: Why does a skydiver float in air? What makes an apple fall from a tree? Why a block connected to a spring oscillates when the spring is stretched? We will find that these motions occur when objects interact with each other, i.e., the apple is interacting with earth, the skydiver is interacting with air, and the block is interacting with the spring.

### 3.1.1 The Concept of Force

The interaction between one object and another or between the object and its environment defines a quantity called force. A force is a pull or a push in a certain direction that may cause the object to move or deform. However, motion does not always occur if the force is not large enough to overcome other forces such as friction or gravity But whether or not an object moves due to a force, there is always some deformation. In this book, it is assumed that objects remain undeformed under the influence of any forces. Experimentally, a force is found to be a vector quantity The net external force acting on an object (the vector sum of all forces acting on the object) causes the object to accelerate where the direction of the acceleration is in the direction of that force.

Hence, acceleration is a measure of force. If the net force equals zero, the acceleration of the object is zero, and the velocity of the object remains unchanged (constant). Forces in nature are one of two:

1. *Contact forces* resulting from direct contact between two objects (e.g., kicking a ball or punching a bag);
2. *Field forces* that can act through empty space and in which physical contact is not necessary (e.g., gravitational force between two objects and the electric force between two electric charges).

### 3.1.2 The Fundamental Forces in Nature

The following fundamental forces are all field forces:

1. The gravitational force between any two objects;
2. The electromagnetic force between two electric charges;
3. The strong nuclear force between subatomic particles which is responsible for the stability of the nuclei;
4. The weak nuclear force which produces certain kinds of radioactive decay and is responsible for the instability of some nuclei.

The first two fundamental forces are examples of long-range forces, which act over a great distance. The second two are examples of short-range forces, which are forces that act over a very short distance. Note that contact forces are fundamentally electromagnetic since they involve electromagnetic forces between the atoms of the surfaces in contact.

(sec-3-2)=
## 3.2 Newton’s Laws

Sir Isaac Newton (1642–1727) formulated his three famous laws of motion describing the relationship between the force acting on an object and the acceleration of that object. Newtonian or classical mechanics which is based mainly on Newton’s three laws of motion, deals only with objects that are

- Large compared to the size of an atom $({\approx }10^{-10}\,\mathrm {m})$.
- Moving at speeds much less than the speed of light $({\approx }3\times 10^{8}\,\mathrm {m}/\mathrm {s})$.

Einstein’s special theory of relativity replaces Newtonian mechanics when an object’s speed approaches the speed of light. On the other hand, quantum mechanics replaces Newtonian mechanics when the object’s dimensions are close to atomic scale.

### 3.2.1 Newton’s First Law

It was believed long ago that a force is necessary to keep an object moving and that any object’s natural state is to be at rest. Later, these statements were proved to be incorrect. To understand this, suppose a block resting on a surface is given a push and is released. As a result, the block will slide for sometime before coming to rest. The time elapsed between pushing the block until it comes to rest will increase as the surface gets smoother. If the surface becomes so smooth, such that friction is almost negligible, the block will continue to move along a straight line with constant speed for a greater distance before coming to rest.

An example of frictionless motion is the motion of the puck in the air-hockey table. The puck floats on a thin column of air that is used as the lubricant. In situations where there is no friction at all, the object will continue to move along a straight line with constant speed without requiring any force to keep it moving. However, a force is required to initiate motion. This concept was formulated by Newton and became his first law of motion: *An object at rest remains at rest and an object in motion will continue in motion with constant velocity* (*constant speed in a straight line*) *unless acted upon by a net external force*. That is, if

```{math}
\Sigma \mathbf {F}=\mathbf {0}
```

```{math}
\mathbf {a}=\mathbf {0}
```

A body’s tendency to stay at rest or maintain uniform motion in a straight line is called inertia. Thus, Newton’s first law is often referred to as the law of inertia, where it defines specific kinds of reference frames called inertial reference frames. An inertial reference frame is a frame in which Newton’s first law is valid. That is, in an inertial frame of reference, an object has no acceleration if there is no net force acting upon it. Any reference frame moving with constant velocity relative to an inertial frame is also inertial. Observers in different inertial frames measure the same acceleration for a moving object. To prove this, consider the two inertial reference frames $\mathrm {S}$ and $\mathrm {S}'$ mentioned in Sect. [](#sec-2-5), where $\mathrm {S}$ is stationary and $\mathrm {S}'$ is moving with constant velocity relative to S. By differentiating Eq. [](#eq-2-20), we have

```{math}
\frac{d\mathbf {v}_{PS}}{dt}=\frac{d\mathbf {v}_{PS'}}{dt}+\frac{d\mathbf {v}_{S'S}}{dt}
```

Because $\mathbf {v}_{S'S}$ is constant we have

```{math}
\mathbf {a}_{PS}=\mathbf {a}_{PS'}
```

That is, the acceleration of the particle $\mathrm {P}$ measured from both inertial reference frames $\mathrm {S}$ and $\mathrm {S}'$ is the same. To show that Newton’s first law is only valid when applied with respect to an inertial frame of reference; consider a girl named Mia that is at rest while watching her friend Lea driving a car moving at constant velocity. Lea has her seatbelt fastened and put her suitcase in the seat right next to her without restraining it. Now, suppose that Lea steps on the brakes, which would cause her vehicle to decelerate, her suitcase will start to move forward. According to Lea, who is in an accelerated frame, the suitcase moved from rest even though there was no apparent net external force acting on it. Therefore, in Lea’s frame, Newton’s first law seems to be incorrect.

The situation, however, is different to Mia, who is in an inertial frame of reference. In her perspective, the suitcase was initially moving with constant velocity and the net force on it was zero. When the car started to decelerate, the net force on the suitcase is still equal to zero and thus the suitcase must continue to move forward with constant velocity and stop by friction or impact with the inside of the car. Therefore, it is apparent to Mia that Newton’s first law is valid. From the previous example, we conclude that Newton’s first law (and in general Newton’s laws) is not valid in all kinds of reference frames; it is only valid when applied with respect to inertial frames. That is, Lea must not apply Newton’s first law in her reference frame.

The same situation would be observed by Lea if she were to turn her car while moving. When the car turns, the suitcase will start to move in the direction opposite to the turn. Once again, Lea observes that the suitcase has moved from rest without any apparent force acting on it which contradicts Newton’s first law in her opinion. Mia sees no contradiction with Newton’s first law because when the car turns, the suitcase tends to continue its initial uniform straight line motion, and thus it moves toward the direction opposite to the turn. Therefore Newton’s laws are obeyed by objects when observed from inertial frames of reference (see [](#fig-3-1)).

To apply classical (Newtonian) mechanics with respect to a noninertial reference frame, new forces named as pseudo forces are introduced. In this book, only inertial frames are used, and all laws are stated with respect to those frames. One convenient inertial frame of reference, used throughout this book, is the surface of the earth. The earth can be considered as an inertial frame since its motion about its axis and about the sun has a small effect on calculations and thus can be neglected.

```{figure} ../images/ch-03/459974_1_En_3_Fig1_HTML.png
:name: fig-3-1

The boy is throwing the water out by pitching the bucket forward. If he stops, the water will continue its motion along a straight line. However, because of the force of gravity, it follows a parabolic path
```

### 3.2.2 The Principle of Invariance

Some quantities such as mass, force, time, and acceleration are invariant, which means that they have the same numerical values when measured in different inertial frames of reference. Other quantities such as velocity, kinetic energy, and work have different values in different inertial frames. However, the laws of physics have the same form in all inertial frames of reference. This is called the principle of invariance.

### 3.2.3 Mass

As mentioned earlier, the tendency of an object to resist any change in its motion (i.e., to remain at rest or maintain uniform motion along a straight line) is called inertia. From experiments and everyday experience, it is observed that a certain force produces different accelerations when applied to different bodies. This variation in the produced acceleration depends upon the quantity of matter contained in the body Such quantity is known as the mass of the body Therefore, mass is a measure of inertia. Objects with large masses have less acceleration when exposed to the same force. Thus, mass is a quantity that relates the acceleration of the body to the force acting on it. The SI unit of mass is the kilogram (kg). Experimentally, it is found that the ratio of the masses of any two bodies (say $m_{1}$ and $m_{2}$) is equal to the inverse of the ratio of the magnitudes of their accelerations if both are acted upon by the same force. That is, we have

```{math}
\frac{m_1}{m_2}=\frac{a_2}{a_1}
```

The mass of any body can be found by comparing its acceleration to the acceleration of a 1 kg mass when both bodies are acted upon by the same force. This leads to the conclusion that mass is independent of force; it is an inherent characteristic of matter. Furthermore, it has been experimentally proved that when two masses $m_{1}$ and $m_{2}$ are attached together, the combined body behaves as a single body of mass $m_{1}+m_{2}$. Thus, mass is a scalar quantity and obeys the rules of ordinary arithmetic.

### 3.2.4 Newton’s Second Law

Unlike Newton’s first law, Newton’s second law describes the situation in which the net force acting on an object is not zero. It was found that when different forces act on an object, the object undergoes different accelerations. The magnitude of the acceleration is directly proportional to the magnitude of the applied force, and its direction is in the direction of that force. Furthermore, this acceleration is inversely proportional to the mass of the object for a certain applied force. These observations are summarized in Newton’s second law of motion: *The acceleration of an object produced by a net external force is directly proportional to the force in a direction parallel to that force and is inversely proportional to its mass* That is,

```{math}
\Sigma \mathbf {F}=m\mathbf {a}
```

In terms of components, the vector equation $\Sigma \mathrm {F}=m\mathrm {a}$ can be written as

```{math}
\Sigma F_{x}=ma_{x}
```

```{math}
\Sigma F_{y}=ma_{y}
```

```{math}
\Sigma F_{z}=ma_{z}
```

where $a_{x}=\ddot{x}, a_{y}=\ddot{y}$ and $a_{z}=\ddot{z}$ In terms of normal and tangential coordinates, the net normal force is

```{math}
\Sigma F_{n}=ma_{n}
```

and the net tangential force is

```{math}
\Sigma F_{t}=ma_{t}
```

where $a_{n}=v^{2}/R$ and $a_{t}=dv/dt$. Finally, in terms of polar coordinates we have

```{math}
\Sigma F_{r}=ma_{r}
```

and

```{math}
\Sigma F_{\theta }=ma_{\theta }
```

where $a_{r}=(\ddot{r}-r\dot{\theta }^{2})$ and $a_{\theta }=(r\ddot{\theta }+2\dot{r}\dot{\theta })$. The unit of force in the SI system is the Newton (N). One Newton (1N) is defined as the force that gives a 1 kg mass an acceleration of 1 $\mathrm {m}/\mathrm {s}^{2}$.

```{math}
1\,\mathrm {N}=1\,\mathrm {k}\mathrm {g}\cdot \mathrm {m}/\mathrm {s}^{2}
```

````{prf:example}
:label: example-3-1
:enumerator: 3.1

A body is exposed to three forces acting in different directions as shown in [](#fig-3-2). Find the magnitude and direction of the resultant force acting on the body and the corresponding acceleration.

```{figure} ../images/ch-03/459974_1_En_3_Fig2_HTML.png
:name: fig-3-2

A body is exposed to three forces acting in different directions
```

:::{admonition} Solution 3.1
:class: dropdown

The net force in the $\mathrm{x}$-direction is

```{math}
\sum F_{x}=F_{1x}+F_{2x}+F_{3x}=F_{1}\cos 60^{\circ}+F_{2}\cos 20^{\circ}-F_{3}\cos 30^{\circ}
```

```{math}
=(100\,\mathrm {N})(0.5)+(50\,\mathrm {N})(0.94)-(75\,\mathrm {N})(0.866)=32.1\,\mathrm {N}
```

The net force in the $\mathrm{y}$-direction is

```{math}
\sum F_{y}=F_{1y}+F_{2y}+F_{3y}=F_{1}\sin 60^{\circ}-F_{2}\sin 20^{\circ}-F_{3}\sin 30^{\circ}
```

```{math}
=(100\,\mathrm {N})(0.866)-(50\,\mathrm {N})(0.34)-(75\,\mathrm {N})(0.5)=32.1\,\mathrm {N}
```

The magnitude of the net force is

```{math}
F_{net}=\sqrt{(32.1)^{2}+(32.1)^{2}}=45.4\,\mathrm {N}
```

The direction of $F_{net}$ relative to the $\mathrm{x}$-axis is

```{math}
\theta =\tan ^{-1}\frac{F_{nety}}{F_{netx}}=\tan ^{-1}\frac{(32.1\mathrm {N})}{(32.1\,\mathrm {N})}=45^{\circ}
```

The acceleration of the body is, therefore,

```{math}
a=\frac{F}{m}=\frac{(45.4\,\mathrm {N})}{(50\,\mathrm {k}\mathrm {g})}=0.91\,\mathrm {m}/\mathrm {s}^{2}
```

and its direction is the same as that of the force.
:::
````

````{prf:example}
:label: example-3-2
:enumerator: 3.2

If a man pushes a 60 kg box with a constant horizontal force of 100 $\mathrm {N}$: (a) how far will the container be moved when its speed reaches a value of 3 $\mathrm {m}/\mathrm {s}$; (b) how far will the container be moved when its speed reaches a value of 3 $\mathrm {m}/\mathrm {s}$ if the same force is applied at $30^{\circ}$ to the horizontal; (c) find the normal force acting on the block in (a) and (b).

:::{admonition} Solution 3.2
:class: dropdown

(a) The acceleration of the container is given by

```{math}
a=\frac{F}{m}=\frac{(100\,\mathrm {N})}{(60\,\mathrm {k}\mathrm {g})}=1.67\,\mathrm {m}/\mathrm {s}^{2}
```

the distance moved when its speed reaches 3 $\mathrm {m}/\mathrm {s}$ is found from

```{math}
v^{2}-v_{0}^{2}=2a(x-x_{0})
```

By taking $x_{0}=0$ at the starting point we have

```{math}
(3\,\mathrm {m}/\mathrm {s})^{2}-0=2(1.67\,\mathrm {m}/\mathrm {s}^{2})(x-0)
```

That gives $x=2.7\,\mathrm {m}.$

(b) If the force is at $30^{\circ}$ to the horizontal, the acceleration is

```{math}
a=\frac{F}{m}=\frac{(100\,\mathrm {N})\cos 30^{\circ }}{(60\,\mathrm {k}\mathrm {g})}=1.45\,\mathrm {m}/\mathrm {s}^{2}
```

```{math}
(3\,\mathrm {m}/\mathrm {s})^{2}-0=2(1.45\,\mathrm {m}/\mathrm {s}^{2})(x-0)
```

and $x=3.1\,\mathrm {m}.$

(c) In situation (a) we have

```{math}
\sum F_{y}=n-mg=0
```

and

```{math}
n=mg=(60\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})=588\,\mathrm {N}
```

In (b) we have

```{math}
\sum F_{y}=n+F\sin \theta -mg=0
```

and

```{math}
n=(588\,\mathrm {N})-(100\,\mathrm {N}) \sin 30^{\circ } =538\,\mathrm {N}
```
:::
````

````{prf:example}
:label: example-3-3
:enumerator: 3.3

A particle of mass 0.5 kg is moving along the curve given by $\mathbf {r}=(1/3t^{4}\mathbf {i}-t^{3}\mathbf {j})\,\mathrm {m}$ where *t* is time. Determine the force acting on the particle.

:::{admonition} Solution 3.3
:class: dropdown

The force acting on the particle is

```{math}
\mathbf {F}=m\frac{d^{2}\mathbf {r}}{dt^{2}}=m\frac{d}{dt}(4/3t^{3}\mathbf {i}-3t^{2}\mathbf {j})=m(4t^{2}\mathbf {i}-6t\mathbf {j})
```

```{math}
=(0.5\,\mathrm {k}\mathrm {g})(4t^{2}\mathbf {i}-6t\mathbf {j})=(2t^{2}\mathbf {i}-3t\mathbf {j})\; \mathrm {N}
```
:::
````

````{prf:example}
:label: example-3-4
:enumerator: 3.4

A particle of mass of 1 kg is moving under the influence of a force given by

```{math}
\mathbf {F}=((12t^{2}-5t)\mathbf {i}+(9t-1)\mathbf {j}-3t^{2}\mathbf {k})\,\mathrm {N}
```

If at $t=0, \mathbf {r}_{0}=\mathbf {0}$ and $\mathbf {v}_{0}=\mathbf {0}$, find the velocity and the position of the particle at any time.

:::{admonition} Solution 3.4
:class: dropdown

```{math}
\mathbf {F}=m\mathbf {a}
```

```{math}
\mathbf {a}=\frac{\mathbf {F}}{m}=((12t^{2}-5t)\mathbf {i}+(9t-1)\mathbf {j}-3t^{2}\mathbf {k})\,\mathrm {m}/\mathrm {s}^{2}
```

```{math}
\mathbf {v}=\int \mathbf {a}dt=\bigg (4t^{3}-\frac{5}{2}t^{2}\bigg )\mathbf {i}+\bigg (\frac{9}{2}t^{2}-t\bigg )\mathbf {j}-t^{3}\mathbf {k}+\mathbf {c}_{1}
```

Since at $t=0$, $\mathbf {v}_{0}=\mathbf {0}$, then $\mathbf {c}_{1}=\mathbf {0}$ and the velocity at any time is

```{math}
\mathbf {v}=\bigg (\bigg (4t^{3}-\frac{5}{2}t^{2}\bigg )\mathbf {i}+\bigg (\frac{9}{2}t^{2}-t\bigg )\mathbf {j}-t^{3}\mathbf {k}\bigg )\,\mathrm {m}/\mathrm {s}
```

```{math}
\mathbf {v}=\frac{d\mathbf {r}}{dt}
```

```{math}
\mathbf {r}=\int \mathbf {v}dt=\int \bigg [\bigg (4t^{3}-\frac{5}{2}t^{2}\bigg )\mathbf {i}+\bigg (\frac{9}{2}t^{2}-t\bigg )\mathbf {j}-t^{3}\mathbf {k}\bigg ]dt
```

```{math}
\mathbf {r}=\bigg (\bigg (t^{4}-\frac{5}{6}t^{3}\bigg )\mathbf {i}+\bigg (\frac{3}{2}t^{3}-\frac{1}{2}t^{2}\bigg )\mathbf {j}-\frac{1}{4}t^{4}\mathbf {k}\bigg )\,\mathrm {m}
```
:::
````

````{prf:example}
:label: example-3-5
:enumerator: 3.5

If a man weighs himself on an elevator that is accelerating upwards at a rate *a* relative to an observer outside the elevator (in an inertial frame) as shown in [](#fig-3-3), what reading will he get for the normal force acting on him by the floor? what is the force if the elevator is accelerating downwards?

:::{admonition} Solution 3.5
:class: dropdown

The normal force is $\mathrm {n}=\mathrm {m}(\mathrm {a}+\mathrm {g})$ for upward acceleration and $\mathrm {n}=\mathrm {m}(\mathrm {g}-\mathrm {a})$ for downward acceleration. Since a weighing scale measures the normal force and calculates the mass from it, the downward journey might be a more pleasant one!
:::
````

```{figure} ../images/ch-03/459974_1_En_3_Fig3_HTML.png
:name: fig-3-3

A man weighing himself in an elevator
```

### 3.2.5 Newton’s Third Law

A force acting on an object is always due to another object in the surrounding environment. Newton’s third law shows that: if body 1 exerts a force $\mathbf {F}_{21}$ on body 2 then body 2 will exert an equal and opposite force $\mathbf {F}_{12}$ on body 1. That is

```{math}
\mathbf {F}_{12}=-\mathbf {F}_{21}
```

Any of these forces can be called an action force. When one of these forces is called an action force the other force is called a reaction (see [](#fig-3-4)). This law is sometimes stated *as* “*To every action there is an equal and opposite reaction*.” Note that *the action and reaction forces always act on different objects*, i.e., they can’t cancel each other out. This law also shows that forces come in pairs and that there is no such thing as a single isolated force.

```{figure} ../images/ch-03/459974_1_En_3_Fig4_HTML.png
:name: fig-3-4

The gravitational force exerted by the Earth on the apple and that exerted by the apple to the Earth form an action-reaction pair
```

````{prf:example}
:label: example-3-6
:enumerator: 3.6

Three blocks of masses $m_{1}, m_{2}$, and $m_{3}$ are placed on a frictionless surface and pushed by a horizontal force *F* as in [](#fig-3-5). Determine (a) the acceleration of the system; (b) the contact forces between $m_{1}$ and $m_{2}$ and between $m_{2}$ and $m_{3}.$

:::{admonition} Solution 3.6
:class: dropdown

The free-body diagram of each block is shown in [](#fig-3-5), where $F_{21}$ is the force exerted on $m_{2}$ by $m_{1}$. (a) Applying Newton’s second law for the system,

```{math}
F=(m_{1}+m_{2}+m_{3})a
```

```{math}
a=\frac{F}{(m_{1}+m_{2}+m_{3})}
```

(b) Applying Newton’s second law for each block, we have $F-F_{12}=m_{1}a, F_{21}-F_{23}=m_{2}a$ and $F_{32}=m_{3}a$. From Newton’s law of action and reaction we have $F_{12}=F_{21}$, and $F_{32}=F_{23}$, and therefore

```{math}
F_{12}=m_{2}a+F_{23}=(m_{2}+m_{3})a=\frac{(m_{2}+m_{3})}{(m_{1}+m_{2}+m_{3})}F
```

```{math}
F_{32}=\frac{m_{3}F}{(m_{1}+m_{2}+m_{3})}
```
:::
````


```{figure} ../images/ch-03/459974_1_En_3_Fig5_HTML.png
:name: fig-3-5

Three blocks of masses $m_{1}, m_{2}$, and $m_{3}$ are placed on a frictionless surface and pushed by a horizontal force *F*
```

(sec-3-3)=

## 3.3 Some Particular Forces

(sec-3-3-1)=

### 3.3.1 Weight

In Sect. [](#sec-2-4-2), we’ve seen that an object in free fall near the surface of the earth has a gravitational acceleration of magnitude 9.8 $\mathrm {m}/\mathrm {s}^{2}$ that is directed toward the center of earth. Using Newton’s second law, we can calculate the force that caused this acceleration. If an object has a mass *m* then the gravitational force is given by $m\mathbf {g}$, and is denoted by $\mathrm {w}$, i.e., $\mathbf {w}=m\mathbf {g}$. $\mathbf {w}$ is known as the weight of an object and is defined as the gravitational force exerted on it by earth (or any other astronomical body, where g is different than that of earth). In Chap. [](#ch-9), we will see that a gravitational force exists between any two bodies. When one of the bodies is an astronomical body, such as the earth or moon, and the other body is relatively smaller in size and mass the gravitational force is then called the weight of the body We will also see that the gravitational force varies with the distance between objects, and that the value of $\mathbf {g}$ becomes less at greater altitudes. Thus, weight is not an intrinsic property of an object. In everyday life, it is common to use the word weight when measuring the mass of a body mass and weight represent different quantities but they are proportional for a given value of $\mathbf {g}$. For two masses at the same location, the ratio of their weights is equal to the ratio of their masses.

(sec-3-3-2)=

### 3.3.2 The Normal Force

If an object is in contact with a surface, either at rest or moving on it, the surface exerts a supporting force $\mathbf {n}$ on the object that is always perpendicular to the surface of contact. This force is called the normal force.

(sec-3-3-3)=

### 3.3.3 Tension

The tension force $\mathbf {T}$ is the force that a cord, rope, cable, or any other similar object exerts on an object attached to it. This force is directed along the rope away from the object at the point where the rope is attached. In solving problems, ropes are usually assumed to be massless (referred to as light ropes) and unstretchable. For any light rope, the magnitude of the tension force *T* is the same at all points along the rope.

(sec-3-3-4)=

### 3.3.4 Friction

Imagine that everything around you is coated with an extremely good lubricant. Simple activities such as walking, sitting, driving a car, or holding objects would become extremely difficult or impossible. Therefore, friction plays a very important role in our everyday life. The frictional force is due to the interaction between the surface atoms of any two bodies in contact. The direction of this force is always parallel to the surface of contact, opposing the motion or the planned motion of one object relative to the other. Hence, the normal and frictional forces are both contact forces and they are always perpendicular to each other.

Consider a block resting on a table. If the block is pushed with a horizontal force $\mathbf {F}$ and remains stationary, it is because that the applied force is balanced by an equal and opposite force. This opposing force is known as the statistical frictional force $\mathbf {f}_{s}$ and it has the value $f_{s}=F$. The statistical frictional force increases with increasing $\mathbf {F}$ (see Fig. [](#fig-3-6)). The name statistical comes from the fact that the block remains stationary.

```{figure} ../images/ch-03/459974_1_En_3_Fig6_HTML.png
:name: fig-3-6

The opposing force is known as the statistical frictional force $\mathbf {f}_{s}$ and it has the value $f_{s}=F$. Its maximum value $f_{s\max }=F$ represents the applied force when the block is at the verge of slipping i.e. it is the minimum force necessary to initiate motion. When the block moves, the retarding frictional force is then called the kinetic frictional force $\mathbf {f}_{k}$
```

However, if $\mathrm {F}$ is increased to a certain maximum value, the block will eventually accelerate (see Fig. [](#fig-3-7)). This maximum value is equal to the maximum frictional force $f_{s\max }=F$ and it represents the applied force when the block is at the verge of slipping, i.e., it is the minimum force necessary to initiate motion. When the block moves, the retarding frictional force is then called the kinetic frictional force $\mathbf {f}_{k}$ and is usually less than $f_{s\max }$. If $f_{k}=F$, the block will move with a constant speed. If $F<f_{s}$ or if $\mathbf {F}$ is removed, the block will decelerate and will eventually be brought to rest. Experiments show that $f_{s\max }$ and $f_{k}$ have the following properties:

```{figure} ../images/ch-03/459974_1_En_3_Fig7_HTML.png
:name: fig-3-7

A graph of the friction force versus the applied force
```

1. $f_{s\max }=\mu _{s}n$, where $\mu _{s}$ is the coefficient of static friction and *n* is the normal force acting on the block. As long as the block is at rest $f_{s}=F,$ where $f_{s}\le \mu _{s}n.$
2. $f_{k}=\mu _{k}n$ where $\mu _{k}$ is the coefficient of the kinetic friction.
3. The directions of $\mathbf {f}_{s}$ and $\mathbf {f}_{k}$ are always parallel to the surface. $\mathbf {f}_{s}$ is opposite to the component of the applied force that is parallel to the surface and $\mathbf {f}_{k}$ is opposite to the instantaneous velocity of the body relative to the surface.

The dimensionless coefficients $\mu _{s}$ and $\mu _{k}$ depend on the nature of the surfaces in contact and are independent of the area of contact between these surfaces. $\mu _{k}$ is generally less than $\mu _{s}$. Table 3.1 lists $\mu _{s}$ and $\mu _{k}$ for some materials. Note that $\mu _{k}$ may vary with speed but such variations are not included here. Friction is a very complex phenomenon. One reason behind this is that the actual area of contact viewed from a microscopic level is much less than the area of contact viewed from a macroscopic level, as in Fig. [](#fig-3-8), even for very smooth surfaces. For our purposes here, the detailed friction mechanism will not be discussed.

| Materials | $\mu _{s}$ (static) | $\mu _{k}$ (kinetic) |
| --- | --- | --- |
| Steel on steel | 0.74 | 0.57 |
| Aluminum on steel | 0.61 | 0.47 |
| Copper on steel | 0.53 | 0.36 |
| Wood on wood | 0.25–0.5 | 0.2 |
| Rubber on concrete | 1.0 | 0.8 |
| Glass on glass | 0.94 | 0.4 |
| Copper on glass | 0.68 | 0.53 |
| Teflon on teflon | 0.04 | 0.04 |

```{figure} ../images/ch-03/459974_1_En_3_Fig8_HTML.png
:name: fig-3-8

The actual area of contact viewed from a microscopic level is much less than the area of contact viewed from a macroscopic level
```

(sec-3-3-5)=

### 3.3.5 The Drag Force

If a fluid (such as gas or liquid) and a body are in relative motion, the body will experience a resistive force opposing the relative motion called the drag force D. The direction of $\mathbf {D}$ is the direction in which the fluid is flowing relative to the body. The drag force depends on some factors, such as the speed of the object. We will consider the situation in which a relatively large object is moving through air at high speed (such as a skydiver or an airplane). In this case, the drag force $\mathrm {D}$ is proportional to the square of the body’s speed and is given by

```{math}
D=\frac{1}{2}c\rho Av^{2}
```

where $\rho$ is the air density, *A* is the effective cross-sectional area of the body taken in a plane perpendicular to its velocity, and *c* is the drag coefficient. *c* is a dimensionless constant that has a value ranging from 0.4 to 2. The value of *c* may vary with *v*, but such variations will be ignored.

```{figure} ../images/ch-03/459974_1_En_3_Fig9_HTML.png
:name: fig-3-9

An object falling through air experiences a drag force $\mathbf {D}$ and a gravitational force $m\mathbf {g}$
```

As an example, consider an object falling through air far from the earth’s surface. The forces acting on the object are the drag force and the gravitational force as in Fig. [](#fig-3-9). As the object falls, its speed increases and thus $\mathbf {D}$ increases from zero until it eventually becomes equal to the object’s weight $(\mathbf {D}=-m\mathbf {g})$. The net force on the object when $(\mathbf {D}=-m\mathbf {g})$ will be equal to zero, and hence the object’s acceleration will become zero $(\mathbf {a}=\mathbf {0})$. As a result the body will fall at a constant speed called the terminal speed $v_{t}$:

```{math}
\Sigma \mathbf {F}=\mathbf {0}
```

```{math}
\frac{1}{2}c\rho Av_{t}^{2}-mg=0
```

```{math}
\frac{1}{2}c\rho Av_{t}^{2}=mg
```

```{math}
v_{t}=\sqrt{\frac{2mg}{c\rho A}}
```

where *m* is the mass of the body.

(sec-3-4)=

## 3.4 Applying Newton’s Laws

It is necessary to follow some steps when solving problems using Newton’s second law. These steps can be summarized in the following:

1. Draw a simple diagram of the objects in the system analyzed;
2. Draw a free-body diagram for each object in the system. In a free-body diagram, the body is represented by a dot, and all external forces (represented by vectors) acting on the body are shown. The forces exerted by the body on other bodies in the system are not included in its free-body diagram;
3. A coordinate system should be drawn in a free-body diagram with the body at its origin. Newton’s second law is then applied along each axis using the components of each force. The coordinate system must be oriented in such a way that simplifies the analysis, i.e., some forces should be directed along the axes;
4. Solve obtained equations for the unknowns.

Note that from here until Chap. [](#ch-5), any object is assumed to behave as a particle, i.e., all of its parts move in exactly the same way When applying Newton’s second law, a particle is represented by a dot on the free-body diagram. Furthermore, the mass or friction of any rope or pulley is neglected.

````{prf:example}
:label: example-3-7
:enumerator: 3.7

A 25 kg block is released from rest at the top of a rough $40^{\mathrm {o}}$ inclined surface. It then accelerates at a constant rate of 0.1 $\mathrm {m}/\mathrm {s}^{2}$. Find: (a) the coefficient of kinetic friction between the box and the surface; (b) the maximum angle the box would be at the verge of slipping if the angle of the incline is changeable.

```{figure} ../images/ch-03/459974_1_En_3_Fig10_HTML.png
:name: fig-3-10

The free-body diagram of a block accelerating down an incline
```

:::{admonition} Solution 3.7
:class: dropdown

(a) The free-body diagram is shown in Fig. [](#fig-3-10). Applying Newton’s second law to the box gives

```{math}
\sum F_{x}=mg\sin \theta -f_{k}=ma
```

```{math}
\sum F_{y}=n-mg\cos \theta =0
```

```{math}
f_{k}=mg\sin \theta -ma=(25\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})\sin 40^{\circ } -(25\,\mathrm {k}\mathrm {g})(0.1\,\mathrm {m}/\mathrm {s}^{2})
```

```{math}
=155\,\mathrm {N}
```

```{math}
n=mg\cos \theta =(25\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2}) \cos 40^{\circ } =187.7\,\mathrm {N}
```

The coefficient of kinetic friction is

```{math}
\mu _{k}=\frac{f_{k}}{n}
```

```{math}
\mu _{k}=\frac{(120\,\mathrm {N})}{(212.2\,\mathrm {N})}=0.57
```

(c) At the verge of slipping the force of static friction is maximum:

```{math}
f_{s\max }=\mu _{s}n
```

Applying Newton’s second law we get

```{math}
\sum F_{x}=mg\sin \theta -f_{s\max }=0
```

```{math}
f_{s\max }=mg\sin \theta
```

Also we have $n=mg\cos \theta$, therefore

```{math}
\mu _{s}=\frac{mg\sin \theta }{mg\cos \theta }=\tan \theta
```

Since $\mu _{s}=0.74$ from Table 3.1, we have

```{math}
\theta =\tan ^{-1}0.74=36.5^{\mathrm {o}}
```
:::
````

````{prf:example}
:label: example-3-8
:enumerator: 3.8

Two masses $m_{1}=2$ kg and $m_{2}=5$ kg are connected by a massless cord that passes over a massless and frictionless pulley (Atwood’s machine) as shown in Fig. [](#fig-3-11). Find the acceleration of the system and the tension in the cord.

:::{admonition} Solution 3.8
:class: dropdown

The free-body diagram of each mass is shown in Fig. [](#fig-3-11). Applying Newton’s second law to each block (taking positive *y* to be upwards) gives

```{math}
\sum F_{1y}=T-m_{1}g=m_{1}a
```

```{math}
\sum F_{2y}=T-m_{2}g=-m_{2}a
```

adding the two equations we have

```{math}
a=\bigg (\frac{m_{2}-m_{1}}{m_{1}+m_{2}}\bigg )g=\bigg (\frac{3\,\mathrm {k}\mathrm {g}}{7\,\mathrm {k}\mathrm {g}}\bigg )(9.8\,\mathrm {m}/\mathrm {s}^{2})=4.2\,\mathrm {m}/\mathrm {s}^{2}
```

Substituting *a* in any of the two equations gives

```{math}
T=\bigg (\frac{2m_{1}m_{2}}{m_{1}+m_{2}}\bigg )g=\left( \frac{2(10\,\mathrm {k}\mathrm {g})}{(7\,\mathrm {k}\mathrm {g})}\right) (9.8\,\mathrm {m}/\mathrm {s}^{2})=28\,\mathrm {N}
```
:::
````

```{figure} ../images/ch-03/459974_1_En_3_Fig11_HTML.png
:name: fig-3-11

The free-body diagram of an Atwoodõs machine
```

````{prf:example}
:label: example-3-9
:enumerator: 3.9

Two blocks of masses $m_{1}=1.5$ kg and $m_{2}=3.2$ kg are connected by a light string that passes over a massless frictionless pulley as shown in Fig. [](#fig-3-12). If the surface is frictionless: (a) what is the distance that $m_{2}$ will drop during the first 0.6 s? (b) if a third block is attached to $m_{1}$ using strong glue, what must its mass be such that the system moves with constant speed?

```{figure} ../images/ch-03/459974_1_En_3_Fig12_HTML.png
:name: fig-3-12

The free-body diagram showing the forces on each block
```

:::{admonition} Solution 3.9
:class: dropdown

(a) The acceleration value is the same for both masses since they are connected by a string. Figure [](#fig-3-12) shows the free-body diagram for each mass. Applying Newton’s law to $m_{1}$ and $m_{2}$ in the direction of motion we have for $m_{2}$

```{math}
\sum F_{2y}=T-m_{2}g=-m_{2}a
```

and for $m_{1}$

```{math}
\sum F_{1x}=m_{1}g\sin \theta -T=-m_{1}a
```

from this we have

```{math}
T=m_{2}(g-a)
```

and

```{math}
m_{1}g\sin \theta -m_{2}(g-a)=-m_{1}a
```

and therefore

```{math}
a=\displaystyle \frac{(m_{2}-m_{1}\sin \theta )g}{m_{1}+m_{2}}=\frac{((3.2\,\mathrm {k}\mathrm {g})-(1.5\,\mathrm {k}\mathrm {g})\sin 45^{\mathrm {o}})(9.8\,\mathrm {m}/\mathrm {s}^{2})}{4.7\,\mathrm {k}\mathrm {g}}
```

```{math}
\,=4.5\,\mathrm {m}/\mathrm {s}^{2}
```

After 0. $6\mathrm {s}$, the distance that $m_{2}$ falls is

```{math}
h=\frac{1}{2}at^{2}=\frac{1}{2}(-4.5\,\mathrm {m}/\mathrm {s}^{2})(0.6 \; \mathrm {s})^{2}=-0.81\,\mathrm {m}
```

(b) If the system moves with constant speed, its acceleration is zero

```{math}
\displaystyle \sum F_{1x}=(m_{1}+m_{3}) g \sin {\theta }-T=0
```

and

```{math}
\sum F_{2y}=T-m_{2}g=0
```

that gives

```{math}
T=m_{2}g
```

and

```{math}
(m_{1}+m_{3})g\sin \theta -m_{2}g=0
```

hence

```{math}
m_{3}=\displaystyle \frac{m_{2}-m_{1}\sin \theta }{\sin \theta }=\frac{((3.2\,\mathrm {k}\mathrm {g})-(1.5\,\mathrm {k}\mathrm {g})\sin 45^{\mathrm {o}})}{\sin 45^{\circ }}=3.03\,\mathrm {k}\mathrm {g}
```
:::
````

````{prf:example}
:label: example-3-10
:enumerator: 3.10

A 3 kg block is hanged from the ceiling as in Fig. [](#fig-3-13). Find the magnitude of $T_{1}, T_{2}$, and $T_{3}.$

```{figure} ../images/ch-03/459974_1_En_3_Fig13_HTML.png
:name: fig-3-13

A block hanged from the ceiling
```

```{figure} ../images/ch-03/459974_1_En_3_Fig14_HTML.png
:name: fig-3-14

The free-body diagram of the block
```

:::{admonition} Solution 3.10
:class: dropdown

The free-body diagrams of the block and the knot are shown in Fig. [](#fig-3-14). From Newton’s second law $T_{3}$ is equal to the weight of the block, i.e.,

```{math}
T_{3}=w=mg=(3\,\mathrm {k}\mathrm {g})(9.8\,\mathrm {m}/\mathrm {s}^{2})=29.4\,\mathrm {N}
```

For the knot, we have

```{math}
:label: eq-3-1
\begin{aligned} \displaystyle \sum F_{x}=T_{2}-T_{1}\sin 50^{\mathrm {o}}=0 \end{aligned}
```

```{math}
:label: eq-3-2
\begin{aligned} \displaystyle \sum F_{y}=T_{1}\cos 50^{\mathrm {o}}-T_{3}=0 \end{aligned}
```

Solving for $T_{1}$ from Eq. [](#eq-3-2) gives

```{math}
T_{1}=\frac{T_{3}}{\cos 50^{\mathrm {o}}}=\frac{(29.4\,\mathrm {N})}{(0.64)}=45.7\,\mathrm {N}
```

Substituting this result into Eq. [](#eq-3-1) we get

```{math}
T_{2}=T_{1} \sin 50^{\circ } =(45.7\,\mathrm {N})(0.76)=35\,\mathrm {N}
```
:::
````

````{prf:example}
:label: example-3-11
:enumerator: 3.11

Figure [](#fig-3-15) shows a weight of 200 $\mathrm {N}$ that is lifted with a constant speed. Find the tension in each part of the rope and the force of lift.

:::{admonition} Solution 3.11
:class: dropdown

Since the pulleys are massless and frictionless we have $2T_{1}=T_{2}$ ($T_{1}$ is the tension in each rope)and $T_{2}= w=200\mathrm {N}$, thus

```{math}
T_{1}=\frac{T_{2}}{2}=\frac{(200\,\mathrm {N})}{2}=100\,\mathrm {N}
```

we also have

```{math}
T_{1}=F=100\,\mathrm {N}
```
:::
````

```{figure} ../images/ch-03/459974_1_En_3_Fig15_HTML.png
:name: fig-3-15

Using two pulleys to reduce the force necessary to lift a weight
```

(sec-3-4-1)=

### 3.4.1 Uniform Circular Motion

In Sect. [](#sec-2-4-5), it was found that a particle moving in a circle with a constant linear speed *v* (uniform circular motion) has a centripetal acceleration directed towards the center of the circle. Its magnitude is given by

```{math}
a_{rad}=\frac{v^{2}}{r}
```

where *r* is the radius of the circle. Figure [](#fig-3-16) shows an object attached to a string in uniform circular motion (the plane of motion is parallel to the Earth’s surface). From Newton’s second law, the centripetal acceleration is caused by a force or net force directed towards the center of the circle. Therefore, as $a_{rad}$, the centripetal (or radial) force $F_{rad}$ has a constant magnitude but its direction changes continuously The magnitude of this centripetal force is given by

```{math}
|\Sigma \mathbf {F}|=F_{rad}=ma_{rad}=m\frac{v^{2}}{r}
```

If at some instant the radial force becomes zero, the object would then move along a straight line path tangent to the circle. Hence, the centripetal force is necessary to keep the object in its circular path. The centripetal force may be any kind of force such as friction, gravity, or tension.

```{figure} ../images/ch-03/459974_1_En_3_Fig16_HTML.png
:name: fig-3-16

An object attached to a string in uniform circular motion
```

````{prf:example}
:label: example-3-12
:enumerator: 3.12

A conical pendulum consists of a bob of mass *m* attached to a light string rotating in a horizontal circle as in Fig. [](#fig-3-17). If the bob rotates with a constant speed and if $\theta$ and *m* are known, find: (a) the tension in the string; (b) the speed of the bob; (c) the period of motion.

```{figure} ../images/ch-03/459974_1_En_3_Fig17_HTML.png
:name: fig-3-17

A conical pendulum consisting of a bob of mass *m* attached to a light string rotating in a horizontal circle
```

:::{admonition} Solution 3.12
:class: dropdown

The horizontal component of the tension force supplies the required centripetal force to keep the bob in its circular path while the vertical component balances the weight of the bob. (a) Applying Newton’s second law in both the $\mathrm {x}$- and $\mathrm {y}$-directions we have

```{math}
T\cos \theta -mg=0
```

```{math}
:label: eq-3-3
\begin{aligned} T=\displaystyle \frac{mg}{\cos \theta } \end{aligned}
```

and

```{math}
:label: eq-3-4
\begin{aligned} T\displaystyle \sin \theta =\frac{mv^{2}}{R} \end{aligned}
```

(b) Dividing Eq. [](#eq-3-4) by Eq. [](#eq-3-3) gives

```{math}
v=\sqrt{gR\tan \theta }
```

(c) The period of motion is given by

```{math}
\tau =\frac{2\pi R}{v}=2\pi \sqrt{\frac{R}{g\tan \theta }}
```

Since $R=L\sin \theta$, we have

```{math}
\tau =2\pi \sqrt{\frac{L\cos \theta }{g}}
```
:::
````

````{prf:example}
:label: example-3-13
:enumerator: 3.13

(a) A car needs to turn on a level road without skidding as in Fig. [](#fig-3-18). Find the maximum speed for which the car can take the curved path of the level road safely (b) If the road is banked, i.e., the outer edge is raised relative to the inner edge as in Fig. [](#fig-3-19), find the maximum speed for which the car can take the curved path of the level road safely without depending on friction.

```{figure} ../images/ch-03/459974_1_En_3_Fig18_HTML.png
:name: fig-3-18

A car turning without skidding
```

```{figure} ../images/ch-03/459974_1_En_3_Fig19_HTML.png
:name: fig-3-19

A car turning on a banked road
```

:::{admonition} Solution 3.13
:class: dropdown

(a) The centripetal force required for the car to remain in its circular path, is in this case, is the force of static friction. The maximum speed for which the car can take the curve without skidding is when the static frictional force is a maximum. That is,

```{math}
f_{s\max }=\mu mg=\frac{mv_{\max }^{2}}{r}
```

Hence

```{math}
v_{\max }=\sqrt{\mu rg}
```

(b) If the road is banked the car can take the turn without depending on friction as the required centripetal force. In that case, the horizontal component of the normal force supplies the necessary centripetal force. Thus we have

```{math}
n\sin \theta =\frac{mv^{2}}{r}
```

and

```{math}
n\cos \theta =mg
```

where *v* is the speed of the car. Dividing these two equations gives

```{math}
\tan \theta =\frac{v^{2}}{rg}
```

If the angle $\theta$ and the curvature *r* are known, then the safe speed limit can be found. If the car moves at a speed lower or higher than that speed then the frictional force must supply the additional centripetal force for the car to stay in its circular path.
:::
````

(sec-3-4-2)=

### 3.4.2 Nonuniform Circular Motion

In Sect. [](#sec-2-4-6), we saw that an object in nonuniform circular motion has both perpendicular (centripetal) and parallel components of acceleration given by

```{math}
a_{rad}=\frac{v^{2}}{r}
```

and

```{math}
a_{t}=\frac{d|\mathbf {v}|}{dt}
```

The total acceleration is

```{math}
\mathbf {a}=\mathbf {a}_{rad}+\mathbf {a}_{t}
```

These radial and tangential accelerations are caused by radial and tangential forces respectively (see Fig. [](#fig-3-20)):

```{math}
F_{rad}=ma_{rad}=m\frac{v^{2}}{r}
```

```{math}
F_{t}=ma_{t}=m\frac{d|\mathbf {v}|}{dt}
```

The net force is

```{math}
\mathbf {F}=\mathbf {F}_{rad}+\mathbf {F}_{t}
```

```{figure} ../images/ch-03/459974_1_En_3_Fig20_HTML.png
:name: fig-3-20

The radial and tangential forces in nonuniform circular motion
```

````{prf:example}
:label: example-3-14
:enumerator: 3.14

An object attached to a light string is rotating in a vertical circle of radius *r* (see Fig. [](#fig-3-21)). Find: (a) the tension in the cord at the lowest and highest points; (b) the minimum speed at the highest point such that the object remains in its circular path.

```{figure} ../images/ch-03/459974_1_En_3_Fig21_HTML.png
:name: fig-3-21

An object attached to a string rotating in a vertical circle
```

:::{admonition} Solution 3.14
:class: dropdown

(a) Applying Newton’s second law in both the tangential and radial directions gives

```{math}
mg\sin \theta =ma_{t}
```

and

```{math}
T-mg\cos \theta =\frac{mv^{2}}{r}
```

At the bottom $\theta =0$ and therefore $a_{t}=0$ and

```{math}
T_{b}=m\bigg (\frac{v_{b}^{2}}{r}+g\bigg )
```

At the top $\theta =180^{0}$ and $a_{t}=0$ and

```{math}
T_{t}=m\bigg (\frac{v_{t}^{2}}{r}-g\bigg )
```

(b) For the object to remain in its circular path, the string must remain taut, i.e., $T_{t}$ must be positive $(T_{t}>0)$. If $T_{t}=0$ then $v_{t}=\sqrt{gr}$. Hence, the velocity must satisfy $v_{t}>\sqrt{gr}.$
:::
````

```{figure} ../images/ch-03/459974_1_En_3_Fig22_HTML.png
:name: fig-3-22

An object subjected to two forces acting in different directions
```

```{figure} ../images/ch-03/459974_1_En_3_Fig23_HTML.png
:name: fig-3-23

A block released from the top of an incline
```

```{figure} ../images/ch-03/459974_1_En_3_Fig24_HTML.png
:name: fig-3-24

Two masses connected by a light string over a frictionless pulley of negligible mass
```

```{figure} ../images/ch-03/459974_1_En_3_Fig25_HTML.png
:name: fig-3-25

A block hanged from the ceiling
```

```{figure} ../images/ch-03/459974_1_En_3_Fig26_HTML.png
:name: fig-3-26

A block held in equilibrium
```

```{figure} ../images/ch-03/459974_1_En_3_Fig27_HTML.png
:name: fig-3-27

Two blocks connected by a light rope and pulled by a force
```

**Problems**

```{exercise}
:label: prob-3-1
:enumerator: 3.1

A 4 kg object is exposed to two forces (see Fig. [](#fig-3-22)). Find the magnitude and direction of the acceleration of the object.
```

```{exercise}
:label: prob-3-2
:enumerator: 3.2

A 0.2 kg block is released from the top of an inclined plane of angle $30^{\mathrm {o}}$ as in Fig. [](#fig-3-23). Find the speed of the block just as it reaches the bottom.
```

```{exercise}
:label: prob-3-3
:enumerator: 3.3

Two masses are connected by a light string that is connected to a frictionless pulley of negligible mass as in Fig. [](#fig-3-24). Find the magnitude of the acceleration of the masses and the tension in the string.
```

```{exercise}
:label: prob-3-4
:enumerator: 3.4

A block is pushed up along a smooth inclined plane of angle of $45^{\mathrm {o}}$ where it is given an initial velocity of 8 $\mathrm {m}/\mathrm {s}$. Determine the time it takes the block to return to its initial position.
```

```{exercise}
:label: prob-3-5
:enumerator: 3.5

Find the tension in each string in the system shown in Fig. [](#fig-3-25).
```

```{exercise}
:label: prob-3-6
:enumerator: 3.6

A 5 kg block is held in equilibrium as in Fig. [](#fig-3-26). Find the normal force acting on the block.
```

```{exercise}
:label: prob-3-7
:enumerator: 3.7

Find the normal force exerted on a 70 kg man standing inside an elevator that is accelerating upwards at a rate of 2 $\mathrm {m}/\mathrm {s}^{2}.$
```

```{exercise}
:label: prob-3-8
:enumerator: 3.8

Find the acceleration of the system shown in Fig. [](#fig-3-27) and the tension in the string if $m_{1}=3$ kg and $m_{2}=4$ kg (assume massless string and frictionless surface).
```

```{exercise}
:label: prob-3-9
:enumerator: 3.9

Two blocks of masses 3 and 5 kg are placed on top of each other as in Fig. [](#fig-3-28). If the coefficient of static friction between the blocks is 0.2 and assuming there is no friction between the lower block and the surface on which it rests, find the maximum horizontal force that can be applied to the lower block such that the blocks move together.
```

```{exercise}
:label: prob-3-10
:enumerator: 3.10

A 1000 kg car move along the track shown in Fig. [](#fig-3-29). Find (a) the maximum speed the car can have at point A such that it does not leave the track (b) the normal force exerted on the car at $\mathrm {B}$ if its speed there is 15 $\mathrm {m}/\mathrm {s}$.
```

```{exercise}
:label: prob-3-11
:enumerator: 3.11

A block of mass *m* on a frictionless table is attached to light string that passes through the center of the table and is connected to a larger block of mass *M* (see Fig. [](#fig-3-30)). If *m* moves in uniform circular motion of radius *r* and speed *v*, find *v* such that *M* remains at rest when released.
```

```{exercise}
:label: prob-3-12
:enumerator: 3.12

A l kg particle moves in the force field given by $\mathbf {F}=2t\mathbf {i}+(5t-1)\mathbf {j}-6t^{2}\mathbf {k}.$ Find the position of the particle at any time if at $t=0, \mathbf {r}_{0}=\mathbf {0}$, and $\mathbf {v}_{0}=\mathbf {0}$.
```

```{figure} ../images/ch-03/459974_1_En_3_Fig28_HTML.png
:name: fig-3-28

Two blocks placed on top of each other, where a horizontal force is applied to the lower block
```

```{figure} ../images/ch-03/459974_1_En_3_Fig29_HTML.png
:name: fig-3-29

A car moving on a curved path
```

```{figure} ../images/ch-03/459974_1_En_3_Fig30_HTML.png
:name: fig-3-30

A block of mass *m* on a frictionless table is attached to light string that passes through the center of the table and is connected to a larger block of mass *M*
```
