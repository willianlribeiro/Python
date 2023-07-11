valor = 'm'
valorf = 'f'
s = ''
while s != valor and s != valorf:
    print('A mensagem aparecerá ate digitar um valor correto.')
    s = str(input('De qual sexo você é [\033[34mM\033[m ou \033[31mF\033[m]?')).lower()
print('Correto')
