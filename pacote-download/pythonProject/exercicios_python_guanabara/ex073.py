"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colo-
cação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em qual posição na tabela está o time da Chapecoense
"""
tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro',
          'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport',
          'América-MG', 'Vitória', 'Paraná')

# Analisando os 5 primeiros colocados
print(f'Os CINCO PRIMEIROS colocados são: {tabela[0]}', end='')
for time in tabela[1:5]:
    print(',', time, end='')

# Analisando os 4 ultimos colocados
#quatro_ultimos = tabela[20:15:-1]
#quatro_ultimos = quatro_ultimos[::-1]
print('')
print(f'Os QUATRO ULTIMOS colocados são: {tabela[-4]}', end='')
for time in tabela[-3:]:
    print(', ', time, end='')

# Lista em ordem alfabética
print('')
print(f'Relação dos times por ordem alfabética: {sorted(tabela)[0]}', end='')
for time in sorted(tabela[1:]):
    print(', ', time, end='')

# Localizando a colocação de um time
print('')
 #for pos, time in enumerate(tabela):
 #   if time == 'Chapecoense':
 #       print(f'A Chapecoense está na {pos + 1}ª posição')
print(f'A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')