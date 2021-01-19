print("-="*40)
nome = str(input("Digite seu Nome: "))
salario = float(input("Digite seu salário: "))

if salario > 1250:
    aumento = "10%"
    aumentoSalarial = (salario * 0.10) + salario
else:
    aumento = "15%"
    aumentoSalarial = (salario * 0.15) + salario

print("-=" * 40)
print("{} o seu salario com aumento de {} vai ficar no total de:R$ {:.2f}.".format(nome,aumento,aumentoSalarial))
print("-=" * 40)
