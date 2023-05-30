def palabra_en_lista(x):
    x1=x.split()
    _x_=[]
    _x_.extend(x1)
    _x1_=len(_x_)
    return _x1_

x=str(input("escriba una plalabra: "))

print(palabra_en_lista(x))