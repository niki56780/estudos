def binario():
    numero=float(input("digite um numero decimal pra saber como ele fica como binario: "))
    if numero == 0:
        print("o numero binario é 0")
    else:
        binario = ""
        
        while numero > 0:
            resto = int(numero % 2)
            binario = str(resto) + binario
            numero = int(numero // 2)
        print("o numero binario é", binario)
binario()