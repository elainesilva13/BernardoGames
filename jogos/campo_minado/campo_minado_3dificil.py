from campo_minado import Campo_minado


class CampoMinadoDificil(Campo_minado):
    def __init__(self):
        super().__init__()

    def configuracoes(self):
        return {"linhas": 9, "colunas": 9, "minas": 8}
