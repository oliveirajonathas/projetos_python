import random
aluno1 = input('Nome aluno 1: ')
aluno2 = input('Nome aluno 2: ')
aluno3 = input('Nome aluno 3: ')
aluno4 = input('Nome aluno 4: ')

lista = [aluno1, aluno2, aluno3, aluno4]

print('A ordem das apresentações é: {}'.format(random.sample([aluno1, aluno2, aluno3, aluno4], k=4)))
random.shuffle(lista)
print('A ordem das apresentações é {}'.format(lista))

