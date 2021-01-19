
import random
from time import sleep
continuar = "S"
nome = str(input("Digite seu nome: "))#Coletando o nome do jogador
print("Olá {}, Meu nome é DevTec9000!\nHoje iremos brincar de Adivinhação!".format(nome))
print("Eu vou escolher um número entre 0 é 5, e você deve tentar adivinhar!! \nVamos nessa?")
while continuar != "N":#Estrutura de repetição para o jogo rodar enquanto o usuário não alterar a condição já estabelecida.
    
    nSorteado = random.randrange(0,5)#sorteando um número Aleatório
    n = int(input("Escolha seu número: "))#Coletando o número que o jogador digitar.
    if(n <= 5 and n >= 0):#Verificando se o número está entre de 0 até 5.
        print("Analisando... ")
        sleep(3)
        print("Vamos ver se você acertou?")
        print("{}: {} VS DevTec9000: {}.".format(nome,n,nSorteado))#informando o número que o jogador escolheu e o  que foi sorteado pelo PC.
        if n == nSorteado: #Codição para verificar vencedor.
            print("Parabéns {}!! Você ACERTOU!".format(nome))
        else:
            print("DevTec9000 Ganhou! \ns{} tente outra vez!".format(nome))
    else:
        print("Número inválido")

    continuar = str(input("Deseja Continuar? \n S. ou N. :")).upper() #Coletando informação para ver se o programa será executado novamente.
    
else:
    print("Obrigado por participar!")
