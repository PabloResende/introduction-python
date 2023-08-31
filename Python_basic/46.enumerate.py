
"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)
# print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)
    #(0, 'Maria')
    # (1, 'Helena')
    # (2, 'Luiz')
    # (3, 'João')
