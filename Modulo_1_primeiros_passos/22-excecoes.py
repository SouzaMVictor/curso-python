# # tratamento de exceções
print("======exemplo de captura de exceções=====")


# ================ EXCEÇÃO 1 ================
#  # ===respostas numéricas que vem do input são string, portanto necessário converter para inteiro === #

# # numero = input("Digite um número inteiro")
#     # TypeError: unsupported operand type(s) for /: 'int' and 'str'
# numero = int(input("Digite um número inteiro"))
# resultado = 10/numero
# print(resultado)

# ================ EXCEÇÃO 2 ================
# try e except
# try:
#     # colocar código que pode dar problema aqui
#     numero = int(input("Digite um número inteiro: "))
#     resultado = 10/numero
#     print(f"resultado:  {resultado}")
# except ValueError as e:
#     print(f"erro de value error: {e}")
# except Exception as e:
#     # dentro da exceção coloca-se o resultado para erros, nesse caso
#     # exception é a exceção do codigo
#     # "e" é a variavel para o erro
#     print(f"erro: {e}")
#     #    erro: invalid literal for int() with base 10: 'a'
# # dessa forma o programa quebra ao fazer errado, mas se colocar no while true ele vai normal até acertar


# é possível também para o codigo propositalmente com o raise dentro do except
try:
    # colocar código que pode dar problema aqui
    numero = int(input("Digite um número inteiro: "))
    resultado = 10/numero
except ValueError as e:
    print(f"erro de value error: {e}")
    raise ValueError("tipo de variável incompatível")
        # Traceback (most recent call last):
    """File "/home/victormsouza/victor/curso-python/Modulo_1_primeiros_passos/22-excecoes.py", line 40, in <module>
    raise ValueError("tipo de variável incompatível")
ValueError: tipo de variável incompatível"""
except Exception as e:
    # dentro da exceção coloca-se o resultado para erros, nesse caso
    # exception é a exceção do codigo
    # "e" é a variavel para o erro
    print(f"erro: {e}")
    #    erro: invalid literal for int() with base 10: 'a'
# dessa forma o programa quebra ao fazer errado, mas se colocar no while true ele vai normal até acertar
else:
    # se nao cair no except, vai fazer isso 
    print(f"resultado {resultado}")
finally:
    print("operação finalizada")
    # independente do que acontecer no except, vai fazer isso
    """
        Digite um número inteiro: 2
        resultado 5.0
        operação finalizada
    """
