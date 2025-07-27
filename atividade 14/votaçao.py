Resultado = {}

def votacao():
    print("vote em um dos tres: \n 1-lula \n 2-bolsonaro \n 3-ciro")
    deputado = input("digite o numero do seu candidato: ")
    if deputado == "1":
        Resultado["lula"] = Resultado.get("lula", 0) + 1
    elif deputado == "2":
        Resultado["bolsonaro"] = Resultado.get("bolsonaro", 0) + 1
    elif deputado == "3":   
        Resultado["ciro"] = Resultado.get("ciro", 0) + 1
    else:
        print("voto nulo")
        Resultado["nulo"] = Resultado.get("nulo", 0) + 1    
    continuar = input("deseja continuar votando? (s/n): ")
    if continuar.lower() == 's':
        votacao()
    else:
        print("resultado final da votacao: ")
        for candidato, votos in Resultado.items():
            print(candidato,":",votos, "votos")
votacao()
   