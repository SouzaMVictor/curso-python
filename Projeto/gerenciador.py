tarefas = []

def adicionar_tarefa(tarefas, nome_tarefa="tarefa padrão"):
    # tarefa: nome da tarefa
    # completada: indicar se foi completada ou não
    # usar um dicionário para nome e o status
    tarefa = {"tarefa": nome_tarefa, "completada": False}

    # na lista "tarefas", adicionar a tarefa
    tarefas.append(tarefa)

    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    # unico parametro é a lista de tarefas(lista)
    for indice, tarefa in enumerate(tarefas, start=1):
        # usado para enumerar a lista a partir do 1 e não do 0 (user friendly)
        status = "✓" if tarefa["completada"] else "X"
        # caracteres que vao ser usados de acordo com o status da tarefa
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. {nome_tarefa} [{status}] ")
    return

def atualizar_nome_tarefa(tarefas,indice_tarefa, novo_nome_tarefa):
    # parametros: tarefas é a lista das tarefas, indice é o numero e novo_nome_tarefa é o que vai substituir o antigo
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    # transformar indice 
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        # verificar tamanho da lista de tarefas
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        # busca o novo indice das tarefas e adiciona o novo nome
        print(f"\nTarefa {indice_tarefa}: '{nome_tarefa}' atualizada para '{novo_nome_tarefa}'")
    else:
        print("\nÍndice fora do intervalo...")
    return

def atualizar_status_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada")
    return

def excluir_tarefa(tarefas):
    for tarefa in tarefas:
        # necessario iterar sobre as tarefas para encontrar qual vai excluir
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas.")
    return
    

while True:
    print("\nMenu do gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefas")
    print("2. Ver tarefas")
    print("3. Atualizar tarefas")
    print("4. Completar tarefas")
    print("5. Deletar tarefas completas")
    print("6. Sair")

    escolha = input("\nDigite a sua escolha: ")
    if escolha == "1":
        nome_tarefa = input("\nDigite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
       print("==== Lista de Tarefas: =====")
       ver_tarefas(tarefas)
    elif escolha == "3":
       ver_tarefas(tarefas)
       indice_tarefa = input("Digite o número da tarefa a ser atualizada: ")
       novo_nome = input("Digite o novo nome da tarefa a ser atualizada: ")
       atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que quer completar: ")
        atualizar_status_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        ver_tarefas(tarefas)
        excluir_tarefa(tarefas)
    elif escolha == "6":
        break
print("Programa finalizado")