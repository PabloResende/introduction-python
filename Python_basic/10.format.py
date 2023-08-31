#.format é uma outra forma de formatação
#os argumentos são colocados dentro das chaves de acordo com a ordem

a = 'AAAA'
b = 'bbbb'
c = '1.1'

string =  'a={} b={} c={}'
format = string.format(a, b, c)

print(string) #a{} b{} c{} (assim não dá certo)
print(format)  #a=AAAA b=bbbb c=1.1)

#outra forma melhor de faze-lo é usando um índice, 0, 1, 2 e por diante, exemplo:

d='ddd'
e='eee'
f='fff'

string1 =  'a={0} b={1} c={2}'
string2 =  'a={2} b={1} c={0} d={1}'

format1 = string1.format(d, e, f)
format2 = string2.format(d, e, f)
print(format1)#a=ddd b=eee c=fff
#há a possibilidade de por os números fora de ordem e ainda repeti-los;
print(format2)#a=fff b=eee c=ddd d=eee

#existem ainda os parâmetros nomeados, aqui os argumentos ganham nomes:

string3 =  'a={nome1} b={juan} c={kevin}'
format3 = string3.format(nome1 = d, juan = e, kevin = f)
print(format3) #a=ddd b=eee c=fff

#uma string mais .format( que é uma função) é chamado de método( method )