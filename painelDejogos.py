import forcaJogo
import adivinhacaoJogo

print("*************************")
print("Bem-Vindo a lista de jogos!")
print("*************************\n")

jogo = int(input("Qual jogo você deseja? (1)Forca  (2)Adivinhação: "))

if(jogo == 1):
    print("Jogando a forca")
    forcaJogo.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação")
    adivinhacaoJogo.jogar()      #criei uma função "def" chamado jogar, primeiro chama a classe depois a função

