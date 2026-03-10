# Explicação do Código Python — API de Restaurantes

Este código faz o download de dados de restaurantes de uma API e os salva em arquivos JSON separados. Veja o passo a passo:

---

## 1. Importações

```python
import requests
import json
```

Importa as bibliotecas `requests` (para fazer chamadas HTTP) e `json` (para manipular arquivos JSON).

---

## 2. Requisição à API

```python
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
```

Faz uma requisição GET para uma URL que retorna uma lista de itens de restaurantes em formato JSON.

---

## 3. Verificação da Resposta

```python
if response.status_code == 200:
```

Verifica se a requisição foi bem-sucedida. O código `200` significa **OK** em HTTP.

---

## 4. Agrupamento dos Dados por Restaurante

```python
dados_restaurante = {}
for item in dados_json:
    nome_do_restaurante = item['Company']
    if nome_do_restaurante not in dados_restaurante:
        dados_restaurante[nome_do_restaurante] = []
    dados_restaurante[nome_do_restaurante].append({
        'item': item['Item'],
        'price': item['price'],
        'description': item['description']
    })
```

Percorre cada item da lista e os **agrupa por nome do restaurante**. O resultado é um dicionário onde:

- **Chave** → nome do restaurante
- **Valor** → lista com seus itens de cardápio (nome, preço e descrição)

---

## 5. Salvamento em Arquivos JSON

```python
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)
```

Para cada restaurante, cria um arquivo `.json` com o nome do restaurante (ex: `McDonald's.json`) contendo seus itens, preços e descrições.

| Parâmetro | Função |
|---|---|
| `ensure_ascii=False` | Garante que acentos e caracteres especiais sejam salvos corretamente |
| `indent=2` | Formata o JSON de forma legível com indentação de 2 espaços |

---

## Resumo do Fluxo

```
API → Lista de itens → Agrupa por restaurante → Cria um arquivo .json por restaurante
```
