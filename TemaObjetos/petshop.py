from cachorro import Cachorro
from cliente import Cliente
from endereco import Endereco
from gato import Gato
from golden import Golden
from peixe import Peixe
from peixe_dourado import Peixe_dourado
from snowshoe import Snowshoe
from pet import Pet

class Petshop():
    def __init__(self):
        self.cliente_em_atendimento:Cliente=None
        
    # def __endereco_do_pet(self):
    #     self.pet_escolhido.dono:Cliente.endereco
    #     self.pet_escolhido.dono.endereco.exib_endereco()


    def atender_cliente(self,cliente:Cliente,):
        self.cliente_em_atendimento=cliente
        self.pet_escolhido=self.__escolha_do_pet()
        self.pet_escolhido.dono=self.cliente_em_atendimento.nome
        self.__interacoes()

    def __escolha_do_pet(self):
        while True:
            escolha = input( "Seja bem vindo ao petshop! Qual animal voce gostaria de ter? Cachorro, gato ou peixe?   ").lower()
            

            if escolha == "cachorro":
                raca_do_cachorro=input("Ecolha qual raça você quer. Golden ou srd    ").lower()

                if raca_do_cachorro=="golden":
                    return Golden(dono=self.cliente_em_atendimento.nome, nome="Arcanine")
                
                if raca_do_cachorro=="srd":
                    return Cachorro()
                print(f"Não temos a raça {raca_do_cachorro}")
                continue            


            if escolha == "gato":
                raca_do_gato=input("Ecolha qual raça você quer. Snowshoe ou sagrado da birmânia?    ").lower()
            
                if raca_do_gato=="sagrado da birmânia":
                    return Gato()
            
                if raca_do_gato=="sagrado da birmania":
                    return Gato()
            
                if raca_do_gato=="snowshoe":
                    return Snowshoe()
                    
                print(f"Não temos a raça {raca_do_gato}")
                continue                

            
            if escolha == "peixe":
                raca_do_peixe=input("Ecolha qual raça você quer. Peixe voador ou peixe dourado    ").lower()

                if raca_do_peixe=="peixe voador":
                    return Peixe()
            
                if raca_do_peixe=="peixe dourado":
                    return Peixe_dourado()
            
                print(f"Não temos a raça {raca_do_peixe}")
                continue



    # def pet_que_a_pessoa_escolheu(self):
    #     self.atender_cliente(self)
    #     self.pet_escolhido = self.__escolha_do_pet()
    #     print('\n\n\n')
    #     print(self.pet_escolhido.__dict__)
    #     coisas_para_interagir = self.__interacoes(self.pet_escolhido)


    def __interacoes(self):
        while True:
            print('\n')

            print("Escolha o que você quer fazer com seu bichinho")

            print("A. Mudar o nome")

            print("B. Alimentar")

            print("C. Brincar")

            print("D. Fazer Aniversário")

            print("E. Crescer")

            print("G. Endereço do pet")

            print(f"F. conversar com {self.pet_escolhido.nome}")

            print("Z. Dormir ")

            escolha = input("A, B, C, D, E, F, G ou Z(acaba o jogo)  ").lower()
            print('\n')

            if escolha == "a":
                novo_nome = input("Novo nome:  ")
                self.pet_escolhido.nome = novo_nome

            if escolha == "b":
                self.pet_escolhido.comer()
                self.pet_escolhido.ficar_feliz(10)

            if escolha == "c":
                self.pet_escolhido.ficar_feliz(20)

            if escolha == "d":
                self.pet_escolhido.fazer_aniversario()
                self.pet_escolhido.ficar_triste(3)

            if escolha == "e":
                self.pet_escolhido.crescer()
                


            if escolha == "f":
                self.pet_escolhido.vocalizar()    

            
            # if escolha == "g":
            #     self.__endereco_do_pet()    
    

            if escolha == "z":
                break
            
            print('\n')
                
            print(self.pet_escolhido.__dict__)


if __name__=="__main__":


    cliente=Cliente(
        nome="Cara do teste",
        sobrenome="do jogo",
        data_nascimento="18/07/1999",
        endereco=Endereco(
            nome_da_rua="Rua do shopping",
            numero="888",
            bairro="Quero sorvete",
            cidade="Porto alegre",
            estado="Rio grande do sul",
            pais="Brasil",
            continente="América do sul"      
        ),
        idade=25)
   
    petshop=Petshop()
    petshop.atender_cliente(cliente)
