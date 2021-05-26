import math
angulo = math.radians(float(input('Informe o valor do ângulo: ')))
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print('Em relação ao ângulo {} temos que:\n'
      'Seu seno é {:.1f}\n'
      'Seu cosseno é {:.1f}\n'
      'Sua tangente é {:.1f}'.format(angulo, sen, cos, tan))
