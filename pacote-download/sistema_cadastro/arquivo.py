def ler():
    from time import sleep
    titulo('PESSOAS CADASTRADAS')
    arquivo = open('registros.txt', 'r')
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
    sleep(0.5)


def escrever(msg=''):
    from time import sleep
    import dados
    titulo('NOVO CADASTRO')
    nome = str(input('Nome: '))
    idade = dados.leiaint('Idade: ')
    arquivo = open('registros.txt', 'a')
    arquivo.write(f'{nome:<30}{idade:>5} anos\n')
    arquivo.close()
    print(f'Novo registro de {nome} adicionado.')
    sleep(0.5)


def titulo(msg):
    tam = len(msg) + 30
    print('-' * tam)
    print(f'{msg:^{tam}}')
    print('-' * tam)

