import requests
import json
import time

#script em python para consumir api do via cep

#loop para percorrer a lista de ceps
for numero in range(0,1000000):
    cepformatado =(f'09{numero:06d}') #converte o cep para o formato de 8 Digitos
    cep = cepformatado #armazena o cep em 8 digitos para uso na requisição
    print(cepformatado) # apenas para debug
    time.sleep(0.5) # para limitar o tempo de interação entre as requisições para não gerar bloqueios


    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/') #efetua a requisição na api do via cep
    
    dados_dict = resposta.json()#armazena a resposta JSON
    print(dados_dict) #apenas para debug
    dados_str = json.dumps(dados_dict, ensure_ascii=False) #conversão do json para string e ajuste de caracteres
    print(dados_str) #apenas para debug
    
    if resposta.status_code == 200 and 'erro' not in dados_dict: #validação da requisição para checar o status code e se há erro na resposta
        print('Requisição bem sucedida') #apenas para debug
        
        #filtro dos dados e armazenamento no dicionário aninhado
        dadosfiltrados = {
            dados_dict.get('uf'):{
                   dados_dict.get('localidade'):{
                    dados_dict.get('logradouro'):dados_dict.get('cep')
                }
            }
        }
        
        print(dadosfiltrados) #apenas para debug
    else:
        print('Faixa de cep não encontrada') #apenas para debug caso a faixa de cep n seja localizada

