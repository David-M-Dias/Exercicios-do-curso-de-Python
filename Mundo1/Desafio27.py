nome = str(input("Digite seu nome completo: ")).upper().strip()
nomeDividido = nome.split() #dividindo o nome
contandoNomes = len(nomeDividido)#contando a quantidade de nomes.
print("Satisfação em conhecer você!")
print("O seu primeiro nome é {}.".format(nomeDividido[0]))#imprimindo o primeiro nome.
print("O seu sultimo nome é {}.".format(nomeDividido[contandoNomes-1]))#imprimindo o ultimo nome.
