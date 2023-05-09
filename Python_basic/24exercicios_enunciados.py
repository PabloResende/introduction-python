
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

entrada = input('digite um número inteiro ')
if entrada.isdigit():# '.isdigit' ou '.(alguma coisa)' ajuda á verificar
    entrada_int = int(entrada)# entrada_int recebe entrada
    par_impar = entrada_int % 2 == 0# modo de verificar se é par ou impar

    par_impar_texto = 'ímpar'# recebe ímpar só para facilitar

    if par_impar: #ou if par_impar == True para ser mais específico porém não precisa
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')

else:
    print('você não digitou um número')

# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
# descrito, exiba a saudação apropriada. Ex.
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

entrada = input('que horas são aí? ')

try:

    hora = int(entrada)#para converter o número em inteiro

    if hora >= 0 and hora <= 11:# tudo maior ou igual á 0-11 vai ser bom dia
        print('bom dia!')
    elif hora >= 12 and hora <= 17:# e assim por diante
        print('boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('boa noite!')
    else:
        print('não conheço essa hora')
        #precisa desse else porque o except só vai pegar strings
        #isso porque tudo que passar por entrada e for int vai ser executado
        #devido á sintaxe 'hora = int(entrada)'
except:
    print('por favor, fale uma hora válida')


# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"


nome = input('qual o seu nome? ')
tamanho_do_nome = len(nome)# len( ) serve para dizer o tamanho do nome por exemplo

if tamanho_do_nome >= 0 and tamanho_do_nome <= 4:
    print('seu nome é curto')
elif  tamanho_do_nome >= 5 and tamanho_do_nome <= 6:
    print('seu nome é longo')

else:
    print('digite um nome')