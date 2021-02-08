num = int(input("Digite um número: "))
x = 0

while x <= 2: 
    if num > 0 :
        resto = num % 2
        div = num // 2
        x = + 1
        num = div
        print(resto)
