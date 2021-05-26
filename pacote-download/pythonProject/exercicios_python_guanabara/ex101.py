"""
Crie um programa que tenha uma função chamada voto()  que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
MENOR de 18 - Não vota
MAIOR de 65 anos - Voto Opcional
"""


def voto(ano_nasc):
    """
    Programa que informa se o voto é opcional, obrigatório ou negado a depender da idade do usuário
    :param ano_nasc: ano de nascimento do usuário
    :return: string informando se o voto é OPCIONAL, OBRIGATÓRIO ou NEGADO
    """
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade >= 65 or 16 <= idade < 18:
        resultado = f'Você tem {idade} anos. Seu voto é OPCIONAL!'
    elif idade < 16:
        resultado = f'Você tem {idade} anos. Por ser menor, NÃO PODE VOTAR!'
    else:
        resultado = f'Você tem {idade} anos. VOTO OBRIGATÓRIO!'
    return resultado


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
help(voto)