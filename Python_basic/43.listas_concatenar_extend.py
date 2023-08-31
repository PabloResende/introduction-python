lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b  #apenas concatena as listas
lista_a.extend(lista_b) #já o extend junta uma lista na outra\
#porém não retorna valor algum, isso ocorre porque ele altera\
#o próprio valor
print(lista_a)#[1, 2, 3, 4, 5, 6]
print(lista_c)#[1, 2, 3, 4, 5, 6]
#ambos retornam o mesmo valor mas de formas diferentes



# Cuidados com dados mutáveis
# = - copiado o valor (imutáveis)
# = - aponta para o mesmo valor na memória (mutável)


lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)#['Qualquer coisa', 'Maria', 1, True, 1.2]
print(lista_b)#['Luiz', 'Maria', 1, True, 1.2]