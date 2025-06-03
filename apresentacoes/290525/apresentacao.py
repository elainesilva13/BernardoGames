import warnings
import pandas as pd
warnings.filterwarnings("ignore")
class Apresentacao():
    def __init__(self):
        self.perguntas=pd.read_csv(r"perguntas_da_apresentação.csv",sep=";")
        self.perguntas["resposta"]=""
        self.primeira_pergunta=True

    def principal(self):
        for indice, pergunta in self.perguntas.iterrows():
            print(f"{pergunta}")
            resposta_do_usuario=input("      ")
            self.perguntas["resposta"].iloc[indice]=resposta_do_usuario
            print(self.perguntas)
            if self.primeira_pergunta== True:
                nome_do_bichinho=resposta_do_usuario
            self.primeira_pergunta=False    
        self.perguntas.to_csv(f"{nome_do_bichinho}.csv", sep=";", index=False)
               

iniciador=Apresentacao()
iniciador.principal()