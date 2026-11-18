# módulos são arquivos que contem definições e instruções que podem ser utilizadas por outros programas

# ====== módulos padrão ======
print("exemplo de importação de módulo padrão: ")

# importar módulo todo
# tem diversos métodos ao fazer math.
import math

raiz_quadrada = math.sqrt(25)

print(raiz_quadrada)


# as vezes nao precisa importar tudo
# importa apenas o método que eu quero
from math import sqrt

raiz_quadrada_2 = math.sqrt(169)
print(raiz_quadrada_2)

# ====== módulos personalizado ======
print("exemplo de importação de módulo personalizado: ")

# criei outro arquivo para demonstrar
    # 23.1
import meu_modulo

mensagem = meu_modulo.saudacao("victor")
dobrado = meu_modulo.dobro(10)

print(mensagem)
print(dobrado)

# também é possível pegar os métodos especificos

# from meu_modulo import saudacao, dobro
# from meu_modulo import dobro

# bibliotecas nativas do python
# https://docs.python.org/pt-br/3/library/index.html

# pesquisar por
# python library (assunto) exemples