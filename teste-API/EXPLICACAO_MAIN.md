# 📄 Explicação Detalhada: `main.py`

> **Arquivo:** `teste-API/main.py`  
> **Tecnologia principal:** [FastAPI](https://fastapi.tiangolo.com/)  
> **Propósito:** Criar uma API REST que expõe dados de restaurantes consultados a partir de uma fonte externa (API pública).

---

## 📦 Visão Geral

Este arquivo define uma **API REST** usando o framework **FastAPI**. A API possui dois endpoints:

| Método | Rota                  | Descrição                                      |
|--------|-----------------------|------------------------------------------------|
| `GET`  | `/api/hello`          | Retorna uma mensagem simples de boas-vindas    |
| `GET`  | `/api/restaurantes/`  | Retorna dados de restaurantes de uma API externa |

---

## 🔍 Análise Linha por Linha

### 1. Importações

```python
from fastapi import FastAPI, Query
import requests
```

| Importação      | Origem    | Para que serve                                                                                                |
|-----------------|-----------|---------------------------------------------------------------------------------------------------------------|
| `FastAPI`       | `fastapi` | Classe principal do framework. É ela que cria a aplicação e gerencia as rotas.                               |
| `Query`         | `fastapi` | Utilitário para tratar **parâmetros de query string** na URL (ex: `?restaurante=McDonald's`). Permite definir valores padrão e validações. |
| `requests`      | `requests` | Biblioteca HTTP para fazer chamadas a APIs externas. Usada aqui para buscar os dados dos restaurantes.       |

---

### 2. Criação da Aplicação

```python
app = FastAPI()
```

- Instancia o objeto principal da aplicação FastAPI.
- Todos os endpoints (rotas) serão registrados nesse objeto `app`.
- Para rodar a API localmente, usa-se o comando:
  ```bash
  uvicorn main:app --reload
  ```

---

### 3. Endpoint 1 — Boas-vindas

```python
@app.get('/api/hello')
def hello_world():
  '''
  Endpoint para retornar uma mensagem de boas-vindas
  '''
  return {'Hello': 'World'}
```

#### 🔹 Como funciona:

- **`@app.get('/api/hello')`** → Decorador que registra a função como um handler para requisições HTTP `GET` na rota `/api/hello`.
- A função `hello_world()` não recebe parâmetros.
- Retorna um **dicionário Python**, que o FastAPI converte automaticamente em **JSON**:
  ```json
  {
    "Hello": "World"
  }
  ```

#### ✅ Exemplo de uso:
```
GET http://localhost:8000/api/hello
```

---

### 4. Endpoint 2 — Lista de Restaurantes

```python
@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
```

#### 🔹 Parâmetro de Query

```python
restaurante: str = Query(None)
```

- **`restaurante`** é um parâmetro opcional da **query string** da URL.
- O tipo `str` indica que espera uma string como valor.
- `Query(None)` define que:
  - O parâmetro vem da **query string** (após o `?` na URL).
  - O valor **padrão é `None`** (ou seja, é totalmente opcional).

#### ✅ Exemplos de uso:
```
GET /api/restaurantes/                         → Retorna TODOS os restaurantes
GET /api/restaurantes/?restaurante=McDonald's  → Filtra apenas o McDonald's
```

---

### 5. Chamada à API Externa

```python
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
```

- A cada requisição ao endpoint, o código busca os dados de restaurantes de uma **API externa** (um arquivo JSON hospedado no GitHub Pages).
- `requests.get(url)` realiza uma requisição HTTP `GET` e armazena a resposta em `response`.

---

### 6. Verificação do Status HTTP

```python
if response.status_code == 200:
    dados_json = response.json()
```

- **`response.status_code`** contém o código HTTP da resposta (ex: `200 OK`, `404 Not Found`, `500 Internal Server Error`).
- Somente se a resposta for **`200` (sucesso)**, os dados são processados.
- **`response.json()`** converte o corpo da resposta (texto JSON) em uma **lista/dicionário Python**.

---

### 7. Retorno sem Filtro (todos os restaurantes)

```python
if restaurante is None:
    return {'Dados': dados_json}
```

- Se o parâmetro `restaurante` **não foi fornecido** na URL, retorna **todos os dados** da API externa sem filtro.
- Resposta JSON:
  ```json
  {
    "Dados": [ ...lista completa de itens... ]
  }
  ```

---

### 8. Filtro por Restaurante

```python
dados_restaurante = []
for item in dados_json:
    if item['Company'] == restaurante:
        dados_restaurante.append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
return {'Restaurante': restaurante, 'Dados': dados_restaurante}
```

#### 🔹 Passo a passo:

1. **`dados_restaurante = []`** → Cria uma lista vazia para guardar os resultados filtrados.
2. **`for item in dados_json:`** → Itera sobre cada item retornado pela API externa. Cada `item` é um dicionário representando um produto de um restaurante.
3. **`if item['Company'] == restaurante:`** → Filtra apenas os itens cujo campo `Company` (nome do restaurante) seja igual ao parâmetro informado na URL.
4. **`.append({...})`** → Adiciona um novo dicionário com apenas os campos relevantes:
   - `item` → Nome do produto (campo `Item` da API externa)
   - `price` → Preço do produto
   - `description` → Descrição do produto
5. **`return {...}`** → Retorna um JSON com o nome do restaurante filtrado e a lista de dados.

#### 📬 Exemplo de Resposta:
```json
{
  "Restaurante": "McDonald's",
  "Dados": [
    {
      "item": "Big Mac",
      "price": "19.90",
      "description": "Pão, carne, alface, queijo..."
    }
  ]
}
```

---

### 9. Tratamento de Erro

```python
else:
    return {'Erro': f'Erro ao fazer a requisição: {response.status_code} - {response.text}'}
```

- Se a API externa retornar um status **diferente de 200**, a função retorna uma mensagem de erro com:
  - O **código HTTP** retornado.
  - O **corpo da resposta** de erro (`response.text`), útil para diagnóstico.

#### 📬 Exemplo de Resposta de Erro:
```json
{
  "Erro": "Erro ao fazer a requisição: 503 - Service Unavailable"
}
```

---

## 🗺️ Fluxo Completo da Função `get_restaurantes`

```
Requisição GET /api/restaurantes/?restaurante=X
         │
         ▼
   Chama API externa (requests.get)
         │
    ┌────┴────┐
    │ Status  │
    ├─────────┤
    │  200 ✅ │──► restaurante é None? ──► Sim ──► Retorna todos os dados
    │         │                        │
    │         │                        └──► Não ──► Filtra por 'Company'
    │         │                                    └──► Retorna dados filtrados
    ├─────────┤
    │ Outro ❌│──► Retorna mensagem de erro com status e texto
    └─────────┘
```

---

## 📊 Estrutura de Dados da API Externa

Os dados retornados pela URL externa têm a seguinte estrutura (por item):

```json
{
  "Company": "Nome do Restaurante",
  "Item": "Nome do Produto",
  "price": "Preço",
  "description": "Descrição do produto"
}
```

---

## 🚀 Como Rodar a API

### 1. Instale as dependências:
```bash
pip install fastapi uvicorn requests
```

### 2. Execute o servidor:
```bash
uvicorn main:app --reload
```

### 3. Acesse a documentação automática:
| Interface         | URL                                      |
|-------------------|------------------------------------------|
| Swagger UI        | http://localhost:8000/docs               |
| ReDoc             | http://localhost:8000/redoc              |

---

## 🔑 Conceitos-Chave Usados

| Conceito          | Descrição                                                                 |
|-------------------|---------------------------------------------------------------------------|
| **FastAPI**       | Framework web moderno e rápido para construção de APIs em Python          |
| **Decorator**     | `@app.get(...)` registra a função como handler de uma rota HTTP           |
| **Query Param**   | Parâmetro passado na URL após `?` (ex: `?restaurante=McDonald's`)         |
| **requests**      | Biblioteca para fazer chamadas HTTP a APIs externas                       |
| **JSON**          | Formato de troca de dados entre a API e seus clientes                     |
| **Status Code**   | Código numérico que indica o resultado de uma requisição HTTP             |

---

## 🔗 Relação com `app.py`

O arquivo `app.py` é um **script auxiliar** que:
- Consome a mesma API externa.
- Organiza os dados por restaurante usando um dicionário.
- Salva cada restaurante em um arquivo `.json` separado no disco local.

Enquanto o `main.py` **serve** os dados via API REST, o `app.py` **baixa e salva** os dados localmente. São propósitos complementares.
