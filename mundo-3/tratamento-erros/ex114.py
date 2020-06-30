# Minha resolução utilizando módulo instalado pelo pip.

import requests

try:
    site = requests.get('http://pudim.com.br')
except:
    print('O site pudim.com.br está inacessível no momento.')
else:
    print('O site pudim.com.br está acessível :)')

# Solução do professor Guanabara, com uma biblioteca 'built-in'.

# import urllib
# import urllib.request

# try:
#     site = urllib.request.urlopen('http://pudim.com.br')
# except urllib.error.URLError:
#     print('Deu erro.')
# else:
#     print('Não deu erro.')