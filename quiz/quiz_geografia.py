import random
import string

from coisas_variadas.modelo_geopy import detalhes_lugar
# Perguntar se o usuario quer jogar com cidades, estados ou paises
# Com base na resposta
# sortear uma letra
# pedir para o usuario escrever um pais com essa letra
# verificar se a primeira letra é igual a letra pedida
# usar bibliotecas de geopy para verificar se o local é válido
# verificar se é mesmo um pais
# se acertar, é contabilizado um ponto
# se o usuario errar, ele perde um ponto
# o usuario perde se ele chegar a -10 pontos
# ele vence se ele chegar a +10 pontos
# a cada acerto, exibir uma mensagem de parabens
# a cada erro, exibir uma mensagem de voce errou e explicar o erro(se nao é um pais ou se é inexistente)
# uma letra é sorteada a cada resposta independentemente de resposta certa ou errada
# d k o q w x y
class QuizGeografia:
    def __init__(self):
        self.pontuacao=0
        self.modo_de_jogo:str
        self.modo= None

    def pergunta_modo(self):
        while True:
            modo_de_jogo=input("""Sejá bem vindo! Você gostaria de jogar com:
                               A) Cidades
                               B) Estados
                               C) Paises
                               D) Todos
                                                     """)
            match modo_de_jogo.upper():
                case "A":
                    return "city"
                case "B":
                    return "state"
                case "C":
                    return "country"
                case "D":
                    return"*"
                case _:
                    continue
            
    def retorna_modo(self):
        match self.modo_de_jogo:
            case "city":
                return "cidade"
            case "state":
                return "estado"
            case "country":
                return "país"   
            # case "*":
            #     return ["cidade", "estado", "pais"]   
            # case _:
            #     return random.choice("cidade", "estado", "país")            

    def retorna_opcao_aleatoria(self):
        lista_de_opcoes={"cidade":"city", "pais":"country"}
        opcao_escolhida=random.choice(list(lista_de_opcoes.items()))
        print (opcao_escolhida)
        return opcao_escolhida


    def sorteia_letra(self):
        letras_do_alfabeto=list(string.ascii_uppercase)
        print(letras_do_alfabeto)
        letras_a_remover=["K", "O", "Q", "W", "X", "Y"]
        letras_a_considerar=[letra for letra in letras_do_alfabeto if letra not in letras_a_remover]
        # letra_aleatoria="N"
        letra_aleatoria=random.choice(letras_a_considerar)
        print(letras_a_considerar)
        return letra_aleatoria
    
    def pergunta_pais(self,letra_aleatoria):
        self.modo=self.retorna_modo()
        opcao_aleatoria_escolhida=self.retorna_opcao_aleatoria()
        if self.modo==None:
            self.modo= opcao_aleatoria_escolhida[0]
        resposta=""
        while len(resposta) <3:
            resposta=input(f"\nDigite um(a) {self.modo} com a letra {letra_aleatoria}:    \n").upper()
        self.modo= opcao_aleatoria_escolhida[1]
        return resposta

    def verifica_letra(self, resposta, letra_aleatoria):
        if resposta=="":
            return False
        if resposta[0] ==letra_aleatoria:
            return True
        return False

    def valida_pais(self,resposta): 
        dic_detalhes=detalhes_lugar(lugar=resposta)
        if dic_detalhes== None:
            return False
        tipo_de_endereco=dic_detalhes.get("addresstype","Addresstype não encontrado").lower()
        if tipo_de_endereco=="municipality":
           tipo_de_endereco="city"
        if tipo_de_endereco=="administrative":
           tipo_de_endereco="country"   
        if tipo_de_endereco== self.modo:
            return True
        if tipo_de_endereco== self.modo_de_jogo:
            return True
        return False

    def valida_resposta(self, pais_respondido, letra_aleatoria_escolhida, ):

        verificacao_da_letra=self.verifica_letra(resposta=pais_respondido,letra_aleatoria=letra_aleatoria_escolhida)
        if verificacao_da_letra==False:
            return -1, f"\nO seu pais não começa com a letra {letra_aleatoria_escolhida} ou é inválido\n"
        verificacao_da_resposta=self.valida_pais(resposta=pais_respondido)
        if verificacao_da_resposta==False:
            return -1, f"\n{pais_respondido} não é um(a) {self.modo}"
        return 1, "\nParabens! Você acertou!\n" 

  


    def principal(self):
        self.modo_de_jogo=self.pergunta_modo()
        while True:
            # if self.modo_de_jogo== "*":
            letra_aleatoria_escolhida=self.sorteia_letra()
            pais_respondido=self.pergunta_pais(letra_aleatoria=letra_aleatoria_escolhida)
            pontos,mensagem=self.valida_resposta(pais_respondido, letra_aleatoria_escolhida)
            print(mensagem)    
            self.pontuacao+=pontos
            print(self.pontuacao)

            if self.pontuacao==10:
                print( "\nParabens! Você ganhou!\n")
                break
            if self.pontuacao==-10:
                print("Sinto muito, você perdeu!")    
                break

iniciador=QuizGeografia()
comecar=iniciador.principal() 
   
# tema: Corrigir a validação do lugar e ajustar a validação quando estver no modo todos(usando dicionários)
# municipality