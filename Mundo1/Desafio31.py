nome  = str(input("Digite seu nome: "))
viagem = int(input("Tudo Bem {}, Agora digite a quantidade de KM é a sua viagem: ".format(nome)))

if viagem <= 200:
    precoViagem = viagem*0.50

else:
    precoViagem = viagem*0.45

print("{} o preço da passagem vai custar {:.2f}".format(nome,precoViagem))
