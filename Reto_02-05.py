q=input("Nombre del estudiante: ")
w=input("Nombre de la asignatura: ")
e=float(input("nota del laboratoro 1°: "))
r=float(input("nota del laboratorio 2°: "))

promedio = (e * 0.3) + (r * 0.7)

dicionario = {
"nombre estudiante": q,
"nombre asignatura": w,
"nota 1:": e,
"nota 2:": r,
"promedio:":round (promedio, 1)
}

print(dicionario)
# ANTES| print(f"Datos ingresados: {lista}/y la nota final: {er}")