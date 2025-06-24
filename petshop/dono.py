import pandas as pd

from petshop.pessoa import Pessoa

class Dono(Pessoa):
    def __init__(self):
        super().__init__()
        self.pet=""



    def pega_nome_planilha_csv(self):
        return r"petshop\fichas\dono.csv"




