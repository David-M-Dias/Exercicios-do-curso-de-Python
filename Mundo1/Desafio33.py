valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

menor = valor1
maior = valor1

if valor2 < valor1 and valor2 <valor3:
    menor = valor2

if valor3 < valor1 and valor3 < valor2:
    menor = valor3

if valor2 > valor1 and valor2 > valor3:
    maior = valor2

if valor3 > valor1 and valor3 > valor2:
    
    maior = valor3

print("O Menor valor é: {}".format(menor))
print("O Maior Valor é {}".format(maior))