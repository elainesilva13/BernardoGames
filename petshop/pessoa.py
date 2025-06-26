import pandas as pd
from abc import ABC, abstractmethod

class Pessoa(ABC): # ABC indica que é uma classe abstrata, ou seja, uma classe modelo para outras
    def __init__(self):
        self.nome=""
        self.idade=""
        self.genero=""
        self.cidade_de_residencia=""

    @abstractmethod
    def pega_nome_planilha_csv(self)->str:
        pass    