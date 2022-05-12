import random

def jogar():    
    print("Bem-vindo ao jogo de adivinhação")
    print("")

    numero_correto = random.randrange(1,101) #numero_correto = round(random.random() * 100)  #round arrendonda, random.random faz numero aleatorios float
    totalTentativas = 0
    totalDePontos = 1000

    print("Qual o nível de dificuldade você quer? ")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Defina um nível: "))

    if nivel == 1:
        totalTentativas = 20
    elif nivel == 2:
        totalTentativas = 10
    else:
        totalTentativas = 5

    print("Total de pontos:",totalDePontos)

    for rodada in range(1,totalTentativas + 1):
        print(f'Tentativa {rodada} de {totalTentativas}') #ou print("Tentativa {0} de {1}".format(rodada, totalTentativas)) se usar nome.lower vai imprimir em minusculo
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou" , chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue #se digitar o número errado, ele vai ignorar o que tem embaixo e começar um novo looping

        if chute == numero_correto:
            print('Você acertou!')
            print("Você ficou com um total de {} pontos".format(totalDePontos))
            break #a partir do momento que é acertado, ele para o looping ignorando o que tem abaixo

        else:
            if chute > numero_correto:
                print("Você digitou um número maior do que o número correto")
                pontosPerdidos = abs(numero_correto - chute)
                totalDePontos = (totalDePontos - pontosPerdidos)
            if chute < numero_correto:
                print("Você digitou um número menor do que o número correto")
                pontosPerdidos = abs(numero_correto - chute) #abs significa absoluto, por mais que o resultado dê negativo, será transformado em positivo
                totalDePontos = (totalDePontos - pontosPerdidos)
        rodada += 1 

    print("Fim do jogo") 

if(__name__ == "__main__"): 
    jogar()
 

#interpolação "R$ {:7.1f}".format(1000.12)
#"R$ {:07.2f}".format(4.11)

#R$  1000.1
#R$ 0004.11 







