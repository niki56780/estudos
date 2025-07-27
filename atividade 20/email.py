import re
def email():
    email= input("digite seu email: ")
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(padrao, email):
        print("email valido")
    else:
        print("cpf invalido, digite no formato seuemail@gmail.com")
email()