q=input("Nombre del estudiante: ")
w=input("Nombre de la asignatura: ")
e=input("nota del laboratoro 1°: ")
r=input("nota del laboratorio 2°: ")

lista= q,w,e,r
e1=float(e)*(30/100)
r1=float(r)*(70/100)
er=e1+r1

print(f"Datos ingresados: {lista}/y la nota final: {(er):.2}")