import os
from pymongo import MongoClient

mongoURL = os.getenv('MONGOURL', 'mongodb://localhost:27017')
client = MongoClient(mongoURL)
database = client['glossaryDB']
collection = database['glossary']

if collection.count_documents({"concept": "ethereum"}) == 0:
    glossary = [
        {'concept': 'цифровой актив',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': '',
                            'connector': ''},
                           ]},
        {'concept': 'блокчейн',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': '',
                            'connector': ''},
                           ]},
        {'concept': 'ethereum',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'блокчейн',
                            'connector': 'является реализацией'},
                           ]},
        {'concept': 'мошенничество',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'цифровой актив',
                            'connector': 'использует'},
                           ]},
        {'concept': 'отмывание средств',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'мошенничество',
                            'connector': 'является разновидностью'},
                           ]},
        {'concept': 'метод машинного обучения',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'мошенничество',
                            'connector': 'используется для опознавания'},
                           ]},
        {'concept': 'бинарная классификация',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'метод машинного обучения',
                            'connector': 'является разновидностью'},
                           ]},
        {'concept': 'метрика',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'метод машинного обучения',
                            'connector': 'используется для оценки'},
                           ]},
        {'concept': 'accuracy',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'метрика',
                            'connector': 'является видом'},
                           ]},
        {'concept': 'precision',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'метрика',
                            'connector': 'является видом'},
                           ]},
        {'concept': 'recall',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'метрика',
                            'connector': 'является видом'},
                           ]},
        {'concept': 'f-Score',
         'definition': '',
         'source': '',
         'childConcepts': [{'child': 'метрика',
                            'connector': 'является видом'},
                           ]}
    ]
    collection.insert_many(glossary)
    print("Database initialized with glossary data.")
else:
    print("Database already exists, no initialization needed.")

print('Databases:', client.list_database_names())
print('Collections:', database.list_collection_names())
