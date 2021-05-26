'''arquivo = open('contatos.txt', 'r')
conteudo = arquivo.read()
print(f'O conteúdo de contatos.txt é: \n{conteudo}')
arquivo.close()
'''
arquivo = open('contatos.txt', 'r')
while True:
    linha = arquivo.readline()
    if linha == '':
        break
    elif linha == 'Fulana,3555-0123\n':
        print(linha)
arquivo.close()

"""arquivo = open('contatos.txt', 'r')
linhas = arquivo.readlines()
print(linhas)
arquivo.close()
for item in linhas:
    registro = item.split(',')
    nome = registro[0]
    fone = registro[1][:-1]
    print(nome, fone)"""
