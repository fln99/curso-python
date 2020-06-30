import requests
from requests.exceptions import ConnectionError

try:
    r = requests.get('http://pudim.com.br')
except ConnectionError:
    print('O site pudim.com.br não está acessível!')
else:
    print('O site pudim.com.br está acessível.')