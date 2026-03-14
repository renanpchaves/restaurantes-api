# RESTAURANTES-API

API simples para consulta de cardápios de restaurantes com sistema de cache, consumindo uma API externa pra gerar uma nova.

## TECNOLOGIAS

- **Python 3.x**
- **FastAPI** - Framework web moderno e rápido
- **Requests** - Cliente HTTP para consumir API externa
- **Uvicorn** - Servidor ASGI (para rodar a aplicação)

## ROTAS

`GET /api/restaurantes/` - Retorna todos os restaurantes e seus cardápios.  
`GET /api/restaurantes/?restaurante={nome}` - Retorna o cardápio de um restaurante específico.  

**Exemplo de parâmetros para buscar um restaurante específico:**
```bash
curl http://localhost:8000/api/restaurantes/?restaurante=KFC
```

**Resposta:**
```json
{
    "Restaurante": "KFC",
    "Cardapio": [
        {
            "item": "Limited Time Cinnabon Dessert  Biscuits",
            "price": 58.53,
            "description": "Uma explosão de sabores em cada mordida."
        },
  ]
}
```

## Como executar
```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`  
Documentação interativa: `http://localhost:8000/docs`