import requests
import json
import time

        #script em python para consumir api do via cep

        #loop para percorrer a lista de ceps
for numero in range(0,100000,1050):
    cepformatado =(f'091{numero:05d}')
    cep = cepformatado
    print(cepformatado)
    time.sleep(1)
    

       #loop para fazer as requisições a api  
    for ceps in cep:
        #solicitar a requisição
        resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        #armazena a resposta JSON
        dados = resposta.json()
        print(dados)
        dados = json.dumps(dados, ensure_ascii=False)
        print(dados)
        #validação da requisição para checar status code e se há erro na resposta
        if resposta.status_code == 200 and 'erro' not in dados:
            print('Requisição bem sucedida')
        #filtrar os dados desejados
            dadosfiltrados = {
                dados.get('uf'):{
                    dados.get('localidade'):{
                        dados.get('logradouro'):dados.get('cep')
                    }
                }
            }
        
            print(dadosfiltrados)
        else:
            print('Faixa de cep não encontrada')
        break
    
