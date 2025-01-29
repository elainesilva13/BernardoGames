class Endereco:
    def __init__(self,nome_da_rua,numero,bairro,cidade,estado,pais,continente,complemento=""):
        
        self.nome_da_rua=nome_da_rua
        self.numero=numero
        self.bairro=bairro
        self.cidade=cidade
        self.estado=estado
        self.pais=pais
        self.continente=continente
        self.complemento=complemento

    def exib_endereco(self):
        print("O endereço é: ")
        for chave,valor in self.__dict__.items():
            print(chave,valor)
