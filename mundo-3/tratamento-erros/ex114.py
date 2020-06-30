import requests
from requests.exceptions import ConnectionError

try:
    site = requests.get('http://pudim.com.br')
except ConnectionError:
    print('O site pudim.com.br está inacessível no momento.')
else:
    print('O site pudim.com.br está acessível :)')