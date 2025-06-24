from abc import ABC, abstractmethod
import pandas as pd

class ModeloPetShop():
    def __init__(self):
        self.nome=""


    def cadastrar(self):
        tabela=self.retorna_dataframe()
        lista_dados=[]
        for chave, valor in self.__dict__.items():
            print(chave)
            resposta=input("     ")
            self.__dict__[chave]=resposta
            lista_dados.append(resposta)
        tabela.loc[len(tabela)]=lista_dados
        self.salva_atualizacoes(tabela)

    
    def modificar(self, modifcar_linha_inteira):
        indice_int=self.pega_indice()
        tabela=self.retorna_dataframe()
        lista_dados=[]
        for chave, valor in self.__dict__.items():
            print(chave)
            informacao_a_adicionar=input("     ")
            self.__dict__[chave]=informacao_a_adicionar
            lista_dados.append(informacao_a_adicionar)
        tabela.iloc [indice_int]=lista_dados
        self.salva_atualizacoes(tabela)


    def mostrar(self):
        tabela=self.retorna_dataframe()
        print(tabela)
        

    def eliminar(self, modifcar_linha_inteira):
        tabela=self.retorna_dataframe()
        if modifcar_linha_inteira== False:
            indices_especificos=self.pega_indices_especificos()
            tabela=tabela.drop(tabela[indices_especificos[0]].iloc[indices_especificos[1]])
            self.salva_atualizacoes(tabela)
            return
        indice=self.pega_indice()
        tabela=tabela.drop(indice)
        self.salva_atualizacoes(tabela)



    def pega_indices_especificos(self):
        lista_indices=[]
        tabela=self.retorna_dataframe()
        while True:
            print(tabela)
            print("Diga o indice que você quer acessar?")
            indice=input("     ")
            if not indice.isnumeric() or int(indice) not in tabela.index:
                print("Esse indice não é valido. Tente novamente")
                continue
            lista_indices.append(int(indice))
            break
        while True:
            print(tabela)
            print("E agora, qual a coluna?")
            coluna=input("    ").lower()
            if not coluna in tabela.columns:
                print("A coluna digitada não existe. Tente de novo")
                continue
            lista_indices.append(coluna)

            return lista_indices


    def pega_indice(self):
        tabela=self.retorna_dataframe()
        while True:
            print(tabela)
            print("Diga o indice que você quer acessar?")
            indice=input("     ")
            if not indice.isnumeric() or int(indice) not in tabela.index:
                print("Esse indice não é valido. Tente novamente")
                continue
            return int(indice)

    @abstractmethod
    def pega_nome_planilha_csv(self)->str:
        pass    

    def retorna_dataframe(self):
        nome_do_arquivo=self.pega_nome_planilha_csv()
        tabela=pd.read_csv(nome_do_arquivo, sep=";")
        return tabela
    
    def salva_atualizacoes(self, tabela:pd.DataFrame):
        nome_do_arquivo=self.pega_nome_planilha_csv()
        tabela.to_csv(nome_do_arquivo, sep=";", index=False)

