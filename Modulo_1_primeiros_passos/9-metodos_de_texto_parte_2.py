# método count()
# conta ocorrencias na string
# nome_completo = "victor souza"
# nome_completo.count("o")
#   2


# método find()
# encontra a posição da ocorrência
#  nome_completo.find("o")
#   4
# strings grandes ->  encontrar  onde aparece
# sempre começa do 0


# método encode()
# codifica a string em bytes
# nome.encode()
#   b'victor'

# metodo decode()
# decodifica os bytes
# necessário uma string já codificada
# nome.encode().decode()
#   'victor'


# metodo replace()
# substitui uma ocorrencia por outra
# nome_completo.replace("o", "a")
#   'victar sauza'
#  muito usado para tratamento de dados, como mudança de caracteres especiais num telefone, por exemplo
# podem ser usados multiplos replaces numa mesma string
# telefone = "(14)99620-2576"
# telefone.replace("(", "").replace(")","").replace("-","")
# '14996202576'
# se nao tiver a ocorrencia nada acontece


# método join()
# usado para combinar todos elementos de uma lista ou tupla numa unica string
# palavras = ["Python", "é", "muito", "legal"]
# frase = " ".join(palavras)
# print(frase)
#   Python é muito legal
# também pode ser usado como "separador" de elementos na string
# "-".join(nome)
#   'v-i-c-t-o-r'


# me´todo split()
# conversao de strings em listas com base num caracter alvo especifico
# nome_completo.split(" ")
#    ['victor', 'souza']
# nome_completo.split("o")
#   ['vict', 'r s', 'uza']

# método strip()
# trtamento de textos com ruidos
# retira o que tem no começo e no final
#  nome_com_ruido.strip("x")
#   'Victor Souza'

# metodo rstrip()
# substitui apenas o ruido a direita

# metodo lstrip()
# substitui apenas o ruido a esquerda


# método startswith()
# retorna um booleano com o resultado da pesquisa da string
# se começa com
# nome_completo.startswith("Vi")
#   False
#       pq começa com 'vi' e não 'Vi'  
# case sensitive!!!
# pode ser só True ou False

# comparadores

# comparador in
# compara se há uma certa ocorrencia na string
# "vic" in nome_completo
#   True

# comparador not in
# se não há uma certa ocorrencia na string
# "vica" not in nome_completo
#   True