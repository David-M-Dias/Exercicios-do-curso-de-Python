frase = str(input("Digite uma frase: ")).lower().strip()
print("A quantidade de letras A na frase é {}.".format(frase.count("a")))
print("A primeira letra a aparece na posição de número {}.".format(frase.find("a")+1))#para procurar a primeira posicao da letra a dentro da frase
print("A ultima letra a aparece na posição de número {}.".format(frase.rfind("a")+1))#usado para encontrar a posicao da ultima letra a da frase.
