from peixe import Peixe
class Peixe_dourado(Peixe):
    def  __init__(self):
        super().__init__(tamanho=0.17, idade=1, alimentacao="alga", raca="Peixinho dourado", cor="Laranja", dono="Você", peso=0.200, nome="Magikarp", felicidade=40)


    def vocalizar(self):

        print(f"Você tenta se comunicar, mas tudo que {self.nome} faz é soltar algumas bolhas.")