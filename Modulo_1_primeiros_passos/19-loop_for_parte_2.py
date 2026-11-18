lista = [20,210,54,56,67,9874]
# elemento = o que está dentro da posição

for indice in range(0, len(lista)):
    # indice = posição que o elemento está
        # variável que eu criei para isso
    # range vai do 0 (indicado por mim) até o que eu indicar que é o tamanho
        # o tamanho da lista
    # len() vai pegar apenas o tamanho da lista
    print("indice",indice)
    # printa do 1 ao 5, um em cada linhas
        # já que o indice vai buscar do 0 ao tamanho da lista
    print("elemento", lista[indice])
    # o elemento é buscado dentro da lista a partir do indice
        # elemento é o que está dentro da lista

    if indice == 3:
        lista[indice] = "six seven"
    else:
        lista[indice] = 0
print("======lista att",lista)

# função enumarate()

print("========enumerate======")
lista_enumerate = ["a", "b","c", "d", "e"]
# necessário passar dois parametros nesse caso
for indice, elemento in enumerate(lista_enumerate):
    print(f"{indice}: {elemento}")