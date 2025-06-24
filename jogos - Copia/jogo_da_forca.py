import random
# capital=["Porto Alegre","Rio de Janeiro"]
# capital.append("Salvador") #append adiciona algo a lista
# fruta=["melancia","banana","morango","maçã"]
# jogo=["minecraft","pokemon","hollow knight"]
# while True:
#     if ("jogo") in Modo_de_jogo:
#          lista_de_letras2=[]
#          lista_de_letras2
#     if ("capital") in Modo_de_jogo:
#         lista_de_letras3=[]
#         lista_de_letras3
#         posicao_aleatoria=int(random.uniform(0,3))

#         palavra2=jogo[posicao_aleatoria].upper()

#         lista_de_letras2=[]
#         lista_de_letras3=[]


#     tentativas=5
#     while tentativas:
#         exibicao=""
#         for letra in palavra2:
#             if letra in lista_de_letras2 or letra== " ":
#                 exibicao+= " "+letra+ " "
#             else:
#                 exibicao+="_ " #exibicao = exibicao + '_ '
#         if "_ " not in exibicao:
#             print(exibicao)
#             print("parabens!")
#             break
#         print(exibicao)
#         palpite2=input ("Digite uma letra: ").upper()
#         lista_de_letras2+=palpite2
#         if palpite2 in palavra2:
#             print("você acertou uma letra!")
#         else:
#             print("você errou!")
#             tentativas-=1

#     if not tentativas:
#         print ("voce perdeu!")
#     deseja_continuar=input("Você gotaria de continuar? ").upper()
#     if deseja_continuar== ("NAO"):
#         break


#     if ("capital") in Modo_de_jogo:
#             posicao_aleatoria2=int(random.uniform(0,3))

#             palavra3=jogo[posicao_aleatoria2].upper()

#             lista_de_letras3=[]
#             tentativas=5
#     while tentativas:
#             exibicao=""
#             for letra in palavra3:
#                 if letra in lista_de_letras3 or letra== " ":
#                     exibicao+= " "+letra+ " "
#                 else:
#                     exibicao+="_ " #exibicao = exibicao + '_ '
#             if "_ " not in exibicao:
#                 print(exibicao)
#                 print("parabens!")
#                 break
#             print(exibicao)
#             palpite3=input ("Digite uma letra: ").upper()
#             lista_de_letras3+=palpite3
#             if palpite3 in palavra3:
#                 print("você acertou uma letra!")
#             else:
#                 print("você errou!")
#                 tentativas-=1

#     if not tentativas:
#             print ("voce perdeu!")
#     deseja_continuar=input("Você gotaria de continuar? ").upper()
#     if deseja_continuar== ("NAO"):
#             break

def escolhe_tema() -> str:
    capital = ["Porto Alegre", "Rio de Janeiro"]
    capital.append("Salvador")  # append adiciona algo a lista
    fruta = ["melancia", "banana", "morango", "maçã"]
    jogo = ["minecraft", "pokemon", "hollow knight"]
    while True:
        Modo_de_jogo = input(
            "Bem vindo ao jogo da forca. Qual tema você gotaria de jogar? Jogo, Capital ou fruta? ").lower()
        if Modo_de_jogo == "jogo":
            return jogo
        if Modo_de_jogo == "capital":
            return capital
        if Modo_de_jogo == "fruta":
            return fruta


def sorteia_palavra(lista: list) -> str:
    posicao_aleatoria = int(random.uniform(0, len(lista)))
    return lista[posicao_aleatoria].upper()


def tracos_e_letras(lista_de_letras: list, palavra: str) -> str:
    exibicao = ""
    for letra in palavra:
        if letra in lista_de_letras or letra == " ":
            exibicao += " "+letra + " "
        else:
            exibicao += "_ "  # exibicao = exibicao + '_ '
    return exibicao


def pede_palpite() -> str:
    palpite = input("Digite uma letra: ").upper()
    return palpite[0]


def valida_palpite(palpite: str, palavra: str) -> bool:
    if palpite in palavra:
        return True
    return False


def verifica_se_ganhou(exibicao) -> bool:
    if "_ " not in exibicao:
        return True
    else:
        return False


def principal():
    tema = escolhe_tema()
    palavra = sorteia_palavra(tema)
    lista_de_letras = []
    tentativas = 5
    while tentativas:
        exibicao = tracos_e_letras(lista_de_letras, palavra)
        print(exibicao)
        ganhou = verifica_se_ganhou(exibicao)
        if ganhou:
            print("parabens, voce ganhou!")
            break

        palpite = pede_palpite()
        acertou = valida_palpite(palpite, palavra)
        if acertou:
            print("Voce acertou uma letra!")
            lista_de_letras.append(palpite)
        else:
            print("Voce errou!")
            tentativas -= 1
    if not tentativas:
        print(f"voce perdeu! A resposta era {palavra}")


while True:
    principal()
    continuar = input("voce deseja continuar?").lower()
    if continuar == "nao":
        break
