while True:#enquanto for verdadeiro:

#os 3 'inputs' a seguir servem para digitar os números mais o  operador
    num1 = input('digite um número')
    num2 = input('digite outro número')
    operador = input('digite um operador')

    numeros_validos = None
    num1_float = 0
    num2_float = 0#sem as linhas '9 e 10' o try pode dar erro

    try:
        num1_float =  float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos  = None

    if numeros_validos is None:#não funciona se usar  =
        print('número inválido')
        continue#continue serve para não parar o código
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('operador inválido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue

    if operador == '+':
        print(f'{num1_float} + {num2_float} =',num1_float + num2_float)
    
    elif operador  == '-':
        print(f'{num1_float} - {num2_float} =',num1_float - num2_float)

    elif operador  == '/':
        print(f'{num1_float} / {num2_float} =',num1_float //  num2_float)
    
    elif operador  == '*':
        print(f'{num1_float} * {num2_float} =',num1_float * num2_float)

    sair = input('quer sair?').lower().startswith('s')
    print('saiu')
    if sair == True:
        break