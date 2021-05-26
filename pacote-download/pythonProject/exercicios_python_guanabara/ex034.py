#Escreva um programa que pergunte o salário de um funcionário e calcule seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%
#Para inferiores ou iguais, o aumento é de 15%
salario = float(input('Informe o salário: '))
if salario > 1250:
    salario = salario*1.1
else:
    salario = salario*1.15
print('O salário reajustado é: R${:.2f}'.format(salario))
