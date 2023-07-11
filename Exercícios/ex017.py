catop = int(input('Coloque aqui o valor do cateto oposto'))
catad = int(input('Coloque aqui o valor do cateto adjacente'))
hip = (catad**2+catop**2)**(1/2)

print('A hipotenusa é igual a {:.2f}'.format(hip))