"""
036) Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado
"""

valor = float(input('QUal o valor do imóvel? R$'))
salario = float(input('Qual o seu salário bruto? R$'))
prazo = int(input('Em quantos anos deseja pagar? '))

prestacao = valor/(prazo*12)
print('O valor de cada prestação será R${:.2f} reais'.format(prestacao))

if prestacao > 0.3*salario:
    print('Solicitação de empréstimo \033[1;31mNEGADA\033[m. Infelizmente você não pode financiar este imóvel.')
else:
    print('Parabéns! O seu crédito foi \033[1;32mAPROVADO\033[m!')
print('Fim do Programa')
