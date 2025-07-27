primo=int(input("digite um numero: "))
if primo <=1:
    print("não é primo")
else:
    for a in range(2,primo):
        if primo % a == 0:
            print("não é primo")
            break
    else:
        print("é primo")