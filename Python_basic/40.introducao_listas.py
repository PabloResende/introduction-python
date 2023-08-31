"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
string = 'ABCDE'
#índice..0..........1..........2.....3..4
#.......-5.........-4.........-3....-2.-1
lista = [123, 'luiz  otavio', 1.2, True,[]]
print(lista[2])#1.2
print(lista[-5])#123
print(type(lista[-2]))#<class 'bool'>
print(lista[1].upper())#LUIZ  OTAVIO
print(lista[0])#123
# print(bool([])) retorna : False
# print(lista, type(lista))[] retorna : <class 'list'>
#é possível alterar o valor de algum elemento da lista:
lista[1] = 'maria'
print(lista)#[123, 'maria', 1.2, True, []]
