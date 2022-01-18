def jogar():
    print("***********************************")
    print("*** Bem vindos ao jogo da Forca ***")
    print("***********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Digite sua letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontramos a letra {} na posição {}".format(letra, index + 1))
            index = index + 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()