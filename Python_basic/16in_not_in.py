#Operadores in e not in
#Strings são iteráveis; 
# 0 1 2 3 4 5 positivos
# O T Á V I O
#-6-5-4-3-2-1 negativos

nome = 'otávio'
print(nome[2])#á
print(nome[-4])#á
print(10 * '-')
print('vio' in nome)#True
print('zero' in nome)#False
print(10 * '-')
print('vio' not in nome)#False
print('zero' not in nome)#True

#joguinho:

nome = input('digite seu nome: ')
encontrar = input('o que deseja  encontrar?')
if encontrar in nome:
    print(F'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
