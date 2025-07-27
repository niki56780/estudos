lista = []  
def adicionar(adicionar):
    input1 = float(input("digite o numero que deseja adicionar: ")) 
    lista.append(input1)
    return adicionar

def listar(listar):
    print(lista) 
    return listar

def remover(remover):
    input3 = float(input("digite o numero que deseja remover: "))
    print("esse item foi removido: ",remover)
    lista.remove(input3)
    return remover


def sistema():
    usuario = str(input("escolha uma das operaçpes a seguir: \n 1 - adicionar\n 2 - listar \n 3 - remover \n escolha: "))

    if usuario == "1":
        input1 = float(input("digite o numero que deseja adicionar: ")) 
        lista.append(input1)  
        novamente(novamente)

    elif usuario == "2": 
        print(lista)
        novamente(novamente)

    elif usuario == "3": 
      input3 = float(input("digite o numero que deseja remover: "))
      print("esse item foi removido: ",remover)
      lista.remove(input3)
      novamente(novamente)
    else:
        print("opçao invalida, tente novamente")   
        novamente(novamente)

def novamente(novamente):
    usuario = str(input("deseja fazer outra operaçao? \n 1 - sim \n 2 - nao \n escolha: "))
    if usuario == "1":
        sistema()
    elif usuario == "2":
        print("obrigado por usar o sistema")
    else:
        print("opçao invalida, tente novamente")    
    return novamente 


sistema()