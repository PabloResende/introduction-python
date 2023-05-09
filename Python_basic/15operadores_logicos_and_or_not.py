'''operadores lógicos
and (e) or (ou) not (não)
and- Todas as condições precisam ser verdadeiras;
Se qualquer valor for considerado falso,
    a expressão inteira será avaliada naquele valor;
or - Qualquer condição verdadeira avalia toda a 
expressão como verdadeira;
Se qualquer valor for considerado verdadeiro a
    expressão  inteira será avaliada naquele valor;
not - Usado  para inverter expressões 
    not True = False
    not False = True
( São considerados falsy( que você já viu )
0 0.0 '' False )
(  Também existe um tipo chamado None que é 
considerado um não valor )
'''

#AND:

entrada = input('Entrar ou Sair ')      
print(entrada)
senha = input('digite a senha: ')

senha_permitida = '1234'

if entrada == 'e' and senha ==  senha_permitida:
    print('você entrou')
else:
    print('você saiu')

# #isso se chama 'avaliação de curto circuito
print(True and False and True)#False porque retorna só o valor falso
print(True and True and True)#todos são True
print(True and 0 and True)# vai voltar o valor 0

#OR:

entrada = input('Entrar ou Sair ')
print(entrada)
senha = input('digite a senha: ')

senha_permitida = '1234'

if (entrada == 'E' or entrada == 'e') and senha ==  senha_permitida:
    print('você entrou')
else:
    print('você saiu')

# #avaliação de curto circuito
print(True or False or True)#True
print(False or 0)#0
print('abc' or False or False)#abc
senha = input('digite a senha: ') or 'sem senha'
print(senha)

#NOT:

#not inverte
print(not 0)#True
print(not 1)#False
