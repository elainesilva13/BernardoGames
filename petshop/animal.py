import pandas as pd
class Animal():
    def __init__(self):
        self.nome=""
        self.telefone=""
        self.idade=""
        self.especie=""
        self.raca=""
        self.genero=""
        self.cor=""
        self.observacoes=""
        self.dono=""

    def cadastrar_novo(self):
        tabela_de_informacoes=pd.read_csv(r"petshop\fichas\animal.csv", sep=";")
        print(tabela_de_informacoes)
        lista_dados=[]
        for k, v in self.__dict__.items():
            print(k)
            resposta=input("     ")
            self.__dict__[k]=resposta
            lista_dados.append(resposta)
        
        tabela_de_informacoes.loc[len(tabela_de_informacoes)]=lista_dados
        tabela_de_informacoes.to_csv(r"petshop\fichas\animal.csv", sep=";", index=False)

        print(self.__dict__)
        print(self.__dict__.get("nome", "nao tem nome "))
        print(self.__dict__.get("cor", "nao tem cor"))
        print(self.__dict__.get("peso", "nao tem peso"))
        print(self.__dict__.get("comprimento", "nao tem comprimento"))
        # print(self.__dict__["morango"])
        print(tabela_de_informacoes.columns)

    def cadastrar_novo_atualizado(self):
            print(self.__dict__)
            tabela_de_informacoes=pd.read_csv(r"petshop/fichas/animal.csv", sep=";")
            print(tabela_de_informacoes)
            lista_dados=[]
            dados=tabela_de_informacoes.columns
            for pergunta in dados:
                print(pergunta)
                resposta=input("     ")
                self.__dict__[pergunta]=resposta            
                lista_dados.append(resposta)
            tabela_de_informacoes.loc[len(tabela_de_informacoes)]=lista_dados
            tabela_de_informacoes.to_csv(r"petshop\fichas\animal.csv", sep=";", index=False)

            print(self.__dict__)
            print(self.__dict__.get("nome", "nao tem nome "))
            print(self.__dict__.get("cor", "nao tem cor"))
            print(self.__dict__.get("peso", "nao tem peso"))
            print(self.__dict__.get("comprimento", "nao tem comprimento"))
            # print(self.__dict__["morango"])
            print(tabela_de_informacoes.columns)

    def cadastrar_novo_validando_colunas_e_atributos(self):
        tabela_de_informacoes=pd.read_csv(r"petshop\fichas\animal.csv", sep=";")
        lista_dados = []
        for pergunta in tabela_de_informacoes.columns:
            resposta = input(f'Qual o {pergunta} do pet?    ') 
            if pergunta in self.__dict__.keys():
                self.__dict__[pergunta]=resposta             
            lista_dados.append(resposta)

        tabela_de_informacoes.loc[len(tabela_de_informacoes)]=lista_dados
        tabela_de_informacoes.to_csv(r"petshop\fichas\animal.csv", sep=";", index=False)
        print(self.__dict__)
        print(tabela_de_informacoes)

iniciador=Animal()
iniciador.cadastrar_novo_validando_colunas_e_atributos()        