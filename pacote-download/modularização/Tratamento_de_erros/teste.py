try:
    a = int(input('Numerador: '))
    b = int(input('Denominador '))
    r = a/b
except Exception as mostra:
    print(f'O erro foi: {mostra.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volta sempre! Muito obrigado!')
