nome = str(input('Digite o seu nome completo: ')).strip()
nome = nome.split()
print(nome)
print('Prazer em te conhecer!\n'
      'Seu primeiro nome é: {}\n'
      'Seu último nome é: {}'.format(nome[0], nome[(len(nome)-1)]))
