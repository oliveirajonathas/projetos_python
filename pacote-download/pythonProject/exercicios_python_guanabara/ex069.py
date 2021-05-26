"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:

a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastrados
c) qantas mulheres tem menos de 20 anos
"""
maior = 0
mulher_menor_vinte = 0
homens = 0
while True:
    idade = 'inicial'
    while not idade.isnumeric():
        idade = input('Informe a idade: ')
    idade = int(idade)

    sexo = 'inicial'
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo: [M/F] ')).strip().upper()[0]
    print('*' * 20)

    if idade > 18:
        maior += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulher_menor_vinte += 1

    continua = 'inicial'
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S] SIM; [N] NÃO ')).strip().upper()[0]
        print('*' * 20)
    if continua == 'N':
        break
print('-=-'*20)
print(f'Análisando os dados cadastrados temos que {maior} pessoas tem mais de 18 anos; {homens} são homens; '
      f'e {mulher_menor_vinte} mulheres tem menos que 20 anos')
print('FIM DO PROGRAMA')
