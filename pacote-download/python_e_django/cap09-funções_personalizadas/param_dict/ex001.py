def registro(**kwargs):
    nome = kwargs['nome']
    idade = kwargs['idade']
    sexo = kwargs['sexo']
    if idade >= 18:
        dirigir = True
    else:
        dirigir = False

    pessoa = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'hab': dirigir
    }
    return pessoa


cadastro = [
    {'nome': 'João', 'idade': 17, 'sexo': 'M'},
    {'nome': 'Maria', 'idade': 56, 'sexo': 'F'},
    {'nome': 'Epitáfio', 'idade': 27, 'sexo': 'M'},
    {'nome': 'Rosângela', 'idade': 12, 'sexo': 'F'}
]

pessoa = dict()

for item in cadastro:
    if item['nome'] == 'Rosângela':
        pessoa = item

res = registro(**pessoa)

print(f'Com {res["idade"]} anos {res["nome"]} pode dirigir: {res["hab"]}')

