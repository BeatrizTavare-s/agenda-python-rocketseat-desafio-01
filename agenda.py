def adicionar_contato(lista_contatos, novo_contato):
    lista_contatos.append(novo_contato)
    return

def ver_contatos(contatos):
    print("\n Lista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "❤" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        print(f"{indice}. {status}  {nome_contato}")

def atualizar_contato(contatos, indice, contato_editado):
    indice_contato_ajudastado = indice - 1
    if indice_contato_ajudastado >= 0 and indice_contato_ajudastado < len(contatos):
        contatos[indice_contato_ajudastado] = contato_editado;
    else:
        print("Índice contato inválido")
    return

def marcar_contato_favorito(contatos, indice):
    indice_contato_ajudastado = indice - 1
    contatos[indice_contato_ajudastado]["favorito"] = True;
    return

def desmarcar_contato_favorito(contatos, indice):
    indice_contato_ajudastado = indice - 1
    contatos[indice_contato_ajudastado]["favorito"] = False;
    return

def ver_contatos_favoritos(contatos):
    print("\n Lista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if(contato["favorito"]):
            status = "❤" if contato["favorito"] else " "
            nome_contato = contato["nome"]
            print(f"{indice}. {status}  {nome_contato}")
    return

def deletar_contatos(contatos, indice):
    indice_contato_ajudastado = indice - 1
    contatos.pop(indice_contato_ajudastado)
    return

contatos = []

while True:
    print("\n Menu da Agenda")
    print("1. Salvar contato")
    print("2. Editar contato")
    print("3. Deletar contato")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar contato como favorito")
    print("6. Listar contatos")
    print("7. Listar contatos favoritos")
    print("8. Sair")


    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(contatos, {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "favorito": False
        })
        ver_contatos(contatos)

    elif opcao == 2:
        ver_contatos(contatos)
        index_contato_para_editar = int(input("Qual o número do contato para edição: "))
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        favorito = input("Marcar como favorito? S/N: ")
        atualizar_contato(contatos, index_contato_para_editar, {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "favorito": favorito,
        })
        ver_contatos(contatos)

    elif opcao == 3:
        index_contato_para_deletar = int(input("Qual o contato para deletar: "))
        deletar_contatos(contatos, index_contato_para_deletar)
        ver_contatos(contatos)

    elif opcao == 4:
        index_contato_para_favoritar = int(input("Qual o contato para marca como favorito: "))
        marcar_contato_favorito(contatos, index_contato_para_favoritar)
        ver_contatos(contatos)

    elif opcao == 5:
        index_contato_para_favoritar = int(input("Qual o contato para marca como favorito: "))
        desmarcar_contato_favorito(contatos, index_contato_para_favoritar)
        ver_contatos(contatos)

    elif opcao == 6:
        ver_contatos(contatos)

    elif opcao == 7:
        ver_contatos_favoritos(contatos)

    elif opcao == 8:
        break
