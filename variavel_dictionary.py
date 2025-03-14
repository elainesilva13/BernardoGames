import json
from unidecode import unidecode

print("Relembrando tipos de variáveis\n\n")
print("A função type retorna o tipo de uma variável\n")

# Variável tipo dicionário:
dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(type(dicionario))  # <class 'dict'>

print("Um dicionário armazena pares de chave e valor.")
print("Exemplo de dicionário:", dicionario)

# Acessando valores por chave
print(f"Nome: {dicionario['nome']}")
print(f"Idade: {dicionario['idade']}")
print(f"Cidade: {dicionario['cidade']}")

# Adicionando novos pares chave-valor
dicionario["cor_favorita"] = "Azul"
print("Após adicionar a cor favorita:", dicionario)

# Modificando um valor
dicionario["idade"] = 31
print("Após modificar a idade:", dicionario)

# Removendo um item
del dicionario["cidade"]
print("Após remover a chave 'cidade':", dicionario)

# Verificando se uma chave existe
existe_nome = "nome" in dicionario
existe_profissao = "profissao" in dicionario
print(f"A chave 'nome' existe? {existe_nome}")
print(f"A chave 'profissao' existe? {existe_profissao}")

# Usando o método get() para acessar valores
cor = dicionario.get("cor_favorita", "Não informada")
print(f"A cor favorita é: {cor}")

# Método keys() retorna todas as chaves
print("Chaves do dicionário:", dicionario.keys())

# Método values() retorna todos os valores
print("Valores do dicionário:", dicionario.values())

# Método items() retorna todos os pares chave-valor
print("Itens (pares chave-valor) do dicionário:", dicionario.items())

# Exemplo de dicionário com múltiplos tipos de valores
dicionario_complexo = {
    "nome": "Maria",
    "enderecos": ["Rua A", "Rua B"],
    "detalhes": {"altura": 1.65, "peso": 55},
    "ativo": True
}
print("Dicionário complexo:", dicionario_complexo)

# Acessando valores em um dicionário complexo
print(f"Endereços de Maria: {dicionario_complexo['enderecos']}")
print(f"Detalhes de Maria: {dicionario_complexo['detalhes']}")
print(f"Altura de Maria: {dicionario_complexo['detalhes']['altura']}")

# Convertendo um dicionário para uma lista de tuplas
lista_dicionario = list(dicionario_complexo.items())
print("Lista de tuplas:", lista_dicionario)

# Usando a função update() para atualizar ou adicionar vários pares de chave-valor
dicionario.update({"cor_favorita": "Verde", "ano_nascimento": 1994})
print("Após usar update:", dicionario)

# Exemplo de dicionário com valores do tipo lista
dicionario_lista = {
    "alunos": ["Lucas", "Ana", "Paulo"],
    "notas": [8.5, 9.0, 7.5]
}
print("Dicionário com listas:", dicionario_lista)
print(f"Notas dos alunos: {dicionario_lista['notas']}")

# Iterando sobre as chaves e valores de um dicionário
print("Iterando sobre o dicionário:")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# Removendo todos os itens de um dicionário
dicionario.clear()
print("Após limpar o dicionário:", dicionario)

# Exemplos de outras operações

# Copiando um dicionário com o método copy()
dicionario_copia = dicionario.copy()
print("Dicionário copiado:", dicionario_copia)

# Usando o método pop() para remover e retornar o valor de uma chave
valor_removido = dicionario_lista.pop("notas", "Chave não encontrada")
print("Valor removido:", valor_removido)
print("Dicionário após o pop:", dicionario_lista)

# Usando o método popitem() para remover e retornar o último par chave-valor
ultimo_item = dicionario_lista.popitem()
print("Último item removido:", ultimo_item)
print("Dicionário após o popitem:", dicionario_lista)

# Atualizando um dicionário com outro dicionário
dicionario_lista.update({"notas": [7.0, 8.5, 9.0]})
print("Dicionário atualizado:", dicionario_lista)

# Ordenando um dicionário por suas chaves
dicionario_ordenado = dict(sorted(dicionario_lista.items()))
print("Dicionário ordenado por chaves:", dicionario_ordenado)

# Convertendo um dicionário para JSON (em formato de string)
dicionario_json = json.dumps(dicionario_lista)
print("Dicionário convertido para JSON:", dicionario_json)

# Convertendo JSON para dicionário
dicionario_de_json = json.loads(dicionario_json)
print("JSON convertido de volta para dicionário:", dicionario_de_json)

# Função lambda com dicionário (para ordenar pelo valor)
dicionario_ordenado_por_valor = dict(
    sorted(dicionario_lista.items(), key=lambda item: item[1]))
print("Dicionário ordenado por valor:", dicionario_ordenado_por_valor)

# Usando unidecode para remover acentos de chaves ou valores
nome_com_acentos = "João"
nome_sem_acentos = unidecode(nome_com_acentos)
print("Nome com acento:", nome_com_acentos)
print("Nome sem acento:", nome_sem_acentos)

# Usando o método setdefault() para obter um valor ou definir um padrão
descricao = dicionario.get("descricao", "Sem descrição")
print("Descrição:", descricao)
dicionario.setdefault("descricao", "Sem descrição")
print("Após setdefault:", dicionario)

# Compreensão de dicionário (dict comprehension)
dicionario_compreensao = {x: x**2 for x in range(5)}
print("Compreensão de dicionário:", dicionario_compreensao)
