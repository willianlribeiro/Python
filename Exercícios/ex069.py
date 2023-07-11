contador = 0
mulhermaior = 0
while True:
    idades = int(input('Qual sua idade?'))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual sexo? [M/F]')).upper().strip()[0]
    if idades >= 18:
        contador += 1
    if sexo == 'F' and idades < 20:
        mulhermaior += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('O cadastro foi finalizado.')
print(f'Foram um total de {contador} pessoas maiores de 18 anos')
print(f'{mulhermaior} mulher(es) cadastrada(s) tem menos de 20 anos.')
