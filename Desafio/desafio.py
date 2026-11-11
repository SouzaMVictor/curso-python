"""
Agenda de contatos: adicionar, listar, editar, apagar e favoritar.
"""
contatos = []


def adicionar_contato(contatos, nome_contato, email_contato, telefone_contato):
    contato = {"contato": nome_contato, "e-mail": email_contato, "telefone": telefone_contato, "favorito": False}
    contatos.append(contato)


def ver_contatos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else "☆"
        print(f"{indice}. Nome: {contato['contato']}, Telefone: {contato['telefone']}, E-mail: {contato['e-mail']} {status}")


def pedir_indice(contatos, mensagem):
    """Pede um número ao usuário e devolve o índice (base 0) válido, ou None."""
    try:
        indice = int(input(mensagem)) - 1
    except ValueError:
        print("Digite um número válido.")
        return None
    if not 0 <= indice < len(contatos):
        print("Contato não encontrado.")
        return None
    return indice


def adicionar_contato_favoritos(contatos, indice):
    contatos[indice]["favorito"] = True
    print(f"Contato '{contatos[indice]['contato']}' adicionado aos favoritos!")


def ver_contatos_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(f"{indice}. Nome: {contato['contato']}, Telefone: {contato['telefone']}, E-mail: {contato['e-mail']} ★")


def editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email):
    contato = contatos[indice]
    # Enter vazio mantém o valor atual
    if novo_nome:
        contato["contato"] = novo_nome
    if novo_telefone:
        contato["telefone"] = novo_telefone
    if novo_email:
        contato["e-mail"] = novo_email


def apagar_contato(contatos, indice):
    removido = contatos.pop(indice)
    print(f"Contato '{removido['contato']}' apagado com sucesso!")


while True:
    print("\n====== Agenda de Contatos ======")
    print("\n1. Adicionar contato")
    print("2. Ver todos os contatos")
    print("3. Apagar contato")
    print("4. Adicionar contato aos favoritos")
    print("5. Editar contato")
    print("6. Ver contatos favoritos")
    print("7. Fechar lista de contatos")

    escolha = input("\nDigite o número da sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone: ")
        email_contato = input("Agora o email: ")
        adicionar_contato(contatos, nome_contato, email_contato, telefone_contato)
        print(f"\nO contato '{nome_contato}' foi adicionado com sucesso!")

    elif escolha == "2":
        print("====== Contatos Salvos ======")
        if not contatos:
            print("\nNenhum contato na agenda! Tente adicionar digitando 1.")
        else:
            ver_contatos(contatos)

    elif escolha == "3":
        if not contatos:
            print("\nNenhum contato na agenda! Tente adicionar digitando 1.")
        else:
            ver_contatos(contatos)
            indice = pedir_indice(contatos, "Digite o número do contato que deseja apagar: ")
            if indice is not None:
                apagar_contato(contatos, indice)

    elif escolha == "4":
        if not contatos:
            print("\nNenhum contato na agenda! Tente adicionar digitando 1.")
        else:
            ver_contatos(contatos)
            indice = pedir_indice(contatos, "Digite o número do contato que deseja adicionar aos favoritos: ")
            if indice is not None:
                adicionar_contato_favoritos(contatos, indice)

    elif escolha == "5":
        if not contatos:
            print("\nNenhum contato na agenda! Tente adicionar digitando 1.")
        else:
            ver_contatos(contatos)
            indice = pedir_indice(contatos, "Digite o número do contato que deseja editar: ")
            if indice is not None:
                print("(Pressione Enter para manter o valor atual)")
                novo_nome = input("Novo nome: ")
                novo_telefone = input("Novo telefone: ")
                novo_email = input("Novo e-mail: ")
                editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email)
                print("Contato editado com sucesso!")

    elif escolha == "6":
        if any(contato["favorito"] for contato in contatos):
            print("====== Contatos Favoritos ======")
            ver_contatos_favoritos(contatos)
        else:
            print("Nenhum contato marcado como favorito...")

    elif escolha == "7":
        print("Programa finalizado")
        break

    else:
        print("Opção inválida. Digite um número de 1 a 7.")