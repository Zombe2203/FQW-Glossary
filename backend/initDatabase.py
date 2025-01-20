import os
from pymongo import MongoClient

mongoURL = os.getenv('MONGOURL', 'mongodb://localhost:27017')
client = MongoClient(mongoURL)
database = client['glossaryDB']
collection = database['glossary']

if collection.count_documents({"concept": "python"}) == 0:
    glossary = [
        {'concept': 'python',
         'definition': 'A high-level, interpreted programming language known for its readability and versatility.',
         'source': 'I said so',
         'childConcepts': [{'child': 'api',
                            'connector': 'provides access via'},
                           {'child': 'docker',
                            'connector': 'gets data from'}
                           ]},

        {'concept': 'docker',
         'definition': 'A platform that enables developers to automate the deployment of applications inside lightweight, portable containers.',
         'source': 'I said so',
         'childConcepts': [{'child': 'container',
                            'connector': 'hosts a'}
                           ]},

        {'concept': 'container',
         'definition': 'A runtime instance of a Docker image, representing a running application in an isolated environment.',
         'source': 'I said so',
         'childConcepts': []},

        {'concept': 'api',
         'definition': 'An interface that allows different software applications to communicate and interact with each other.',
         'source': 'I said so',
         'childConcepts': []}
    ]
    collection.insert_many(glossary)
    print("Database initialized with glossary data.")
else:
    print("Database already exists, no initialization needed.")

print('Databases:', client.list_database_names())
print('Collections:', database.list_collection_names())
