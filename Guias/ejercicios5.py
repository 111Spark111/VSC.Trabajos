#reto 5
x=input("ingrese un numero: ")
while x==str(x):
    print("porfabor solo use numeros")
    x=input(":")

xc=x/2

if int(xc):
    print("es un numero par")
else:
    print("es un numero inpar")