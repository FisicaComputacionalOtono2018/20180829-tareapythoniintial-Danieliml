#Daniel Lima Lopez
#30/08/2017
#Calcular la velocidad (en m/s) de los corredores de la carrera de 1.500 metros.
#La entrada consistirá en parejas de números (minutos y segundos) que dan el
#tiempo del corredos; por cada corredor, el algoritmo debe imprimir el tiempo 
#en minutos y segundos, así como la velocidad media. Ejemplo de entrada de 
#datos: (3,53)(3,40)(3,46)(3,52)(4,0)

import numpy as np

print ("Calcular la velocidad (en m/s) de los corredores de la carrera de 1.500 metros")
aux = 0
datos = input("Ingresa las distancias en el formato (m1,s1)(m2,s2)...(mn,sn)")

for i in range(0,len(datos)):
  if datos[i] == '(':
    aux = aux + 1

print ("El numero de corredores es:", aux)
    
datos = datos.replace(')(',' ').replace('(','').replace(')','').replace(',',' ')

m = np.arange(aux)
s = np.arange(aux)
a = np.arange((aux*2+1))
a[aux*2] = len(datos)

aux2 = 0
for i in range (0,len(datos)):
  if datos[i] == ' ':
    a[aux2+1] = i
    aux2 = aux2 + 1
   
maux = 0
saux = 0
auxc = 0
for i in range(0,aux*2):
  n = 0
  r = a[i+1] - auxc
  
  jaux = 0
  for j in range(auxc,a[i+1]):
    
    suma = int(datos[j])*10**(r-jaux-1)
    n = n + suma
    jaux = jaux + 1  
    auxc = a[i+1] + 1
  
  if i%2 == 0:
    m[maux] = n
    maux = maux + 1
  else:
    s[saux] = n
    saux = saux + 1
      
vaux = 0 

for i in range(0,aux):
  print ("El tiempo del corredor", 1+i,"fue de:",m[i],"minutos y",s[i],"segundos")

for i in range(0,aux):
  print ("La velocidad del corredor",1+i,"es:",float(1500/(m[i]*60+s[i])),"m/s")
  vaux = vaux + float(1500/(m[i]*60+s[i]))
  
print ("La velocidad promedio de todos los corredores es:",float(vaux/aux))
