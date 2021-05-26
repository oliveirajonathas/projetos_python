#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

numero = randint(0, 5) #Faz o computador "Pensar"
#print(numero)
print('-=-'*20)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
escolha = int(input('Adivinha que número estou pensando: '))
print('Processando...')
sleep(3)
if escolha == numero:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Eu pensei em {}!'.format(numero))
