#Daniel Lima Lopez
#30/08/2017
#Lea dos conjutnos de coeficientes (a,b y c; d,e y f) y visualizar los valores de  x y y

print ("ax + by = c")
print ("dx + ey = f")

a = float(input("Ingresa a:"))
b = float(input("Ingresa b:"))
c = float(input("Ingresa c:"))
d = float(input("Ingresa d:"))
e = float(input("Ingresa e:"))
f = float(input("Ingresa f:"))

print ("",a,"X +",b,"Y =",c)
print ("",d,"X +",e,"Y =",f)

print ("X =", (c*e - b*f)/(a*e - b*d))
print ("Y =", (a*f - c*d)/(a*e - b*d))
