import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
init(autoreset=True)

#Integral from-to
a , b = 0 , 1 
#Function return our function example which the exponent represent the sensor data with time
def f(x):
    return np.exp(-x**2)

n = 4
h = (b - a) / n
#the numpy.linspace will return value between a and b with interval of (n)
x_nodes = np.linspace(a, b, n + 1)
#setting the step value into the function
y_nodes = f(x_nodes)

y_values_simsons = []
def simSons(h, arr_nodes):
    intern_simsons = 0
    list_intern = []
    
    for nodes in range(1, len(arr_nodes)-1):
        if(nodes % 2 != 0):
            cal_trap_step = (4*arr_nodes[nodes])
            list_intern.append(float(cal_trap_step))
            intern_simsons += cal_trap_step
        elif(nodes%2 ==0):
            cal_trap_step = (2*arr_nodes[nodes])
            list_intern.append(float(cal_trap_step))
            intern_simsons += cal_trap_step
        
    
    res_simsons = h/3 * (arr_nodes[0] + intern_simsons + arr_nodes[-1])

    global y_values_simsons
    y_values_simsons = [float(arr_nodes[0])] + list_intern + [float(arr_nodes[-1])]
    
    return float(res_simsons)
#calulcating with trapezoidal method
res = simSons(h, y_nodes)
print(Fore.CYAN + "╔═══════════════════════════════════════════════════════════════╗")
print(Fore.CYAN + "║             Simpson's Rule Integration Results                ║")
print(Fore.CYAN + "╚═══════════════════════════════════════════════════════════════╝\n")
x_values_simsons = x_nodes
print(Fore.YELLOW + f"➤ Simpson's estimate value is: {res:.3f}\n")

print(Fore.GREEN + "➤ The integral steps (x values):")
print("  " + ", ".join([f"{x:.3f}" for x in x_values_simsons]) + "\n")

print(Fore.MAGENTA + "➤ Function evaluations at each step:")
print(Fore.MAGENTA + "  " + "-" * 50)

for i, x in enumerate(x_values_simsons):
    print(f"  f(x{i}) = {f(x):.3f} at x = {x:.3f}")

print(Fore.CYAN + "\n" + "*" * 65)
# Plot function
x_dense = np.linspace(a, b, 800)
y_dense = f(x_dense)

plt.figure(figsize=(10, 6))
plt.plot(x_dense, y_dense, 'o-', label='∫ e^(-x^2) dx', linewidth=4, color='magenta')
plt.plot(x_nodes, y_nodes, 'o-', label='Sample points', color='green')
plt.plot(x_values_simsons, y_values_simsons, 'o-', label='f(x) values', linewidth=1, color='purple')
plt.fill_between(x_nodes, y_nodes, alpha=0.3, color='orange', label=f'Trapezoidal area ≈ {res}')

plt.text(x=0.6, y=3.8, s='Green: ∫₀¹ -x² dx', color='green', fontsize=11)
plt.text(x=0.6, y=3.6, s='Mahenta: Simsons line', fontsize=11 , color='magenta')
plt.text(x=0.6, y=3.4, s='Purple: Simsons step calculation', fontsize=11, color='purple')
plt.text(x=0.6, y=3.2, s='Orange: Simsons apx area', fontsize=11, color='orange')


plt.show()