import pandas as pd
from abc import ABC, abstractmethod

class Pessoa():
    def __init__(self):
        self.idade=""
        self.genero=""
        self.cidade_de_residencia=""

    @abstractmethod
    def pega_nome_planilha_csv(self)->str:
        pass    