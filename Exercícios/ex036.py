cores = {'Azul':'\033[7m',
         'Amarelor':'\033[7;37;41m',
         'Limpa':'\033[m'
         }
emprestimo = int(input('Informe primeiramento o {}valor da casa{} que pretende comprar:'.format(cores['Azul'],cores['Limpa'])))
valor = int(input('Agome me informa sua {}renda mensal'.format(cores['Azul'])))
tempo = int(input('Em {}quantos anos{} pretende pagar imóvel?'.format(cores['Azul'],cores['Limpa'])))
anos = tempo*12
prestacao = emprestimo/anos
if valor <= prestacao*0.3:
    print('{}Infelizmente não será possivel realizar o emprestimo{}'.format(cores['Amarelor'],cores['Limpa']))
else:
    print('Calculei aqui e o empréstimo pode ser liberado. A prestação ficaria R${:.2f} mais juros, em {}x vezes'.format(float(prestacao), anos))