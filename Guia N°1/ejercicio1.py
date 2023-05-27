parrafo = """La Universidad de los Lagos es una institucion estatal fundada en 1993.
 Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio.
   Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y 
   participacion democratica."""
palabras = parrafo.split()  
contador = 0
for palabra in palabras:
    if palabra.lower() == "universidad":
        contador += 1
resultado = (contador)  
print(resultado)