"""
Crie um programa que tenha uma tupla única com os nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados de forma tabular.
"""
print(60*'-')
print('{:^60}'.format('MERCADINHO J&R'))
print(60*'-')

produtos = ('Manteiga', 2.50, 'Pasta de Dente', 3.00, 'Filé Mignon Kg', 40.00, 'Cebola Kg', 2, 'Alho Poró', 12,
            'Aquarius Fresh', 3.5, 'Sandália Havaiana', 38, 'Filtro São João', 120)

produto = produtos[::2]
preco = produtos[1::2]

for i in range(0, len(produto)):
    print(f'{produto[i]:-<50}R${preco[i]:7.2f}')

print(60*'-')

'''
Solução do professor, considerando a lógica de que os produtos estão em index par e os preços em index ímpar

print(60*'-')
print('{:^60}'.format('MERCADINHO J&R'))
print(60*'-')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print(60*'-')
'''