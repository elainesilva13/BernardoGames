import pandas as pd
import warnings
from produtos import Produtos
from funcionario import Funcionario
from animal import Animal
warnings.filterwarnings("ignore")


class PetShop():
    
    def __init__(self):
        pass


    def pergunta_acao(self):
        while True:
            print("Seja bem vindo ao nosso petshop! O que você quer fazer?")
            print("A)Adicionar produto")
            print("B)Adicionar funcionário")
            print("C)Adicionar ficha de animal")
            resposta=input("        ").upper()
            match resposta:
                case "A":
                    return "adicionar produto"
                case "B":
                    return "adicionar funcionario"
                case "C":
                    return "adicionar ficha de animal"
                case _:
                    print("Informação invalida. Digite novamente")
                    continue    

    def principal(self):
        escolha=self.pergunta_acao()




iniciador=PetShop()
iniciador.principal()
