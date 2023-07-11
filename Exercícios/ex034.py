salario = int(input('Coloque o valor do seu salário para calcular o aumento: '))
if salario >= 1250:
    salario = salario + salario*0.10
else:
    salario = salario + salario*0.15
print('O valor com o aumento salarial fica: R${}'.format(salario))