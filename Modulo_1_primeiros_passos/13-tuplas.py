# coleção ordenada e imutável de elementos

# criando uma tupla de exemplo
minha_tupla = (1,2,3,4,5,6)
print(minha_tupla)
# (1, 2, 3, 4, 5, 6)

# acessar elementos
print(minha_tupla[0])
#   1
print(minha_tupla[2])
#   3
print(minha_tupla[4])
#   5
print(minha_tupla[-1])
#   6

# por ser imutavel, não tem como alterar itens da tupla!
    # varios metodos perdidos


# método count()
# quantas vezes um elemento aparece na tupla
tupla_count = (1,2,3,4,3,3,35,5,67,8)
contagem = tupla_count.count(3)
print("quantiadade de vezes que aparece o elemento 3:", contagem)
#   quantiadade de vezes que aparece o elemento 3: 3


# metodo index()
# primeira ocorrencia do indice 3
indice = tupla_count.index(3)
print("primeira ocorrencia do elemento 3:", indice)
#   primeira ocorrencia do elemento 3: 2