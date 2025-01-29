from gato import Gato
class Snowshoe(Gato):
    def __init__(self):
        super().__init__(tamanho=0.18, idade=1, alimentacao="Ração", raca="Snowshow", cor="Branco com marrom e preto", dono="Tu mesmo", peso=1.800, nome="Peludo", felicidade=37)


    def crescer(self):
        super().crescer()
        self.tamanho *=0.95
        self.tamanho=round(self.tamanho,4)