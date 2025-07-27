num=int(input("digite um numero: "))

for b in range(num,101):
    if b % 3 == 0 and b % 5 == 0:
        print("fizzbuzz")
    elif b % 3 == 0:
        print("fizz")
    elif b % 5 == 0:
        print("buzz")
    else:
        print(b)