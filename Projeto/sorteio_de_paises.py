import random
import time

lista_de_paises = []
 
def ultimo_pais(intervalo=0.5):
    pais_vencedor =  list(lista_de_paises[0])
    for letra in pais_vencedor:
        time.sleep(intervalo)
        print(letra, end="", flush=True)
    print()


def suspense(texto, pontos=3, intervalo=0.5):
    print(texto, end="", flush=True)
    for _ in range(pontos):
        time.sleep(intervalo)
        print(".", end="", flush=True)
    print()

def adicionar_pais(lista_de_paises, nome_do_pais="pais padrão"):
    lista_de_paises.append(nome_do_pais)
    print(f"\n{nome_do_pais} adicionado à lista!")

def ver_lista_de_paises(lista_de_paises):
    if not lista_de_paises:
        print("A lista está vazia. Adicione países pela opção 1")
        return
    for index, pais in enumerate(lista_de_paises, start=1):
        print(f"{index}. {pais}")

def remover_pais_aleatorio(lista_de_paises):
    if not lista_de_paises:
        print("Não há países para remover! Adicione um país pela opção 1.")
        return
    if len(lista_de_paises) == 1:
        print(f"Já temos um vencedor: {lista_de_paises[0].upper()}!")
        return
    pais_removido = random.choice(lista_de_paises)
    lista_de_paises.remove(pais_removido)
    suspense("Removendo país aleatório")
    print(f"\nO país eliminado foi: {pais_removido.upper()}!")
    time.sleep(1)
    if len(lista_de_paises) >=3:
        print(f"\nLista atualizada:")
        for index,pais in enumerate(lista_de_paises,start=1):
            print(f"{index}. {pais}")
    if len(lista_de_paises) == 2:
        print(f"Restaram dois países! Quem será o vencedor? {lista_de_paises[0]} ou {lista_de_paises[1]}?")
        time.sleep(1)
        remover_pais_aleatorio(lista_de_paises)
        return
    if len(lista_de_paises) == 1:
        time.sleep(1)
        suspense("\nE o destino das próximas férias é", pontos=3, intervalo=0.4)
        # print(f"\n{lista_de_paises[0].upper()}\n")
        ultimo_pais()
        time.sleep(10)
        
print("===== Sorteador de países para as próximas férias =====")
print("\nAdicione os países que deseja visitar nas próximas férias e sorteie até chegar ao último.\nEsse será o país de destino!\n")

while True:
    print("\nEscolha dentre as opções a seguir:")
    print("1. Adicionar países à lista.")
    print("2. Ver lista.")
    print("3. Remover um país aleatório.")
    print("4. Sair")
    print("5. Ultimo")

    escolha = input("\nDigite sua escolha: ")
    if escolha == "1":
        nome_do_pais = input("Digite o nome do país que deseja adicionar: ").strip().capitalize()
        if not nome_do_pais.strip():
            print("Nenhum país adicionado.")
            continue
        adicionar_pais(lista_de_paises, nome_do_pais)
    elif escolha == "2":
        ver_lista_de_paises(lista_de_paises)
    elif escolha == "3":
        remover_pais_aleatorio(lista_de_paises)
    elif escolha == "4":
        break
    elif escolha == "5":
        ultimo_pais()
    else:
        print("\nOpção inválida!")
