texto = 'entrando...' #para iterar sobre essa string é preciso:

i = 0 #criar um índice
novo_texto = ''

while i < len(texto):# então criar um laço de repetição onde\
    #enquanto o índice for menor que 'tamanho_string':
    letra = texto[i] #letra recebe texto e índice
    novo_texto += letra #então é criada uma variável junto com += pra que print na horizontal
    i += 1 #item obrigatório
print(novo_texto)#mostrar a string que nesse caso é 'texto' mais a letra\
#mais a letra que queres mostrar que nesse caso é o índice\
#se print estiver com espaços mostra na vertical



senha_salva = '1234'
senha_digitada = ''
repeticoes = 0

while senha_digitada != senha_salva: #enquanto senha_digitada for diferente de senha_salva:
    senha_digitada = input('sua senha({repeticoes}x)')#mostra quantas senhas foram digitadas

    if senha_digitada != senha_salva:
        print('senha inválida')
        
    if senha_digitada == senha_salva:
        print('bem_vindo')
        break

    repeticoes += 1

    print(repeticoes)# pode virar um loop infinito