"""
039) Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
from datetime import date
sexo = str(input('Qual seu sexo? Masculino - M ou Feminino - F\n')).upper()

if sexo == 'M':
    ano_nascimento = int(input('Em que ano você nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        prazo = 18 - idade
        alistamento = ano_atual + prazo
        print('Você tem {} anos! Deverá se alistar no serviço militar daqui a {} anos. Seu alistamento '
              'será em {}'.format(idade, prazo, alistamento))
    elif idade == 18:
        print('Você está com {} anos! É hora de se alistar no serviço militar!'.format(idade))
    else:
        prazo = idade - 18
        alistamento = ano_atual - prazo
        print('Você tem {} anos e já deveria ter se alistado há {} anos! Compareça a uma unidade '
              'do serviço militar, pois deveria ter se alistado em {}!'.format(idade, prazo, alistamento))
elif sexo == 'F':
    print('No Brasil, mulheres não são obrigados a realizarem o alistamento!')
else:
    print('Opção inválida! Tente novamente!')
