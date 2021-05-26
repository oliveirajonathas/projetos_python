preco = float(input('Qual o preço do produto? '))
taxa = float(input('Qual o desconto percentual a ser aplicado? '))
taxa = 1 - (taxa/100)
preco_com_desconto = preco*taxa
print('O valor com {:.1f}% de desconto é R${:.2f}'.format((1-taxa)*100, preco_com_desconto))
