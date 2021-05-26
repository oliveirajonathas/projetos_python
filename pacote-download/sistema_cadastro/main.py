"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
import dados
import arquivo

while True:
    arquivo.titulo('MENU PRINCIPAL')
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
    print('\033[33m3\033[m - \033[34mSair do Sistema\033[m')
    print('-' * 44)
    opcao = dados.leiaint('\033[33mSua Opção:\033[m ', 1, 3)
    if opcao == 1:
        arquivo.ler()
    elif opcao == 2:
        arquivo.escrever()
    elif opcao == 3:
        break
arquivo.titulo('ATÉ LOGO!')