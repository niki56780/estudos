def senha():
    verificar = input("digite uma senha:")
    comfirma = input("digite novamente sua senha: ")
    if verificar == comfirma:
        print("sua senha esta correta, bem vindo")
    elif verificar != comfirma:
        print("apartir de agora voce tera 3 chances ou seja bloqueado")
        tentativa1 =input("digite sua senha novamente: ")

        if tentativa1 == verificar:
            print("sua senha esta correta, bem vindo")
        elif tentativa1 != verificar:
           print("sua senha esta errada, voce tem mais 2 chances")
           tentativa2 = input("digite sua senha novamente: ")  

           if tentativa2 == verificar:
              print("sua senha esta correta, bem vindo")
           elif tentativa2 != verificar:
              print("sua senha esta errada, voce tem mais 1 chance")
              tentativa3 = input("digite sua senha novamente: ")

              if tentativa3 == verificar:
                 print("sua senha esta correta, bem vindo")
              elif tentativa3 != verificar:
                 print("tentativas esgotadas e conta bloqueada")
senha()
    