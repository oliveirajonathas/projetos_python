import estrutura
import validacoes
import arquivo

arquivo.existearquivo()

while True:
    estrutura.cabecalho('SISTEMA DE CADASTRO')
    opcao = estrutura.menu(['Listar Pessoas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        arquivo.lerarquivo()
    if opcao == 2:
        estrutura.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = validacoes.leiainteiro('Idade: ')
        arquivo.escreverarquivo(nome, idade)
    if opcao == 3:
        break
