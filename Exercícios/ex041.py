from datetime import date
print('Preencha o campo com seu ano de nascimento para saber sua categoria')
idade = int(input('Qual ano nasceu?'))
anos = date.today().year - idade
if anos < 9:
    print('Sua categoria é a \033[1;36mMIRIM\033[m')
elif anos < 14:
    print('Sua categoria é a \033[1;34mINFANTIL\033[m')
elif anos < 19:
    print('Sua categoria é a \033[1;35mJUNIOR\033[m')
elif anos < 20:
    print('Sua categoria é a \033[1;30mSENIOR\033[m')
else:
    print('Sua categoria é a \033[1;47mMASTER\033[m')
print('05 / 05 /',date.today().year)