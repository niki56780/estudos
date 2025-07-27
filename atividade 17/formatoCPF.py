import re
def cpf():
    cpf = input("digite seu cpf: ")
    padrao = r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$'

    if re.match(padrao, cpf):
        print("cpf valido")
    else:
        print("cpf invalido, digite no formato xxx.xxx.xxx-xx")
cpf()