import pandas as pd
import warnings
warnings.filterwarnings("ignore")  #ignorar alertas

def main():
    compras = 5
    tabela_produtos=pd.read_csv(r"estoque_atualizado.csv", sep=";")

    while compras:

        print(tabela_produtos)
        i_produto = int(input('Qual produto você quer? '))
        print(tabela_produtos.iloc[i_produto]) #iloc[i] =  seleciona uma determinada linha
        print(f'O valor de {tabela_produtos['produto'].iloc[i_produto]} é {tabela_produtos['valor'].iloc[i_produto]}')
        deseja_comprar = input("Deseja comprar? S ou N  ")
        if deseja_comprar.upper() == 'S':
            tabela_produtos['estoque'].iloc[i_produto] -= 1
            print(f'Agora o estoque de {tabela_produtos['produto'].iloc[i_produto]} é {tabela_produtos['estoque'].iloc[i_produto]}')
            compras -= 1
    tabela_produtos.to_csv('estoque_atualizado.csv', sep=';', index=False)
    




main()