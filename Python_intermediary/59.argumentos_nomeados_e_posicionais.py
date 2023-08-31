"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
#parâmetros são variáveis passadas pela 'def alguma coisa()'
#no caso os parâmetros ficam dentro dos parenteses
#valor = argumentos
#definição = parâmetros

#jeito não muito legal
# def soma(x, y):
    # definição:
    # print(x + y) #3
# print(soma(1, 2)
# )#retorna None porque é o padrão e funções
# dentro dos parenteses são os\
# argumentos dados as variáveis parâmetros
# se um argumento for nomeado, todos os próximos\
# também terão que ser nomeados

import random


def soma(x, y):
    print(f'{x=} y={y},' '|', 'x + y = ', x + y )
soma(1, 2)
# x=1 y=2,| x + y =  3
soma(x = 1, y = 2)# isso são parâmetros nomeados
# x=1 y=2,| x + y =  3
soma(
    x = random.randint(0,9),\
          y = random.randint(0, 9)
) # tentativa de criar valores aleatórios