
# ## Listas (Lists)

# ### Definição:
# Listas são coleções mutáveis de elementos. Elas permitem adicionar, remover e modificar elementos depois de criadas. Listas são uma das estruturas de dados mais usadas em Python.

# ### Sintaxe:

# lista = [1, 2, 3, 4]


# ### Características das Listas:
# - São mutáveis: Podemos modificar, adicionar ou remover elementos a qualquer momento.
# - Podem conter tipos de dados diferentes.
# - São indexadas, ou seja, podemos acessar os elementos usando índices (como em tuplas).
# - Aceitam repetição de elementos.

# ### Métodos e Operações:

# #### Acessando Elementos:

# lista = [10, 20, 30, 40]
# print(lista[2])  # Saída: 30


# #### Modificando Elementos:

# lista[1] = 25  # Modificando o segundo elemento
# print(lista)  # Saída: [10, 25, 30, 40]


# #### Métodos Disponíveis para Listas:
# 1. append(): Adiciona um item no final da lista.

#    lista = [1, 2, 3]
#    lista.append(4)
#    print(lista)  # Saída: [1, 2, 3, 4]


# 2. insert(): Insere um item em uma posição específica.

#    lista = [1, 2, 3]
#    lista.insert(1, 1.5)  # Insere 1.5 na posição 1
#    print(lista)  # Saída: [1, 1.5, 2, 3]


# 3. remove(): Remove a primeira ocorrência de um item.

#    lista = [1, 2, 3, 2]
#    lista.remove(2)
#    print(lista)  # Saída: [1, 3, 2]


# 4. pop(): Remove o item em uma posição específica e o retorna.

#    lista = [10, 20, 30]
#    print(lista.pop(1))  # Saída: 20
#    print(lista)  # Saída: [10, 30]


# 5. sort(): Ordena os itens da lista.

#    lista = [3, 1, 2]
#    lista.sort()
#    print(lista)  # Saída: [1, 2, 3]


# 6. reverse(): Inverte a ordem dos itens na lista.

#    lista = [1, 2, 3]
#    lista.reverse()
#    print(lista)  # Saída: [3, 2, 1]


# 7. extend(): Adiciona os elementos de outra lista ao final da lista original.

#    lista = [1, 2]
#    lista.extend([3, 4])
#    print(lista)  # Saída: [1, 2, 3, 4]


# 8. clear(): Remove todos os elementos da lista.

#    lista = [1, 2, 3]
#    lista.clear()
#    print(lista)  # Saída: []


# #### Operações:
# - Concatenação:

#    lista1 = [1, 2]
#    lista2 = [3, 4]
#    lista_concat = lista1 + lista2
#    print(lista_concat)  # Saída: [1, 2, 3, 4]


# - Multiplicação:

#    lista = [1, 2]
#    lista_multiplicada = lista * 3
#    print(lista_multiplicada)  # Saída: [1, 2, 1, 2, 1, 2]


# - Verificando a existência de um elemento:

#    lista = [10, 20, 30]
#    print(20 in lista)  # Saída: True
#    print(40 in lista)  # Saída: False
