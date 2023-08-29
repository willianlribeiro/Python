from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos, o voto não é obrigatório'
    elif 18 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é opcional'
    else:
        return f'Com {idade} anos, o voto é obrigatório'


nasc = int(input('Em que ano você nasceu?'))
print(voto(nasc))
