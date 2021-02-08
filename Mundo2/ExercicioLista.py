# Preencha uma lista com 10 números.
x = 0
lista = []
# preenchendo a lista com valores desejados
for x in range (10):
    
    lista = lista + [int(input('Digite um número:'))] # adicionando valores a lista
    x = x + 1 # adicionando ao contador

print(lista)
