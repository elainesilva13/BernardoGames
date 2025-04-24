import time
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
    
    
    def bem_vindo(self): #remover redundâncias
        print("\nBem vindo a nossa loja! O que você gostaria de fazer?\n")
        while True:
            print("\nA)Comprar algum produto\n")
            print("\nB)Sair da loja\n")    
            print(f"\nSeu dinheiro é: {self.dinheiro}\n")
            o_que_fazer=input("        ").upper()
            match o_que_fazer:
                case "A":
                    return True
                case "B":
                    break
            continue


    def comprar_ou_olhar(self):
        print("\nEstes são os nossos produtos!\n")
        for produto in self.produtos_e_precos:
            print(f"\n{produto}")
        while True:    
            print("\nAgora, o que você quer fazer?")
            print("\nA)Quero comprar um produto")
            print("\nB)Quero ver o preço de um produto")
            print("\nC)Sair")
            print(f"\nSeu dinheiro é: {self.dinheiro}")
            o_que_fazer2=input("\n              ").upper()
            if o_que_fazer2=="A":    
                return "comprar"
            if o_que_fazer2=="B":   
                return "olhar"
            if o_que_fazer2=="C":    
                break

    def mostrar_preco(self):
        escolha_do_preco=input("\nQual produto você gostaria de ver o preço?   ").lower()
        if escolha_do_preco in self.produtos_e_precos:
            print(f"\nO produto custa: {self.produtos_e_precos[escolha_do_preco]}")
            time.sleep(2)
        else:
            print("\nO produto digitado não existe. Tente novamente.")
            time.sleep(2)
    
    def comprar_um_produto(self):
        # while com no máximo 8 linhas (lembre-se do return)
        # nenhum else (lembre-se do return) Dica: use "False"/"None" ao invés de True
        while True:
            print("\nQual produto você gostaria de comprar?")
            compra=input("           ").lower()
            produto_existe=self.verifica_se_produto_existe(compra) #melhoria nome da variável
            if produto_existe== True:
                verificacao_do_estoque=self.verifica_estoque(compra)
            else:
                print("\nO seu produto não existe. Tente novamente.")
                time.sleep(2)
                break #sugestão: use return
            if verificacao_do_estoque== True:
                verificacao_do_dinheiro=self.verifica_dinheiro(compra)
                # print(verificacao_do_dinheiro)
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
        if compra in self.produtos_e_quantidades:
            return True

    def verifica_estoque(self, compra):
        estoque_do_item=self.produtos_e_quantidades[compra]
        # print(estoque_do_item)
        if estoque_do_item==0:
            return False
        return True

    def verifica_dinheiro(self,compra):
        preco_do_produto=self.produtos_e_precos[compra]
        # print(preco_do_produto)
        if self.dinheiro < preco_do_produto:
            return False
        return True

    def principal(self):
        comprar_ou_sair=self.bem_vindo() # rever esta função (é mesmo necessária?)
        while True:
            decisao1=self.comprar_ou_olhar()
            print(decisao1)
            if decisao1== "comprar":
                self.comprar_um_produto()    
            if decisao1=="olhar":
                self.mostrar_preco()




iniciador=Loja()
comecar=iniciador.principal() 