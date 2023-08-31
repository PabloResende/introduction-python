'''
CONSTANTE= variáveis que não vão mudar
( use se letras maiúsculas para identificar)
muitas condições no mesmo if = mais confuso ( ruim )
quanto mais afastamento da margem = mais complexidade ( ruim )
quanto mais simples o código melhor
'''
import time

velocidade= 61 #velocidade do carro
local_do_carro = 99 #local onde o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #a distância que radar pega

#se o local do carro for >=  100 - 1 (99) ele está no range do radar
#e se for <= 100 + 1 (101) ele também está no radar
if local_do_carro >= (LOCAL_1 - RADAR_RANGE ) and \
    local_do_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('detectando velocidade...')
    time.sleep(.4)
    print('veículo multado')
else:
    print('no limite')

#forma mais legível de fazer esse código:

import time

velocidade = 61
local_1 = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_passou_radar_1 = velocidade > RADAR_1
carro_passo_radar_1 = local_1 >= (LOCAL_1 - RADAR_RANGE ) and\
    local_1 <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passo_radar_1 and velocidade_passou_radar_1

if carro_passo_radar_1:
    print('detectando...')
    time.sleep(.4)

if carro_multado:
    print('carro multado')

else:print('no limite')