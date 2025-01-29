from cachorro import Cachorro
class Golden(Cachorro):
    def __init__(self, dono, nome):
        super().__init__(
            tamanho=0.56, idade=4, alimentacao="ração", raca="golden", cor="dourado", dono=dono, 
            peso=30.000, nome=nome, felicidade=60)
    

    def comer(self):
        super().comer()
        self.peso *=1.05