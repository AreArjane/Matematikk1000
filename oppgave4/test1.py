import numpy as np
import matplotlib.pyplot as plt

#Integral from-to
a , b = 0 , 1 
#Function return our function example which the exponent represent the sensor data with time
def f(x):
    return np.exp(-x**2)
#Calculating the trapezoidal method. The function expected a h value and list of noes representing the integral step
#loop range start from the second element of array and end with left last element. Therfoe having {(arr_nodes) - 1} 
#intern_trapezoidal the value we add together inside the trapezoidal step 2 * f(xn) where a < n < b
#cal_trap_step multiplty the f(xn) where a < n < b with (2) following trapezoidal formula
#Finally adding all together with res_trap [0] return first element , [-1] return last element of array. 
#y_values_y holding the trapezoidal step result for plotting, defin it as golbal to be modify in function
y_values_trapezoidal = []
def trapezoidal(h, arr_nodes):
    intern_trapezoidal = 0
    list_intern = []
    for nodes in range(1, len(arr_nodes)-1):
        cal_trap_step = (2*arr_nodes[nodes])
        list_intern.append(float(cal_trap_step))
        intern_trapezoidal += cal_trap_step
    
    res_trap = h/2 * (arr_nodes[0] + intern_trapezoidal + arr_nodes[-1])

    global y_values_trapezoidal
    y_values_trapezoidal = [float(arr_nodes[0])] + list_intern + [float(arr_nodes[-1])]

    return float(res_trap)


#subintervals (must be even for simsons method)
n = 4
h = (b - a) / n
#the numpy.linspace will return value between a and b with interval of (n)
x_nodes = np.linspace(a, b, n + 1)
#setting the step value into the function
y_nodes = f(x_nodes)

#calulcating with trapezoidal method
res = trapezoidal(h, y_nodes)
print(f"Trapezoida {res}")
x_values_trapezoidal = x_nodes
print(x_values_trapezoidal)
print(y_values_trapezoidal)
# Plot function
x_dense = np.linspace(a, b, 800)
y_dense = f(x_dense)

plt.figure(figsize=(10, 6))
plt.plot(x_dense, y_dense, 'b-', label='f(x) = e^{-x^2}', linewidth=4, color='magenta')
plt.plot(x_nodes, y_nodes, 'bo-', label='Sample points', color='green')
plt.plot(x_values_trapezoidal, y_values_trapezoidal, 'bo-', label='f(x) values', linewidth=1, color='purple')
plt.fill_between(x_nodes, y_nodes, alpha=0.3, color='orange', label=f'Trapezoidal area ≈ {res}')

plt.text(x=0.6, y=1.8, s='Green: f(x)', color='green', fontsize=11)
plt.text(x=0.6, y=1.7, s='Mahenta: Trapezoidal line', color='magenta', fontsize=11)
plt.text(x=0.6, y=1.6, s='Purple: Trapezoidal calculation', color='purple', fontsize=11)
plt.text(x=0.6, y=1.5, s='Orange: trapezoidal apx area', color='orange', fontsize=11)


plt.show()
