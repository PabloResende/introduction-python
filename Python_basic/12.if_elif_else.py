#if(se), elif(se não se), else(se não)
#todos os 3 são boleanos

entrada = input('você quer entrar ou sair ')
if entrada == 'entrar':#o if é o pode ir só, mas o else não
    print('você entrou')
elif entrada == 'sair':
    print('você saiu')
else:
    print('erro')

