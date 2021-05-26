'''Desenvolva um programa que pergunte a distância d euma viagem em Km. Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas'''

distancia = float(input('Qual a distância em quilômetros a ser percorrida durante a sua viagem? '))
if distancia <= 200:
    preco = distancia*0.5
else:
    preco = distancia*0.45
print('Valor da passagem: R${:.2f}'.format(preco))
print('FIM DO PROGRAMA')
