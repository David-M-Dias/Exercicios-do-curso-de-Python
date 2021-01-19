#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input("Digite um número qualquer: "))
print("O número digitado: {} \nSeu antecessor: {} \nSeu sucessor: {}".format(n,n-1,n+1))