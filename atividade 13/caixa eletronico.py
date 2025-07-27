#um caixa eletronico???????
def operacao():
    print("este é seu caixa eletronico virtual voce tem as seguintes opcoes: \n 1- depositar \n 2- sacar ")
    escolha= input("digite sua escolha:")
    if escolha =="1":
        deposito =float(input("digite quanto deseja depositar:"))
        print("voce depositou: ",deposito)
    elif escolha =="2":
        sacar = float(input("digite quanto deseja sacar: "))
        print("voce sacou:",sacar)
operacao()