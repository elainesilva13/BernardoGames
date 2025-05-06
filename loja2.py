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
        #self.produtos_e_precos={"celular":980, "computador":1450, "ps5":3800, "caixa de som":170, "controle de tv universal":135, "controle de ps5": 370, "televisão":2400, "impressora":1900, "balinha": 3,"sair":False}
        print(self.dinheiro)
        self.numero_de_compras_maximo=5
        self.lista_de_compras=[]

    def cliente_entra(self):
        while True:
            lista_de_alternativas=["A","B"]
            print("\nUm cliente entrou na sua loja. O que você quer fazer??")
            print("\nA)Mostrar os produtos")
            print("\nB)Adicionar um produto")
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
            print(f"\nO cliente comprou esse(s) produto(s):{self.lista_de_compras}") #por que continua oferecendo se p cçiente já foi embora?
        
        produtos = self.tabela_produtos['produtos'].to_list()
        produtos.append('sair')
        #escolha_do_cliente=random.choice(list(self.produtos_e_precos.items()))
        escolha_do_cliente:str=random.choice(produtos)
        if escolha_do_cliente=="sair":
            print("\nO cliente saiu!")
            if self.lista_de_compras==None:
                print("\nO cliente não comprou nenhum produto!")
                return False    
            print(f"\nO cliente comprou esse(s) produto(s): {self.lista_de_compras}")
            return False
        preco_produto = self.tabela_produtos.loc[self.tabela_produtos['produto']== escolha_do_cliente, 'preco'].values[0]
        # filtra/busca valores= tabela.loc[repete a variavel tabela[coluna que vai olhar] == condição/o que você procura, coluna que você quer].vales[0] - [0] é para retornar o primeiro que achar, se quiser todos na forma de tupla, só tirar o [0]
        print(f"\nO cliente comprou um(a) {escolha_do_cliente}")
        self.lista_de_compras.append(escolha_do_cliente)
        self.dinheiro+=preco_produto
        print(f"\nO seu dinheiro é: {self.dinheiro}")
        self.numero_de_compras_maximo-=1
        return True # se estiver trabalhando com "False", use o "True" também! (booleanos)
        
        
    def adicionar_um_produto_bernardo(self):
        produto_adicionado=input("Qual produto você quer adicionar?    ")
        preco_do_produto=input("E agora, qual é o preço dele?")
        # self.produtos_e_precos[produto_adicionado]=preco_do_produto
        # print(self.produtos_e_precos)
        self.tabela_produtos['produto'][produto_adicionado]=preco_do_produto
        #print(self.tabela_produtos)
          
    def adicionar_um_produto(self):
        produto_adicionado=input("Qual produto você quer adicionar?    ")
        preco_do_produto=input("E agora, qual é o preço dele?")
        estoque_do_produto=input("Por fim, quantas unidades temos?")

        df_1_linha = pd.DataFrame(data={
            'produto': [produto_adicionado],
            'valor' : [preco_do_produto],
            'estoque': [estoque_do_produto]
        })

        self.tabela_produtos = pd.concat([self.tabela_produtos, df_1_linha], ignore_index=True)
        self.tabela_produtos.to_csv(r"estoque originaly.csv", sep=';', index=False)
        # self.produtos_e_precos[produto_adicionado]=preco_do_produto
        print(self.produtos_e_precos)
        #self.tabela_produtos['produto'][produto_adicionado]=preco_do_produto
        print(self.tabela_produtos)


    def principal(self):
        comeco=self.cliente_entra()
        while True:
            if comeco =="A":
                mostrar_produtos=self.escolha_do_cliente()
            if comeco=="B":
                produto_adicionado=self.adicionar_um_produto() #Por que uma variável está recebendo o retorno da função sendo que esta não retorna nada
                continue
            #EVITAR:
            #if mostrar_produtos==False:
            #    break

            if not mostrar_produtos: # = 0, = None o = False
                break

iniciador=Loja2()
comecar=iniciador.principal() 

# corrigir os bugs
# corrigir o loop infinito
# opção de mais de um clientes