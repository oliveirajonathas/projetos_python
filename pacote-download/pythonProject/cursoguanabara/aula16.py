lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[::2])
print(lanche[1:3])
print(lanche[2:])

print(len(lanche))

# Indicado quando precisamos de cada elemento e também da posição de cada elemento.
for cont in range(0, len(lanche)):
    print(cont, lanche[cont])

# Indicado quando precisamos apenas de cada elemento
for comida in lanche:
    print(comida)

# Essa forma reproduz o mesmo resultado do for com range no acesso aos elementos das tuplas
for posicao, comida in enumerate(lanche):
    print(posicao, comida)

# a operação abaixo junta as duas tuplas na ordem que são "somadas"
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8)) # retorna a posição da primeira ocorrência do elemento 8, partindo da posição 0
print(c.index(5, 2)) # retorna a posição da primeira ocorrência do elemento 5, partindo da posição 2
print(c.count(5))

# o Python aceita deferentes tipos de dados numa mesma variável composta
pessoa = ('Jonathas', 29, 'M', 114.5)
print(pessoa)
# O comando del APAGA a tupla... é a única coisa que se pode fazer com uma tupla depois de definida
del(pessoa)
