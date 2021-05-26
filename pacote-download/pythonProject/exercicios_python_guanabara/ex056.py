"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final o programa mostre:
- A média de idade do grupo
- O nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
"""
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
mais_nova = 0
for i in range(1, 5):
    print('----{}ª PESSOA ----'.format(i))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Informe o sexo:\n'
                     '[1] M\n'
                     '[2] F\n')).strip()
    soma_idade += idade
    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if idade < 20 and sexo in 'Ff':
        mais_nova += 1
media_idade = soma_idade/4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('Das pessoas informadas, {} mulheres tem menos de 20 anos'.format(mais_nova))
