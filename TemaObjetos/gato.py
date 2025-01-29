from pet import Pet

class Gato(Pet):
    def __init__(self,tamanho,idade,alimentacao,raca,cor,dono,peso,nome,felicidade):
        # self.pelo=pelo
        # self.alimentacao=alimentacao
        # self.idade=idade
        super().__init__ (tamanho,idade,alimentacao,raca,cor,dono,peso,nome,felicidade)

    # def vocalizar(self):
    #     print("miau!")

    # def fazer_aniversario(self):
    #      self.idade +=1
if __name__=="__main__":
    gato=Gato(tamanho=0.25,idade=1,alimentacao='peixe',raca="sagrado da birmânia",cor="Brancos com marrom",dono='Jubileudo',peso=4.000,nome='meias',felicidade=30)         


    print(gato.__dict__)
    gato.fazer_aniversario()



    print('\n\n\n\n\n\n')
    print(gato.__dict__)