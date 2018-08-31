#Daniel Lima Lopez
#30/08/2017
#Leer cuatro números y al final escribir el mayor de los cuatro.

import numpy as np

v = np.arange(4)

for i in range(0,4):
  v[i] = float(input("Ingrese un numero:"))
  
print (v)  


for i in range(0,4):
  aux = 0
  for j in range (0,4):
    if v[j] > v[i]:
      aux = 1
  if aux == 0:
    print ("El numero mayor es:",v[i])
    break
