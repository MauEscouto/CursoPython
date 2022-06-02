import random

def gerar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numeroA = random.randrange(0,3)
    palavra_secreta = palavras[numeroA].upper()
    return palavra_secreta

def pede_chute():
    chute = input("\nChute uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta,chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra): 
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def jogar():
    print("\nBem-vindo ao jogo da Forca")

    palavra_secreta = gerar_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou= False
    erros = 0

    while(not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta,chute,letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6 
        acertou = not "_" in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)  

if(__name__ == "__main__"): 
    jogar()


#if(fruta_pedida in frutas) verifica se tem a fruta digitada dentra da lista "frutas"

# letras_faltando = str(letras_acertadas.count('_'))   count conta a quantidade de digitos que tem dentro da lista              
#print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
