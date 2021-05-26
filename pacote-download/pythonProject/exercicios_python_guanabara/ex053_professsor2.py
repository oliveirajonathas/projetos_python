frase = str(input("Digite a frase: ")).strip().upper()
junto = frase.split()
junto = ''.join(junto)
inverso = junto[::-1]

if junto == inverso:
    print('A frase "{}" é um PALÍNDROMO'.format(frase))
else:
    print('A frase "{}" não é um PALÍNDROMO'.format(frase))
