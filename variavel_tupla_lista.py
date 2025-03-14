
# ## Tuplas (Tuples)

# ### Definição:
# Tuplas são coleções imutáveis de elementos. Elas são muito semelhantes às listas, mas não podem ser alteradas depois de criadas. Ou seja, não podemos adicionar, remover ou modificar elementos de uma tupla.

# ### Sintaxe:

# tupla = (1, 2, 3)


# ### Características das Tuplas:
# - São imutáveis: Uma vez criadas, não podem ser modificadas.
# - Podem conter tipos de dados diferentes.
# - São indexadas, ou seja, podemos acessar os elementos usando índices (como em listas).
# - Aceitam repetição de elementos.

# ### Métodos e Operações:

# #### Acessando Elementos:

# tupla = (10, 20, 30, 40)
# print(tupla[1])  # Saída: 20


# #### Slicing:

# print(tupla[1:3])  # Saída: (20, 30)


# #### Métodos Disponíveis para Tuplas:
# Tuplas têm poucos métodos, já que são imutáveis, mas aqui estão os mais importantes:

# 1. count(): Retorna o número de ocorrências de um valor específico na tupla.

#    tupla = (10, 20, 20, 30)
#    print(tupla.count(20))  # Saída: 2


# 2. index(): Retorna o índice da primeira ocorrência de um valor.

#    tupla = (10, 20, 30, 20)
#    print(tupla.index(20))  # Saída: 1


# #### Operações:
# - Concatenação:

#    tupla1 = (1, 2)
#    tupla2 = (3, 4)
#    tupla_concat = tupla1 + tupla2
#    print(tupla_concat)  # Saída: (1, 2, 3, 4)


# - Multiplicação:

#    tupla = (1, 2)
#    tupla_multiplicada = tupla * 3
#    print(tupla_multiplicada)  # Saída: (1, 2, 1, 2, 1, 2)


# - Verificando a existência de um elemento:

#    tupla = (10, 20, 30)
#    print(20 in tupla)  # Saída: True
#    print(40 in tupla)  # Saída: False
