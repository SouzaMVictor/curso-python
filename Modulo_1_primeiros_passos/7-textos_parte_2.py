# formatação dos textos
# separação por vírgula depois da string
nome = "victor"
sobrenome = "souza"
nome_completo = "victor souza"
nome_completo_com_aspas = """ victor
souza"""
nome_completo_com_quebra = "victor \
souza"
print("nome completo (1a forma):", nome_completo)
# nome completo (1a forma): victor souza

# separação por +
print("nome completo (2a forma):"+ nome_completo)
# nome completo (2a forma):victor souza
# a soma não põe um espaço de formaa automatica igual a vírgula

# concatenação de strings com +
print("nome completo (3a forma):"+ "victor"+"souza")
# nome completo (3a forma):victorsouza

# concatenação de strings com virgula
print("nome completo (4a forma):"+ "victor","souza")
# nome completo (4a forma):victor souza

# concatenação com aspas
print("nome completo (5a forma):"+ nome_completo_com_aspas)
""" nome completo (4a forma): victor
souza"""

# concatenação com quebra
print("nome completo (6a forma):"+ nome_completo_com_quebra)
# nome completo (5a forma):victor souza

# concantenação usando uma variavel
# %s e depois assume a variavel
# usa a variável dentro da string
print("nome completo (7a forma):%s"%nome_completo)
# nome completo (7a forma):victor souza

# concantenação usando duas variaveis
# se for usar mais de uma variavel, tem que ter o parenteses antes e depois
# mais segura no tratamento de dados
print("nome completo (8a forma):%s %s"%(nome,sobrenome))
# nome completo (8a forma):victor souza

# format
# string formatada
# f antes e depois coloca as variaveis nas chaves
# visivelmente agradavel caso as variaveis sejam bem escritas
print(f"nome completo (9a forma):{nome} {sobrenome}")
# nome completo (9a forma):victor souza


# função format()
# segue a ordem para substituir as chaves
print("nome completo (10a forma):{} {}".format(nome, sobrenome))
# nome completo (10a forma):victor souza