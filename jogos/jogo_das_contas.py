# dois numeros seram sorteados
# sortear uma operação matematica
# sera perguntado para o usuario um resultado de operção matematica etnre os dois numeros
# dar dez segundos pra o usuario
# verificar a resposta
import random
import time
# x_decimal = random.uniform(0, 150)
# x = int(x_decimal)
# y_decimal = random.uniform(0, 150)
# y = int(y_decimal)
# lista_de_operacoes= ["+","-",".",":"]
# posicao_aleatoria=int(random.uniform(0,4))

# # tempo=10
# # while tempo== +0:
# #     tempo=-1
# #     if tempo ==0:
# #         break
# # operacao=lista_de_operacoes[posicao_aleatoria]

# if operacao== "+":
#     resultado=x+y
# if operacao== "-":
#     resultado=x-y
# if operacao== ".":
#     resultado=x*y
# if operacao== ":":
#     resultado=x//y
# palpite_string=input (f"Quanto o é {x} {operacao} {y}? ")
# palpite=int (palpite_string)
# if palpite== resultado:
#     print("parabens,você acertou!")
# else:
#     print(f"o resultado era {resultado}")


def sorteia_numero() -> dict:
    numeros = {}
    x_decimal = random.uniform(0, 150)
    x = int(x_decimal)
    numeros["x"] = x
    y_decimal = random.uniform(0, 150)
    y = int(y_decimal)
    numeros["y"] = y
    return numeros


def sorteia_operacao() -> str:
    lista_de_operacoes = ["+", "-", ".", ":"]
    posicao_aleatoria = int(random.uniform(0, 4))
    return lista_de_operacoes[posicao_aleatoria]


def resultado(x, y, operacao) -> str:
    if operacao == "+":
        return x+y
    if operacao == "-":
        return x-y
    if operacao == ".":
        return x*y
    if operacao == ":":
        return x//y


def verificacao(x, y, operacao, operacao_escolhida) -> bool:
    result = resultado(x, y, operacao)
    print(f"Quanto o é {x} {operacao} {y}? ")
    contador1(operacao_escolhida)
    palpite = valida_numero()
    if palpite == result:
        print("parabens,você acertou!")
        return True
    else:
        print(f"o resultado era {result}")
        return False


def valida_numero() -> int:
    while True:
        palpite_string = input("Sua resposta:   ")
        try:
            palpite = int(palpite_string)
            return palpite
        except:
            print("Digite uma resposta valida")


def contador1(operacao_escolhida):
    if operacao_escolhida == "+":
        tempo = 10
        return tempo
    if operacao_escolhida == "-":
        tempo = 15
        return tempo
    if operacao_escolhida == ".":
        tempo = 30
        return tempo
    if operacao_escolhida == ":":
        tempo = 30
        return tempo


def contador2(tempo):
    while tempo:
        print(tempo)
        time.sleep(1)
        tempo -= 1


def principal():

    numeros = sorteia_numero()
    x = numeros["x"]
    y = numeros["y"]
    operacao_escolhida = sorteia_operacao()
    verificacao(x, y, operacao_escolhida,)


def deseja_continuar():
    while True:

        continuar = input("voce deseja continuar? S ou N?  ").upper()
        if continuar[0] == "N":

            return False
        if continuar[0] == "S":
            return True


while True:

    principal()
    continuar = deseja_continuar()
    if continuar == False:
        break