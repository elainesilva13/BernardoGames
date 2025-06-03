# carregar o arquivo perguntas.csv em um dataframe
#iterar por cada pergunta apresentando-a ao usuário e abrindo um input para capturar a resposta
#a cada iteração, atualizar o csv com a resposta
#salvar o dataframe como um novo csv resposta.csv
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

class ExemploCsv():
    def __init__(self):
        self.perguntas=pd.read_csv(r"perguntas.csv", sep=";")
        self.perguntas["respostas"]=""
        self.perguntas["respondido por"]=""

    def mostrar_pergunta(self):
        nome=input("Qual o seu nome?    ")
        for indice, linha in self.perguntas.iterrows():
            print(f"{linha["Pergunta"]}")
            resposta=input("       ")
            self.perguntas['respostas'].iloc[indice]=resposta
            self.perguntas['respondido por'].iloc[indice]=nome

            print(self.perguntas)
        self.perguntas.to_csv("perguntas_respondidas.csv", sep=";", index=False)
       

if __name__=="__main__":
    iniciador=ExemploCsv()
    iniciador.mostrar_pergunta()