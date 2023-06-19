def obtener_numeros_positivos():
    numeros = []
    while True:
        num = int(input("Ingrese un número entero positivo y -1 que terminar: "))
        if num == -1:
            break
        elif num > 0:
            numeros.append(num)
    return numeros
def resultados(numeros):
    suma_total = sum(numeros)
    suma_pares = sum(num for num in numeros if num % 2 == 0)
    suma_impares = sum(num for num in numeros if num % 2 != 0)
    promedio = suma_total / len(numeros) if len(numeros) > 0 else 0
    numero_mayor = max(numeros) if len(numeros) > 0 else 0
    resultado = f"La suma de pares es: {suma_pares}\n"
    resultado += f"La suma de impares es: {suma_impares}\n"
    resultado += f"La suma total es: {suma_total}\n"
    resultado += f"El promedio es: {promedio}\n"
    resultado += f"El número mayor ingresado fue: {numero_mayor}\n"
    if numero_mayor > promedio:
        resultado += f"El número es mayor es {numero_mayor}"
    elif numero_mayor < promedio:
        resultado += f"El número es menor es {numero_mayor}"
    else:
        resultado += f"El número es igual es {numero_mayor}"
    return resultado
numeros_ingresados = obtener_numeros_positivos()
resultados = resultados(numeros_ingresados)
print(resultados)
