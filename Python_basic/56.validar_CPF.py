"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
import time
import sys
import re
MULTIPLICADOR = 0
i = 0
try:
    # expressão regular:
    cpf = input('digite seu cpf ')
    cpf_formatado = re.sub(
        r'[^0-9]',
        '',
        cpf
    )
    char_repetidos = cpf == cpf[0] * len(cpf)
    if char_repetidos:
        sys.exit()#essa parte quebra o código caso\
        #os caracteres sejam repetidos demais

    time.sleep(.3)
    print('validando seus dados...')

    for i in range(9):
        MULTIPLICADOR += int(cpf_formatado[i]) * (10 - i)

    primeiro_digito_cpf = (MULTIPLICADOR * 10) % 11
    verificar_primeiro_digito_cpf =(
        0 if primeiro_digito_cpf > 9 else primeiro_digito_cpf
    )
    ultimos_digitos_cpf = int(cpf.replace('.', '')[10:11])
    if verificar_primeiro_digito_cpf == ultimos_digitos_cpf:
        time.sleep(.3)
        print('verificado com sucesso')
    elif verificar_primeiro_digito_cpf == 0:
        time.sleep(.3)
        print('CPF inválido')

except ValueError:
    print('digite um cpf válido')
except AttributeError:
    print('digite apenas numeros')
except IndexError:
    print('digite um cpf válido')

# versão do professor:

# cpf_enviado_usuario = '74682489070'
# nove_digitos = cpf_enviado_usuario[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito in nove_digitos:
#     resultado_digito_1 += int(digito) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11

# resultado_digito_2 = 0
# for digito in dez_digitos:
#     resultado_digito_2 += int(digito) * contador_regressivo_2
#     contador_regressivo_2 -= 1
# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
#     # print(f'{cpf_enviado_usuario} é válido')
# else:
#     print('CPF inválido')