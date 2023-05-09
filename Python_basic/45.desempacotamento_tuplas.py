'''introdução a desempacotamento + tuples( tuplas )'''

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)#em python se usa essas 'underlines' para dizer:
#'olha! essa é uma variável como qualquer outra\
#mas eu não vou usa-la'
#já o '*resto' serve para empacotar em outra lista\
#o que sobrou


# Tipo tupla - Uma lista imutável
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])#Luiz
print(nomes)#('Maria', 'Helena', 'Luiz')
print(resto)#[]