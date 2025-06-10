import pandas as pd

class Funcionario():
    
    def __init__(self):
        self.nome=""
        self.idade=""
        self.genero=""
        self.salario=""
        self.cidade_de_residencia=""

    def cadastro(self):
        tabela_de_informacoes=pd.read_csv(r"petshop\fichas\funcionario.csv", sep=";")
        print(tabela_de_informacoes)
        lista_dados=[]
        for chave, valor in self.__dict__.items():
            print(chave)
            resposta=input("     ")
            self.__dict__[chave]=resposta
            lista_dados.append(resposta)
        
        tabela_de_informacoes.loc[len(tabela_de_informacoes)]=lista_dados
        tabela_de_informacoes.to_csv(r"petshop\fichas\funcionario.csv", sep=";", index=False)

        print(self.__dict__)






iniciador=Funcionario()
iniciador.cadastro()        
