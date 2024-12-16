print("Relembrando tipos de variáveis\n\n")
print("A função type retorna o tipo de uma variável\n")

print("Variável tipo string:")
string = "Armazena uma palavra ou um texto"
print(type(string)) # <class 'str'>

string2 = "Exemplo de outra string"
string_concatenada = string + string2
print("Para concaternar 2 ou mais strings, podemos usar '+'")
print(string_concatenada) #concatenar: "juntar"

string_com_uper_case = string.upper()
print(string_com_uper_case)
print("Quando usamos 'variavel.funcao()' indica que a função é um MÉTODO")

string_com_lower_case = string.lower()
print(string_com_lower_case)

string_com_title_case = string.title()
print(string_com_title_case)

lista_criada_a_partir_de_uma_string = string.split() # sem parâmetro, o separador padrão é " " (espaço)
print(lista_criada_a_partir_de_uma_string)
print(f'O tipo da variável lista_criada_a_partir_de_uma_string é {type(lista_criada_a_partir_de_uma_string)}')
string_separa_por_ponto_e_virgula = 'valor;descrição'
outra_lista = string_separa_por_ponto_e_virgula.split(';')
print(outra_lista)
print(type(outra_lista))
print("O método split transforma uma string em uma lista. Nesta lista, todos os elementos serão STRINGS")
outro_split = '1,2,3,4,5,6'
mais_uma_lista = outro_split.split(',')
primeiro_elemento_de_mais_uma_lista = mais_uma_lista[0]
print(f"O tipo do primeiro elemento da lista mais_uma_lista é {type(primeiro_elemento_de_mais_uma_lista)}")
print(primeiro_elemento_de_mais_uma_lista)
qualquer_palavra = 'qualquer'
print(f"Pegamos a primeira letra de uma palavra assim: qualquer_palavra[0] => {qualquer_palavra[0]}")
print(f"Pegamos da primeira até a terceira letra de uma palavra assim: qualquer_palavra[0:3] => {qualquer_palavra[0:3]}")
string_com_varios_dados = "Bernardo-----Rio Grande do Sul-----10----Verde"
nome = string_com_varios_dados[0:8]
estado=string_com_varios_dados[13:30]
idade = string_com_varios_dados[35:37]
cor_favorita =string_com_varios_dados[41:46]
print(nome)
print(estado)
print(idade)
print(cor_favorita)
string_assim = '[1,2,3,4]'
string_sem_colchete = string_assim.replace("[", '')
string_sem_colchete = string_sem_colchete.replace("]", '')
lista_assim = string_sem_colchete.split()
print(lista_assim)
print(type(lista_assim))
for e in lista_assim:
    print(e, end=', ')
print('\n')
numero_dez = 10
outra_string_concatenada = 'exemplo' + str(numero_dez)
print(outra_string_concatenada)