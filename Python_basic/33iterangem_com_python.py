frase  = 'o Python é  uma linguagem de programação '\
' multiparadigma '\
' Python foi criado por Guido Van Rossum.'

# print(frase.count('P'))#serve para contar quantas vezes
# #tal  ou tais caracteres apareceram na frase

i = 0# serve para contar os índices
qtd_apareceu_mais_vezes = 0
letra_que_mais_apareceu = ''

while i  < len(frase):
    letra_atual = frase[i]#'letra_atual' recebe 'frase' e 'i'

    if letra_atual == ' ':# esse if serve para pular os espaços
        i += 1 #essa atribuição serve para ir subindo o índice
        continue

    qtd_atual = frase.count(letra_atual)#count conta a quantidade de  caracteres \
    #dentro de 'frase' e 'letra_atual' recebe frase, já 'qtd_apareceu_mais_vezes_atual' \
    # serve para resumir tudo

    if qtd_apareceu_mais_vezes < qtd_atual:# se 'qtd_apareceu_mais_vezes' for menor que\
        #'qtd_apareceu_mais_vezes_atual', só o  maior irá aparecer porque o maior recebe o menor(embaixo):
        qtd_apareceu_mais_vezes = qtd_atual
        letra_que_mais_apareceu = letra_atual #'letra_que_mais_apareceu' recebe tudo para resumir  melhor


    i += 1


print('a letra que apareceu mais vezes foi '
    f'"{letra_que_mais_apareceu}"que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
) #a letra que apareceu mais vezes foi "o" que apareceu  10x
print(qtd_atual)#1
print(qtd_apareceu_mais_vezes)#10
print(letra_que_mais_apareceu)#o
print(frase)#o Python é  uma linguagem de programação  multiparadigma \
#Python foi criado por Guido Van Rossum.
print(letra_atual)#.