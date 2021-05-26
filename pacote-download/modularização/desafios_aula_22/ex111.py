"""
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamdos moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo
funcionando.
"""
from ex111.utilidadeCeV import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 50)
