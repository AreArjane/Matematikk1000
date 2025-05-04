# Project README

This project implements solutions to four mathematical and computational problems (`oppgaver`) in Python:

1. **Theta Angle Calculation**: Compute the polar angle $\theta$ of a complex number using Python's \texttt{atan2} function.
2. **Maximal Point of a Function**: Analyze and find the maximum of the function $f(x) = e^{-x/4} \cdot \arctan x$ using calculus and Newton–Raphson iteration.
3. **Solving $Ax = b$ via Cramer's Rule**: Implement Cramer's rule to solve linear systems when $A$ is a non-singular square matrix.
4. **Motion Sensor Data Visualization**: Approximate the integral $\int_0^1 e^{-x^2} dx$ with the trapezoidal and Simpson's rules, and visualize sample sensor data over time.

---

## Table of Contents

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)

  * [1. Theta Angle Calculation](#1-theta-angle-calculation)
  * [2. Maximal Point of a Function](#2-maximal-point-of-a-function)
  * [3. Solving $Ax = b$ via Cramer's Rule](#3-solving-ax--b-via-cramers-rule)
  * [4. Motion Sensor Data Visualization](#4-motion-sensor-data-visualization)
* [Contributing](#contributing)
* [License](#license)

---

## Prerequisites

* Python 3.7 or higher
* Required libraries:

  * `numpy`
  * `scipy` (for numerical integration and root finding)
  * `matplotlib` (for plotting)

Install dependencies with:

```bash
pip install numpy scipy matplotlib
```

---

## Installation

1. Clone the repository:

   ```bash
   ```

git clone [https://github.com/yourusername/math-oppgaver.git](https://github.com/yourusername/math-oppgaver.git)
cd math-oppgaver

````
2. (Optional) Create and activate a virtual environment:
   ```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate     # Windows
````

3. Install dependencies as above.

---

## Usage

Below are usage examples for each task. You can import and run the functions from the provided modules.

### 1. Theta Angle Calculation

**Module:** `theta_angle.py`

This function computes the polar angle $\theta$ of a complex number $z = x + iy$ in radians, returning a value in $[0,2\pi)$.

```python
from theta_angle import theta_from_cartesian

# Example:
x, y = -1, 1
theta = theta_from_cartesian(x, y)
print(f"Angle: {theta:.4f} rad")  # Should be in second quadrant (~2.3562)
```

**Behavior by quadrant:**

* $x>0, y\ge0$: $\theta = \arctan(y/x)$
* $x>0, y<0$: $\theta = \arctan(y/x) + 2\pi$
* $x<0$: $\theta = \arctan(y/x) + \pi$
* $x=0, y>0$: $\theta = \pi/2$
* $x=0, y<0$: $\theta = 3\pi/2$
* $x=y=0$: raises `ValueError` (undefined angle)

---

### 2. Maximal Point of a Function

**Module:** `max_point.py`

We analyze $f(x) = e^{-x/4} \cdot \arctan x$ and derive the condition for a critical point:

$$
\arctan x - \frac{4}{x^2 + 1} = 0.
$$

Use Newton–Raphson to find the root of $g(x) = \arctan x - 4/(x^2 + 1)$:

```python
from max_point import find_maximum

# Find maximum near an initial guess, e.g., x0 = 1
x_max, f_max = find_maximum(x0=1.0)
print(f"Max at x={x_max:.4f}, f(x)={f_max:.4f}")
```

The module implements:

* Analytical derivative of $g(x)$
* Iterative update $x_{n+1} = x_n - g(x)/g'(x)$
* Convergence check and maximum value computation

---

### 3. Solving $Ax = b$ via Cramer's Rule

**Module:** `cramer.py`

This function solves $Ax = b$ for square matrix $A$ with non-zero determinant:

```python
import numpy as np
from cramer import solve_cramer

A = np.array([[2, -1, 0], [1, 3, 2], [0, 5, 1]])
b = np.array([1, 4, -2])
x = solve_cramer(A, b)
print("Solution x:", x)
```

Features:

* Checks that $A$ is square
* Computes $\det(A)$ and raises `ValueError` if zero
* Constructs matrices $A_i$ replacing column $i$ with $b$
* Returns solution vector $x = (\det(A_1)/\det A, \dots)$

---

### 4. Motion Sensor Data Visualization

**Module:** `motion_visualization.py`

Demonstrates numerical integration of $\int_0^1 e^{-x^2} dx$ using:

* **Trapezoidal rule**
* **Simpson's rule**

Also plots example sensor readings over time.

```python
from motion_visualization import integrate_and_plot

# No arguments: uses default n=4 intervals and sample data
integrate_and_plot()
```

**Output:**

* Prints approximate integral values for each method
* Displays a line plot of sensor data vs. time (minutes)

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with tests and documentation.

---

## License

MIT License © 2025
