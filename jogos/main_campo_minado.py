from jogos.campo_minado.construtor_campo_minado import ConstrutorCampoMinado


def main():
    construtor = ConstrutorCampoMinado()
    campo_usuario = construtor.escolhe_campo()
    campo_usuario.jogo()


if __name__ == "__main__":
    main()
