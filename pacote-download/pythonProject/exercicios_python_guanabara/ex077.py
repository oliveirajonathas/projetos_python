"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais.
"""
palavras = ('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'Sao Paulo', 'Atletico-MG', 'Atletico-PR', 'Cruzeiro',
          'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceara', 'Vasco', 'Sport',
          'America-MG', 'Vitoria', 'Parana')

for item in palavras:
    substring = item.upper()
    print(f'As vogais em {substring} são: ', end='')
    for i in range(0, len(substring)):
        if substring[i] == 'A' or substring[i] == 'E' or substring[i] == 'I' or substring[i] == 'O' or substring[i] == 'U':
            print(substring[i], end='')
    print('')
