import time
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
# perguntar o que o usuario quer fazer
# verificar se é valido
# realizar a ação pedida
# caso digite "sair", o loop acaba
# mostrar os produtos com seus preços e quantidades
# pedir para comprar o produto
# verificar se tem dinheiro suficiente
# se não tiver mais do produto, dizer que está em falta
# diminuir em um a quantidade do produto
class Loja():
    def __init__(self):
        self.dinheiro=8000
        self.produtos_e_precos={"celular":980, "computador":1450, "ps5":3800, "caixa de som":170, "controle de tv universal":135, "controle de ps5": 370, "televisão":2400, "impressora":1900, "balinha": 3}
        self.produtos_e_quantidades={"celular":4, "computador":3, "ps5":2, "caixa de som":8, "controle de tv universal": 23, "controle de ps5": 6, "televisão":4, "impressora": 7, "balinha": 117}
        self.tabela_produtos=pd.read_csv(r"lojas\estoque originaly.csv", sep=";")
    
    # def bem_vindo(self): #remover redundâncias
    #     print("\nBem vindo a nossa loja! O que você gostaria de fazer?\n")
    #     while True:
    #         print("\nA)Comprar algum produto\n")
    #         print("\nB)Sair da loja\n")    
    #         print(f"\nSeu dinheiro é: {self.dinheiro}\n")
    #         o_que_fazer=input("        ").upper()
    #         match o_que_fazer:
    #             case "A":
    #                 return True
    #             case "B":
    #                 break
    #         continue


    def comprar_ou_olhar(self):
        print("\nEstes são os nossos produtos!\n")
        #for produto in self.produtos_e_precos:
        #    print(f"\n{produto}")
        # for indice, linha in self.tabela_produtos.iterrows():
            # print(f'{linha['produto']} - R$ {linha['valor']}')

        print(self.tabela_produtos)
        while True:    
            print("\nAgora, o que você quer fazer?")
            print("\nA)Quero comprar um produto")
            print("\nB)Sair")
            print(f"\nSeu dinheiro é: {self.dinheiro}")
            o_que_fazer2=input("\n              ").upper()
            if o_que_fazer2=="A":    
                return "comprar"
            if o_que_fazer2=="B":   
                return "sair"
             
            

    # def mostrar_preco(self):
    #     escolha_do_preco=input("\nQual produto você gostaria de ver o preço?   ").lower()
    #     if escolha_do_preco in self.produtos_e_precos:
    #         print(f"\nO produto custa: {self.produtos_e_precos[escolha_do_preco]}")
    #         time.sleep(2)
    #     else:
    #         print("\nO produto digitado não existe. Tente novamente.")
    #         time.sleep(2)
    
    def comprar_um_produto(self):
        # while com no máximo 8 linhas (lembre-se do return)
        # nenhum else (lembre-se do return) Dica: use "False"/"None" ao invés de True
        while True:
            # compra=input("\nQual produto você gostaria de comprar?").lower()
            compra= int(input("Qual produto você quer?(digite o numero da posição na tabela)  "))  
            # produto_existe=self.verifica_se_produto_existe(compra) 
            # if produto_existe== True:
            if self.tabela_produtos['produto'].iloc[compra]:  
                verificacao_do_estoque=self.verifica_estoque(compra)
            else:
                print("\nO seu produto não existe. Tente novamente.")
                time.sleep(2)
                break #sugestão: use return
            if verificacao_do_estoque== True:
                verificacao_do_dinheiro=self.verifica_dinheiro(compra)
            else:
                print("\nO produto escolhido está fora de estoque no momento! Escolha outro produto.")
                time.sleep(2)
                break    
            if verificacao_do_dinheiro==True:
                self.dinheiro-=self.tabela_produtos['valor'].iloc[compra]
                self.tabela_produtos['estoque'].iloc[compra]-=1
                print("Compra efetuada com sucesso!")
                print(f"\nO seu dinheiro é: {self.dinheiro}")
                time.sleep(2)
                break
            else:
                print("\nVocê não possui dinheiro suficiente par realizar essa compra. Tente comprar outro produto!")
                time.sleep(2)
                break


    def comprar_um_produto_sem_while(self):
        # Técnica "primeiro que sai": quando cai na primeira condição verdadeira, retorna, sem necessidade de continuar percorrendo o código
        # Use essa técnica para eliminar "else"
        compra=input("\nQual produto você gostaria de comprar?").lower()
        if not self.verifica_se_produto_existe(compra):
            print("\nO seu produto não existe. Tente novamente.")
            return
        if not self.verifica_estoque(compra):
            print("\nO produto escolhido está fora de estoque no momento! Escolha outro produto.")
            return 
        if not self.verifica_dinheiro(compra):
            print("\nVocê não possui dinheiro suficiente par realizar essa compra. Tente comprar outro produto!")
            return    
        
        self.dinheiro-=self.produtos_e_precos[compra]
        self.produtos_e_quantidades[compra]-=1
        print("Compra efetuada com sucesso!")
        print(f"\nO seu dinheiro é: {self.dinheiro}")

    def comprar_um_produto_while_reduzido(self):
        while True:
            compra=input("\nQual produto você gostaria de comprar?").lower()
            if not self.verifica_se_produto_existe(compra):
                print("\nO seu produto não existe. Tente novamente.")
                continue
            if not self.verifica_estoque(compra):
                print("\nO produto escolhido está fora de estoque no momento! Escolha outro produto.")
                continue
            if not self.verifica_dinheiro(compra):
                print("\nVocê não possui dinheiro suficiente par realizar essa compra. Tente comprar outro produto!")
                continue
            break

        self.dinheiro-=self.produtos_e_precos[compra]
        self.produtos_e_quantidades[compra]-=1
        print("Compra efetuada com sucesso!")
        print(f"\nO seu dinheiro é: {self.dinheiro}")
        

        

        while True:
            compra=input("\nQual produto você gostaria de comprar?").lower()
            produto_existe=self.verifica_se_produto_existe(compra) 

            if produto_existe== True:
                verificacao_do_estoque=self.verifica_estoque(compra)
            else:
                print("\nO seu produto não existe. Tente novamente.")
                time.sleep(2)
                break #sugestão: use return
            if verificacao_do_estoque== True:
                verificacao_do_dinheiro=self.verifica_dinheiro(compra)
            else:
                print("\nO produto escolhido está fora de estoque no momento! Escolha outro produto.")
                time.sleep(2)
                break    
            if verificacao_do_dinheiro==True:
                self.dinheiro-=self.produtos_e_precos[compra]
                self.produtos_e_quantidades[compra]-=1
                print("Compra efetuada com sucesso!")
                print(f"\nO seu dinheiro é: {self.dinheiro}")
                time.sleep(2)
                break
            else:
                print("\nVocê não possui dinheiro suficiente par realizar essa compra. Tente comprar outro produto!")
                time.sleep(2)
                break



    def verifica_se_produto_existe(self, compra): #melhoria nome da função
        #if compra in self.produtos_e_quantidades:
        #    return True
        if compra in self.tabela_produtos['produto'].to_list():
            return True
        return False


    def verifica_estoque(self, compra):
        # estoque_do_item=self.produtos_e_quantidades[compra]
        estoque_do_item=self.tabela_produtos['estoque'].iloc[compra]
        if estoque_do_item==0:
            return False
        return True

    def verifica_dinheiro(self,compra):
        preco_do_produto=self.tabela_produtos['valor'].iloc[compra]
        if self.dinheiro < preco_do_produto:
            return False
        return True

    def principal(self):
        while True:
            decisao=self.comprar_ou_olhar()
            if decisao== "comprar":
                self.comprar_um_produto()    
                time.sleep(2)
            if decisao== "sair":
                self.tabela_produtos.to_csv(r"lojas\estoque originaly.csv", sep=";", index=False)
                print(f"Obrigado por comprar na nossa loja! ")
                break




iniciador=Loja()
comecar=iniciador.principal() 