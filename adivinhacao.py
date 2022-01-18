import random


def jogar():
    print("*************************")
    print("Bem vindos ao melhor jogo da sua vida!")
    print("*************************")

    numero_secreto = random.randrange(1, 101)
    numero_de_tentativas = 0
    pontos = 1000

    print('Escolha o seu nível de dificuldade')
    print('(1) Fácil    (2) Médio      (3) Difícil')

    nivel = int(input("Defina: "))

    if(nivel == 1):
        numero_de_tentativas = 20
    elif(nivel == 2):
        numero_de_tentativas = 10
    else:
        numero_de_tentativas = 5

    for rodada in range(1, numero_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,numero_de_tentativas))

        chute_str = input("Digite seu número entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 0 or chute > 100):
            print("Você deve digitar um valor entre 1 e 100")
            continue

        acertou = (chute == numero_secreto)
        maior =  chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Quen quen quennnnn, voce errou!")
                print('O seu chute foi maior que o número secreto')
            elif(menor):
                print("Quen quen quennnnn, voce errou!")
                print('O seu chute foi menor que o número secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos 

    print('Fim do Jogo')

if( __name__ == "__main__"):
    jogar()