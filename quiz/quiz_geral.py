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
        self.tabela_perguntas_e_respostas=pd.read_csv(r"quiz.csv", sep=";")

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
        lista_de_modos=list(self.tabela_perguntas_e_respostas["tema"].unique())
        while True:
            print("Seja bem vindo ao quiz geral! Com qual tema você gostaria de jogar?")
            for numero, materia  in enumerate(lista_de_alternativas):
                print(f"{numero+1}){materia}")
            tema_do_jogo=input("      ").upper()

            # print("Seja bem vindo ao quiz geral! Com qual tema você gostaria de jogar?")
            # print("A)História")
            # print("B)Geografia")
            # print("C)Ciências")
            # print("D)Português")
            # print("E)Pegadinhas")
            # if tema_do_jogo not in lista_de_alternativas:
            #     continue
            # match tema_do_jogo:
            #     case "A":
            #         return "história"
            #     case "B":
            #         return "geografia"
            #     case "C":
            #         return "ciências"
            #     case "D":
            #         return "português"
            #     case "E":
            #         return "pegadinhas"
                    

    def carrega_perguntas_e_respostas(self, tema):
            
        temas=list(self.tabela_perguntas_e_respostas["tema"].unique())
        print(temas)
        self.perguntas_e_respostas=self.tabela_perguntas_e_respostas[self.tabela_perguntas_e_respostas["tema"]== tema]
        self.perguntas_e_respostas = self.perguntas_e_respostas.reset_index()
        print(self.perguntas_e_respostas)

    def sorteia_pergunta_outra_forma(self):
        lista_indices = list(self.perguntas_e_respostas.index)
        indice_pergunta = random.choice(lista_indices)
        print(self.perguntas_e_respostas.iloc[indice_pergunta])

    def sorteia_pergunta(self): #quebrar em 3 funções
        qtd=len(self.perguntas_e_respostas)    
        indice_pergunta = random.randint(0, qtd) #randint = sorteia número inteiro
        pergunta=(self.perguntas_e_respostas['pergunta'].iloc[indice_pergunta])
        resposta_certa=self.perguntas_e_respostas['resposta_certa'].iloc[indice_pergunta]
        lista_de_alternativas=[
            resposta_certa,
            self.perguntas_e_respostas['resposta_errada1'].iloc[indice_pergunta],
            self.perguntas_e_respostas['resposta_errada2'].iloc[indice_pergunta]]

        random.shuffle(lista_de_alternativas)    

        print(pergunta)
        # print(f"A){self.perguntas_e_respostas['resposta_certa'].iloc[indice_pergunta]}")
        # print(f"B){self.perguntas_e_respostas['resposta_errada1'].iloc[indice_pergunta]}")
        # print(f"C){self.perguntas_e_respostas['resposta_errada2'].iloc[indice_pergunta]}")
        for i, alternativa in enumerate(lista_de_alternativas):
            print(f"{i+1}){alternativa}")
        resposta_para_teste=int(input("           "))-1
        if lista_de_alternativas[resposta_para_teste]== resposta_certa:
            print("Você acertou!")
            self.pontuacao+=1
            print(self.pontuacao)
            return 
        print(f"Você errou! A resposta era {resposta_certa}")
        self.pontuacao-=1
        
     
       
       


    def principal(self):
        tema=self.pergunta_jogo_com_dicionario()
        self.carrega_perguntas_e_respostas(tema)
        pergunta_sorteada=self.sorteia_pergunta()


iniciador=QuizGeral()
comecar=iniciador.principal() 