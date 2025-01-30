from campo_minado import Campo_minado


class CampoMinadoFacil(Campo_minado):
    def __init__(self):
        super().__init__()

    def configuracoes(self):
        return {"linhas": 4, "colunas": 4, "minas": 2}
