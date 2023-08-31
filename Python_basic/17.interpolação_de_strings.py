''' 
interpolação básica de strings use se '%' seguido dos seguintes carácteres:
s - string
d e i - int
f - float 
x e X hexadecimal(ABCDEf0123456789)
'''
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o menor preço é R$%.2f' % (nome, preco)
print(variavel)#Luiz, o menor preço é R$1000.96 

print('o hexadecimal de %d é %04x' % (15, 15))#o hexadecimal de 15 é 000f    
# or
print('o hexadecimal de %d é %x' % (15, 15))#o hexadecimal de 15 é f
# or
print('o hexadecimal de %d é %08x' % (15, 15))#o hexadecimal de 15 é 0000000f 
#or
print('o hexadecimal de %d é %08x' % (1500, 1500))#o hexadecimal de 1500 é 000005dc
#or
print('o hexadecimal de %d é %08X' % (15, 15))#o hexadecimal de 15 é 0000000F 