"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitos
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou na lista.
"""
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    print('Deseja continuar? S/N')
    continua = str(input('Sua opção: ')).strip().upper()[0]
    while True:
        if continua in 'NS':
            break
    if continua == 'N':
        break
print(30*'-=')
print(f'Foram digitados {len(lista)} valores!')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é: {lista}')
verifica = int(input('Posso verificar se existe algum número na lista pra você. Digite um número: '))
if verifica in lista:
    pos = lista.index(verifica)
    print(f'O valor 5 faz parte da lista, e está na posição: {pos}!')
else:
    print(f'O valor {verifica} não foi digitado!')

