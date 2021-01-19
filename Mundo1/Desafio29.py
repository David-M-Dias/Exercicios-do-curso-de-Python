print("-=-"*20)
print("\t  Departamento de trânsito de Municipal")
print("-=-"*20)
limite = 80
precoPorKmExcedido = 7
velocidade = int(input("Digite a velocidade alcançada: "))
if velocidade > limite :
    excessoDeVelocidade = velocidade - limite
    multa = excessoDeVelocidade * precoPorKmExcedido
    
    print("-=-"*20)
    print("\t  MULTA POR EXCESSO DE VELOCIDADE")
    print("-=-"*20)
    print("Você passou pelo radar acima da velocidade permitida")
    print("O valor a pagar: R$ {:.2f}".format(multa))
    print("-=-"*20)
    
else:
    print("Parabens! Continue andando dentro do limite!")
