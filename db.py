import datetime 
from pymongo import MongoClient

user = 'localhost'
port = 27017

conn = MongoClient(user, port)

# uma única instancia do MongoDB pode suportar diversos
# banco de dados

db = conn.cadastrodb # criando bd cadastrodb

# uma colecao é um grupo de documentos armazenados no MongoDB
# relativamente parecido com conceito de tabelas de banco de dados relacionais

collection = db.cadastrodb


person1 = {
    "nome": "Jefferson",
    "email": "jeff@test.com",
    "senha": "teste1234"
}

collection = db.persons

person_id = collection.insert_one(person1).inserted_id

print(db.name) # nome do banco de dados

print(db.list_collection_names()) # listando as coleções disponiveis

# utilizando List Comprehension:
person = [p for p in collection.find()]

print(person)

print(collection.find_one({"nome": "J"}))
