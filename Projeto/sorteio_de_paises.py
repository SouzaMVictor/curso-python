import random
import time

def contagem_regressiva(segundos=3):
    for i in range(segundos, 0, -1):
        print(f"\r  {i}...", end="", flush=True)
        time.sleep(1)

def suspense(texto, pontos=3, intervalo=0.5):
    print(texto, end="", flush=True)
    for _ in range(pontos):
        time.sleep(intervalo)
        print(".", end="", flush=True)
    print()


lista_de_paises = []

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
        print(f"\n{lista_de_paises[0].upper()}\n")
        
print("===== Sorteador de países para as próximas férias =====")
print("\nAdicione os países que deseja visitar nas próximas férias e sorteie até chegar ao último.\nEsse será o país de destino!")

while True:
    print("Escolha dentre as opções a seguir:")
    print("1. Adicionar países à lista.")
    print("2. Ver lista.")
    print("3. Remover um país aleatório.")
    print("4. Sair")

    escolha = input("\nDigite sua escolha: ")
    if escolha == "1":
        nome_do_pais = input("Digite o nome do país que deseja adicionar: ").strip()
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
    else:
        print("\nOpção inválida!")
