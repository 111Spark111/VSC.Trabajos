ciudades=["Santiago","Temuco","Osorno","Punta Arenas"]
ICA=[134,99,245,50]
minimo= ICA.index(min(ICA))
print(f"la ciudad con el idice mas bajo es {ciudades[minimo]} con un indice  de {ICA[minimo]} ICA")
maximo=ICA.index(max(ICA))
print(f"La ciudad con el indice mas alto es {ciudades[maximo]} con un indice de {ICA[maximo]} ICA")

for i in range(len(ciudades)):
    if ICA[i] >= 0 and ICA[i] <=50:
        print(ciudades[i],"Tiene un indice de aire BUENO ")
    elif ICA[i] >= 51 and ICA[i] <= 100:
        print((ciudades)[i],"Tiene un indice de aire MODERADO")
    elif ICA[i] >= 101 and ICA[i] <= 150:
        print((ciudades)[i],"Tiene un indice de aire DAÑINO PARA GRUPOS SENCIBLES")
    elif ICA[i] >= 151 and ICA[i] <=200:
        print((ciudades)[i],"Tiene un indice de aire DAÑINO PARA LA SALUD")
    elif ICA[i] >= 201 and  ICA[i] <=300:
        print((ciudades)[i],"Tiene un indice de aire MUY DAÑINO PARA LA SALUD")
    else:
        print((ciudades)[i],"Tiene un indice de aire PELIGROSO")