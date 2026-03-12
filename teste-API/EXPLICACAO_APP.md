# 📄 Explicação Detalhada: `app.py`

## 📌 Visão Geral

Este script Python realiza o consumo de uma **API REST** pública que retorna dados de restaurantes em formato JSON. Após receber e processar esses dados, o script **organiza as informações por restaurante** e **salva cada um em um arquivo `.json` separado** no diretório local.

---

## 📦 Importações

```python
import requests
import json
```

| Biblioteca | Função |
|---|---|
| `requests` | Biblioteca de terceiros usada para fazer requisições HTTP (GET, POST, etc.) de forma simples e intuitiva. |
| `json` | Biblioteca nativa do Python para serializar (converter objeto Python → texto JSON) e desserializar (texto JSON → objeto Python) dados. |

> ⚠️ **Atenção:** A biblioteca `requests` **não é nativa** do Python. Para usá-la, é preciso instalá-la com:
> ```bash
> pip install requests
> ```

---

## 🌐 Fazendo a Requisição HTTP

```python
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)
```

### O que acontece aqui?

1. **`url`** — Armazena o endereço (endpoint) da API que contém os dados dos restaurantes.
2. **`requests.get(url)`** — Envia uma requisição do tipo **GET** para a URL. Esse método solicita ao servidor que retorne os dados disponíveis naquele endereço.
3. **`response`** — É o objeto de resposta retornado pela requisição. Ele contém:
   - O status da resposta (ex.: `200 OK`, `404 Not Found`).
   - O corpo da resposta (os dados JSON).
4. **`print(response)`** — Exibe a representação do objeto de resposta, que geralmente mostra algo como `<Response [200]>`, indicando o código de status HTTP.

---

## ✅ Verificando o Status da Resposta

```python
if response.status_code == 200:
    ...
else:
    print(f'Erro ao fazer a requisição: {response.status_code}')
```

### Códigos de Status HTTP mais comuns

| Código | Significado |
|---|---|
| `200` | **OK** — Requisição bem-sucedida. |
| `404` | **Not Found** — Recurso não encontrado. |
| `500` | **Internal Server Error** — Erro no servidor. |

O atributo **`response.status_code`** retorna o código numérico HTTP da resposta. O script só processa os dados se o status for `200` (sucesso). Caso contrário, exibe uma mensagem de erro informativa com o código recebido.

---

## 🔄 Processando os Dados JSON

```python
dados_json = response.json()
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

### Passo a passo detalhado:

#### 1. Convertendo a resposta para Python
```python
dados_json = response.json()
```
O método `.json()` converte automaticamente o corpo da resposta (texto JSON) em uma **lista de dicionários Python** — cada dicionário representa um item do cardápio de um restaurante.

**Exemplo de estrutura esperada da API:**
```json
[
  {
    "Company": "Restaurante A",
    "Item": "Pizza",
    "price": "35.90",
    "description": "Pizza de calabresa"
  },
  {
    "Company": "Restaurante A",
    "Item": "Suco",
    "price": "8.00",
    "description": "Suco de laranja"
  },
  {
    "Company": "Restaurante B",
    "Item": "Hambúrguer",
    "price": "25.00",
    "description": "Hambúrguer artesanal"
  }
]
```

---

#### 2. Criando o dicionário agrupador
```python
dados_restaurante = {}
```
Um **dicionário vazio** é criado para servir como estrutura de agrupamento. A chave será o **nome do restaurante** e o valor será uma **lista de itens** daquele restaurante.

---

#### 3. Iterando sobre cada item da API
```python
for item in dados_json:
    nome_do_restaurante = item['Company']
```
O laço percorre cada elemento da lista. Para cada item, extrai o nome do restaurante a partir da chave `'Company'`.

---

#### 4. Agrupando itens por restaurante
```python
    if nome_do_restaurante not in dados_restaurante:
        dados_restaurante[nome_do_restaurante] = []

    dados_restaurante[nome_do_restaurante].append({
        'item': item['Item'],
        'price': item['price'],
        'description': item['description']
    })
```

- **`if nome_do_restaurante not in dados_restaurante`** — Verifica se o restaurante **ainda não existe** como chave no dicionário. Se não existir, cria uma lista vazia para ele.
- **`.append(...)`** — Adiciona um novo dicionário com os dados do item (`item`, `price`, `description`) à lista do restaurante correspondente.

**Resultado final de `dados_restaurante` após o loop:**
```python
{
    "Restaurante A": [
        {"item": "Pizza", "price": "35.90", "description": "Pizza de calabresa"},
        {"item": "Suco", "price": "8.00", "description": "Suco de laranja"}
    ],
    "Restaurante B": [
        {"item": "Hambúrguer", "price": "25.00", "description": "Hambúrguer artesanal"}
    ]
}
```

---

## 💾 Salvando os Dados em Arquivos JSON

```python
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)
```

### Passo a passo:

#### 1. Iterando sobre o dicionário agrupado
```python
for nome_do_restaurante, dados in dados_restaurante.items():
```
O método `.items()` retorna pares `(chave, valor)` do dicionário. Aqui:
- `nome_do_restaurante` = nome do restaurante (ex.: `"Restaurante A"`)
- `dados` = lista de itens daquele restaurante

---

#### 2. Definindo o nome do arquivo
```python
nome_do_arquivo = f'{nome_do_restaurante}.json'
```
Usa uma **f-string** para criar o nome do arquivo dinamicamente. Por exemplo: `Restaurante A.json`.

---

#### 3. Abrindo e escrevendo no arquivo
```python
with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)
```

| Parâmetro | Significado |
|---|---|
| `'w'` | Modo de abertura: escrita. Cria o arquivo se não existir; sobrescreve se existir. |
| `encoding='utf-8'` | Garante suporte a caracteres especiais como acentos (`ã`, `ç`, `é`). |
| `json.dump(dados, arquivo, ...)` | Serializa o objeto Python (`dados`) e escreve no arquivo. |
| `indent=2` | Formata o JSON com indentação de 2 espaços, deixando-o legível. |
| `ensure_ascii=False` | Permite que caracteres não-ASCII (acentos, etc.) sejam salvos diretamente, sem escape. |

O operador **`with`** é um gerenciador de contexto que garante que o arquivo seja **fechado corretamente** após a escrita, mesmo que ocorra um erro.

**Exemplo de conteúdo de `Restaurante A.json` gerado:**
```json
[
  {
    "item": "Pizza",
    "price": "35.90",
    "description": "Pizza de calabresa"
  },
  {
    "item": "Suco",
    "price": "8.00",
    "description": "Suco de laranja"
  }
]
```

---

## 🗺️ Fluxo Geral do Script

```
Início
  │
  ▼
Faz requisição GET para a API
  │
  ▼
Status é 200? ──── NÃO ──► Exibe mensagem de erro
  │
 SIM
  │
  ▼
Converte JSON → lista de dicionários Python
  │
  ▼
Agrupa itens por nome do restaurante em um dicionário
  │
  ▼
Para cada restaurante:
  └─► Cria um arquivo .json com seus itens
  │
  ▼
Fim
```

---

## ✨ Conceitos-Chave Utilizados

| Conceito | Descrição |
|---|---|
| **Requisição HTTP GET** | Método usado para buscar/recuperar dados de um servidor. |
| **JSON** | Formato leve de troca de dados amplamente usado em APIs. |
| **Dicionário Python** | Estrutura de dados `{chave: valor}` usada para agrupar os restaurantes. |
| **Laço `for`** | Itera sobre coleções de dados (listas e dicionários). |
| **f-string** | Forma moderna de formatar strings em Python 3.6+. |
| **Gerenciador de contexto (`with`)** | Garante abertura e fechamento seguro de recursos como arquivos. |
| **`json.dump()`** | Serializa objetos Python para o formato JSON e os escreve em um arquivo. |