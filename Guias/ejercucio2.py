#ejercicio 4
q=input("tu nombre: ")
w=input("el segundo nombre: ")

if q[0]==w[0] and q[-1]==w[-1]:
    print(f"comiensan con la misma letra |{q[0]}| y terminan con la misma letra |{q[-1]}|")
elif q[0]!=w[0] and q[-1]==w[-1]:
    print(f"el ultimo es igual |{q[-1]}| el primero no")
elif q[0]==w[0] and q[-1]!=w[-1]:
    print(f"el primero es igual|{q[0]}| el ultimo no")
else:
     print("no empiesan o terminan iguales")
#ejercicio 5
a=float(input("primera nota: "))
s=float(input("segunda nota: "))
d=float(input("tercera nota: "))
promedio=(a*0.3)+(s*0.4)+(d*0.3)

if promedio>6.0:
    print(f"el estudiante aprueba con distincion {promedio}")
elif promedio>4.0:
    print(f"el estudiante aprobo con promedio {promedio}")
else:
    print(f"el estudiante reprobo con un promedio de {promedio}")