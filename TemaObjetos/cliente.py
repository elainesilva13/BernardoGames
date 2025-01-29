from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, data_nascimento, endereco, idade):
        super().__init__(nome, sobrenome, data_nascimento, endereco, idade)
        