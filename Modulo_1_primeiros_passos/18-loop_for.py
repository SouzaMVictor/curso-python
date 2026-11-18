# estrutura que permite repetir um bloco de codigo enquanto uma condição for verdadeira
# iterar sobre uma sequencia de elementos
    # lista, tupla, dicionarios

lista = [1,2,3,4,5]
print("=================print usando lista===============")
for elemento in lista:
# elemento é uma variável que foi criada
    print(elemento)
# para cada elemento dentro da lista, printar os elementos
    """
    1
    2
    3
    4
    5
    """
    # pra cada elemento ele esta usando um print diferente

print("=================print usando tupla===============")

tupla = (1,2,3,4,5,6)
for elemento in tupla:
    print(elemento)
"""
1
2
3
4
5
6
"""

print("=================print usando dicionario===============")
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo", "isDev": True}
#  valores, chaves ou chave-valor

print("=====for usando chaves=====")
for chave in pessoa.keys():
    print(chave)
"""
=====for usando chaves=====
nome
idade
cidade
isDev
"""


print("=====for usando valores=====")
for valor in pessoa.values():
    print(valor)
"""
=====for usando valores=====
João
30
São Paulo
True
"""
print("=====for usando chave-valor=====")

for chave, valor in pessoa.items():
    # items retorna uma tupla
    print(f'{chave}: {valor}')

"""
=====for usando chave-valor=====
nome: João
idade: 30
cidade: São Paulo
isDev: True
"""

# loop for junto com a função range()
# range retorna um intervalo numerico numa lista
print(list(range(0,10)))
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for numero in range(0,5):
    print("numero:", numero)
"""
numero: 0
numero: 1
numero: 2
numero: 3
numero: 4
"""

# função length()
    # retorna a quantidade de elementos dentro da lista
print("=========range() com length()===========")
print(len(lista))
for indice in range(0, len(lista)):
    # começando do 0 e vai até o tamanho da lista
    print("indice:",indice)
    # a posição (indice)
    print("elemento", lista[indice] )
    # o que está dentro da lista na posição do indice!!!!
    # importante porque é dinamico.
    # ao inves de printar do 1 ao 5 como deveria, ele vai pegar o valor que está na lista, independente do que for
    # nesso, foram 4 indices
"""
indice: 0
indice: 1
indice: 2
indice: 3
indice: 4
"""