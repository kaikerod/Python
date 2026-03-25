from pymongo import MongoClient

# Definindo o MongoClient e definindo o endereço da conexão
client = MongoClient("mongodb://localhost:27017/")

# Selecionando o banco de dados relacionado com o cliente e que se chama escola
db = client["escola"]

# Selecionando a coleção relacionada com o banco de dados e que se chama estudantes
estudantes = db["estudantes"]

# Inserindo dados na coleção
estudantes.insert_one({"nome": "Joao", "idade": 20})

# Buscando dados no banco
for estudante in estudantes.find():
    print(estudante)