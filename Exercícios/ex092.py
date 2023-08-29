from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Digite seu nome:'))
ano = int(input('Qual ano de nascimento ? ####'))
cadastro['idade'] = datetime.now().year - ano
cadastro['ctps'] = int(input('Número da carteira de trabalho (Digite 0 caso não tenha)'))
if cadastro['ctps'] != 0:
    cadastro['ano de contratação'] = int(input('Ano de contratação:'))
    cadastro['salário'] = str(input('Salário:'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['ano de contratação'] + 35) - datetime.today().year)
for k, v in cadastro.items():
    print(f' - {k} tem valor {v}')