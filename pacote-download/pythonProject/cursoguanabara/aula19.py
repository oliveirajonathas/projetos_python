pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(pessoas)
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
print(20*'-')
for k, v in pessoas.items():
    print(f'{k} = {v}')