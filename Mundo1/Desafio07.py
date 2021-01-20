#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print("-="*20)
print("\t***BOLETIM  ESCOLAR***")
print("-="*20)
nt1 = float(input("Digite a primeira nota: "))
nt2 = float(input("Digite a segunda nota: "))
media = (nt1+nt2)/2
print("Como você tirou {} na primeira avaliação, e tirou {} na segunda! Presumimos que sua media será {}".format(nt1,nt2,media))