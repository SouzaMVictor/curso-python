pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo", "isDev": True}
pessoa["Sobrenome"] = "Silva"
print(pessoa)
#    {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'isDev': True, 'Sobrenome': 'Silva'}

# atualizar valores já existentes dentro do dicionário
pessoa["idade"] = 31
print(pessoa)
#    {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo', 'isDev': True, 'Sobrenome': 'Silva'}

# remover par chave e valor
del pessoa["Sobrenome"]
print(pessoa)
#   {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo', 'isDev': True}


# metodos

# metodo keys()
# retorna uma lista de todas as chaves presentes no dicionario
chaves = pessoa.keys()
# print("chaves do dicionario", chaves)
#   chaves do dicionario dict_keys(['nome', 'idade', 'cidade', 'isDev'])
# por ser uma lista, é possível utilizar os métodos das listas

# print(chaves[0])
#   TypeError: 'dict_keys' object is not subscriptable
# necessidade de transformar em uma lista em si
chaves = list(pessoa.keys())
print(chaves[0])
#   nome


# value()
# retorno dos valores dos dicionarios
# valores = pessoa.values()
# valores = pessoa.values()
# print(valores)
#   dict_values(['João', 31, 'São Paulo', True])

# acessar valor especifico do dicionario
valores = list(pessoa.values())
print("segundo valor da lista:",valores[1])
#   segundo valor da lista: 31


# método items()
# retorna uma lista onde cada elemento é uma tupla com a chave e o valor
# itens = pessoa.items()
# print("pares chave-valor da lista", itens)
#   pares chave-valor da lista dict_items([('nome', 'João'), ('idade', 31), ('cidade', 'São Paulo'), ('isDev', True)])

# acessar chaves e valores especificos
itens = list(pessoa.items())
print(itens[0][1])
# o [0] vai acessar ao primeiro par chave-valor, então "nome" e "João" 
# o [1] vai acessar o valor da chave, entãõ "João"
    # João

print("primeira chave-valor:%s = %s" % (itens[0][0], itens[0][1]))
#   primeira chave-valor:nome = João

# com string formatada
print(f"primeira chave-valor: {itens[0][0]} = {itens[0][1]}")
#   primeira chave-valor: nome = João