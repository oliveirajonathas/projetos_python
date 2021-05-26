"""
ex057) Faça um prograa que leia o sexo de uma pessoa, mas
só aceite 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto
"""
sexo = str(input('Digite o sexo:\n'
                 '[M] - Masculino\n'
                 '[F} - Feminino\n'
                 ' - Sua resposta: ')).strip().upper()[0]
print(sexo)
while sexo not in 'MmFf':
    print('Opção \033[31mINVÁLIDA\033[m. Tente novamente!\n')
    sexo = str(input('Digite o sexo:\n'
                     '[M] - Masculino\n'
                     '[F} - Feminino\n'
                     ' - Sua resposta: ')).strip().upper()[0]

print('Muito obrigado. Sexo "{}" registrado com sucesso.'.format(sexo))
