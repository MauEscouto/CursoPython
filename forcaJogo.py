import random

def jogar():
    print("\nBem-vindo ao jogo da Forca")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numeroA = random.randrange(0,3)

    palavra_secreta = palavras[numeroA].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou= False
    erros = 0

    while(not enforcou and not acertou):
        chute = input("Chute uma letra: ")
        chute = chute.strip().upper() #strip remove os espaços digitados no input

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra): #upper torna a letra digitada no input em maiuscula 
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6 
        acertou = not "_" in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

if(__name__ == "__main__"): 
    jogar()


#if(fruta_pedida in frutas) verifica se tem a fruta digitada dentra da lista "frutas"

# letras_faltando = str(letras_acertadas.count('_'))   count conta a quantidade de digitos que tem dentro da lista              
#print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
