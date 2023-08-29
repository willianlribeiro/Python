def notas(* num, sit=False):
    nt = dict()
    nt['Qntd notas'] = len(num)
    nt['Maior nota'] = max(num)
    nt['Menor nota'] = min(num)
    nt['Média notas'] = sum(num) / len(num)
    if sit:
        if nt['Média notas'] >= 7:
            nt['Situação'] = 'Boa'
        elif nt['Média notas'] >= 5:
            nt['Situação'] = 'Razoável'
        else:
            nt['Situação'] = 'Ruim'
    return nt


print(notas(3, 10, 10, 6, 8, sit=True))
