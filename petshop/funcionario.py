import pandas as pd

from petshop.modelo import ModeloPetShop

class Funcionario(ModeloPetShop):
    
    def __init__(self):
        super().__init__()
        self.idade=""
        self.genero=""
        self.salario=""
        self.cidade_de_residencia=""

    # def cadastro(self):
    #     tabela_de_informacoes=pd.read_csv(r"petshop\fichas\funcionario.csv", sep=";")
    #     print(tabela_de_informacoes)
    #     lista_dados=[]
    #     for chave, valor in self.__dict__.items():
    #         print(chave)
    #         resposta=input("     ")
    #         self.__dict__[chave]=resposta
    #         lista_dados.append(resposta)
        
    #     tabela_de_informacoes.loc[len(tabela_de_informacoes)]=lista_dados
    #     tabela_de_informacoes.to_csv(r"petshop\fichas\funcionario.csv", sep=";", index=False)

    #     print(self.__dict__)

    def pega_nome_planilha_csv(self):
        return r"petshop\fichas\funcionario.csv"





if __name__=="__main__":

    iniciador=Funcionario()
    iniciador.cadastro()        
