"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
Refatorar um código é edita-lo
"""

def soma(x, y, z= None):

    if z is not None:
        print(
            f'{x=}, {y=}, {z=}',\
                x + y + z
)
    else:
        print(
            f'{x=}, {y=}, {z=}',\
              x + y
)

soma(1, 2) #x=1, y=2, z=None 3
soma(300, 100) #x=300, y=100, z=None 400
soma(9, 7, z=0) #x=9, y=7, z=0 16