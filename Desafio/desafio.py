"""
Desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito. O resultado da aplicação deve ser apresentado no terminal, assim como foi visto no módulo "Introdução ao Python".

 -Mostrar uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
 -Implementar funcionalidade para adicionar um contato (Nome, Telefone, Email, Favorito) -Desenvolver visualização da lista de contatos cadastrados 
-Criar funcionalidade para editar um contato existente 
-Desenvolver visualização da lista de contatos favoritos
 -Criar funcionalidade para apagar um contato "
"""
contatos = []
# 1.
def adicionar_contato(contatos, nome_contato, email_contato, telefone_contato):
    contato = {"contato": nome_contato, "e-mail": email_contato, "telefone": telefone_contato, "favorito": False}
    contatos.append(contato)
    return

# 2.
def ver_contatos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        nome_contato = contato["contato"]
        print(f"{indice}. Nome: {nome_contato}, Telefone: {telefone_contato}, E-mail: {email_contato}")
    return



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
        print("====== Contatos Salvos ======")
        if  not contatos:
            print("\nNenhum contato na agenda! Tente adicionar digitando 1.")
        else:
            ver_contatos(contatos)
    elif escolha == "2":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone: ")
        email_contato = input("Agora o email: ")
        adicionar_contato(contatos, nome_contato, email_contato, telefone_contato)
        print(f"\n O contato de {nome_contato} foi adicionado com sucesso!")
    elif escolha == "7":
        break

print("Programa finalizado")