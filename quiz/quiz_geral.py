import pandas as pd
import random
import warnings
warnings.filterwarnings("ignore")
# o usuario escolhera um tema
# o usuario irá dizer a dificudade que quer jogar(quantidade de perguntas)
# as perguntas vão ser filtradas com base nesse tema
# as perguntas estarão armazenadas em uma planilia csv
# serão apresentadas as perguntas de forma aleatória
# serão mostradas tres alternativas
# o usuario irá responder qual a opção correta
# a resposta será validada
# a cada acerto irá se ganhar um ponto
# a cada erro se perde um ponto 

class QuizGeral():
    def __init__(self):
        self.perguntas_e_respostas:pd.DataFrame
        self.jogador:str
        self.pontuacao:int
        self.placar:pd.DataFrame

    def pergunta_jogo_com_dicionario(self):
        temas = {
            'A': 'História',
            'B': 'Geografia',
            'C': 'Ciências',
            'D':'Português',
            'E': 'Pegadinhas'
        }

        while True:
            print("Seja bem vindo ao quiz geral! Com qual tema você gostaria de jogar?")
            for chave, valor in temas.items():
                print(f'{chave}) {valor}')
            tema_do_jogo=input("      ").upper()
            if tema_do_jogo.upper() not in temas.keys():
                continue
            return temas[tema_do_jogo].lower()

    def pergunta_jogo(self): 
        lista_de_alternativas=["A","B","C","D","D","E"]
        while True:
            print("Seja bem vindo ao quiz geral! Com qual tema você gostaria de jogar?")
            print("A)História")
            print("B)Geografia")
            print("C)Ciências")
            print("D)Português")
            print("E)Pegadinhas")
            tema_do_jogo=input("      ").upper()
            if tema_do_jogo not in lista_de_alternativas:
                continue
            match tema_do_jogo:
                case "A":
                    return "história"
                case "B":
                    return "geografia"
                case "C":
                    return "ciências"
                case "D":
                    return "português"
                case "E":
                    return "pegadinhas"
                    

    def carrega_perguntas_e_respostas(self, tema):
        tabela_perguntas_e_respostas=pd.read_csv(r"quiz.csv", sep=";")    
        self.perguntas_e_respostas=tabela_perguntas_e_respostas[tabela_perguntas_e_respostas["tema"]== tema]
        self.perguntas_e_respostas = self.perguntas_e_respostas.reset_index()
        print(self.perguntas_e_respostas)

    def sorteia_pergunta_outra_forma(self):
        lista_indices = list(self.perguntas_e_respostas.index)
        indice_pergunta = random.choice(lista_indices)
        print(self.perguntas_e_respostas.iloc[indice_pergunta])

    def sorteia_pergunta(self): #quebrar em 3 funções
        qtd=len(self.perguntas_e_respostas)    
        indice_pergunta = random.randint(0, qtd) #randint = sorteia número inteiro
        # numero_de_questoes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        pergunta=(self.perguntas_e_respostas['pergunta'].iloc[indice_pergunta])
        
        print(pergunta)
        print(f"A){self.perguntas_e_respostas['resposta_certa'].iloc[indice_pergunta]}")
        print(f"B){self.perguntas_e_respostas['resposta_errada1'].iloc[indice_pergunta]}")
        print(f"C){self.perguntas_e_respostas['resposta_errada2'].iloc[indice_pergunta]}")
        resposta_para_teste=input("           ").lower()
        if resposta_para_teste== "a":
            print("Você acertou!")
            return
        print("Você errou!")    


    def principal(self):
        tema=self.pergunta_jogo_com_dicionario()
        self.carrega_perguntas_e_respostas(tema)
        pergunta_sorteada=self.sorteia_pergunta()


iniciador=QuizGeral()
comecar=iniciador.principal() 