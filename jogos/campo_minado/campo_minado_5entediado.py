from campo_minado import Campo_minado


class CampoMinadoEntediado(Campo_minado):
    def __init__(self):
        super().__init__()

    def configuracoes(self):
       return {"linhas": 15, "colunas": 15, "minas": 18}    
