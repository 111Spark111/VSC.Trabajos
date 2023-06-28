# Tuplas________________________________________________________________________________________________________________________
t = 1, 2, 3
tupla = "Pedro", "juan", "Digo", "TIto"

tuplaordenada = sorted(tupla)
print(tuplaordenada)

print(type(t))
print(type(tupla)) #tipo de datos con los que se trabaja

alumnas = [("Lorena", 6.5, 6.9), ("Maria", 3.9, 4.1), ("Anais", 5.4, 4.8)]
print(alumnas)

for estudiante in alumnas:
    print(estudiante)

# Listas_______________________________________________________________________________________________________________________

Nuevalista = [0,1,2,[10,20,30]] #una lista dentro de otra

print(Nuevalista[3][0]) #pocicion de la lista -> []

l = list(range(1,11)) #crea una lista
print(sum(l)) 
