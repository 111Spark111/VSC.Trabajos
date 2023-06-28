#ejercicio numero 2
def Nombres_usuario():
    print("Escriba tantos nombres como quiera, luego para proseguir solo escriba textualmente |continuar|")
    x=input("presione enter para iniciar: ")
    lista=[]
    while x!="continuar":
        x=input("Nombre:")
        lista.append(x)
    lista.pop()
    return lista

def contar_letras():
    x=Nombres_usuario()
    x1=("".join(x))
    lx1=len(x1)
    print(f"los nombres son |{x}| y las letras en total en estos nombres son |{lx1}|")

def resultados():
    contar_letras() 

resultados()



"""
def Contar_letras():
    cl=len(lista1)
    print(cl)
Contar_letras()
"""