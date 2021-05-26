#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez
frase = str(input('Digite uma frase qualquer: '))
frase = frase.upper().strip()
print('Sua frase tem {} letras "A"'.format(frase.count('A')))
print('A primeira ocorrência é na posição {}'.format(frase.find('A')))
print('A última ocorrência é na posição {}'.format(frase.rfind('A')))
