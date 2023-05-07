x=input("dato: ")
q=(x*2)
print(type(q))
print(f"el dato {q}")
numeros=[1,2,3]
palabras=["hola","como esta","mondongo"]
print(f"el tercer numero de la lista es {numeros[-1]}")
print(list(range(4,8)))# crea listas "range" segido de ("x") numero de elementos/ o ("x,z") desde un valor a otro
print(numeros,palabras)
print(len(palabras))
print(palabras[2])
#___________________________________________________________Clase___________________________________________________________________________
#                                                          (Claves)
datos_personales= {
    "nombre":{"carlos"},
    "apellido":{"Rivera"},
    "edad":19,
    "ColoColo":{"Campeon"}
}
print(len(datos_personales))
del datos_personales("nombre")#eliminar campo/clave del diccionario
