from datetime import date
print('Digite o ano de nascimento de 7 pessoas e eu direi quantos são de maior e quantos não')
demaior = 0
demenor = 0
for c in range(0, 7):
    ano = date.today().year - int(input('Digite o ano de nascimento da {} pessoa'.format(c+1)))
    if ano >= 18:
        demaior += 1
    else:
        demenor += 1
print('Das datas informadas, {} são de maior e {} são de menor'.format(demaior, demenor))
