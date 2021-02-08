#crie uma lista, preencha com 3 valores, passar os valores finais de uma lista para a posição inicial da segunda lista.

lista = []
lista2 = []
x = 0

for x in range (10): # estrutura de repetição 
    lista = lista + [int(input("Digite um número: "))] # adicionando valores a lista
    
    x = x + 1 # acrescendo valor a variavel x para dar continuidade a estrutura de repetição.

for x in range (10):
    lista2 = lista2 + [(lista[9-x])]

    x = x + 1

print(lista)
print(lista2)