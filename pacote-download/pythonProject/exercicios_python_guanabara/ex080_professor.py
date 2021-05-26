lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:  # Se o valor for o primeiro digitado ou for maior que o último elemento da lista, ele é acrescentado
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:  # Se o valor nem é o primeiro e nem é maior que o último, será um valor intermediário
        pos = 0
        while pos < len(lista):  # Aqui, vamos varrer cada elemento da lista
            if n <= lista[pos]:  # Se o valor digitado é menor ou igual ao elemento da lista
                lista.insert(pos, n)  # Inserimos o valor naquela posição da lista
                print(f'Adicionado na posição {pos}')
                break  # O break interrompe a execução do while assim que o valor intermediário é inserido
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram: {lista}')
