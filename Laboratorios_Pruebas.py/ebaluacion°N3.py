censo={
    "LR_id":14,
    "LR_superficie":18426,
    "LR_habitantes":404432,
    "Ar_id":9,
    "Ar_superficie":31843,
    "Ar_habitantes":1046322
}
print(censo)

LRd=404432/18426
Ard=1046322/31843
censo["LR_densidad"]=(LRd)
censo["Ar_densidad"]=(Ard)
censo["lr_capital"]="valdivia"
censo["ar_capital"]="temuco"
censo["lr_comunas"]="rio bueno","la union","paillaco"
censo["ar_comunas"]="villarrica","purren","anglo"
censo["lr_provincia"]="ranco","valdivia"
censo["ar_provincia"]="cautin","malleco"
censo["lr_cordenadas"]=-53.1625,"°"
censo["ar_cordenadas"]=-70.9225,"°"

print(censo)

#_______________________________2______________________

a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]

c.insert(-1,10)
abc=(a,b,c)
d=[4,5,6]
abcd=(abc,d)

print(abcd)