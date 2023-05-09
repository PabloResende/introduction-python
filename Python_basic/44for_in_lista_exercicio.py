
"""
for in com listas
exiba os nomes e os índices usando for in mais lista
"""
lista = ['Maria', 'Helena', 'Luiz']
#para adicionar algo a lista teria que ser antes de len:
lista.append('joão')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
    # 0 Maria
    # 1 Helena
    # 2 Luiz
    # 3 joão