def jogar():
    print("\nBem-vindo ao jogo da Forca")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou= False

    while(not enforcou and not acertou):
        chute = input("Chute uma letra: ")
        chute = chute.strip() #strip remove os espaços digitados no input

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #upper torna a letra digitada no input em maiuscula 
               letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)


if(__name__ == "__main__"): 
    jogar()


#if(fruta_pedida in frutas) verifica se tem a fruta digitada dentra da lista "frutas"

# letras_faltando = str(letras_acertadas.count('_'))   count conta a quantidade de digitos que tem dentro da lista              
#print( 'Ainda faltam acertar {} letras'.format(letras_faltando))