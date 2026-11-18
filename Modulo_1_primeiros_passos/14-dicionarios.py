# coleção não ordenada de pares chaves e valores
# dicionario = objeto
# dicionarios dentro de um outro dicionario
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo", "isDev": True}

print("meu dicionario de exemplo:", pessoa)
#   meu dicionario de exemplo: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'isDev': True}

# acessar valores pela chave
print("Nome:", pessoa["nome"])
#   Nome: João
# python mostra de antemão os valores que podem ser colocados aqui

print("Idade:", pessoa["idade"])
#   Idade: 30


# print("Sobrenome:", pessoa[sobrenome])
#   NameError: name 'sobrenome' is not defined

# atribuir valores ao dicionário
pessoa["Sobrenome"] = "Silva"
print("Sobrenome:", pessoa["Sobrenome"])
#   Sobrenome: Silva