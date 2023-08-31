'''
Introdução a try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
numero_str = input('vou dobrar o número que você digitar ')
# if numero.isdigit():
#     numero = float(numero)
#     print(f'o dobro de {numero} é {numero * 2:.1f}')
# else:
#     print('isso não é um número')
try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.1f}')
except:
    print('isso não é um número')
