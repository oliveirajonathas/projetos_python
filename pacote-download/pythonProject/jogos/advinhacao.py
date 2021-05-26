def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhações")
    print("*********************************")

    import random

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    tentativa_atual = 1
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Defina o nível: "))

    if (dificuldade==1):
        total_de_rodadas = 12
    elif (dificuldade==2):
        total_de_rodadas = 8
    else:
        total_de_rodadas = 2

    for rodada in range(1, total_de_rodadas + 1):

        print("Tentativa {} de {}".format(rodada,total_de_rodadas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("O número digitado deve estar entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        if(acertou):
            print("Você acertou e fez {}".format(pontos))
            break
        elif(maior):
            print("Palpite maior que o valor correto")
            if (rodada==total_de_rodadas):
                print("Você perdeu, o número secreto era {} e você fez {} pontos".format(numero_secreto,pontos))
        elif(menor):
            print("Palpite menor que o valor correto")
            if (rodada == total_de_rodadas):
                print("Você perdeu, o número secreto era {} e você fez {} pontos".format(numero_secreto,pontos))

    print("Fim do jogo")