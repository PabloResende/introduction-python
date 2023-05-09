'''Input serve para coletar os dados dos usuários, porém apenas em string
    por isso saber fazer a coerção é importante, caso seja necessário ter 
    esses dados em outro formato como int, float, etc...'''

nome = input('qual é o seu nome ')
print(F'o seu nome é {nome}')

n1 = input('digite um numero ')
n2 = input ('digite outro numero ')
#forma ruim de fazer
r= int(n1) * int(n2)
#outra forma:
int_n1 = int(n1)
int_n2 = int(n2)
#ruim:
print(f'a soma desses numeros é {r}')#a soma desses numeros é 6
#melhor:
print(int_n1 + int_n2)#5
print(int_n1 * int_n2)#6
#para concatena tem uma outra forma:

nome = input("qual seu nome? ")
sobrenome = input("qual seu sobrenome")
print(f'seu nome é {nome + sobrenome}')#seu nme é pablo silva