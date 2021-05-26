"""
Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta
"""
elementos = []
expressao = str(input('Digite uma expressão matemática: ')).strip()
for caractere in expressao:
    elementos.append(caractere)
aberto = 0
fechado = 0

if '(' in expressao:
    for item in elementos:
        if item == '(':
            aberto += 1
        elif item == ')':
            fechado += 1
    if aberto == fechado:
        print('Sua expressão é válida!')
    else:
        print('Expressão inválida!')
