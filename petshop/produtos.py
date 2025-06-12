import pandas as pd
from petshop.modelo import ModeloPetShop

class Produtos():
    
    def __init__(self):
        super().__init__()
        self.preço_do_produto=""
        self.estoque=""

    # def adiciona_produto(self):    
    #     tabela_de_produtos=pd.read_csv("petshop/fichas/produtos.csv", sep=";")
    #     lista_dados=[]
    #     for chave, valor in self.__dict__.items():
    #         print(chave)
    #         resposta=input("     ")
    #         self.__dict__[chave]=resposta
    #         lista_dados.append(resposta)
        
    #     tabela_de_produtos.loc[len(tabela_de_produtos)]=lista_dados
    #     tabela_de_produtos.to_csv(r"petshop\fichas\produtos.csv", sep=";", index=False)
    def pega_nome_planilha_csv(self):  
        return r"petshop\fichas\produtos.csv"

if __name__=="__main__":

    iniciador=Produtos()
    iniciador.adiciona_produto()        
