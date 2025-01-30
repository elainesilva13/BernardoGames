from campo_minado import Campo_minado


class CampoMinadoComplicado(Campo_minado):
    def __init__(self):
        super().__init__()
    def configuracoes(self):
        return {"linhas": 13, "colunas": 13, "minas": 15}
    

    