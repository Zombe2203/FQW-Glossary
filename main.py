from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pymongo import MongoClient

from classesReqRes import CreateRequest, BaseResponse, UpdateRequest, ConceptResponse

app = FastAPI()

client = MongoClient('mongodb://localhost:27017')
database = client['glossaryDB']
collection = database['glossary']

myDictionary = {
    'python': 'A high-level, interpreted programming language known for its readability and versatility.',
    'docker': 'A platform that enables developers to automate the deployment of applications inside lightweight, portable containers.',
    'docker image': 'A lightweight, standalone, and executable package that includes everything needed to run a piece of software, including code, runtime, libraries, and dependencies.',
    'docker container': 'A runtime instance of a Docker image, representing a running application in an isolated environment.',
    'devops': 'A set of practices that combines software development and IT operations to shorten the development lifecycle and improve software delivery.',
    'api': 'An interface that allows different software applications to communicate and interact with each other.',
    'rpc': 'A protocol that allows a program to execute code on another machine as if it were a local function call.'
}

# Автор
@app.get('/author')
async def author():
    return {'author': 'Mikhail Fatov'}

# Весь глоссарий
@app.get('/fullGlossary')
async def fullGlossary():
    documents = collection.find()
    responseDocument = []
    for document in documents:
        responseDocument.append({
            # TODO use ObjectID from bson?
            # id = document['_id'],
            'concept': document['concept'],
            'definition': document['definition'],
            'source': document['source'],
            'childConcepts': document['childConcepts']
        })
    return JSONResponse(content=responseDocument)

# Конкретный концепт
@app.get('/concept/{conceptName}')
async def concept(conceptName: str):
    conceptName = conceptName.lower()
    document = collection.find_one({'concept': conceptName})
    if document:
        conceptName = conceptName.capitalize()
        return ConceptResponse(
            # TODO use ObjectID from bson?
            # id = document['_id'],
            concept = conceptName,
            definition = document['definition'],
            source = document['source'],
            childConcepts = document['childConcepts']
        )
    else:
        print(404)
        return BaseResponse(
            status=404,
            message=f'[{conceptName.capitalize()}] does not exists in dictionary.'
        )

# Добавление определения
# TODO rewise
@app.post('/create')
async def create(request: CreateRequest):
    if request.concept.lower() in myDictionary:
        return BaseResponse(
            status = 406,
            message = f'{request.concept.capitalize()} already exists in dictionary. Use /update/{request.Concept.capitalize()} instead.'
        )
    else:
        myDictionary[request.concept.lower()] = request.Definition
        return BaseResponse(
            status = 200,
            message = f'Successfully added your definition of {request.Concept.capitalize()}'
        )

# Обновление определения
#TODO rewise
@app.put('/update/{definitionName}')
async def update(request: UpdateRequest, definitionName: str):
    if definitionName.lower() in myDictionary:
        myDictionary[definitionName.lower()] = request.newDefinition
        return BaseResponse(
            status = 200,
            message = f'Successfully changed definition of {definitionName.capitalize()}'
        )
    else:
        return BaseResponse(
            status=404,
            message=f'{definitionName.capitalize()} does not exists in dictionary. Use /create instead.'
        )

# Удаление определения
#TODO rewise
@app.delete('/remove/{definitionName}')
async def remove(definitionName: str):
    if definitionName.lower() in myDictionary:
        myDictionary.pop(definitionName.lower())
        return BaseResponse(
            Status = 200,
            Message = f'{definitionName.capitalize()} successfully removed from dictionary'
        )
    else:
        return BaseResponse(
            Status=404,
            Message=f'{definitionName.capitalize()} is not in the dictionary.'
        )
