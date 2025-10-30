import requests
import json
import time

#script em python para consumir api do via cep
#cep = '01000000'
#loop para percorrer a lista de ceps
for numero in range(1,1000000):
    cepformatado =f'0{numero:07d}'
    cep = cepformatado
    print(cepformatado)
    time.sleep(2)
    for ceps in cepformatado:
        #solicitar a requisição
        resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        #validação da requisição
        if resposta.status_code == 200:
            print('Requisição bem sucedida')
            #armazenar os dados em formato json
            dados = resposta.json()
            #filtrar os dados desejados
            dadosfiltrados = {
            'cep': dados.get('cep'),
            'logradouro': dados.get('logradouro'),
            'bairro': dados.get('bairro'),
            'localidade': dados.get('localidade')
            }
            print(dadosfiltrados)
        else:
            print('Requisição mal sucedida')
        break





