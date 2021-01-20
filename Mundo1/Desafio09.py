#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

print("<><>"*10)
print("\t\tTABUADA")
print("<><>"*10)

n = int(input("Digite um número: "))

for x in range (11):
    print("{} x {} = {}".format(n,x,n*x))
    x = + 1