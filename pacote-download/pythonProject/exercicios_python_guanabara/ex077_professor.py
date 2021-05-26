"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais.
"""
palavras = ('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'Sao Paulo', 'Atletico-MG', 'Atletico-PR', 'Cruzeiro',
          'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceara', 'Vasco', 'Sport',
          'America-MG', 'Vitoria', 'Parana')

for item in palavras:
    print(f'As vogais em {item} são: ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end='')
    print('')
