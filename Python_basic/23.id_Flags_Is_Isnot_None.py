'''
Flag (bandeira) para quando ser quer demarcar um local
None = não valor 
is e is not = é ou não é um (valor, tipo, identidade)
ID = identidade
'''


v1 = 'a'
v2 = 'a'
v3 = 'b'
print(id(v1))#140728131884096
print(id(v2))#140728131884096 resultado igual
print(id(v3))#140728131578424

condição = False #vai resultar em:
# não faça algo
#None True
#None False
#se for condição = True o resultado será o contrário
passou_no_if = None

if condição:
    passou_no_if = True
    print('faça algo')
else:
    print('não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
