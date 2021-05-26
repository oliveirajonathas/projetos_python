import math
cateto_o = float(input('Informe a medida do cateto oposto: '))
cateto_a = float(input('Informe a medida do cateto adjacente: '))

hipotenusa = math.hypot(cateto_o, cateto_a)

print('A Hipotenusa é: {}'.format(hipotenusa))
