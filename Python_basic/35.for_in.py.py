#outra opção de repetição
import time

# string = 'ハロー・ワールド'
# i = 0
# len(string)
# while i < len(string):
#     show_string = string[i]
#     i += 1
#     print(show_string)
#     time.sleep(.2)

#for é mais usado em casos onde não varia a string, diferente de while que\
#que pode ter vários resultados
string = 'ハロー・ワールド'

for letter in string:# para cada 'letra' do iterável 'string':
    print(letter)
    time.sleep(.2)