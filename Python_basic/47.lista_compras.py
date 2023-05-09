import os
import time

lista = []

while True:
    print('Selecione uma opção')
    time.sleep(0.2)
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    time.sleep(.2)

    if opcao == 'i':
        os.system('cls')
        valor = input('Qual item deseja adicionar? ')
        time.sleep(.2)
        lista.append(valor)
    elif opcao == 'a':
        indice_string = input(
            'escolha um indice para apagar'
)
        time.sleep(.2)
        try:
            indice = int(indice_string)
            del lista[indice]
        except ValueError:
            print('por favor digite um número')
        except IndexError:
            print('índice não na lista')
        except Exception:
            print('erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('por favor, i a ou l')