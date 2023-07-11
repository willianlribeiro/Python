frase = str(input('Coloque uma frase e descubra se é um palindromo')).strip().lower()
frase2 = frase.split()
frasejunta = ''.join(frase2)
fraseinvertida = frasejunta[::-1]
if fraseinvertida == frasejunta:
    print('{} \033[35mé um Palindromo\033[m, pois fica igual de trás pra frente\n{}\n{}'.format(frase, frasejunta, fraseinvertida))
else:
    print('{} \033[35mnão\033[m é um  Palindromo'.format(frase))

