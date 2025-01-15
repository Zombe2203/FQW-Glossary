from pymongo import MongoClient

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

# {
#     'python': 'A high-level, interpreted programming language known for its readability and versatility.',
#     'docker': 'A platform that enables developers to automate the deployment of applications inside lightweight, portable containers.',
#     'docker image': 'A lightweight, standalone, and executable package that includes everything needed to run a piece of software, including code, runtime, libraries, and dependencies.',
#     'docker container': 'A runtime instance of a Docker image, representing a running application in an isolated environment.',
#     'devops': 'A set of practices that combines software development and IT operations to shorten the development lifecycle and improve software delivery.',
#     'api': 'An interface that allows different software applications to communicate and interact with each other.',
#     'rpc': 'A protocol that allows a program to execute code on another machine as if it were a local function call.'
# }

client = MongoClient('mongodb://localhost:27017')
database = client['glossaryDB']
collection = database['glossary']
collection.insert_many(glossary)

print('Databases:', client.list_database_names())
print('Collections:', database.list_collection_names())

allDocuments = collection.find()
for item in allDocuments:
    print(item)
