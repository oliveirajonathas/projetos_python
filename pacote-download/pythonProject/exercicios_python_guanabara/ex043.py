"""
043) Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de
acordo com a tabela abaixo:
- Abaixo de 18.5: ABAIXO DO PESO
- Entre 18.5 e 25: PESO IDEAL
- 25 até 30: SOBREPESO
- 30 até 40: OBESIDADE
- Acima de 40: OBESIDADE MÓRBIDA
"""
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso/pow(altura, 2)
cores = {'limpa'   :'\033[m',
         'azul'    :'\033[1;34m',
         'verde'   :'\033[1;32m',
         'roxo'    :'\033[1;35m',
         'amarelo' :'\033[1;33m',
         'vermelho':'\033[1;31m'}
if imc <= 18.5:
    print('Você está {}ABAIXO DO PESO IDEAL{}'.format(cores['azul'], cores['limpa']))
elif (imc > 18.5) and (imc <= 25):#o Python aceita: 18.5 < imc <= 25
    print('Você está com o {}PESO IDEAL{}'.format(cores['verde'], cores['limpa']))
elif (imc > 25) and (imc <= 30):#o Python aceita: 25 > imc <= 30
    print('Você está com {}SOBREPESO{}'.format(cores['roxo'], cores['limpa']))
elif (imc > 30) and (imc <= 40):#o Python aceita: 30 < imc <= 40
    print('Você está com {}OBESIDADE{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('Você está com {}OBESIDADE MÓRBIDA{}'.format(cores['vermelho'], cores['limpa']))
