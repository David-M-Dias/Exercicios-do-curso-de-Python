print("-=" * 30)
print("\t\t\tBanco do Povo")
print("-=" * 30)

nome = str(input("Digite seu nome: "))
salario = float(input("Digite o seu salário: R$ "))
emprestimoPretendido = float(input("Digite o valor do emprestimo desejado: "))
anos = int(input("Digite em quantos anos deseja pagar: "))

meses = anos * 12 #convertendo os anos em meses

limiteParcela = salario * ( 30 / 100) #limite da parcela no valor y para 30% de salario x.

parcelaMensal = emprestimoPretendido / meses

if parcelaMensal > limiteParcela:
    print("Caro {}, Lamentamos informar mas o emprestimo no valor de R${:.2f} foi negado.\nPois a parcela no valor de R${:.2f} execede o limite mensal programado.".format(nome,emprestimoPretendido,parcelaMensal))

else:
    print("\n{} seu emprestimo foi aprovado!".format(nome))
    print("As parcelas serão no valor de {:.2f} e deverão ser pagas em {} meses.".format(parcelaMensal,meses))
    




