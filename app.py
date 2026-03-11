import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    print(f'\n Response: {response.status_code}\n')
    dados_company = {}

    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_company:
            dados_company[nome_restaurante] = []

        dados_company[nome_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })

else:
    print (f'O erro foi: {response.status_code}')

for nome_restaurante, dados in dados_company.items():
    nome_do_arquivo = f'{nome_restaurante}.json'
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante,indent=4)