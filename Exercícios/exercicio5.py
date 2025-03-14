# Complete e corrija o código de modo que ao final seja impressa a tabuada do número fornecido pelo usuário. 
# A saída deve ser semelhante a essa:
#
# Tabuada do 2:
# 2 x 1 = 2
#....
# 2 x 10 = 20

print('Tabuada\n') # \n = pula linha
fator = input('Digite um número: ')
tabuada = {}
for x in ("COMPLETE AQUI"):
    tabuada['COMPLETE AQUI'] = x * fator

print(f'Tabuada do {fator}')
for fator2, resultado in tabuada.items():
    print(f'{fator} x {fator2} = {resultado}')