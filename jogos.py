import forca
import adivinhacao

def escolher_jogo():
    print("*****************************")
    print("***** Decida o seu jogo *****")
    print("*****************************")


    print('Qual jogo você vai querer jogar?')
    print('(1) Forca     (2) Adivinhação')

    jogo = int(input('Decida: '))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()