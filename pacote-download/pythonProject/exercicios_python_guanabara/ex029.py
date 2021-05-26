#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, nostre uma mensagem
#dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

deslocamento = float(input('Qual o deslocamento em quilômetros? '))
tempo        = float(input('Qual o intervalo de tempo em horas? '))
velocidade = deslocamento/tempo
print('Sua velocidade média é de: {:.1f}Km/h.'.format(velocidade))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado no valor de: R${:.2f}, por exceder a velocidade em {}km/h'.format(multa, (velocidade-80)))
print('Fim do Programa')
