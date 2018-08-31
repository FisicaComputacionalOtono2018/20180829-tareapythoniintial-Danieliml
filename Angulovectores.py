#Daniel Lima Lopez
#30/08/2017
#Calcular el angulo entre dos vectores

import math
import numpy as np

v1 = np.arange(3)
v2 = np.arange(3)

v1[0] = input("Ingresa v1 x: ")
v1[1] = input("Ingresa v1 y: ")
v1[2] = input("Ingresa v1 z: ")
v2[0] = input("Ingresa v2 x: ")
v2[1] = input("Ingresa v2 y: ")
v2[2] = input("Ingresa v2 z: ")

p = v1 @ v2

mv1 = math.sqrt((v1[0])**2 + v1[1]**2 + v1[2]**2)
mv2 = math.sqrt((v2[0])**2 + v2[1]**2 + v2[2]**2) 

a = math.acos(p / (mv1 * mv2))

print ("El aungulo entre los vectores es", a*180/math.pi)
