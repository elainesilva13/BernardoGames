import pandas as pd

from petshop.pessoa import Pessoa
from petshop.modelo import ModeloPetShop

class Dono(ModeloPetShop):
    def __init__(self):
        super().__init__()
        self.idade=""
        self.cidade_de_residencia=""
        self.pet=""
        self.especie_do_pet=""




    def pega_nome_planilha_csv(self):
        return r"petshop\fichas\dono.csv"




