def contaLetras(texto):
    texto = texto.strip()
    letra = [char for char in texto if char.isalpha()]
    return len(letra)  


frase = input("Digite uma frase: ").strip()
letra = [char for char in frase if char.isalpha()]
print(f"Número de letras na frase: {len(letra)}")
    