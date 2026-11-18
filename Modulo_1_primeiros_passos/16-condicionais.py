# permitem tomar decisões com base em decisões

# if, elif, else
# se, senão se, senão


# if
idade = 18
# print("exemplo de comando if:")

# if idade >= 18:
#     # maior ou igual
#     print("maior de idade")
# # se for verdadeiro, vai acontecer

# if idade == 19:
#     # exatamente igual
#     print("vc tem 19 anos")

# if idade <= 17:
#     # menor ou igual
#     print("vc é menor de idade")

# if idade != 10:
#     # qualquer valor diferente. não é igual
#     print("vc nao tem 10 anos")



# else
# print("exemplo de comando else:")

# if idade >= 18:
#     print("vc é maior de idade")
# else:
#     print("vc não é maior de idade")


# elif

# print("exemplo de comando elif:")
# if idade <=12:
#     print("vc é criança")
# elif idade >12 & idade <=17:
#     print("vc é adolescente")
# elif idade >= 18:
#     print("vc é adulto")
# else:
#     print("idade nao suportada")


# como construir um condicional em uma linha
mensagem = "pode tirar carteira de habilitação" if idade >=18 else "voce nao pode tirar carteira de habilitação"
print(mensagem)