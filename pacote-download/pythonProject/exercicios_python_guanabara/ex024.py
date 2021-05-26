#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = input('Digite o nome da cidade: ')
cidade = cidade.upper().strip()
print('Começa com santo? {}'.format('SANTO' in cidade[:5]))
