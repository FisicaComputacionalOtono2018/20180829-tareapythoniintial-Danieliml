#Daniel Lima Lopez
#30/08/2017
#Función que devuelva 
#los 3 ángulos con respecto a los ejes x, y y z de un vector tridimencional.

import math
import numpy as np

v = np.arange(3)

v[0] = input("Ingresa v x: ")
v[1] = input("Ingresa v y: ")
v[2] = input("Ingresa v z: ")

mv2 = math.sqrt(v[0]**2 + v[1]**2)
mv3 = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
ax = math.acos(v[0]/mv2)
ay = math.asin(v[0]/mv2)
az = math.asin(v[2]/mv3)

print ("El angulo con el eje x es:",ax*180/math.pi)
print ("El angulo con el eje y es:",ay*180/math.pi)
print ("El angulo con el eje z es:",az*180/math.pi)
