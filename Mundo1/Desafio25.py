nome = str(input("Digite seu nome: ")).strip()
nome = nome.upper()
resultadoBusca = nome.count("SILVA")
print("ANALISANDO. . .")
if resultadoBusca == 0:
    print(" O nome {} não contem a 'Silva'.".format(nome))

else:
    print(" O nome {} contem 'Silva'.".format(nome)) 