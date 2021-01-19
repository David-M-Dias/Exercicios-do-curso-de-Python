milhar = 0
centena = 0
dezena = 0
unidade = 0


n = int(input("Digite um número ENTRE 0 e 9999: "))

dadosN = str(n)
DadosN = len(dadosN)
if n >= 1000 and n < 10000:
    milhar = dadosN[0]
    centena = dadosN[1]
    dezena = dadosN[2]  
    unidade = dadosN[3]
    print("\n Milhar : {} \n Centena: {} \n Dezena: {} \n Unidade: {}".format(milhar, centena, dezena, unidade))
if n < 1000 and n > 99:
    centena = dadosN[0]
    dezena = dadosN[1]  
    unidade = dadosN[2]
    print("\n Centena: {} \n Dezena: {} \n Unidade: {}".format(centena, dezena, unidade))
    
if n <= 100 and n >= 9:
    dezena = dadosN[0]  
    unidade = dadosN[1]
    print("\n Dezena: {} \n Unidade: {}".format(dezena, unidade))
    
if n < 10 and n >= 0:
    unidade = dadosN[0]
    print("\n unidade: {}".format(unidade))


    

    
            

