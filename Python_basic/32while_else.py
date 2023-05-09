'''while/else'''
string = 'valor qualquer'

i =  0# muito normal usar a variável 'i' para contar índices
while i <len(string):
    letra = string[1]

    #if letra == '#' (se tiver um # o if é executado no lugar do else)
    # break (se haver esse break o else não é executado)

    print(letra)
    i += 1
else:
    print('o else foi executado')
print('fora do while')