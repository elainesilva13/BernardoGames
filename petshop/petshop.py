import pandas as pd
import warnings
from petshop.modelo import ModeloPetShop
from petshop.produtos import Produtos
from petshop.funcionario import Funcionario
from petshop.animal import Animal
warnings.filterwarnings("ignore")


class PetShop():
    
    def __init__(self):
        pass

    def pergunta_objeto_a_manipular(self):
        while True:
            print("Seja bem vindo ao petshop. O que você quer fazer?")
            print("A)Acessar produto")
            print("B)Acessar funcionário")
            print("C)Acessar ficha de animal")
            print("Z)Sair")
            resposta=input("      ").upper()
            match resposta:
                case "A":
                    return Produtos()
                case "B":
                    return Funcionario()
                case "C":
                    return Animal()
                case "Z":
                    quit()
                case _:
                    print("Você não digitou uma informação valida. Tente novamente")
                    continue    

            
    def pergunta_acao(self, objeto_a_ser_manipulado:ModeloPetShop):
        while True:
            print("O que deseja fazer?")
            print("A)Adicionar")
            print("B)Modificar")
            print("C)Excluir")
            print("D)Olhar")
            print("Z)Cancelar")
            resposta=input("        ").upper()
            match resposta:
                case "A":
                    return objeto_a_ser_manipulado.cadastrar()
                case "B":
                    modifcar_linha_inteira=self.especifica_tamanho_da_acao()
                    return objeto_a_ser_manipulado.modificar(modifcar_linha_inteira)
                case "C":
                    modifcar_linha_inteira=self.especifica_tamanho_da_acao()
                    return objeto_a_ser_manipulado.eliminar(modifcar_linha_inteira)
                case "D":
                    return objeto_a_ser_manipulado.mostrar()
                case "Z":
                    return "Voltar"
                case _:
                    print("Informação invalida. Digite novamente")
                    continue    

    # def adiciona_produto(self):
    #     produto=Produtos()
    #     produto.cadastrar()

    # def adiciona_funcionario(self):
    #     funcionario=Funcionario()
    #     funcionario.cadastrar()

    # def adiciona_animal(self):
    #     animal=Animal()
    #     animal.cadastrar()

    # def modifica_produto():
    #     pass  


    def especifica_tamanho_da_acao(self):
        while True:    
            print("Voce quer modificar uma linha inteira ou uma informação especifica?")
            print("A)Linha inteira")
            print("B)Informação especifica")
            resposta=input("     ").upper()
            match resposta:
                case "A":
                    return False
                case "B":
                    return True
                case _:
                    print("A opção digitada não é valida. Tente de novo")
                    continue




    def principal(self):
        while True:
            objeto_a_ser_manipulado=self.pergunta_objeto_a_manipular()
            o_que_fazer_com_o_objeto=self.pergunta_acao(objeto_a_ser_manipulado)
                    
            




iniciador=PetShop()
iniciador.principal()
