import random
import string
# sortear uma letra
# pedir para o usuario escrever um pais com essa letra
# usar bibliotecas de geopy para verificar se o local é válido
# verificar se é mesmo um pais
# se acertar, é contabilizado um ponto
# se o usuario errar, ele perde um ponto
# o usuario perde se ele chegar a -10 pontos
# ele vence se ele chegar a +10 pontos
# a cada acerto, exibir uma mensagem de parabens
# a cada erro, exibir uma mensagem de voce errou e explicar o erro(se nao é um pais ou se é inexistente)
# uma letra é sorteada a cadaresposta independentemente de resposta certa ou errada

class QuizGeografia:
    def __init__(self):
        pass

    def sorteia_letra(self):
        letras_do_alfabeto=string.ascii_uppercase
        letra_aleatoria=random.choice(letras_do_alfabeto)
        return letra_aleatoria