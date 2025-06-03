import pandas as pd
import warnings
warnings.filterwarnings("ignore")
class PetShop():
    def __init__(self):
        self.perguntas_do_animal=pd.read_csv(r"perguntas_ficha_animal.csv",sep=";")
        self.perguntas_do_animal["resposta"]=""
        self.pergunta_do_nome=True



    def pergunta_acao(self):
        while True:
            o_que_fazer={"A":"Criar ficha de pet", "B":"Criar ficha de funcionario"}
            print("Bem vindo ao nosso petshop! O que você quer fazer?")
            for letra, acao in o_que_fazer.items():
                print(f"{letra}) {acao}")
            resposta=input("       ").upper()
            if resposta in o_que_fazer.keys():
                return o_que_fazer[resposta]
            print("Você não digitou uma resposta valida")    
    

    def ficha_do_animal(self):
        for indice, pergunta in self.perguntas_do_animal.iterrows():
            print(f"{pergunta}")
            resposta_do_usuario=input("      ")
            self.perguntas_do_animal["resposta"].iloc[indice]=resposta_do_usuario
            print(self.perguntas_do_animal)
            if self.pergunta_do_nome== True:
                nome_do_bichinho=resposta_do_usuario
            self.pergunta_do_nome=False    
        self.perguntas_do_animal.to_csv(f"{nome_do_bichinho}.csv", sep=";", index=False)


    def principal(self):
        while True:
            acao_a_ser_realizada=self.pergunta_acao()
            if acao_a_ser_realizada== "Criar ficha de pet":
                self.ficha_do_animal()



iniciador=PetShop()
comecar=iniciador.principal() 