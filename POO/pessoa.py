class Pessoa:
    def __init__(
            self,
            nome,
            sobrenome,
            data_nascimento,
            endereco,
            idade
            ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    def casar(self, novo_sobrenome):
        self.sobrenome = novo_sobrenome

pessoa = Pessoa(
    nome="Bernardo",
    sobrenome='Gheno Xavier',
    data_nascimento='2012-12-06',
    endereco='Rua qualquer, 30, RS',
    idade=12
)
print('\n\n\n\n')
print(pessoa.__dict__) # __dict__ mostra os atributos como um dicionário
print(pessoa.nome)
print(pessoa.sobrenome)
print(pessoa.idade)
print('Fez aniversário')

pessoa.fazer_aniversario()

print(pessoa.idade)


pessoa.casar('Gheno Seilá')

print(pessoa.sobrenome)

print(pessoa.__dict__) # __dict__ mostra os atributos como um dicionário

print('\n')

print(pessoa)

outra_pessoa = Pessoa( #instanciar = cria um objeto 
    nome="Bernardo",
    sobrenome='Gheno Xavier',
    data_nascimento='2012-12-06',
    endereco='Rua qualquer, 30, RS',
    idade=12
)
outra_pessoa.nome = 'Ricardo'

print('\n')

print(outra_pessoa.__dict__)
print(pessoa.__dict__)

# numero = 10
# numero2 = numero
# numero2 *= 20

# print(numero)
# print(numero2)