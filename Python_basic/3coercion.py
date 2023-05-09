'''Conversão de tipos, coerção
    type conversion, typecasting, coercion
    é o ato de converter um tipo em outro
    tipos imutáveis e primitivos
    str, int, float, bool'''

print(1+1)
print('a' + 'b')
#impossível concatenar uma str vom um int:
#print('1' + a) por isso usa se a concatenação

print('1', type('1'))
#'1' é uma str mesmo sendo um número devido as aspas

print(int('1'), type(int('1')))#int para converter a string em um número inteiro

#para fazer a soma de uma str com um int e ou float é necessário fazer uma coerção:
print(int('1') + 1)
print(float('1') + 1)
print(float('1.5') + 1)
print(bool(''))
print(str(11) + 'b')
