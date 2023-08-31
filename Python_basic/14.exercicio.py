primeiro_valor = input('digite um número: ')
segundo_valor = input('digite ouro número: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')

elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor} é maior que {primeiro_valor}')
#ou
# else:
#     print(f'{segundo_valor} é maior que o {primeiro_valor}')

else:
    primeiro_valor == segundo_valor
    print('os números são iguais')
