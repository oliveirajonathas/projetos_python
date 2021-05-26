#Criar um programa que leia o nome completo de uma pessoa e mostre:
#a) O nome com todas as letras maiúsculas
#b) O nome com todas as minúsculas
#c) Quantas letras ao todo (sem considerar espaços)
#d) Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: '))
nome = nome.strip()
print('Analisando o seu nome...')
print('Com letras maiúsculas: ', nome.upper())
print('Com letras minúsculas: ' ,nome.lower())
print('Quantidade de letras sem contar espaços vazios: ',int(len(nome) - nome.count(' ')))
#print('Quantidade de letras do Primeiro Nome: ',int(nome.find(' ')))
separa = nome.split()
print(separa)
print('Quantidade de letras do Primeiro Nome: {}'.format(len(separa[0])))
print('Fim do programa')