from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para visualizar o cardapio dos restaurantes.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        todos_dados_json = response.json()

        if restaurante is None:
            return {'Dados': todos_dados_json}

        print(f'\n Response: {response.status_code}\n')
        dados_company = []
        for item in todos_dados_json:
            if item['Company'] == restaurante:
                dados_company.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_company}

    else:
        return {'Erro': f'{response.status_code} - {response.text}'}