import time
import random
import pandas as pd
# o vendedor terá certa quantia de dinheiro
# fazer entrar um cliente entrar na loja
# fechar a loja ou mostrar a tabela
# se fechar a loja, o jogo acaba
# o cliente compra um produto aleatório ou sai
# se ele sair, o jogo acaba
class Loja2():
    def __init__(self):
        self.dinheiro=3000
        self.tabela_produtos=pd.read_csv(r"estoque originaly.csv", sep=";")
        self.produtos_e_precos={"celular":980, "computador":1450, "ps5":3800, "caixa de som":170, "controle de tv universal":135, "controle de ps5": 370, "televisão":2400, "impressora":1900, "balinha": 3,"sair":False}
        print(self.dinheiro)
        self.numero_de_compras_maximo=5
        self.lista_de_compras=[]

    def cliente_entra(self):
        while True:
            lista_de_alternativas=["A","B"]
            print("\nUm cliente entrou na sua loja. O que você quer fazer??")
            print("\nA)Mostrar os produtos")
            print("\nB)Fechar a loja")
            escolha=input("       ").upper()
            if escolha not in lista_de_alternativas:
                continue
            return escolha
        
    def escolha_do_cliente(self):
        
        print("\nVocê mostrou a tabela de produtos para o cliente")
        print(self.tabela_produtos)
        print("\nO cliente está escolhendo um produto agora...")
        time.sleep(2)
        if self.numero_de_compras_maximo==0:
            print("\nO cliente saiu!")
            print(f"\nO cliente comprou esse(s) produto(s):{self.lista_de_compras}")
        escolha_do_cliente=random.choice(list(self.produtos_e_precos.items()))
        if escolha_do_cliente[0]=="sair":
            print("\nO cliente saiu!")
            if self.lista_de_compras==None:
                print("\nO cliente não comprou nenhum produto!")
                return False    
            print(f"\nO cliente comprou esse(s) produto(s): {self.lista_de_compras}")
            return False
        print(f"\nO cliente comprou um(a) {escolha_do_cliente[0]}")
        self.lista_de_compras.append(escolha_do_cliente[0])
        self.dinheiro+=escolha_do_cliente[1]
        print(f"\nO seu dinheiro é: {self.dinheiro}")
        self.numero_de_compras_maximo-=1

        
        
        
        

    def principal(self):
        comeco=self.cliente_entra()
        while True:
            if comeco =="A":
                mostrar_produtos=self.escolha_do_cliente()
            if comeco=="B":
                break    
            if mostrar_produtos==False:
                break


iniciador=Loja2()
comecar=iniciador.principal() 