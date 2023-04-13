#Datos numericos
peso=1
estatura=1
imc=0
#____________________________ignorar las definiciones de bariables por ariba de esta linea_______________________________________________________________
#                          Buscar funciones propias del python (len,float, int, str,type, list,count, tupla)
print("IMC: {:.2k}".format(imc))
inc=peso /(estatura**2)


listas= list()-[0,7,8,9]
len="leer numero de datos/(,x,c,v) eso serian 3 elemento)"
count="cuenta los elementos repetidos en una lista"

#_______________________________
arreglos=[0,9,"n",6,True]
#con dos[] se entiende como lista
#________________________________
print(type(listas))

numeros=[1,2,3,34,54,False,"palabras"]
print(numeros)
print(len(12))
print(numeros.count(3))

#acceder a elementos especificos en lista
listado=["sero 0/-3","uno 1/-2","dos 2/-1"]
print(listado[1])#busca el segundo elemento de la lista
print(listado[ -1])#busca el primer elemento de la lista, en direccion inbersa
c,p,x=listado#asigna bariable a listado
print(p)#exige bariable que es igual al listado
print(listas[0])#el numero en el corchete indica el elemnto de la lista del 0 al infinito/y (listas) se remplasa por el nombte del listado
#se pueden sumar listas, siempre y cuando solo sean numeros
#___________________________________________________________________________________________________________________________________________
#TUPLAS/no son modificables
#Como dividir tupla/combirtiendola en lista
grupo=("pedro",100,"juan","diegito",200)
grupo=list(grupo)
print("trozo de la tupla",grupo[0:3])

conjunto_vacio=list(grupo)
conjunto_vacio={}#diccionario o set?/ se inician de la misma manera
print(type(conjunto_vacio))
conjunto_color= set("azul","rojo","verde")
conjunto_animal= {"gato","perro","loro"}
print(conjunto_animal[1])