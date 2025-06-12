import pandas as pd
import warnings
from petshop.produtos import Produtos
from petshop.funcionario import Funcionario
from petshop.animal import Animal
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
            print("D)Modificar produtos")
            print("Z)Sair")
            resposta=input("        ").upper()
            match resposta:
                case "A":
                    return self.adiciona_produto()
                case "B":
                    return self.adiciona_funcionario()
                case "C":
                    return self.adiciona_animal()
                case "D":
                    return self.modifica_produto()
                case "Z":
                    quit()
                case _:
                    print("Informação invalida. Digite novamente")
                    continue    

    def adiciona_produto(self):
        produto=Produtos()
        produto.adiciona_produto()

    def adiciona_funcionario(self):
        funcionario=Funcionario()
        funcionario.cadastrar()

    def adiciona_animal(self):
        animal=Animal()
        animal.cadastrar_novo_validando_colunas_e_atributos()

    def modifica_produto():
        pass

    def principal(self):
        while True:
            self.pergunta_acao()
        
            




iniciador=PetShop()
iniciador.principal()
