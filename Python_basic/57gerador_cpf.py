import random

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))
    # print(nove_digitos)#assim dá errado\
    #o print tem q ficar de fora
print(nove_digitos)
print(
    random.randint(0,20)
)


# frase = 'ハローワールド'
# for i in frase:
    # print(frase) têm que printar o indice e não a frase
    # print(i)