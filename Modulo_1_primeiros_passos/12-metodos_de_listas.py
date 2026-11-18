# demonstram a mutabilidade das listas
# depois da atribuição de um novo valor, ele passa a ter esse valor.

minha_lista = [1,2,3,4,5]
print(minha_lista)
    # [1, 2, 3, 4, 5]

# alterar elemento da lista em determinada posição
minha_lista[0] = "python"
print(minha_lista)
#   ['python', 2, 3, 4, 5]


# método append()
# adiciona um elemento no final da lista
minha_lista.append(6)
print("após append(6):", minha_lista)
#   após append(6): ['python', 2, 3, 4, 5, 6]

# método index()
# retorna o indice do elemento que eu quero
indice = minha_lista.index(6)
print(indice)
#   5


# método insert()
# insere um elemento em um indice especifico
# primeiro coloca o lugar que vai ser adicionado, depois o que vai ser adicionado
minha_lista.insert(2, 10)
print(minha_lista)
#   ['python', 2, 10, 3, 4, 5, 6]
# 10 assumiu o lugar do 3, sem substitui-lo

# metodo pop()
# remove e retorna o elemento de um indice especifico
elemento_removido = minha_lista.pop(4)
print("elemento removido", elemento_removido)
#   elemento removido 4
print("minha lista pos elemento removido pelo pop(4)", minha_lista)
#   minha lista pos elemento removido pelo pop(4) ['python', 2, 10, 3, 5, 6]


# metodo remove()
# remove elemento com valor especificado
print("======================")
print("minha_lista atual:", minha_lista)
#   minha_lista atual: ['python', 2, 10, 3, 5, 6]
print("======================")
minha_lista.remove(6)
# removo o 6 da lista
print(minha_lista)
#   ['python', 2, 10, 3, 5]


# metodo sort()
# organiza a lista em ordem crescente
lista_desorganizada = [1,4,6,2,5,9]
lista_desorganizada.sort()
print("minha lista organizada: ",lista_desorganizada)
#   minha lista organizada:  [1, 2, 4, 5, 6, 9]