def contatos():
    livraria = {}
    while True:
        autor = str(input("digite o nome do autor: "))
        livro = str(input("digite o telefone do contato: "))
        livraria[autor] = livro
        continuar = input("deseja adicionar outros pra esse autor? s/n: ")
        if continuar.lower() != 'n':
            break
        elif continuar.lower() != 's':
            livraria[autor] = livraria.get(autor, []) + [livro]
            continuar = input("deseja adicionar outro contato? s/n: ")

    buscar_autor= str(input("digite o nome do autor que deseja buscar "))
    if buscar_autor in livraria:
        print("o ",buscar_autor,"foi encontrado na lista com os seguintes livros ",livraria[buscar_autor])
    else:
        print("nao foi encontrado tal contato na agenda")
contatos()
