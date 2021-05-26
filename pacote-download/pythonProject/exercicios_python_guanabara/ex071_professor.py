valor = int(input('Quanto deseja sacar? '))
cedula = 50
total_cedulas = 0

while True:
    if valor >= cedula:
        valor -= cedula
        total_cedulas += 1
        print(valor)
    else:
        if total_cedulas > 0:
            print(f'{total_cedulas} de R${cedula:.2f}')
            total_cedulas = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if valor == 0:
            break
print('{:-^20}'.format(' Pode retirar o dinheiro '))
