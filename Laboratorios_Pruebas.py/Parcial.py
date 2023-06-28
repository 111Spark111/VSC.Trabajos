#ejercicio1
x=input("ingrese su palabra: ")

if x[0]==x[-1] and x[1]==x[-2] and x[2]==x[-3]:
    print("esto se trata de un palindromo")
elif x[0]!=x[-1] and x[1]!=x[-2] and x[2]!=x[-3]:
    print("esto no es un palindromo")
else:
    print("esto no es un palindromo")

#ejercicio3
Temperaturas_Mínimas = {9, 5, 2, 7, 6, 1}
Temperaturas_Máximas = {12, 14, 11, 10, 15, 9}
nueve={9}
if len(Temperaturas_Máximas.intersection(nueve))>=0 and len(Temperaturas_Mínimas.intersection(nueve))>=0:
    print(f"se encuentra el nueve dentro de las dos listas el 9")
else:
    print("no se encuentra")

esto={6,17}
if  len(esto.intersection(Temperaturas_Máximas))>=2 or len(esto.intersection(Temperaturas_Mínimas))>=2:
    print("se encuentra dento el 6 y 17")
else:
    print("no se encuentra, ya se ambas o una de las temperaturas 6° y/o 17°")


TM4={i**4 for i in Temperaturas_Mínimas}
TX4={i**4 for i in Temperaturas_Máximas}
print(f"las temperaturas elebadas por 4 son {TM4} y {TX4}")
Temperatura_MM=TM4.union(TX4)
print(f"la union de ambos sets: {Temperatura_MM}")

#ejercicio2

"""
x=1
while x<=11:
    xo=list(range(1,x))
    print(xo)
    x+=1
"""

for x in "         1         ","        232        ","       34543       ","      4567654      ","     567898765     ","    67890109876    ","   78901232109987   ","  890123454321098  "," 90123456765432109 ","0123456789876543210":
    print(x)
