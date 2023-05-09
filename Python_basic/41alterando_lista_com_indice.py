"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [1, 2 , 3, 4]
lista[2] = 30 # essa linha muda o item 3 para 30
del lista[1] #já essa parte deleta o 2
print(lista)
print(lista[1]) #então o novo 1 é o 30\
# #porque o 2 foi apagado
#um método mais 'clean' de mudar algo na lista:
lista.append(50)
lista.append(60)
print(lista)#[1, 2, 3, 4, 50]
penultimo_item = lista.pop(3)#é possível também escolher o que o pop vai remover
ultimo_item = lista.pop()#append adiciona um item no final\
#e pop remove um do final
print(lista, 'removido', ultimo_item)#[1, 30, 4, 50] removido 60
print(lista, 'removido', penultimo_item)#[1, 30, 4] removido 50