num = 0
while num <= 100:
    print(num)
    num += 2     #a la bariable se le suma 2 cada repeticion 

# print(Fore.RED + "Primer Bucle terminado!\n")

while num <= 200:
    print(num)
    num += 2
else: 
    print("Mi condicion es igual o mayor a 200") # se puede combinar con else

while num <= 300:
    print(num)
    num += 2
    if num == 250:
        print("Mi condicion es igual a 250") #combinable con if

# por lo que parese no se puede poner un While dentro de un if <<<- investigar