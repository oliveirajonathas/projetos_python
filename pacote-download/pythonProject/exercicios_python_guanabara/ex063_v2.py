n = int(input('Quantos termos você quer mostrar? '))

hoje = 0
amanha = 1

print(hoje, '; ', amanha, '; ', end='')

qtd_termos = 2
while qtd_termos < n:
    depois = hoje + amanha
    print(depois, '; ', end='')
    hoje = amanha
    amanha = depois
    qtd_termos += 1
print('FIM')