nome = input("Digite seu nome: ")

print("O nome em MAIUSCULO: ",nome.upper()) #COLOCAR LETRAS MAIUSCULA 

print("O nome em minusculos: ",nome.lower()) #COLOCAR LETRAS MINUSCULAS

print("A quantidade de letras digitadas: ", len(nome)) # Contar a quantidade de caracter na variavel

print("Colocando a Primeira Letra Maiuscula: ",nome.capitalize())# Deixa só a primeira letra maiuscula

# contar todas as  letras sem espaços
dividirNome = nome.split()
posicao0 = len(dividirNome[0])
posicao1 = len(dividirNome[1])
posicao2 = len(dividirNome[2])

resultado = posicao0+posicao1+posicao2
print("A quantidade de Letras Obtidas sem os espaços são: {}".format(resultado))


divididonome = nome.split() # dividindo os dados sem o espaço
QuantletrasNome= len(divididonome[0]) # letras do primeiro nome
print("A quantidade de Letras do Primeiro nome é: {}".format(QuantletrasNome))