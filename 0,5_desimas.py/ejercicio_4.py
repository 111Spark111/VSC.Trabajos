def desglosar_vuelto(vuelto):
    lucas = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    desglose = {}
    for luca in lucas:
        cantidad = vuelto // luca
        if cantidad > 0:
            desglose[luca] = cantidad
            vuelto -= cantidad * luca
    return desglose
monto_total = int(input("Ingrese el monto total de la compra: "))
monto_pagado = int(input("Ingrese el monto pagado: "))
if monto_pagado < monto_total:
    print("El monto es insuficiente.")
else:
    vuelto = monto_pagado - monto_total
    desglose_vuelto = desglosar_vuelto(vuelto)
    print("Desglose del vuelto:")
    for luca, cantidad in desglose_vuelto.items():
        print(f"${luca} pesos")

