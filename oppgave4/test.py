import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.exp(-x**2)

# Define the interval and number of subintervals
a, b = 0, 1
n = 4
h = (b - a) / n

# Create x values at the trapezoid points
x_trap = np.linspace(a, b, n + 1)
y_trap = f(x_trap)

# Plot the actual function curve
x_dense = np.linspace(a, b, 400)
y_dense = f(x_dense)

plt.figure(figsize=(10, 6))
plt.plot(x_dense, y_dense, 'b-', label='f(x) = e^{-x^2}')
plt.fill_between(x_dense, y_dense, alpha=0.1, color='red')

# Plot trapezoids and label them
for i in range(n):
    xs = [x_trap[i], x_trap[i], x_trap[i+1], x_trap[i+1]]
    ys = [0, y_trap[i], y_trap[i+1], 0]
    plt.fill(xs, ys, 'green', edgecolor='red', alpha=0.6, label=f'Trapezoid {i+1}' if i == 0 else "")

    # Mark the trapezoid index in the middle of each
    mid_x = (x_trap[i] + x_trap[i+1]) / 2
    mid_y = (y_trap[i] + y_trap[i+1]) / 2
    plt.text(mid_x, mid_y + 0.05, f'T{i+1}', ha='center', fontsize=9, color='white', weight='bold')

# Plot trap points and label them
plt.plot(x_trap, y_trap, 'ko', label='Sample points')
for xi, yi in zip(x_trap, y_trap):
    plt.text(xi, yi + 0.03, f'({xi:.2f}, {yi:.2f})', fontsize=8, ha='center')

# Final plot decorations
plt.title("Trapezoidal Rule Approximation of ∫₀¹ e^{-x²} dx with n=4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.ylim(0, 1.2)
plt.show()
