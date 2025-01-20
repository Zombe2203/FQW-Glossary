import os
from pymongo import MongoClient

mongoURL = os.getenv('MONGOURL', 'mongodb://localhost:27017')
client = MongoClient(mongoURL)
database = client['glossaryDB']
collection = database['glossary']

print(client.list_database_names())
print(database.list_collection_names())
documents = collection.find()
responseDocument = []
for document in documents:
    responseDocument.append({
        'id': document['_id'],
        'concept': document['concept'],
        'definition': document['definition'],
        'source': document['source'],
        'childConcepts': document['childConcepts']
    })

print(responseDocument)