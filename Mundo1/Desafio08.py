#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print("<><>"*10)
print("\t CALCULANDO MEDIDAS")
print("<><>"*10)

metro = int(input("Digite a quantidade de metros que deseja converter: "))
centimetro = metro * 100
milimetro = metro * 1000

print("<><>"*10)
print("Convertendo...")
print("Quantidade em Metros: {} \nQuantidade em Centímetros: {} \nQuantidade em milímetros: {}".format(metro,centimetro,milimetro))
print("<><>"*10)
