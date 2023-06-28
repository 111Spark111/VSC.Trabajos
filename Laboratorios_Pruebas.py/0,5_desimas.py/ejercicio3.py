def es_bisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True

año = int(input("Ingrese un año: "))
if es_bisiesto(año):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")
