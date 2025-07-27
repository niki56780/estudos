
def is_palindro(string):
    verif = False

    string2 = string[::-1]

    if string == string2:
        verif = True

    return verif

verificar = input("Digite uma palavra ou frase: ")
if is_palindro(verificar):
    print("a palavra", verificar, "é um palíndromo.")
else:
    print("a palavra ",verificar,"não é um palíndromo.")