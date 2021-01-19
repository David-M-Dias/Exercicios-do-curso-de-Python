frase = "Curso em Video Python"
print(len(frase))# para contar a quatidade de caracteres em frase.

print(frase[3:12])#para separar letras de frase apartir da casa 3 (lembrando que começa de 0 então a posicao e 4) ate a numero 12 sendo que a 12 será excluída.

print(frase[3::2])#Inicia o print da 3 casa da frase até a ultima posicão, mas irá saltar de 2 em 2 casa printando as letras da casa selecionada.

print(frase.upper())# todas as letras de frase passarao para MAIUSCULAS.

print(frase.lower())# todas as letras de frase passarão a ser minúsculas.

print(frase.count('o'))# para contar determinada letra dentro de frase.

print(frase.strip()) # ira remover os espaços (se houver) da frente e do final.

print(frase.replace("Python","Android"))# replace substitui a frase escolhida por outra.

dividido = frase.split() # para dividir os valores contidos dentro da variavel frase 
print(dividido[1]) #imprimir o que estiver na posicao um da frase dividida
print(dividido[1][1]) #imprimir a letra contida na posicao 1 (0 e,1 m) da frase contida na posicao 1 (em).


print("Video" in frase) # função IN para procurar algo dentro da variavel

print()

