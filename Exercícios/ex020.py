import random
al1 = str(input('1 aluno'))
al2 = str(input('2 aluno'))
al3 = str(input('3 aluno'))
al4 = str(input('4 aiuno'))
ordap = [al1, al2, al3, al4]
random.shuffle(ordap)
print(ordap)