#operadores de atribuição:
# = += -= *= /= //= %= **=


contador = 0# aqui o valor inicial é zero, por tanto:

while contador < 10:# enquanto contador for menor que zero ele soma( se fosse <= iria contar até 11)
    contador = contador + 1# se fosse 100000 no lugar o contador iria somar 'contador + 1' até chegar lá
    print(contador)#sem isso não mostraria a execução de cima sendo feita

print('acabou')# printa 'acabou'  quando chegar na meta

#jeito  melhor de fazer essa atribuição: 'contador = contador + 1'

contador2 = 1

contador2 += 2 # 3, também pode adicionar '' nos números para concatenar
print(contador2)

#outro  exemplo:

contador3 = 10


contador3 *= '2' #2222222222 se tirar as aspas o resultado é 20
print(contador3)
