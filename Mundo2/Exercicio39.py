anoAtual = 2021
idadeAlistamento = 18

nome = input("Digite seu nome: ")
anoNascimento = int(input("Digite o ano de nascimento: "))

idade = anoAtual - anoNascimento

if idade == 18 :
    print(f"{nome}, você completou {idade} anos de idade e está na hora de se presentar ao Serviço Militar Obrigatório!")

elif idade < 18 :

    print(f"{nome}, voce ainda tem {idade} anos. faltam {idadeAlistamento - idade} anos para pode se alistar!")

else: 
    print(f"{nome}, você possui {idade} anos de idade, O Seu alistamento foi no ano de {anoNascimento + idadeAlistamento}, Já se passaram {idade - idadeAlistamento} anos do seu período de alistamento  militar obrigatório.")
