q=2
w=3
e=20
r=20
a=q/w
print("resultado",a)
print("no se que hace esto {:.2f}".format(a))#el {:.2f} son cuantos decimales deben verse en pantalla

c2=complex(3,-5)#una parte real y la parte imaginaria despues de la coma
print(" hola " * 10)#aparesera "hola" 10 veses
print(" hola "*(int((9*2)/5)),"/n")# int=entero
#____________________________________________________________Terminos en operaciones_______________________________________________________

# a==b se afirma que "a" tendra el mismo valor que "b"
e==r
# simbolo de distinto =!
print(e==r)#saldra true o false
print(q<w)
animal1="gato"
animal2="leopardo"
print(animal1<animal2)#esto es incorecto
print(len(animal1)<len(animal2))# len= esto lee el numero de elementos

#___________________________________________________boleanos________________________________________________________________________________

bencina = False
encendido = True
edad=19

if bencina and encendido: #se puede usar el (and= y) y el (or= o)
    print("el beiculo puede avanzar")
else:
    print("el beiculo no puede avanzar")

#tambien el (if not= combierte el dato "False a True" y "True a False") 
if not bencina and not encendido:
        print("el beiculo puede avanzar")
else:
    print("el beiculo no puede avanzar")

if not bencina or (encendido and edad >= 18):
   print("el beiculo puede avanzar")
else:
    print("el beiculo no puede avanzar")