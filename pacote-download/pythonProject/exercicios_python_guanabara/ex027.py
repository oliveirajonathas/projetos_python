#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome
#separadamente

nome = input('Digite o seu nome completo: ')
nome = nome.strip()
primeiro_espaco = nome.find(' ')
ultimo_espaco   = nome.rfind(' ')
print('O seu primeiro nome é: {}'.format(nome[:primeiro_espaco]))
print('O seu último nome é: {}'.format(nome[(ultimo_espaco+1):]))
