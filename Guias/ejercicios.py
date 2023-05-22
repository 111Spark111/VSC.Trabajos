print("tres numeros")
q=input(":")
w=input(":")
e=input(":")
m=max(q,w,e)
n=min(q,w,e)
print("mayor: ",m, "y menor:",n)
#______________________________________________________________________________-
print("dos palabras")
q=(str(input("palabra1: ")))#str son palabras
w=(str(input("palabra2: ")))
if len(q)>len(w):
    print(f"mayor |{q}| menor |{w}|")
elif len(q)<len(w):
    print(f"mayor |{w}| menor |{q}|")
else:
    print("tienen la misma cantidad de letras")
#_____________________________________________________________________________-
print("los lados del triangulo son:")
z=float(input(":"))# \n es para bajar una linea
x=float(input(":"))
c=float(input(":"))

p=(z+x+c)/2
area=(p*(p-z)*(p-x)*(p-c))**0.5

if z==x==c:
    print(f"es equilatero, de area {area}")
elif z<x==c or z==x<c or z==c<x:
    print(f"es escaleno de area {area}")
else:
    print(f"es escaleno de area {area}")