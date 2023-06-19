ingresar = int(input("indique cuantos numeros que va a ingresar: "))

lista = []
for i in range(ingresar):
    num = input(f"ingrese su {i + 1} numero: ")
    lista.append(num)
print(lista)

def sumatotal():
    total = 0
    for i in range(ingresar):
        total += int(lista[i])
    return total
print (f"la suma total es: {sumatotal()}")

def sumapares():
    total = 0
    pares = []
    for i in range(ingresar):
        if int(lista[i]) % 2 == 0:
            pares.append(lista[i])
        if int(lista[i]) % 2 != 0:
            pares.append(0)
        total += int(pares[i])
    return total
print(f"la suma de los numeros pares es: {sumapares()}")

def sumaimpares():
    total = 0
    impares = []
    for i in range(ingresar):
        if int(lista[i]) % 2 != 0:
            impares.append(lista[i])
        if int(lista[i]) % 2 == 0:
            impares.append(0)
        total += int(impares[i])
    return total
print(f"la suma de los numeros impares es: {sumaimpares()}")