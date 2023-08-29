geral = list()
dados = dict()
somaidades = media = 0
mulheres = list()
maisvelhos = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome:'))
    dados['sexo'] = str(input('Sexo [M/F]:'))
    dados['idade'] = int(input('Idade:'))
    if dados['sexo'] in 'Ff':
        mulheres.append(dados.copy())
    somaidades += dados['idade']
    geral.append(dados.copy())
    continuar = str(input('Adicionar mais pessoas? [S/N]'))
    media = somaidades / len(geral)
    if dados['idade'] >= media:
        maisvelhos.append(dados.copy())
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {len(geral)} pessoas')
print(f'A média de idade é {media:.2f} anos')
print(f"As mulheres cadastradas: ")
for m, n in enumerate(mulheres):
    print(f"{n['nome']}")
print(f'Os que tem idade acima da média dos cadastrados são:')
for p, np in enumerate(maisvelhos):
    print(f'{np["nome"]} ')
