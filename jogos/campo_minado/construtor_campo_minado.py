from jogos.campo_minado.campo_minado_1facil import CampoMinadoFacil
from jogos.campo_minado.campo_minado_2medio import CampoMinadoMedio
from jogos.campo_minado.campo_minado_3dificil import CampoMinadoDificil
from unidecode import unidecode


class ConstrutorCampoMinado:
    def __init__(self):
        pass

    def escolhe_campo(self):
        while True:
            dificuldade = unidecode(input("""seja bem vindo(a) ao campo minado! Agora me diga, qual o nivel de dificuldade que voce gostaria de jogar?
                fácil
                        
                médio
                        
                dificil
                        
                complicado
                        
                entediado

                horas livres
                            
                            """).lower())

            if dificuldade == "facil":
                return CampoMinadoFacil()

            if dificuldade == "medio":
                return CampoMinadoMedio()

            if dificuldade == "dificil":
                return CampoMinadoDificil()

            # if dificuldade == "complicado":
            #     dicionario = {"linhas": 13, "colunas": 13, "minas": 15}
            #     return dicionario

            # if dificuldade == "entediado":
            #     dicionario = {"linhas": 16, "colunas": 16, "minas": 25}
            #     return dicionario
            # if dificuldade == "horas livres":
            #     dicionario = {"linhas": 20, "colunas": 20, "minas": 40}
            #     return dicionario
