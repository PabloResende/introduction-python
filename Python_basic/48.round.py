"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal#quando se quer ter máxima de precisão

numero_1 = decimal.Decimal('0.1')#para que dê certo é precisa que os\
#números estejam como strings
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)#0.8
print(f'{numero_3:.2f}')#0.80
print(round(numero_3, 2))#0.80
#o round é usado pra fazer\
#essa formatação específica que a 'f' string usa