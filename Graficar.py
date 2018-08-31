#Daniel Lima Lopez
#30/08/2017
#Graficar las siguietes funciones en una misma gráfica. En el rango de -10 a 15.
#f1(x) = 2x^2 + 5x - 2
#f2(x) = 4x + 1

import numpy as np
import matplotlib.pyplot as plt

def f1(x):
  im = np.arange(250)
  
  for i in range(0,250):
    im[i] = 2*(x[i])**2 + 5*x[i] - 2
  return im
    
def f2(x):
  im = np.arange(250)
  for i in range(0,250):
    im[i] = 4*x[i] + 1
  return im

x = np.arange(-10.0,15.0,0.1)
y1 = np.arange(-10.0,15.0,0.1)
y2 = np.arange(-10.0,15.0,0.1)

plt.figure(1)
plt.subplot(111)
plt.plot(x,f1(x),x,f2(x))
plt.savefig('Graficas')
plt.show()
