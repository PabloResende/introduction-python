#iterando strings com while
#------0123456789101112
nome = 'pablo silva' #iteráveis
#------1110987654321

i  = 0
novo_nome = ''#string vazia
while i < len(nome):#indice é menor que len...
    letra = nome[i]#letra é igual nome 'pablo silva' e indice é '0'
    novo_nome += letra#enquanto o número de letras de 'nome' for maior que\
    #indice = 0, as variáveis 'letra' e 'novo_nome' serão verdadeiras\
    #juntas elas funcionam da seguinte forma:
    #novo nome adiciona uma letra começando do indice que no caso é\
    #0, e vai seguindo enquanto len(nome) for maior que  indice, pra isso vai\
    #vai pegando mais letras de 'nome'
    
    #ou:
    #novo_nome += f'*{letra}' resultado do print: *p*a*b*l*o* *s*i*l*v*a

    i += 1

print(novo_nome)#pablo silva