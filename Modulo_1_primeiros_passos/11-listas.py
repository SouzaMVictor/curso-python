# lista = arrays
# coleção de elementos ordenaveis e mutaveis
# pode conter vários elementos

minha_lista = [1,2,3,4,5]
# numerica
minha_lista2 = ["victor", "souza", "matias"]
# string
minha_lista3 = ["python",2,3, "javascript", "html", True]
# strings, numeros e booleanos
# pode ter até outras listas

# todos tem um indice que começa do 0

print("Minha lista de exemplo", minha_lista)
#   Minha lista de exemplo [1, 2, 3, 4, 5]


# exibição dos elementos
# usado para acessar elementos de forma individual
print("minha lista na posição[0]:", minha_lista[0])
#   minha lista na posição[0]: 
print("minha lista 3 na posição[3]:", minha_lista3[3])
#   minha lista 3 na posição[3]: javascript

# fatiamento dos elementos da lista
# slice
print(minha_lista3[0:5])
# quero do começo até 'html'
#    ['python', 2, 3, 'javascript', 'html']
# necessário colocar um a mais para fatiar até ele
# html é na posição 4 então é 5 na lista fatiada

# fatiar do começo até o alvo
print(minha_lista3[:5])
#   ['python', 2, 3, 'javascript', 'html']
# geralmente nao poe o 0

# fatiar de um alvo até o final
print(minha_lista3[2:])
#   [3, 'javascript', 'html', True]