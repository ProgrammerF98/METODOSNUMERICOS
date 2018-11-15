# Metodo de Euler
# y' - e^x = 0 y(0) = 1 y(5) = ?
# dy/dx = e^x
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return 2*x*y #aquí poner derivada

def euler(y0, x, h, f):
    y = []
    y.append(y0)
    for i in range(1, len(x)):
        y.append(y[i-1] + h*f(x[i-1], y[i-1])) #formula de euler
    return y

n = 11 #despejar n
a = 1 #valor inicial
b = 1.15 #valor de incognita
h = 0.05
x = np.linspace(a,b,n)
y = euler(1,x,h,f)

plt.plot(x,y,'g')
#plt.plot(x,[math.exp(xi) for xi in x], 'b')
plt.grid()

print('Valor de h:', h)

print('Valor x: ', x[-1])
print('Valor calculado y: ', y[-1])
