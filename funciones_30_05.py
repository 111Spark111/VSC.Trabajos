#declarando una funcion simple
print("__________________________declara funcion________________________________")
def mi_primera_funcion():
    print("esta es mi primera funcion")
mi_primera_funcion()

#declarar una funcion
print("_____________________declara funcion y utilisandola_________________________")
def concatenar(lista1,lista2):
    return lista1 + lista2

lista1=[1,2,3]
lista2=[4,5,6]

print(concatenar(lista1,lista2))

def multiplica(numero1,numero2):
    return numero1*numero2

print(multiplica(3,3))
#eclara funcion y utilisandola
print("_______________________eclara funcion y utilisandola_______________________")

def resta(a,b):
    return a-b
a=int(input("ingrese el balor de a:"))
b=int(input("ingrese el balor de b:"))

resultado=resta(a,b)
print(resultado)