import pandas as pd

class Produtos():
    
    def __init__(self):
        self.nome_do_produto=""
        self.preço_do_produto=""
        self.estoque=""

    def adiciona_produto(self):    
        tabela_de_produtos=pd.read_csv("petshop/fichas/produtos.csv", sep=";")
        lista_dados=[]
        for chave, valor in self.__dict__.items():
            print(chave)
            resposta=input("     ")
            self.__dict__[chave]=resposta
            lista_dados.append(resposta)
        
        tabela_de_produtos.loc[len(tabela_de_produtos)]=lista_dados
        tabela_de_produtos.to_csv(r"petshop\fichas\produtos.csv", sep=";", index=False)

iniciador=Produtos()
iniciador.adiciona_produto()        
