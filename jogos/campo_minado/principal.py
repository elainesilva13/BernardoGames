# client = responsável pela solicitação da execução do script e por
# "juntar" e organizar a execução conforme necessário

from construtor_campo_minado import ConstrutorCampoMinado


def executa_jogo():
    construtor = ConstrutorCampoMinado()
    jogo = construtor.escolhe_campo()
    jogo.jogo()


executa_jogo()
