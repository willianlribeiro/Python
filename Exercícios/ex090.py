nome = str(input('Nome'))
situ = ''
media = int(input(f'Média de {nome}'))
if media < 6:
    situ = 'Reprovado'
if media == 6:
    situ = 'Recuperação'
if media > 6:
    situ = 'Aprovado'
notas = {'nome': nome, 'media': media}
print(f'O nome é : {notas["nome"]}')
print(f'A média dele(a) é : {notas["media"]}')
print(f'Situação de {notas["nome"]} : {situ}')
