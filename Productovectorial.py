#Daniel Lima Lopez
#30/08/2017
#Calcular el producto vectorial de dos vectores

import math
import numpy as np

v1 = np.arange(3)
v2 = np.arange(3)
v = np.arange(3)

v1[0] = input("Ingresa v1 x: ")
v1[1] = input("Ingresa v1 y: ")
v1[2] = input("Ingresa v1 z: ")
v2[0] = input("Ingresa v2 x: ")
v2[1] = input("Ingresa v2 y: ")
v2[2] = input("Ingresa v2 z: ")

v[0] = v1[1]*v2[2] - v1[2]*v2[1]
v[1] = -(v1[0]*v2[2] - v1[2]*v2[0])
v[2] = v1[0]*v2[1] - v1[1]*v2[0]

print ("El producto vectorial de v1 X v2 es:", v)
