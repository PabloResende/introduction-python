#for + range
#range -> range(start, stop, step)

numeros = range(0, 10, 2)#(o '0' é o start, o '10' é o número base\
# já o 'step' é por exemplo 'pule de 2 em 2)

#dá pra fazer negativo, basta pôr um  step negativo
# numeros = range(0, -10, -1)
# resultado:
# 0
# -1
# -2
# -3
# -4
# -5
# -6
# -7
# -8
# -9
for numero in numeros:
    print(numero)
#resultado:
# 0
# 2
# 4
# 6
# 8

#teste:
print('_____________\n')


nome ='pablo'

for letra in nome:
    print(letra)
#resultado:
#_____________

# p
# a
# b
# l
# o