# operações aritméticas
# soma, subtração, multiplicação, divisão, módulo

# soma
# +
soma  = 1 + 1
print("1 + 1 = ", soma)
# 1 + 1 =  2

# subtração
# -
subtracao = 2 - 1
print("2 - 1 = ", subtracao)
# 2 - 1 =  1

# multiplicação
# *
multiplicacao = 2 * 2
print("2 * 2 = ", multiplicacao)
# 2 * 2 =  4

# divisão
# /
divisao = 5/2
divisao2 = 4/2
print("5/2 = ", divisao)
# 5/2 =  2.5
# a divisão vai gerar um float, SEMPRE. independente se for um número inteiro.
print("4/2 = ", divisao2)
# 4/2 =  2.0
print(type(divisao2))
# <class 'float'>


# como converter tipos de números?
# função int() para converterem inteiros
print("usando int para arredondar o resultado da divisao: ", int(divisao))
# usando int para arredondar o resultado da divisao:  2

print(type(int(divisao)))
# <class 'int'>

# função float() para converter em real com ponto flutuante
print("valor em float da divisão exata:", float(divisao2))
# valor em float da divisão exata: 2.0

# módulo
# %
# mostra o restante da divisão
modulo = 5 % 2
print(modulo)
# 1
# 2 cabe 2 vezes dentro de 5.
# 2 × 2 = 4.
# 5 − 4 = 1.

# divisão inteira
# //
# não mostra o resto da divisão 
divisao_inteira = 5//2
print(divisao_inteira)
# 2
print(type(divisao_inteira))
# <class 'int'>