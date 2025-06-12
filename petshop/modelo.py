from abc import ABC, abstractmethod
import pandas as pd

class ModeloPetShop():
    def __init__(self):
        self.nome=""


    def cadastrar(self):
        nome_do_arquivo=self.pega_nome_planilha_csv()
        tabela_de_produtos=pd.read_csv(nome_do_arquivo, sep=";")
        lista_dados=[]
        for chave, valor in self.__dict__.items():
            print(chave)
            resposta=input("     ")
            self.__dict__[chave]=resposta
            lista_dados.append(resposta)
        tabela_de_produtos.loc[len(tabela_de_produtos)]=lista_dados
        tabela_de_produtos.to_csv(nome_do_arquivo, sep=";", index=False)


    @abstractmethod
    def pega_nome_planilha_csv(self)->str:
        pass    
