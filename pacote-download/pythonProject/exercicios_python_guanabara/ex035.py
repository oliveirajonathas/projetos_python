#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
#triângulo
lado1 = float(input('Digite a dimensão do primeiro lado: '))
lado2 = float(input('Digite a dimensão do segundo lado: '))
lado3 = float(input('Digite a dimensão do terceiro lado:'))

if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3 < lado2+lado1:
    print('Com essas dimensões, será possível criar um triângulo!')
else:
    print('Com essas dimensões não é possível criar um triângulo!')
