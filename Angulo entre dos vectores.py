# -*- coding: utf-8 -*-
"""TareaPython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ProgramasParaFisicaComputacional/Tarea_PythonInicial/blob/master/TareaPython.ipynb

De le solución y convierta en código pyton los siguientes problemas. 


1. Escriba una función que calcula el ángulo entre dos vectores.
2. Escriba una función que devuelva los 3 ángulos con respecto a los ejes x, y y z de un vector tridimencional.
3. Escriba una función que calcule el producto vectorial entre dos vectores tridimensionales.
4. Traduzca el diagrama de flujo mostrado en la imagen al lenguaje Python y describa lo que realiza. 
![alt text](http://isapedraza.web.cern.ch/isapedraza/tmpWork/FisicaComputacional/diagrama.png)

5. Diseñar un algoritmo en python que imprima y sume una serie la serie de números 3,6,9,12,...,99
6. Escribir un algoritmo en python que lea cuatro números y que al final escriba el mayor de los cuatro.
7. Diseñar un algorimo  en pytohn para calcular la velocidad (en m/s) de los corredores de la carrera de 1.500 metros. La entrada consistirá en parejas de números (minutos y segundos) que dan el tiempo del corredos; por cada corredor, el algoritmo debe imprimir el tiempo en minutos y segundos, así como la velocidad media. 
  Ejemplo de entrada de datos: (3,53)(3,40)(3,46)(3,52)(4,0)(0,0). El último par de datos se utilizará como fin de entrada de datos. 
 
8. Escribir un algoritmo que calcule la superficie de un triángulo en función de la base y la altura. ($A= 1/2 *Base * Altura$)
 
9. Un sistema de ecuaciones lineales 
 \begin{equation}
ax + by = c
 \end{equation}
\begin{equation}
dx + ey = f
\end{equation}
 
 se puede resolver con las siguientes fórmulas: 
\begin{equation}
x = \frac{ce-bf}{ae-bd}
\end{equation}

\begin{equation}
y = \frac{af-cd}{ae-bd}
\end{equation}


10. Diseñar un programa en Python que lea los dos conjutnos de coeficientes (a,b y c; d,e y f) y visualice los valores de $x$ y $y$. 
 
 11. Diseñe un programa que grafique las siguietes funciones en una misma gráfica. En el rango de -10 a 15. 
 \begin{equation}
f1(x) = 2x^2 + 5x - 2
\end{equation}
\begin{equation}
f2(x) = 4x + 1
\end{equation}
---



---
"""

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