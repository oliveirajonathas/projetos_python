salario = float(input('Informe o salário: '))
taxa = float(input('Qual o percentual de aumento: '))
taxa = 1 + taxa/100
novo_salario = salario * taxa

print('O salário reajustado com taxa de {:.1f}% de aumento é R${:.2f} reais'.format((taxa-1)*100, novo_salario))
