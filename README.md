Desafio 1 mentoria: Busca de CEPs pelo Via CEP

Este projeto é composto por um script Python projetado para iterar sobre uma faixa de CEPs e consultar dados de endereços utilizando a API pública do ViaCEP.

Funcionalidade Principal
Gerar CEPs em uma faixa definida que pode ser formatada conforme a necessidade (nesse projeto iniciamos nas faixas a partir de 09000000 indo até 09999999).

Faz requisições para a API do ViaCEP para cada CEP gerado.

Valida a resposta para identificar CEPs válidos e retorna dados formatados (UF, Localidade, Logradouro e CEP).

Possui um time.sleep() para a frequência das requisições.

É necessário para este projeto possuir Python com as bibliotecas requests, json e time instaladas 

Link para a Api utilziada https://viacep.com.br/

Como Utilizar:
Clone o repositório para a sua máquina local.
Certifique-se de ter as bibliotecas instaladas e execute o script principal.

O projeto prevê melhorias como o tratamento mais adequado de erros, inclusão de input de usuário por faixa de cep determinada e inserção de funções. 