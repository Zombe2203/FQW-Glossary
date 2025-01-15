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

# Описание
@app.get('/about')
async def about():
    return {'about': 'This is a glossary with some definitions. It can be accessed and modified using handles.'}

# Автор
@app.get('/author')
async def author():
    return {'author': 'Mikhail Fatov'}

# Весь словарь
#TODO mongo
@app.get('/fullGlossary')
async def allConcepts():
    return JSONResponse(content=myDictionary)

# Список терминов
#TODO mongo
@app.get('/allDefinitions')
async def allDefinitions():
    responseDict = {}
    counter = 1
    for item in myDictionary.keys():
        responseDict[counter] = item.capitalize()
        counter += 1
    return JSONResponse(content=responseDict)

# Конкретное определение
@app.get('/concept/{conceptName}')
async def concept(conceptName: str):
    conceptName = conceptName.lower()
    document = collection.find_one({'concept': conceptName})
    if document:
        conceptName = conceptName.capitalize()
        return ConceptResponse(
            concept = conceptName,
            definition = document['definition'],
            source = document['source'],
            childConcepts = document['childConcepts']
        )
    else:
        return None

# Добавление определения
#TODO four fields, also change in README
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
#TODO mongo
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
