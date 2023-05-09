"""
split e join com list e str
split - divide uma string (list)
strip - remove os espaços
join - une uma string
"""

frase = '   Olha só que   , coisa interessante          '#espaços propositais
lista_frases_cruas = frase.split(',')#essa é a frase original apenas cortada\
#depois da vírgula( é comum por um espaço também depois da vírgula)

lista_frases = []#já esta recebe os novos valores
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())#aqui a uma lista adicionou\
#a outra e depois foram removidos os espaços com 'strip'
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)#têm que criar uma lista vazia e passar\
#o que que deseja mudar depois do join