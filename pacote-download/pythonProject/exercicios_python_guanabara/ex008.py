metros      = float(input('Informe a dimensão em metros: '))
print('{} metros equivale a\n'
      '{} decimetros\n'
      '{} centimetros\n'
      '{} milimetros\n'
      '{} quilometros\n'
      '{} hectometros\n'
      '{} decametros'.format(metros, metros*10, metros*100, metros*1000, metros/1000, metros/100, metros/10 ))
