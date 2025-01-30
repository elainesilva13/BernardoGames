from campo_minado_1facil import CampoMinadoFacil
from campo_minado_2medio import CampoMinadoMedio
from campo_minado_3dificil import CampoMinadoDificil
from campo_minado_4complicado import CampoMinadoComplicado
from campo_minado_5entediado import CampoMinadoEntediado
from campo_minado_6horas_livres import CampoMinadoHorasLivres
# from unidecode import unidecode


class ConstrutorCampoMinado:
    def __init__(self):
        pass

    def escolhe_campo(self):
        while True:
            dificuldade =(input("""seja bem vindo(a) ao campo minado! Agora me diga, qual o nivel de dificuldade que voce gostaria de jogar?
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

            if dificuldade == "complicado":
               
                return CampoMinadoComplicado()

            if dificuldade == "entediado":
                return CampoMinadoEntediado()


            if dificuldade == "horas livres":
                return CampoMinadoHorasLivres()