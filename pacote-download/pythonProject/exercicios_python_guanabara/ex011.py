largura = float(input('Qual a largura, em metros, da parede? '))
altura  = float(input('Qual a altura, em metros, da parede? '))
area    = largura * altura
litros_de_tinta = area/2
print('Você precisará de {} litros de tinta para pintar a sua parede de {}m²'.format(litros_de_tinta, area))
