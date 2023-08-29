import urllib
import urllib.request

pudim = 'http://pudim.com.br/'
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('Não é possível acessar o site no momento')
else:
    print('O site está disponível')
