reais = float(input('Quantos reais você tem? R$'))
dolares = reais / 5.80
print('Com R${:.2f} reais, você pode comprar U$${:.2f} dólares'.format(reais, dolares))
