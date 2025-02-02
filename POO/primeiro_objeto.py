class Acoes:

    def piar():
        pass

    def cacar():
        pass


    def miar():
        pass


class MeiosLocomocao:
    
    def nadar():
        pass

    def correr():
        pass



class Passarinho:
    def __init__(self):
        self.cor = 'amarelo'
        self.tamanho = 'pequeno'
        self.peso = 'leve'

    def piar():
        pass

class Gatinho:

    def cacar():
        pass

    def miar():
        pass


class Martelo:
    # todo "def" dentro de uma classe é um MÉTODO
    # método: para que serve a classe

    def __init__(self): # características do objeto: ATRIBUTOS
        self.cor = 'metálica'
        self.material = 'ferro'
        self.resistente = True
        self.cabo = 'madeira'

    def martela(self, prego):
        pass

    def arranca_prego(self):
        pass


def teste(pessoa, fruta):
    print(f'{pessoa} gosta de comer {fruta}')

teste('Bernardo', 'uva') # parametro posicional = os parâmetros são identificados pela posição (passados na mesma ordem que solicitados pela função)
teste(fruta='uva', pessoa='Bernardo') # parametro nomeado = os parâmetros são identificados apontando-se o nome do respectivo parâmetro ao acionar a função