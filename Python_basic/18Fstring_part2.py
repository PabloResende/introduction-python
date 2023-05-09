''''
formatação básica de  strings
s - string
d - int
f - float
.<número  de dígitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
= força o número a parecer antes do ponto
< - direita 
> - esquerda
^ - centro
sinal - = ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a __repr__ __str__ 
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel : >10}')#move para esquerda
print(f'{variavel : ^10}')#fica centralizado
print(f'{variavel :$>10}')#é possível preencher os espaços com  quaisquer caracteres
# (mas não se pode pular espaço depois de :)
print(f'{variavel :>10}.')#ABC.( o ponto fica do lado de fora)
print(f'{1000.152305587: .2f}')#1000.15
print(f'{1000.190458289:0=+10,.1f}')#+001,000.2 tá mostrando que é positivo '+' e
# e também os alguns números antes do ponto
print(f'{1000.190458289:3=+10,.1f}')#+331,000.2
print(f'{1000.190458289:3=-10,.1f}')#3331,000.2
print(f'{1000.190458289:0=-10,.1f}')#0,001,000.2
print(f'{1000.190458289:=10,.1f}')# 1,000.2
print(f'o hexadecimal de 1500 é {1500:08x}')#o hexadecimal de 1500 é 000005dc