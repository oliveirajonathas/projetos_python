"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
no intervalo de 1 até 500
"""
soma = 0
for numero in range(1, 501, 2):#o passo 2 exclui o número de iterações que consideram números pares, melhorando
    #a eficiência do programa
    if numero % 3 == 0:
        soma += numero
print('A soma é: {}'.format(soma))
