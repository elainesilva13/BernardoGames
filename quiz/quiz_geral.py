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
        self.pontuacao=0
        self.placar:pd.DataFrame
        self.tabela_perguntas_e_respostas=pd.read_csv(r"quiz.csv", sep=";")
        self.lista_indices_perguntas=[]
        self.lista_de_alternativas=[]
        self.resposta_certa=None

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
        lista_de_modos=list(self.tabela_perguntas_e_respostas["tema"].unique())
        while True:
            print("Seja bem vindo ao quiz geral! Com qual tema você gostaria de jogar?")
            for numero, materia  in enumerate(lista_de_modos):
                print(f"{numero+1}){materia.title()}")
            tema_do_jogo=input("      ").upper()
            try:
                tema_do_jogo_int = int(tema_do_jogo) - 1
            except:
                print('Você não digitou uma opção válida')
                continue
            if tema_do_jogo_int >= len(lista_de_modos) or tema_do_jogo_int < 0:
                print('A opção que você digitou não existe')
                continue
            tema_materia = lista_de_modos[tema_do_jogo_int]
            return tema_materia

    def pergunta_jogo_outra_forma(self): 
        lista_de_modos=list(self.tabela_perguntas_e_respostas["tema"].unique())
        while True:
            print("Seja bem vindo ao quiz geral! Com qual tema você gostaria de jogar?")
            for numero, materia  in enumerate(lista_de_modos):
                print(f"{numero+1}){materia.title()}")
            tema_do_jogo=input("      ").upper()
            if not tema_do_jogo.isnumeric():
                print('Você não digitou uma opção válida')
                continue
            tema_do_jogo_int = int(tema_do_jogo) - 1
            if (
                tema_do_jogo_int < 0 or
                tema_do_jogo >= len(lista_de_modos)
            ):
                print('Você não digitou uma opção válida')
                continue
            
            return lista_de_modos[tema_do_jogo_int]


    def pergunta_jogo_opcao_mais_simples(self): 
        lista_de_modos=list(self.tabela_perguntas_e_respostas["tema"].unique())
        while True:
            print("Seja bem vindo ao quiz geral! Com qual tema você gostaria de jogar?")
            for numero, materia  in enumerate(lista_de_modos):
                print(f"{numero+1}){materia.title()}")
            tema_do_jogo=input("      ").upper()
            try:
                tema_do_jogo_int = abs(int(tema_do_jogo) - 1)
                return lista_de_modos[tema_do_jogo_int]
            except:
                print('Você não digitou uma opção válida')

    def pergunta_dificuldade(self):
        lista_de_dificuldades=list(self.tabela_perguntas_e_respostas["nivel"].unique())
        while True:
            print("Agora, diga qual dificuldade você quer:")
            for numero, dificuldade  in enumerate(lista_de_dificuldades):
                print(f"{numero+1}){dificuldade.title()}")
            dificuldade_escolhida=input("      ")
            try:
                dificuldade_escolhida=int(lista_de_dificuldades)-1
                return dificuldade_escolhida
            except:
                print("Você digitou uma dificuldade inválida")
                continue    



    def pergunta_jogo_antigo(self):
        while True:    
            tema_do_jogo=input("      ").upper()
            print("Seja bem vindo ao quiz geral! Com qual tema você gostaria de jogar?")
            print("A)História")
            print("B)Geografia")
            print("C)Ciências")
            print("D)Português")
            print("E)Pegadinhas")
            lista_de_alternativas=["A","B","C","D","D","E"]
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

    def carrega_perguntas_e_respostas(self, tema, dificuldade):
            
        temas=list(self.tabela_perguntas_e_respostas["tema"].unique())
        
        print(temas)
        self.perguntas_e_respostas=self.tabela_perguntas_e_respostas[self.tabela_perguntas_e_respostas["tema"]== tema]
        self.perguntas_e_respostas = self.perguntas_e_respostas.reset_index()
        print(self.perguntas_e_respostas)
        self.lista_indices_perguntas=list(self.perguntas_e_respostas.index)
        print(self.lista_indices_perguntas)
        

    def sorteia_pergunta_outra_forma(self):
        lista_indices = list(self.perguntas_e_respostas.index)
        indice_pergunta = random.choice(lista_indices)
        print(self.perguntas_e_respostas.iloc[indice_pergunta])

    def sorteia_pergunta(self): #quebrar em 3 funções
        indice_pergunta=random.choice(self.lista_indices_perguntas)
        pergunta=(self.perguntas_e_respostas['pergunta'].iloc[indice_pergunta])
        self.resposta_certa=self.perguntas_e_respostas['resposta_certa'].iloc[indice_pergunta]
        self.lista_de_alternativas=[
            self.resposta_certa,
            self.perguntas_e_respostas['resposta_errada1'].iloc[indice_pergunta],
            self.perguntas_e_respostas['resposta_errada2'].iloc[indice_pergunta]]

        random.shuffle(self.lista_de_alternativas)    
        print(pergunta)
        self.lista_indices_perguntas.remove(indice_pergunta)
        return pergunta
       
    def pergunta_resposta(self,pergunta_escolhida):
        for i, alternativa in enumerate(self.lista_de_alternativas):
            print(f"{i+1}){alternativa}")
        resposta=int(input("           "))-1
        self.valida_resposta(resposta)


    def valida_resposta(self,resposta):
        if self.lista_de_alternativas[resposta]== self.resposta_certa:
            print("Você acertou!")
            self.pontuacao+=1
            print(f"Sua pontuação é:{self.pontuacao}")
            return 
        print(f"Você errou! A resposta era {self.resposta_certa}")
        self.pontuacao-=1
        print(f"Sua pontuação é:{self.pontuacao}")
     
       
       


    def principal(self):
        tema=self.pergunta_jogo_opcao_mais_simples()
        dificuldade=self.pergunta_dificuldade
        self.carrega_perguntas_e_respostas(tema,dificuldade)
        while len(self.lista_indices_perguntas):
            pergunta_escolhida=self.sorteia_pergunta()
            self.pergunta_resposta(pergunta_escolhida)
        


iniciador=QuizGeral()
comecar=iniciador.principal() 
#         print(self.lista_indices_perguntas)
#        
#        