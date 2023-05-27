tarifa_diurna = 12000  
tarifa_nocturna = 16000  
incremento_domingo_diurno = 2000  
incremento_domingo_nocturno = 3000  
empleado1 = {}
empleado1["Lunes"] = tarifa_nocturna * 10  
empleado1["Martes"] = tarifa_nocturna * 10  
empleado1["Miercoles"] = tarifa_nocturna * 10  
empleado1["Jueves"] = tarifa_diurna * 10  
empleado1["Viernes"] = tarifa_diurna * 10  
empleado1["Total_semanal"] = sum(empleado1.values())  
empleado2 = {}
empleado2["Martes"] = tarifa_nocturna * 10  
empleado2["Miercoles"] = tarifa_nocturna * 10  
empleado2["Jueves"] = tarifa_nocturna * 10  
empleado2["Domingo"] = (tarifa_diurna + incremento_domingo_diurno) * 10  
empleado2["Total_semanal"] = sum(empleado2.values())  
empleado3 = {}
empleado3["Miercoles"] = tarifa_diurna * 10  
empleado3["Jueves"] = tarifa_diurna * 10  
empleado3["Viernes"] = tarifa_diurna * 10  
empleado3["Sabado"] = tarifa_nocturna * 10  
empleado3["Domingo"] = (tarifa_nocturna + incremento_domingo_nocturno) * 10  
empleado3["Total_semanal"] = sum(empleado3.values())  
print("Empleado 1:")
print(empleado1)
print("")
print("Empleado 2:")
print(empleado2)
print("")
print("Empleado 3:")
print(empleado3)
