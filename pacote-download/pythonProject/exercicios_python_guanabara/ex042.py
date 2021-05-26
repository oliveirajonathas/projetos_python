"""
042) Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero, Isósceles ou Escaleno.
"""
lado1 = float(input('Primeira dimensão: '))
lado2 = float(input('Segunda dimensão: '))
lado3 = float(input('Terceira dimensão: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 != lado2 != lado3 != lado1: #Enquanto a igualdade, na linha 12, é inclusiva, a
    #diferença precisa testar todas as possibilidades!
        print('Será formado um triângulo ESCALENO!')
    elif lado1 == lado2 == lado3:
        print('Será formado um triângulo EQUILÁTERO!')
    else:
        print('Será formado um triângulo ISÓSCELES!')
else:
    print('Não é possível formar um triângulo com as dimensões escolhidas')
