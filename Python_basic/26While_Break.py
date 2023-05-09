''''
repetições
While(enquanto) - executa uma ação enquanto
a condição for verdadeira
'''

condicao = True

while condicao:
    nome = input('qual o seu nome?')
    print(f'seu nome é {nome}')#  exemplo de código  infinito

    if nome == 'sair':
        break#  para parar o  código

print('acabou')

#outro exemplo:


contador = 0# aqui o valor inicial é zero, por tanto:

while contador < 10:# enquanto contador for menor que zero ele soma( se fosse <= iria contar até 11)
    contador = contador + 1# se fosse 100000 no lugar o contador iria somar 'contador + 1' até chegar lá
    print(contador)#sem isso não mostraria a execução de cima sendo feita

print('acabou')# printa 'acabou'  quando chegar na meta