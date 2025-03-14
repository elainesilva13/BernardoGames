
# ---

# ## 3. Sets (Conjuntos)

# ### Definição:
# Um set é uma coleção não ordenada de elementos únicos. Ou seja, não é possível ter elementos repetidos. Além disso, sets são mutáveis, mas não mantêm a ordem dos elementos.

# ### Sintaxe:

# meu_set = {1, 2, 3}


# ### Características dos Sets:
# - Não permite elementos duplicados: Se tentarmos adicionar um valor duplicado, ele será ignorado.
# - São não ordenados: Não podemos acessar os elementos por índices, pois a ordem não é garantida.
# - São mutáveis: Podemos adicionar ou remover elementos após a criação.

# ### Métodos e Operações:

# #### Adicionando e Removendo Elementos:
# 1. add(): Adiciona um elemento ao set.

#    meu_set = {1, 2, 3}
#    meu_set.add(4)
#    print(meu_set)  # Saída: {1, 2, 3, 4}


# 2. remove(): Remove um elemento específico do set. Lança erro se o elemento não existir.

#    meu_set = {1, 2, 3}
#    meu_set.remove(2)
#    print(meu_set)  # Saída: {1, 3}


# 3. discard(): Remove um elemento, mas não lança erro se o elemento não existir.

#    meu_set = {1, 2, 3}
#    meu_set.discard(2)
#    print(meu_set)  # Saída: {1, 3}


# 4. pop(): Remove e retorna um elemento arbitrário.

#    meu_set = {1, 2, 3}
#    print(meu_set.pop())  # Saída: 1 (ou outro elemento, pois não tem ordem)


# 5. clear(): Remove todos os elementos do set.

#    meu_set = {1, 2, 3}
#    meu_set.clear()
#    print(meu_set)  # Saída: set()


# #### Operações:
# - União:

#    set1 = {1, 2}
#    set2 = {2, 3}
#    union_set = set1 | set2
#    print(union_set)  # Saída: {1, 2, 3}


# - Interseção:

#    set1 = {1, 2}
#    set2 = {2, 3}
#    intersection_set = set1 & set2
#    print(intersection_set)  # Saída: {2}


# - Diferença:

#    set1 = {1, 2}
#    set2 = {2, 3}
#    difference_set = set1 - set2
#    print(difference_set)  # Saída: {1}


# - Diferença Simétrica (Elementos que estão em um set ou no outro, mas não em ambos):

#    set1 = {1, 2}
#    set2 = {2, 3}
#    symmetric_difference_set = set1 ^ set2
#    print(symmetric_difference_set)  # Saída: {1, 3}


# #### Verificação de Subconjunto e Superset:
# - issubset(): Verifica se todos os elementos de um set estão em outro set.

#    set1 = {1, 2}
#    set2 = {1, 2, 3}
#    print(set1.issubset(set2))  # Saída: True


# - issuperset(): Verifica se todos os elementos de um set estão em outro set.

#    set1 = {1, 2, 3}
#    set2 = {1, 2}
#    print(set1.issuperset(set2))  # Saída: True
