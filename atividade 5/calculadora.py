def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def dividir(a,b):
    return a / b

def multiplicar(a,b):
    return a * b

def calculadora():
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o seugndo numero: "))
    usuario = str(input("escolha uma das operaçpes a seguir: \n 1 - soma \n 2 - subtraçao \n 3 - divisao \n 4 - multiplicaçao \n escolha: "))

    if usuario == "1":
        print(somar(num1, num2))

    elif usuario == "2": 
        print(subtrair(num1, num2))
        

    elif usuario == "3": 
        print(dividir(num1, num2))

    elif usuario == "4":
        print(multiplicar(num1, num2))
    else:
        print("opçao invalida, tente novamente")    


calculadora()