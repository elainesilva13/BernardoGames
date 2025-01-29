from pet import Pet

class Peixe(Pet):
    def __init__(self,tamanho,idade,alimentacao,raca,cor,dono,peso,nome,felicidade):
        # self.especie=especie
        # self.tamanho=tamanho
        # self.habitat=habitat
        super().__init__(tamanho,idade,alimentacao,raca,cor,dono,peso,nome,felicidade) 
   
    def crecser(self):
         self.tamanho +=0.2

# tamanho=0.40
if __name__=="__main__":
    peixe=Peixe(tamanho=0.40,idade=1,alimentacao="plâncton",raca="peixe voador",cor='azul',dono="sei la",peso=1.400,nome="voador",felicidade=25)   
    print('\n\n\n\n\n\n')
    print(peixe.__dict__)
# print(tamanho)