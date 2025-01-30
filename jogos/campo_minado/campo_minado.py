import random
from campo_minado_1facil import CampoMinadoFacil
from campo_minado_2medio import CampoMinadoMedio
from campo_minado_3dificil import CampoMinadoDificil
from campo_minado_4complicado import CampoMinadoComplicado
from campo_minado_5entediado import CampoMinadoEntediado
from campo_minado_6horas_livres import CampoMinadoHorasLivres


Facil=CampoMinadoFacil
Medio=CampoMinadoMedio
Dificil=CampoMinadoDificil
Complicado=CampoMinadoComplicado
Entediado=CampoMinadoEntediado
Horas_livres=CampoMinadoHorasLivres




class Campo_minado:
    "Classe interface"

    def __init__(self):
        dicionario = self.configuracoes()
        self.linhas = dicionario['linha']
        self.colunas = dicionario['coluna']
        self.minas = dicionario['minas']


    def jogo(self):
        # config = self.configuracoes()
        localizacao_das_minas = self.prepara_lista_de_minas()

        # print(localizacao_das_minas)
        explodiu = False
        lista_de_coordenadas = []
        casas_a_percorrer = self.linhas * self.colunas - self.minas
        while explodiu == False:
            self.campo(self.linhas, self.colunas, lista_de_coordenadas,
                       localizacao_das_minas)

            #  linhas, colunas, lista_de_coordenadas: list[list], lista_de_minas, fim_de_jogo=False)
            coordenadas_do_usuario = self.coordenadas()
            print(coordenadas_do_usuario)
            explodiu = self.verificacao_da_casa(
                coordenadas_do_usuario, localizacao_das_minas)
            if coordenadas_do_usuario not in lista_de_coordenadas:
                lista_de_coordenadas.append(coordenadas_do_usuario)
            else:
                print("Coordenada já foi digitada. Tente outra!")
            if len(lista_de_coordenadas) == casas_a_percorrer:
                print("Parabéns, você venceu!")
                break
        # self.campo(linhas, colunas, lista_de_coordenadas: list[list], lista_de_minas, fim_de_jogo=False)

        "configurar campo"
        "configurar posição das minas"
        "verificar se pisou em mina"

        "exibir quantas minas estão no perimetro do local clicado"
        "desenhar o campo"

    def configuracoes(self):
        raise Exception("Definir a dificuldade")

    def prepara_lista_de_minas(self, config):
        lista_de_minas = []
        qtdminas = config["minas"]
        while qtdminas:

            linhas = config["linhas"]
            sorteia_linha = int(random.uniform(0, linhas))
            colunas = config["colunas"]
            sorteia_coluna = int(random.uniform(0, colunas))
            localizacao_da_mina = [sorteia_linha, sorteia_coluna]
            if localizacao_da_mina not in lista_de_minas:
                lista_de_minas .append(localizacao_da_mina)
                qtdminas -= 1
        return lista_de_minas

    def campo(self, linhas, colunas, lista_de_coordenadas: list[list], lista_de_minas, fim_de_jogo=False):
        print('\n ', end='   ')
        numeros = 0
        numeros2 = 0
        for numero in range(colunas):
            print(f"{numeros2:2}", end=" ")
            numeros2 += 1
        print("\n")
        for linha in range(linhas):
            for coluna in range(-1, colunas):
                if coluna == -1:
                    print(f"{numeros:2}", end="  ")

                    numeros += 1
                    continue
                if [linha, coluna] in lista_de_coordenadas and not fim_de_jogo:
                    bombas_vizinhas = self.pega_vizinhos(
                        x=linha, y=coluna, lista_minas=lista_de_minas)
                    print(bombas_vizinhas, end=" ")
                elif [linha, coluna] in lista_de_minas and fim_de_jogo:
                    print(" X", end=" ")
                else:
                    print(" .", end=" ")
            print("\n")

    def coordenadas(self, config):

        while True:
            coordenadas_das_linhas = input("Qual linha você deseja ir?    ")
            if not coordenadas_das_linhas.isnumeric():

                print("A sua coordenada não é válida. Digite novamente.")
                continue
            coordenadas_das_linhas = int(coordenadas_das_linhas)

            if coordenadas_das_linhas >= config["linhas"]:
                print(f"""A sua coordenada não é válida. Digite de 0 á {
                    config["linhas"]-1}.""")
                continue
            break

        while True:
            coordenadas_das_colunas = input("Qual coluna você deseja ir?    ")

            if not coordenadas_das_colunas.isnumeric():
                print("A sua coordenada não é válida. Digite novamente.")
                continue
            coordenadas_das_colunas = int(coordenadas_das_colunas)
            if coordenadas_das_colunas >= config["colunas"]:
                print(f"""A sua coordenada não é válida. Digite de 0 á {
                    config["colunas"]-1}.""")
                continue

            break
        return [coordenadas_das_linhas, coordenadas_das_colunas]

    def verificacao_da_casa(self, coordenadas, localizacao_minas, config):
        if coordenadas in localizacao_minas:
            print("Booooooooooooooommmmm!!!!")
            return True

        return False

    def pega_vizinhos(self, x, y, lista_minas) -> str:
        bombas_proximas = 0

        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Cima, Baixo, Esquerda, Direita
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonais

        for dx, dy in direcoes:
            viz_x, viz_y = x + dx, y + dy

            if [viz_x, viz_y] in lista_minas:
                bombas_proximas += 1

        return f"{bombas_proximas:2}"


# campo_minado = Campo_minado()
# campo_minado.jogo()
