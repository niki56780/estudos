def contatos():
    dicionario = {}
    while True:
        nome = str(input("digite o nome do contato: "))
        telefone = str(input("digite o telefone do contato: "))
        dicionario[nome] = telefone
        continuar = input("deseja adicionar outro contato? s/n: ")
        if continuar.lower() != 's':
            break

    buscar_nome= str(input("digite o nome do contato que deseja buscar "))
    if buscar_nome in dicionario:
        print("o ",buscar_nome,"esta na lista de contatos existente e seu numero é ",telefone)
    else:
        print("nao foi encontrado tal contato na agenda")
contatos()
