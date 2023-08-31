nome = 'pablo'
idade =19 
peso = 58
altura = 1.65

#F string é a função que permite por variáveis dentro de strings
linha_1 = f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg'
print(linha_1)#pablo tem 19 anos, 1.65 de altura e pesa 58kg

#outra opção de formatação é {x:.xf} que serve para contar as casas decimais depois do ponto:
linha_2 = f'{nome} tem {idade} anos, {altura} de altura e pesa {peso:.2f}kg'
linha_3 = f'{nome} tem {idade} anos, {altura} de altura e pesa {peso:.10f}kg'

print(linha_2)#pablo tem 19 anos, 1.65 de altura e pesa 58.00kg
print(linha_3)#pablo tem 19 anos, 1.65 de altura e pesa 58.0000000000kg

#também é possível por uma vírgula para converter em dinheiro ou semelhante:

nome2 = 'pablo'
dinheiro = 15000
linha_4 = f'{nome} tem {dinheiro:,.1f} reais'
print(linha_4)# pablo tem 15,000.0 reais