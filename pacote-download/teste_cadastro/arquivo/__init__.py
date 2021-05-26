import estrutura


def existearquivo():
    try:
        arq = open('cadastro.txt', 'rt')
    except FileNotFoundError:
        criararquivo()
    else:
        arq.close()


def criararquivo():
    try:
        arq = open('cadastro.txt', 'wt+')
    except:
        print('Erro ao tentar crar o arquivo.')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def lerarquivo():
    estrutura.cabecalho('PESSOAS CADASTRADAS')
    try:
        arq = open('cadastro.txt', 'rt')
    except FileNotFoundError or FileExistsError:
        print('ERRO ao LER o arquivo! Arquivo não encontrado, ou não existe!')
    else:
        conteudo = arq.readlines()
        for linha in conteudo:
            linha = linha.split(';')
            linha[1] = linha[1].replace('\n', '')
            print(f'{linha[0]:<30}{linha[1]:>3} anos')
        arq.close()


def escreverarquivo(nome, idade):
    try:
        arq = open('cadastro.txt', 'at')
    except FileNotFoundError or FileExistsError:
        print('ERRO ao ESCREVER o arquivo! Arquivo não encontrado, ou não existe!')
    else:
        cad = f'{nome};{idade}\n'
        arq.write(cad)
        arq.close()

