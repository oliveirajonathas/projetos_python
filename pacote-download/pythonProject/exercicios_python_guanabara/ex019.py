import random

aluno1 = input('Nome aluno 1: ')
aluno2 = input('Nome aluno 2: ')
aluno3 = input('Nome aluno 3: ')
aluno4 = input('Nome aluno 4: ')

sorteado = random.choice([aluno1, aluno2, aluno3, aluno4])

print('O sorteado para apagar o quadro foi: {}'.format(sorteado))
