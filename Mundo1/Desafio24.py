cidade = input("Digite o nome de uma cidade: ")
cidade = cidade.strip()
cidadeM = cidade.upper()
resposta = cidade.split()
resposta = cidadeM.find("SANTO")
print("Analisando ...") 
if resposta == 0: 
    print("A cidade de {} COMEÇA com a palavra SANTO.".format(cidadeM))
else:
    print("A cidade de {} não começa com a palavra SANTO.".format(cidadeM))
    