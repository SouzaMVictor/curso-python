# bloco de codigo reutilizável
# executa uma tarefa especifica quando chamado
# iniciar com def
# variaveis que a função recebe = PARAMETROS
def saudacao(nome):
    print(f"olá, {nome}!")

print("\nchamar função saudação: ")
saudacao("victor")
saudacao("lê")

# função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado


print("\nchamar função quadrado: ")
print(quadrado(2))


# função com multiplos parametros

def area_do_retangulo(lado_maior,lado_menor):
    area = lado_maior * lado_menor
    return area

print("\nchamar função area do retangulo: ")
print(area_do_retangulo(4,5), "metros quadrados")