dias = int(input('Por quantos dias o veículo foi alugado? '))
km = float(input('Quantos Km rodados? '))
preco = 60*dias + 0.15*km
print('O preço a pagar é R${:.2f} reais, tendo em vista o período de\n'
      '{} dias e {}Km rodados'.format(preco, dias, km))
