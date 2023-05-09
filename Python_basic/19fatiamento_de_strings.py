''' fatiamento de strings
 012345678
 olá mundo
-987654321
Fatiamento [i:f:p:] [::]
Obs: a função len retorna a quantidade 
de caracteres da sting
'''

var = 'olá mundo'
print(var [-4])#ou 5, ambos resultam em 'u'
print(var [4:])#mundo (mostrou o resto da frase porque,
# nada foi colocado depois de ':')
print(var [4:7])#mun( porque para antes de chegar no 7)
#então sempre deve ser fatiado um número antes
#(ou seja, o índice final geralmente não é incluído)
print(len(var))#usa se para checar o tamanho de
# determinada string( resultado vai ser 9)
print(var[0:9:1])#checa do início ao fim,
# e pula de um em um(R = 'Olá mundo')
print(var[0:9:2])#igual o de cima,
# porém pula de 2 em 2 (R = 'oámno')
print(var[::-1])#inverte a string (R= 'odnum álo')

