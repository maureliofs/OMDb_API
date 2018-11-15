import requests
import json
from operator import itemgetter
from collections import OrderedDict

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
        #OrderedDict(sorted(dic.items(), key=lambda t: t[1]))
        for i in dic['Search']:
            print("Titulo: " + i['Title'] + "\n" "Ano: " + i['Year'])
            # return print('{' + '"Title"' + ':"' + dic['Title'] + '",'+'"Year"'+':"' + dic['Year'] + '"}')