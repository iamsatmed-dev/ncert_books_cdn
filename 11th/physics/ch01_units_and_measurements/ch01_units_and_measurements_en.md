# NCERT: Class 11 Physics — Chapter 1
# Units and Measurement (मात्रक एवं मापन)

> **NCERT Class 11 Physics** | **Digital Study Edition** | With Vector Diagrams & LaTeX Math

---

## 📑 Chapter Contents
1. [1.1 Introduction](#11-introduction)
2. [1.2 The International System of Units](#12-the-international-system-of-units)
   - [Table 1.1: SI Base Quantities and Units](#table-11-si-base-quantities-and-units)
   - [Fig 1.1: Plane Angle & Solid Angle](#fig-11-plane-angle-and-solid-angle)
   - [Table 1.2: General Use Non-SI Units](#table-12-some-units-retained-for-general-use)
3. [1.3 Significant Figures](#13-significant-figures)
   - [1.3.1 Rules for Significant Figures](#131-rules-for-determining-significant-figures)
   - [1.3.2 Rounding off Uncertain Digits](#132-rounding-off-the-uncertain-digits)
   - [1.3.3 Rules for Arithmetic Calculations](#133-rules-for-determining-uncertainty-in-arithmetic-calculations)
4. [1.4 Dimensions of Physical Quantities](#14-dimensions-of-physical-quantities)
5. [1.5 Dimensional Formulae and Dimensional Equations](#15-dimensional-formulae-and-dimensional-equations)
6. [1.6 Dimensional Analysis and its Applications](#16-dimensional-analysis-and-its-applications)
   - [1.6.1 Checking Dimensional Consistency of Equations](#161-checking-dimensional-consistency-of-equations)
   - [1.6.2 Deducing Relation among Physical Quantities](#162-deducing-relation-among-physical-quantities)
7. [Chapter Summary](#summary)
8. [Exercises & Solved Numericals](#exercises)

---

## 📄 Page 1

### 1.1 Introduction

Measurement of any physical quantity involves comparison with a certain basic, arbitrarily chosen, internationally accepted reference standard called **unit**. 

The result of a measurement of a physical quantity is expressed by a number (or numerical measure) accompanied by a unit:

$$\text{Physical Quantity} = n \times u$$

where $n$ is numerical value and $u$ is the unit.

Although the number of physical quantities appears to be very large, we need only a limited number of units for expressing all the physical quantities, since they are inter-related with one another. 

* **Fundamental or Base Units:** The units for the fundamental or base quantities are called fundamental or base units.
* **Derived Units:** The units of all other physical quantities can be expressed as combinations of the base units. Such units obtained for the derived quantities are called derived units.
* **System of Units:** A complete set of these units, both the base units and derived units, is known as the system of units.

---

### 1.2 The International System of Units

In earlier times scientists of different countries were using different systems of units for measurement. Three such systems, the **CGS**, the **FPS** (British system) and the **MKS** system were in use extensively:

* **CGS system:** centimetre, gram, second
* **FPS system:** foot, pound, second
* **MKS system:** metre, kilogram, second

The system of units which is at present internationally accepted for measurement is the **Système International d'Unités** (French for International System of Units), abbreviated as **SI**. 

The SI was developed by the *Bureau International des Poids et Mesures* (BIPM) in 1971 and recently revised by the General Conference on Weights and Measures in November 2018. The SI units use a decimal system, making conversions within the system simple and convenient.

---

## 📄 Page 2

In SI, there are **seven base units** as given in Table 1.1. Besides the seven base units, there are two supplementary dimensionless units defined for:

1. **Plane Angle ($d\theta$):** Ratio of length of arc $ds$ to radius $r$.
   $$d\theta = \frac{ds}{r} \text{ radian (rad)}$$

2. **Solid Angle ($d\Omega$):** Ratio of intercepted area $dA$ of spherical surface about apex $O$ to square of radius $r^2$.
   $$d\Omega = \frac{dA}{r^2} \text{ steradian (sr)}$$

Both plane angle and solid angle are dimensionless physical quantities ($[M^0 L^0 T^0]$).

<div class="ncert-diagram-card" data-page="2">
  <div class="diagram-preview-box" onclick="window.openImageModal && window.openImageModal('data/diagrams/11th_physics_ch01_units_and_measurements_fig_1_1.png', 'Fig. 1.1: Plane Angle and Solid Angle')">
    <img src="data/diagrams/11th_physics_ch01_units_and_measurements_fig_1_1.png" alt="Fig. 1.1 Description of (a) plane angle dθ and (b) solid angle dΩ" />
  </div>
  <div class="diagram-caption-box">
    <div class="diagram-caption-text">
      <strong>Fig. 1.1:</strong> Description of (a) plane angle $d\theta = \frac{ds}{r}\text{ rad}$ and (b) solid angle $d\Omega = \frac{dA}{r^2}\text{ sr}$.
    </div>
    <button class="diagram-btn-pdf" onclick="window.goToPdfPage && window.goToPdfPage(2);">
      📄 View in PDF (Page 2)
    </button>
  </div>
</div>

#### Table 1.1: SI Base Quantities and Units

| Base Quantity | Name | Symbol | Definition & BIPM Standard |
| :--- | :--- | :--- | :--- |
| **Length** | metre | $\text{m}$ | Defined by taking the fixed numerical value of the speed of light in vacuum $c$ to be $299\,792\,458$ when expressed in the unit $\text{m}\cdot\text{s}^{-1}$, where the second is defined in terms of $\Delta\nu_{\text{Cs}}$. |
| **Mass** | kilogram | $\text{kg}$ | Defined by taking the fixed numerical value of the Planck constant $h$ to be $6.62607015 \times 10^{-34}$ when expressed in the unit $\text{J}\cdot\text{s} = \text{kg}\cdot\text{m}^2\cdot\text{s}^{-1}$. |
| **Time** | second | $\text{s}$ | Defined by taking the fixed numerical value of caesium frequency $\Delta\nu_{\text{Cs}}$, the unperturbed ground-state hyperfine transition frequency of caesium-133 atom, to be $9\,192\,631\,770$ when expressed in $\text{Hz}$ ($\text{s}^{-1}$). |
| **Electric Current** | ampere | $\text{A}$ | Defined by taking the fixed numerical value of elementary charge $e$ to be $1.602176634 \times 10^{-19}$ when expressed in $\text{C} = \text{A}\cdot\text{s}$. |
| **Thermodynamic Temperature** | kelvin | $\text{K}$ | Defined by taking the fixed numerical value of the Boltzmann constant $k$ to be $1.380649 \times 10^{-23}$ when expressed in $\text{J}\cdot\text{K}^{-1} = \text{kg}\cdot\text{m}^2\cdot\text{s}^{-2}\cdot\text{K}^{-1}$. |
| **Amount of Substance** | mole | $\text{mol}$ | One mole contains exactly $6.02214076 \times 10^{23}$ elementary entities (Avogadro constant $N_A$ expressed in $\text{mol}^{-1}$). |
| **Luminous Intensity** | candela | $\text{cd}$ | Defined by taking fixed numerical value of luminous efficacy of monochromatic radiation of frequency $540 \times 10^{12}\text{ Hz}$, $K_{\text{cd}}$, to be $683$ when expressed in $\text{lm}\cdot\text{W}^{-1} = \text{cd}\cdot\text{sr}\cdot\text{W}^{-1}$. |

---

## 📄 Page 3

#### Table 1.2: Some units retained for general use (Though outside SI)

| Name | Symbol | Value in SI Unit |
| :--- | :--- | :--- |
| **minute** | $\text{min}$ | $60\text{ s}$ |
| **hour** | $\text{h}$ | $60\text{ min} = 3600\text{ s}$ |
| **day** | $\text{d}$ | $24\text{ h} = 86400\text{ s}$ |
| **year** | $\text{y}$ | $365.25\text{ d} = 3.156 \times 10^7\text{ s}$ |
| **degree** | $^\circ$ | $1^\circ = (\pi / 180)\text{ rad}$ |
| **litre** | $\text{L}$ | $1\text{ dm}^3 = 10^{-3}\text{ m}^3$ |
| **tonne** | $\text{t}$ | $10^3\text{ kg} = 1\text{ Mg}$ |
| **carat** | $\text{c}$ | $200\text{ mg}$ |
| **bar** | $\text{bar}$ | $0.1\text{ MPa} = 10^5\text{ Pa}$ |
| **curie** | $\text{Ci}$ | $3.7 \times 10^{10}\text{ s}^{-1}$ |
| **roentgen** | $\text{R}$ | $2.58 \times 10^{-4}\text{ C/kg}$ |
| **quintal** | $\text{q}$ | $100\text{ kg}$ |
| **barn** | $\text{b}$ | $100\text{ fm}^2 = 10^{-28}\text{ m}^2$ |
| **are** | $\text{a}$ | $1\text{ dam}^2 = 10^2\text{ m}^2$ |
| **hectare** | $\text{ha}$ | $1\text{ hm}^2 = 10^4\text{ m}^2$ |
| **standard atmosphere** | $\text{atm}$ | $101325\text{ Pa} = 1.013 \times 10^5\text{ Pa}$ |

---

### 1.3 Significant Figures

Every measurement involves errors. The reported result of measurement should indicate the precision of measurement. Normally, the reported result contains all the digits that are known reliably plus one uncertain digit:

> **Definition:** The reliable digits plus the first uncertain digit are known as **significant digits** or **significant figures**.

* Example: In pendulum oscillation period $1.62\text{ s}$, digits $1$ and $6$ are reliable/certain, while digit $2$ is uncertain. Measured value has **$3$ significant figures**.
* Example: Length $287.5\text{ cm}$ has **$4$ significant figures** ($2, 8, 7$ are certain, $5$ is uncertain).

---

## 📄 Page 4

### 1.3.1 Rules for Determining Significant Figures

1. **All non-zero digits are significant.** Example: $2308$ has 4 significant figures.
2. **All zeros between two non-zero digits are significant**, no matter where the decimal point is. Example: $2.005$ has 4 significant figures.
3. **If the number is less than 1, the zero(s) on the right of decimal point but to the left of the first non-zero digit are not significant.** In $\underline{0}.\underline{00}2308$, the underlined zeros are not significant. It has 4 significant figures.
4. **The terminal or trailing zero(s) in a number without a decimal point are not significant.** Thus $123\text{ m} = 12300\text{ cm} = 123000\text{ mm}$ all have only 3 significant figures.
5. **The trailing zeros in a number with a decimal point are significant.** $3.500\text{ g}$ has 4 significant figures, and $0.06900\text{ m}$ has 4 significant figures.
6. **Change of units does not change the number of significant figures.** To remove ambiguities, scientific notation ($a \times 10^b$) is best used:
   $$4.700\text{ m} = 4.700 \times 10^2\text{ cm} = 4.700 \times 10^3\text{ mm}$$
   Here each expression clearly has 4 significant figures.

---

## 📄 Page 5

### 1.3.2 Rounding off the Uncertain Digits

1. If the insignificant digit to be dropped is **greater than 5**, the preceding digit is raised by 1.
   * $2.746 \to 2.75$ (for 3 significant figures)
2. If the insignificant digit to be dropped is **less than 5**, the preceding digit is left unchanged.
   * $1.743 \to 1.74$ (for 3 significant figures)
3. If the insignificant digit to be dropped is **5**:
   * If preceding digit is **even**, drop 5 without change: $2.745 \to 2.74$
   * If preceding digit is **odd**, raise preceding digit by 1: $2.735 \to 2.74$

In intermediate steps of multi-step calculations, retain **one extra digit** beyond significant figures to avoid round-off accumulation.

---

## 📄 Page 6

### 1.3.3 Rules for Arithmetic Calculations

#### 1. Multiplication and Division:
The final result should retain as many significant figures as are there in the original number with the least significant figures.

$$\text{Density} = \frac{\text{Mass}}{\text{Volume}} = \frac{4.237\text{ g}}{2.51\text{ cm}^3} = 1.688047\dots \to 1.69\text{ g}\cdot\text{cm}^{-3}$$

Since volume ($2.51$) has only 3 significant figures, density is rounded to **3 significant figures**.

#### 2. Addition and Subtraction:
The final result should retain as many decimal places as are there in the number with the least decimal places.

$$\begin{aligned}
& 436.32\text{ g} \\
+ & 227.2\text{ g} \quad (\text{least decimal places: 1}) \\
+ & 0.301\text{ g} \\
\hline
= & 663.821\text{ g} \to \mathbf{663.8\text{ g}}
\end{aligned}$$

---

## 📄 Page 7

### 1.4 Dimensions of Physical Quantities

The nature of a physical quantity is described by its **dimensions**. All physical quantities can be expressed in terms of combinations of the seven base quantities denoted with square brackets $[\ ]$:

* Length: $[L]$
* Mass: $[M]$
* Time: $[T]$
* Electric current: $[A]$
* Thermodynamic temperature: $[K]$
* Luminous intensity: $[cd]$
* Amount of substance: $[mol]$

> **Definition:** The **dimensions** of a physical quantity are the powers (or exponents) to which the base quantities are raised to represent that quantity.

* **Volume:** $[L] \times [L] \times [L] = [L^3] = [M^0 L^3 T^0]$
* **Velocity:** $\frac{[L]}{[T]} = [M^0 L T^{-1}]$
* **Acceleration:** $\frac{[L]}{[T]^2} = [M^0 L T^{-2}]$
* **Force:** $[M] \times \frac{[L]}{[T]^2} = [M L T^{-2}]$

---

## 📄 Page 8

### 1.5 Dimensional Formulae and Dimensional Equations

The expression which shows how and which of the base quantities represent the dimensions of a physical quantity is called the **dimensional formula**.

* Volume: $[V] = [M^0 L^3 T^0]$
* Speed: $[v] = [M^0 L T^{-1}]$
* Force: $[F] = [M L T^{-2}]$
* Mass density: $[\rho] = [M L^{-3} T^0]$

An equation obtained by equating a physical quantity with its dimensional formula is called a **dimensional equation**.

---

### 1.6 Dimensional Analysis and its Applications

#### 1.6.1 Checking Dimensional Consistency of Equations
> **Principle of Homogeneity of Dimensions:** The magnitudes of physical quantities may be added or subtracted only if they have the same dimensions.

In an equation $A + B = C$, $[A] = [B] = [C]$.

**Test of Equation of Motion:**
$$x = x_0 + v_0 t + \frac{1}{2} a t^2$$

Dimensions of each term:
* $[x] = [L]$
* $[x_0] = [L]$
* $[v_0 t] = [L T^{-1}][T] = [L]$
* $\left[\frac{1}{2} a t^2\right] = [L T^{-2}][T^2] = [L]$

As every term on both sides has dimension $[L]$, the equation is **dimensionally consistent**.

---

## 📄 Page 9

#### 1.6.2 Deducing Relation among Physical Quantities

Consider a simple pendulum. Its time period $T$ may depend on:
1. Mass of bob $m$ ($[M]$)
2. Length of pendulum $L$ ($[L]$)
3. Acceleration due to gravity $g$ ($[L T^{-2}]$)

Let $T = k \cdot m^x \cdot L^y \cdot g^z$, where $k$ is a dimensionless constant.

Equating dimensions on both sides:
$$[M^0 L^0 T^1] = [M]^x \cdot [L]^y \cdot [L T^{-2}]^z = [M^x L^{y+z} T^{-2z}]$$

Equating powers of $M$, $L$, $T$:
* $x = 0$
* $y + z = 0 \implies y = -z$
* $-2z = 1 \implies z = -1/2, \quad y = 1/2$

Substituting values:
$$T = k \cdot m^0 \cdot L^{1/2} \cdot g^{-1/2} = k \sqrt{\frac{L}{g}}$$

Experimentally, $k = 2\pi$, hence:
$$T = 2\pi \sqrt{\frac{L}{g}}$$

---

## 📄 Page 10

### 📝 Summary

1. **Fundamental Quantities:** Physics is a quantitative science based on 7 base quantities ($L, M, T, A, K, \text{mol}, \text{cd}$) and 2 supplementary angles (radian, steradian).
2. **SI System:** Globally standard decimal unit system revised in 2018 based on fundamental invariants of nature ($c, h, e, k, N_A, \Delta\nu_{\text{Cs}}, K_{\text{cd}}$).
3. **Significant Figures:** Reliable digits + one uncertain digit indicate precision of measurement.
4. **Dimensional Consistency:** Terms added or subtracted must have identical dimensions.
5. **Limitations of Dimensional Analysis:** Cannot determine dimensionless proportionality constants ($k = 2\pi$), trigonometric, logarithmic or exponential terms.

---

## 📄 Page 11 & 12

### 🎯 Exercises & NCERT Numericals

#### Exercise 1.1: Fill in the Blanks
* **(a)** The volume of a cube of side $1\text{ cm}$ is equal to $\mathbf{10^{-6}\text{ m}^3}$.
  * *Reason:* $V = (1\text{ cm})^3 = (10^{-2}\text{ m})^3 = 10^{-6}\text{ m}^3$.
* **(b)** The surface area of a solid cylinder of radius $2.0\text{ cm}$ and height $10.0\text{ cm}$ is equal to $\mathbf{1.5 \times 10^4\text{ mm}^2}$.
  * *Reason:* $A = 2\pi r (r + h) = 2 \times 3.14 \times 20\text{ mm} \times (20 + 100)\text{ mm} \approx 1.5 \times 10^4\text{ mm}^2$.
* **(c)** A vehicle moving with a speed of $18\text{ km}\cdot\text{h}^{-1}$ covers $\mathbf{5\text{ m}}$ in $1\text{ s}$.
  * *Reason:* $18 \times \frac{5}{18}\text{ m/s} = 5\text{ m/s}$.
* **(d)** The relative density of lead is $11.3$. Its density is $\mathbf{11.3\text{ g}\cdot\text{cm}^{-3}}$ or $\mathbf{11.3 \times 10^3\text{ kg}\cdot\text{m}^{-3}}$.

#### Exercise 1.2: Unit Conversions
* **(a)** $1\text{ kg}\cdot\text{m}^2\cdot\text{s}^{-2} = \mathbf{10^7\text{ g}\cdot\text{cm}^2\cdot\text{s}^{-2}}$
* **(b)** $1\text{ m} = \mathbf{1.057 \times 10^{-16}\text{ ly}}$
* **(c)** $3.0\text{ m}\cdot\text{s}^{-2} = \mathbf{3.888 \times 10^4\text{ km}\cdot\text{h}^{-2}}$
* **(d)** $G = 6.67 \times 10^{-11}\text{ N}\cdot\text{m}^2\cdot\text{kg}^{-2} = \mathbf{6.67 \times 10^{-8}\text{ cm}^3\cdot\text{s}^{-2}\cdot\text{g}^{-1}}$

#### Exercise 1.3: New System of Units
A calorie equals $4.2\text{ J} = 4.2\text{ kg}\cdot\text{m}^2\cdot\text{s}^{-2}$. In a new system where unit of mass is $\alpha\text{ kg}$, unit of length is $\beta\text{ m}$, and unit of time is $\gamma\text{ s}$:
$$1\text{ cal} = 4.2 \times [\alpha\text{ kg}]^{-1} [\beta\text{ m}]^{-2} [\gamma\text{ s}]^2 = \mathbf{4.2\, \alpha^{-1} \beta^{-2} \gamma^2 \text{ new units}}.$$
