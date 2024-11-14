import random
def jogo():
    config= configuracoes()
    "configurar campo"
    "configurar posição das minas"
    "verificar se pisou em mina"
    "exibir quantas minas estão no perimetro do local clicado"
    "desenhar o campo"
def configuracoes():
    dicionario={"linhas":15,"colunas":15,"minas":10}    
    return dicionario

def prepara_lista_de_minas(config):
    lista_de_minas=[]
    linhas= config["linhas"]
    sorteio= int(random.uniform(0,linhas))
    colunas= config["colunas"]
    sorteio2= int(random.uniform(0,colunas))
    localizacao_da_mina=[sorteio, sorteio2]
    lista_de_minas .append (localizacao_da_mina)
