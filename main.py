from fastapi import FastAPI, Query, HTTPException
import requests
import time

app = FastAPI()
cache = {"data": None, "timestamp": 0}


def get_dados_cached():
    """
    Retorna dados com cache de 5min, com validação de erros
    """
    if time.time() - cache["timestamp"] > 300:
        url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            cache["data"] = response.json()
            cache["timestamp"] = time.time()
        except requests.exceptions.RequestException as e:
            if cache["data"]:
                return cache["data"]
            raise HTTPException(status_code=503, detail=f"Erro: {str(e)}")
    return cache["data"]


@app.get("/api/restaurantes/")
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para visualizar o cardapio dos restaurantes.
    """
    todos_dados_json = get_dados_cached()

    if restaurante is None:
        return {"Dados": todos_dados_json}

    dados_company = []
    for item in todos_dados_json:
        if item["Company"] == restaurante:
            dados_company.append(
                {
                    "item": item["Item"],
                    "price": item["price"],
                    "description": item["description"],
                }
            )

    if not dados_company:
        raise HTTPException(
            status_code=404, detail=f'Restaurante "{restaurante} não encontrado.'
        )  # validação caso exista typo no nome do restaurante na URL

    return {"Restaurante": restaurante, "Cardapio": dados_company}
