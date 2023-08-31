#Built in
#tipos imutáveis: int, bool, float, str

string = 'luiz otavio'
outra_variavel = f'{string[:3]}abc {string[:4]}'#luiabc luiz
#explicação: nesse caso foi usado a f string junto com os chaves para fazer
#o fatiamento da letra 'Z'e substituí-la por 'abc'
print(outra_variavel)
print(string.capitalize())#é um método de string usado para
#deixar a primeira letra maiúscula
print(string.zfill(15))#0000luiz otávio
#retorna com zeros á esquerda até preencher os 15 caracteres
#dentro das aspas; pode ser outros números além de 15
#( os 15 conta com a string 'luiz otávio' )
