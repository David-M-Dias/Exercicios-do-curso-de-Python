# Faça um programa que receba um número e faça a contagem regressiva apartir do número digitado.

x = 0
y = 0
n = int(input("Digite um número : "))
print("=-="*20)
print("\t\t CONTAGEM REGRESSIVA")
print("=-="*20)
print("Número Escolhido: {}".format(n))
for x in range (n):
    n = n - 1

    print("{}".format(n))
    x =+1
    