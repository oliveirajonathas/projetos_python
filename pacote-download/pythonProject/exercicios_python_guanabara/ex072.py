"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por exetenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                   'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                   'dezenove', 'vinte')

continuar = ''
while True:
    while True:
        numero = int(input('Digite um número entre 0 a 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente! ', end='')

    print(f'O número digitado foi {numero_extenso[numero]}')


    continuar = str(input('Quer continuar? [S/N]'))
    if continuar == 'N':
        break
