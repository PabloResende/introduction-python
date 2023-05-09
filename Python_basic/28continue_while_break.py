contador = 0

while contador <= 100:
    contador +=1 # '+=1' adiciona +1 ao argumento 'contador'
    #enquanto for menor que 100, é um operador de atribuição

    if contador == 6:
        print('não vou mostrar o 6')
        continue #serve para continuar o código
    
    if contador >= 10 and contador <= 23:# pula do 10 ao 23
       print('não vou mostrar o', contador)
       continue

    print(contador)

    if contador == 40:
         break
