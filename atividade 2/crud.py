usuarios = []

def criar():
    usuario= input("digite seu nome: ")
    usuarios.append(usuario)
    return criar

def listar():
    print(usuarios)
    return listar

def atualizar():
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in usuarios:
        nome_novo = input("Qual nome deseja colocar no lugar? ")
        usuarios[usuarios.index(nome_antigo)] = nome_novo
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")
    return atualizar

def deletar():
    deletar = input("digite quem voce deseja deletar")
    usuarios.remove(deletar)
    print("usuario deletado com sucesso")
    return deletar

criar()
listar()
atualizar()
deletar()