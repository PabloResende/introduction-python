"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# print('valor' if True else 'outro valor')
# #se valor fosse 'false' então o else seria 'ativado'

digito = 9
novo_digito = 0 if digito > 9 else digito#mesma coisa que a linha de baixo
novo_digito = digito if digito <= 9 else 0
#se o digito for maior do que 9 ele retorna 0
#útil para validação de 'CPF' por exemplo
print(novo_digito)#9
print('valor' if True else 'outro valor' if True else 'fim')#valor
#NUNCA REPITA O EXEMPLO DE CIMA