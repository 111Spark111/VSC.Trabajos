numero = int(input("Ingrese un número: "))
factorial = 1
if numero == 0:
    factorial = 1
else:
    i = 1
    while i <= numero:
        factorial *= i
        i += 1
print("El factorial de", numero, "es:", factorial)
