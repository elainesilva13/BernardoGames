import random


def jogo():
    config = configuracoes()
    localizacao_das_minas = prepara_lista_de_minas(config)

    linhas = config["linhas"]

    # print(localizacao_das_minas)
    explodiu = False
    lista_de_coordenadas = []
    colunas = config["colunas"]
    casas_a_percorrer = linhas*colunas-config["minas"]
    while explodiu == False:
        campo(colunas, linhas, lista_de_coordenadas, localizacao_das_minas)
        coordenadas_do_usuario = coordenadas(config)
        print(coordenadas_do_usuario)
        explodiu = verificacao_da_casa(
            coordenadas_do_usuario, localizacao_das_minas, config)
        if coordenadas_do_usuario not in lista_de_coordenadas:
            lista_de_coordenadas.append(coordenadas_do_usuario)
        else:
            print("Coordenada já foi digitada. Tente outra!")
        if len(lista_de_coordenadas) == casas_a_percorrer:
            print("Parabéns, você venceu!")
            break
    campo(colunas, linhas, lista_de_coordenadas,
          localizacao_das_minas, fim_de_jogo=True)

    "configurar campo"
    "configurar posição das minas"
    "verificar se pisou em mina"

    "exibir quantas minas estão no perimetro do local clicado"
    "desenhar o campo"


def configuracoes():
    while True:
        dificuldade = input("""seja bem vindo(a) ao campo minado! Agora me diga, qual o nivel de dificuldade que voce gostaria de jogar?
            fácil
                      
            médio
                      
            dificil
                      
            complicado
                      
            entediado

            horas livres
                           
                        """).lower()

        if dificuldade == "facil":
            dicionario = {"linhas": 4, "colunas": 4, "minas": 2}
            return dicionario

        if dificuldade == "fácil":
            dicionario = {"linhas": 4, "colunas": 4, "minas": 2}
            return dicionario

        if dificuldade == "médio":
            dicionario = {"linhas": 6, "colunas": 6, "minas": 4}
            return dicionario

        if dificuldade == "medio":
            dicionario = {"linhas": 6, "colunas": 6, "minas": 4}
            return dicionario

        if dificuldade == "difícil":
            dicionario = {"linhas": 9, "colunas": 9, "minas": 8}
            return dicionario

        if dificuldade == "dificil":
            dicionario = {"linhas": 9, "colunas": 9, "minas": 8}
            return dicionario

        if dificuldade == "complicado":
            dicionario = {"linhas": 13, "colunas": 13, "minas": 15}
            return dicionario

        if dificuldade == "entediado":
            dicionario = {"linhas": 16, "colunas": 16, "minas": 25}
            return dicionario
        if dificuldade == "horas livres":
            dicionario = {"linhas": 20, "colunas": 20, "minas": 40}
            return dicionario


def prepara_lista_de_minas(config):
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


def campo(linhas, colunas, lista_de_coordenadas: list[list], lista_de_minas, fim_de_jogo=False):
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
                bombas_vizinhas = pega_vizinhos(
                    x=linha, y=coluna, lista_minas=lista_de_minas)
                print(bombas_vizinhas, end=" ")
            elif [linha, coluna] in lista_de_minas and fim_de_jogo:
                print(" X", end=" ")
            else:
                print(" .", end=" ")
        print("\n")


def coordenadas(config):

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


def verificacao_da_casa(coordenadas, localizacao_minas, config):
    if coordenadas in localizacao_minas:
        print("Booooooooooooooommmmm!!!!")
        return True

    return False


def pega_vizinhos(x, y, lista_minas) -> str:
    bombas_proximas = 0

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Cima, Baixo, Esquerda, Direita
                (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonais

    for dx, dy in direcoes:
        viz_x, viz_y = x + dx, y + dy

        if [viz_x, viz_y] in lista_minas:
            bombas_proximas += 1

    return f"{bombas_proximas:2}"


jogo()
