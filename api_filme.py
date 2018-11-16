import requests
import json
from operator import itemgetter
from collections import OrderedDict
import operator

def requisicao(nome):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=5b5be94f&type=movie&s='+nome)
        return req
    except:
        print('Erro de conexão')
        return None

while True:
    nome = input('Digite o nome do filme ou EXIT para sair: ')
    if nome == 'EXIT':
        exit()
    else:
        result = requisicao(nome)
        dic = json.loads(result.text)
        print('----------------------------------------------')
        for i in sorted(dic['Search'], key=operator.itemgetter('Year')):
            print("Titulo:", i['Title'])
            print("Ano:", i['Year'])
            print('----------------------------------------------')