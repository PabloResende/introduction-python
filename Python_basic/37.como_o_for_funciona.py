'''
iterável -> range, str, etc.
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''
texto1 = iter('pablo') # isso ou você pode usar: 'pablo'.__iter__()
# print(texto)#<str_ascii_iterator object at 0x00000244041D2F80>
# print(texto.__next__())#repetindo esse exato print vai mostrando letra por ou:
print(next(texto1)) #p
print(next(texto1)) #a e assim por diante até acabarem os valores

print('_______\n')


numeros = range(0, 100, 8)

# for numero in numeros:
    # print(numero)
#0
# 8
# 16
# 24
# 32
# 40
# 48
# 56
# 64
# 72
# 80
# 88
# 96

#explicando o que o 'for' faz:
#for letra in texto ou:
#   #print(letra)
texto = 'luiz' #iterável
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

