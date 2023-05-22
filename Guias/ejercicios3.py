#ejercicio 6
Grupo1={"marcos","grabriela","benjamin","matias"}
Grupo2={"marcos","nicolas","diego","matias"}
interseccion= Grupo1.intersection(Grupo2)
print(f"Los 2 grupos comparten estas personas {interseccion}")
#ejercicio 7
trabajadores=["marti","tomas","nicolai","beto","enrique"]
edades=[34,28,42,29,31]
relacionados=list(zip(trabajadores,edades))
print(f"los trabajadores y sus edades son: {relacionados}")
#ejercicio 8
x=str(input("mes: "))
if x in ("marzo", "abril", "mayo"):
    print("pertenese a primavera")
elif x in("junio", "julio", "agosto"):
    print("pertenese a verano")
elif x in ("septiembre", "octubre", "noviembre"):
    print("pertenese a otoño")
elif x in ("diciembre", "enero", "febrero"):
    print("pertenese a invierno")
else:
    print("eso no es un mes")
#ejercicio 9
numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]

numeros.remove(numeros[-1])
numeros.insert(0, 2)
numeros=list(set(numeros))
S=sum(numeros)
media=S/8
mediana=numeros[3],numeros[4]
print(f"{numeros} de media: {media} y mediana: {mediana} ")
#ejercicio 10
Agenda= {
    "Nombre" : "martin R.",
    "Direccion" : "calle san martin 31",
    "Ciudad" : "Osorno",
    "Numero telefonico" : "144180081"
}
Agenda["redes_sociales"]="Facebook","Instagram","Twitter"

Pre_facebook=Agenda["redes_sociales"][0]

print(f"red social: {Pre_facebook} , \n{Agenda}")
#print(Agenda("resdes_sociales")) X