
#Daniel Lima Lopez
#30/08/2017
#Imprimir y sumar la serie de números 3,6,9,12,...,99

aux = 0

for i in range(1,100):
  if i%3 == 0:
    print (i)
    aux = aux + i

print (aux)
