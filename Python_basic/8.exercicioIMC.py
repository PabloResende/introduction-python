nome = 'Pablo'
altura = 1.65
peso = 58
imc = (peso // (altura * altura))
#ou imc = peso / (altura * altura)
# print(nome, 'tem', altura, 'de altura, pesa', peso,'kg e seu imc é de', imc)
print(f'{nome} têm {altura} de altura, pesa {peso}kg e seu imc é de {imc}')
#outra forma é usar a potenciação, exemplo;
#imc = peso / altura ** 2

#três pontos se chama ellipses, serve para indicar que ali haverá um código:
#print(...) ira printar como 'ellipses'