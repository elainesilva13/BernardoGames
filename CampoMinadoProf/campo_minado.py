import random

def  prepara_lista_minas(config):
    lista_minas = []
    qtd_minas = config['minas']
    while qtd_minas:
        x = random.randint(0, config['linhas'] - 1)
        y = random.randint(0, config['colunas'] - 1)
        if (x, y) not in lista_minas:
            lista_minas.append((x, y))
            qtd_minas -= 1
    return lista_minas
    

def configuracoes() -> dict:
    while True:
        nivel = input("Escolha um nivel:\n 1. Fácil\n 2. Médio\n 3. Difícil: ")
        try:
            nivel = int(nivel)
        except:
            continue
        if nivel == 1:
            return {
                'minas': 10,
                'colunas': 10,
                'linhas': 10
            }
        if nivel == 2:
            return {
                'minas': 20,
                'colunas': 15,
                'linhas': 15
            }
        if nivel == 3:
            return {
                'minas': 50,
                'colunas': 20,
                'linhas': 20
            }
        
def desenha_campo(config, lista_minas, revelados_dic:dict={}, fim_jogo=False) -> None:
    print('\n  ', end=' ')
    for col in range(config['colunas']):
        print(f'{col:2}', end='.')
    for x in range(config['linhas']):
        print('\n'+f'{x:2}', end='.')
        for y in range(config['colunas']):
            if (x,y) in lista_minas and fim_jogo:
                print(' X', end='.')
            elif (x,y) in revelados_dic.keys():
                print(revelados_dic[(x,y)], end='.')
            else:
                print('  ', end='.')
    print('\n')

def pega_vizinhos(x, y, lista_minas) -> str:
    bombas_proximas = 0    

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Cima, Baixo, Esquerda, Direita
                (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonais
    
    for dx, dy in direcoes:
        viz_x, viz_y = x + dx, y + dy
        
        if (viz_x, viz_y) in lista_minas:
            bombas_proximas += 1
    
    return  f"{bombas_proximas:2}" 

def pega_palpite(config) -> list[int, int]:
    while True:
        try:
            x = int(input('Digite a coordenada x (linha) :'))
            y = int(input('Digite a coordenada y (coluna):'))
            if 0 <= x < config['colunas'] and 0 <= y < config['colunas']:
                return x, y
        except:
            pass
        print("Digite coordenadas válidas")

def jogo():
    config = configuracoes()
    area = config['colunas'] * config['linhas'] - config['minas']
    lista_minas:list = prepara_lista_minas(config)
    revelados_dic = {}
    ganhou = False
    perdeu = False

    while not ganhou and not perdeu:
        desenha_campo(config, lista_minas, revelados_dic, False)
        x, y = pega_palpite(config)
        if (x, y) in lista_minas:
            print('Você explodiu! D=')
            perdeu = True
            desenha_campo(config, lista_minas=lista_minas, fim_jogo=True)
        else:
            minas_vizinhas:int = pega_vizinhos(x, y, lista_minas)
            revelados_dic[(x, y)] = minas_vizinhas

        if len(revelados_dic) == area:
            ganhou = True
            print('Você venceu!')
            desenha_campo(config, lista_minas=lista_minas, fim_jogo=True)

jogo()

    