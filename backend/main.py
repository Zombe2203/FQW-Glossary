import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

from classesReqRes import BaseResponse, ConceptResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mongoURL = os.getenv('MONGOURL', 'mongodb://localhost:27017')
client = MongoClient(mongoURL)
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
            'id': str(document['_id']),
            'concept': document['concept'],
            'definition': document['definition'],
            'source': document['source'],
            'childConcepts': document['childConcepts']
        })
    return JSONResponse(content=responseDocument)

# Конкретный концепт
@app.get('/concept/{conceptName}')
async def concept(conceptName):
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
        print(404)
        return BaseResponse(
            status=404,
            message=f'[{conceptName.capitalize()}] does not exists in dictionary.'
        )