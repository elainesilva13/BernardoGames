class Pet:
    def __init__(self, tamanho, idade, alimentacao, raca, cor, dono, peso, nome, felicidade):
        self.tamanho = tamanho
        self.idade = idade
        self.alimentacao = alimentacao
        self.raca = raca
        self.cor = cor
        self.dono = dono
        self.peso = peso
        self.nome = nome
        self.__felicidade = felicidade

    def ficar_feliz(self, pontos_de_felicidade):
        if pontos_de_felicidade < 0:
            print("A felicidade não pode ser negativa!")
            return
        self.__felicidade += pontos_de_felicidade
        if self.__felicidade > 100:
            self.__felicidade = 100

    def ficar_triste(self, pontos_de_tristeza):
        if pontos_de_tristeza < 0:
            print("A felicidade não pode ser negativa!")
            return
        self.__felicidade -= pontos_de_tristeza
        if self.__felicidade < 0:
            self.__felicidade = 0

    def crescer(self):
        self.tamanho += 0.03
        self.tamanho = round(self.tamanho, 2)

    def fazer_aniversario(self):
        self.idade += 1

    def comer(self):
        print(f"comendo um delicioso {self.alimentacao}")
        self.peso += 0.20
        self.peso = round(self.peso, 2)

    def vocalizar(self):
        # print("Este animal não produz som.Ele é bem quieto.")
        raise Exception("cdfvrvfvas")
