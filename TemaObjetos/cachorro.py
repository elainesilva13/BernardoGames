from pet import Pet

class Cachorro(Pet):
    def __init__(self,tamanho,idade,alimentacao,raca,cor,dono,peso,nome,felicidade):
        # self.raca= raca
        # self.peso=peso 
        # self.altura= altura 
        # self.alimentacao= alimentacao
        super().__init__ (tamanho,idade,alimentacao,raca,cor,dono,peso,nome,felicidade)

    # def crescer(self):
    #     self.altura += 0.02

    # def comer_demais(self):
    #     self.peso += 0.500 

    def vocalizar(self):
        print("au au!")

if __name__=="__main__":
    cachorro=Cachorro(raca='pug',tamanho=0.30,peso=7.500,alimentacao='ração',idade=2,cor="creme",dono="Tio Davi",nome="Au Au",felicidade=70)

    print(cachorro.__dict__)
    cachorro.comendo()
    cachorro.crescer()    

    # altura= 0.30

    # peso= 7.500


    # alimentacao='ração'
        
    print('\n\n\n\n\n\n')
    print(cachorro.__dict__)




