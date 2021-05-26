n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma      = n1+n2
produto   = n1*n2
quociente = n1/n2
resto     = n1%n2
div_exata = n1//n2
potencia  = n1**n2

print('A soma é {} \nO produto é {} \nO quociente é {} \nO resto é {} \nA divisão exata é {} \nA potência é {}'
      .format(soma, produto, quociente, resto, div_exata, potencia))
