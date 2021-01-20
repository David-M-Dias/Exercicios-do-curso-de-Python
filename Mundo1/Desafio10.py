#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# valor ficticio do dolar 4,05.


dollar = 4.05

print("**"*20)
print("\tCaixa Eletrônico")
print("**"*20)

carteira = float(input("Digite quanto dinheiro você tem: "))
print("Com R$ {:.2f} obtem-se USD$ {:.2f} em uma conversão direta. ".format(carteira,carteira/dollar))