"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo
"""
from random import randint
print('*'*20)
print('Jogo do par ou ímpar')
print('*'*20)
vitoria = 0

while True:
    # Computador e Jogador escolhem um número
    computador = randint(1, 11)
    numero = int(input('Digite um número: '))
    # Jogador escolhe se quer PAR ou IMPAR
    jogador = 'nada'
    while jogador not in 'PI':
        jogador = str(input('Qual sua escolha: [P] PAR ou [I] ÍMPAR')).strip().upper()[0]
    # É feita a verificação se o resultado é PAR ou IMPAR
    calculo = (computador + numero) % 2
    if calculo == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    # Definindo o vencedor
    if jogador == resultado:
        if resultado == 'P':
            resultado = 'PAR'
        else:
            resultado = 'IMPAR'
        vitoria += 1
        print('-=-'*20)
        print(f'Você jogou {numero} e o computador jogou {computador}... Deu {resultado}')
        print('Você ganhou! Vamos jogar NOVAMENTE...')
        print('-=-' * 20)
    else:
        if resultado == 'P':
            resultado = 'PAR'
        else:
            resultado = 'IMPAR'
        print('-=-' * 20)
        print(f'Você jogou {numero} e o computador jogou {computador}... Deu {resultado}')
        print(f'Você PERDEU! Você venceu {vitoria} vez(es).')
        print('-=-' * 20)
        break
print('FIM DE JOGO')
