import random
x=[]
for _ in range(20):
    xd=random.randint(40,350)
    x.append(xd)
print(x)
_x=input("pida buscar algun numero dentro de la lista: ")
_x=int(_x)
if _x in x :
    ocurrencias=x.count(_x)
    print(f"se encuentra en la lista el numero: {_x}")
    print(f"en esta cantidad de ocasiones: {ocurrencias}")
else:
    ocurrencias=x.count(_x)
    print("no se encuentra entre los numeros creados al azar")
    print(f"un total de: {ocurrencias} apariciones")
""""
def random_numeros20(x):
    lis=[]
    for i in range(x):
        _lis= random.randint(40,350,20)
        x.append(_lis)
    lis.append(x)
    return lis
    return random_numeros20
"""