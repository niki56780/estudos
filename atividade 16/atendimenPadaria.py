def atendimento():
    nome = input("qual seu nome: ")
    print(f"Ola, {nome} Como posso ajudar você hoje?")
    print("temos essas opcoes: \n 1-salgados \n 2- bolos ")
    escolha = input("digite sua escolha: ")

    if escolha == "1":
        print("temos \n 1-coxinha \n2-pastel")
        salgado=input("digite sua escolha:")

        if salgado == "1":
             print("voce escolheu coxinha o valor dela é 10 reais")
  
             quantas = int(input("quantas voce quer?"))
             dindin = quantas * 10

             print("o valor ficou entao de",dindin," reais")
             entrega = (input("deseja que seja feita a entrega? s/n:"))

             if entrega == "s".lower():
                print("a entrega sera feita em 30 min")
             elif entrega == "n".lower():
                print("ok, voce pode vir buscar em 20 min")
             else:
                print("opçao invalida")
        elif salgado == "2":
             print("voce escolheu pastel o valor dele é 8 reais")
             quantas = int(input("quantas voce quer?"))
             dindin= quantas * 8
             print("o valor ficou entao de",dindin," reais")
             entrega = (input("deseja que seja feita a entrega? s/n:"))

             if entrega == "s".lower():
                print("a entrega sera feita em 30 min")
             elif entrega == "n".lower():
                print("ok, voce pode vir buscar em 20 min")
             else:
                print("opçao invalida")
        else:
            print("opçao invalida")
    elif escolha == "2":
        print("voce  escolheu bolos temos: \n 1- brigadeiro \n 2- cenoura")
        bolo = input("digite sua escolha: ")
        if bolo == "1":
            print("voce escolheu bolo de brigadeiro o valor dele é 50 reais")
            quantas = int(input("quantos voce quer?"))
            dindin= quantas * 50
            print("o valor ficou entao de ",dindin," reais")
            entrega = str(input("deseja que seja feita a entrega? s/n:"))

            if entrega == "s".lower():
              print("a entrega sera feita em 30 min")
            elif entrega == "n".lower():
             print("ok, voce pode vir buscar em 20 min")
            else:
              print("opçao invalida")  

        elif bolo == "2":
            print("voce escolheu bolo de cenoura o valor dele é 60 reais")
            quantas = int(input("quantos voce quer?"))
            dindin= quantas * 60
            print("o valor ficou entao de ",dindin," reais")
            entrega = (input("deseja que seja feita a entrega? s/n:"))

            if entrega == "s".lower():
              print("a entrega sera feita em 30 min")
            elif entrega == "n".lower():
             print("ok, voce pode vir buscar em 20 min")
            else:
              print("opçao invalida")
    else:
        print("opçao invalida") 

    print("atendimento finalizado")   

def novo_cliente(): 
   clientes=input("novo cliente? s/n: ")
   if clientes == "s".lower():
      atendimento()
   else:
     print("obrigado pela preferencia")

atendimento()
novo_cliente()

    