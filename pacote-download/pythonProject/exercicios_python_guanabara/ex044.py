"""
044) Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
preco = float(input('Qual o valor do produto? R$'))
forma_pagamento = int(input('Qual a forma de pagamento?\n'
                            '[1] à vista com dinheiro/cheque\n'
                            '[2] à vista com cartão\n'
                            '[3] em até 2x com cartão\n'
                            '[4] em 3x ou mais com cartão\n'
                            ''))
if 1 <= forma_pagamento <= 4:
    if forma_pagamento == 1:
        preco = preco*0.9
        forma_pagamento = 'à vista com dinheiro/cheque'
    elif forma_pagamento == 2:
        preco = preco*0.95
        forma_pagamento = 'à vista com cartão'
    elif forma_pagamento == 3:
        forma_pagamento = 'em até 2x no cartão'
    elif forma_pagamento == 4:
        preco = preco*1.2
        forma_pagamento = 'em 3x ou mais com cartão'
    print('Você escolheu a forma de pagamento: \033[1;33m{}\033[m e irá pagar \033[1;32mR${:.2f}\033[m '
          'pelo produto.'.format(forma_pagamento, preco))
else:
    print('Opção inválida! Tente Novamente!')
