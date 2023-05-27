list_numa = []
for i in range(500, 810, 10):
  list_numa.append(i)
sum_list = sum(list_numa)
print(list_numa)
list_nume = []
for i in range(456, -2, -2):
  list_nume.append(i)
sum_list = sum(list_nume)
print(list_nume)
a = (list_numa, list_nume)
sum_d = sum(list_numa + list_nume)
print("La suma de todos los numeros son", sum_d)