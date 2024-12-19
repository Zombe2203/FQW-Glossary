from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

myDictionary = {
    'python': 'A high-level, interpreted programming language known for its readability and versatility.',
    'docker': 'A platform that enables developers to automate the deployment of applications inside lightweight, portable containers.',
    'docker image': 'A lightweight, standalone, and executable package that includes everything needed to run a piece of software, including code, runtime, libraries, and dependencies.',
    'docker container': 'A runtime instance of a Docker image, representing a running application in an isolated environment.',
    'devops': 'A set of practices that combines software development and IT operations to shorten the development lifecycle and improve software delivery.',
    'api': 'An interface that allows different software applications to communicate and interact with each other.',
    'rpc': 'A protocol that allows a program to execute code on another machine as if it were a local function call.'
}

class DefinitionResponse(BaseModel):
    Concept: str
    Definition: str

class BaseResponse(BaseModel):
    Status: int
    Message: str

class CreateRequest(BaseModel):
    Concept: str
    Definition: str

class UpdateRequest(BaseModel):
    NewDefinition: str

@app.get('/about')
async def about():
    return {'about': 'This is a dictionary with some definitions. You can modify them'}

@app.get('/author')
async def author():
    return {'author': 'I am mfatov and I made this...'}

# Весь словарь
@app.get('/allConcepts')
async def allConcepts():
    return JSONResponse(content=myDictionary)

# Список терминов
@app.get('/list')
async def list():
    responseDict = {}
    counter = 1
    for item in myDictionary.keys():
        responseDict[counter] = item.capitalize()
        counter += 1
    return JSONResponse(content=responseDict)

# Конкретное определение
@app.get('/definition/{definitionName}')
async def definition(definitionName: str):
    definitionName = definitionName.lower()
    definitionText = myDictionary.get(definitionName)
    definitionName = definitionName.capitalize()
    return DefinitionResponse(
        Concept = definitionName,
        Definition = definitionText
    )

# Добавление определения
@app.post('/create')
async def create(request: CreateRequest):
    if (request.Concept.lower() in myDictionary):
        return BaseResponse(
            Status = 406,
            Message = f'{request.Concept.capitalize()} already exists in dictionary. Use /update/{request.Concept.capitalize()} instead.'
        )
    else:
        myDictionary[request.Concept.lower()] = request.Definition
        return BaseResponse(
            Status = 200,
            Message = f'Successfully added your definition of {request.Concept.capitalize()}'
        )

# Обновление определения
@app.put('/update/{definitionName}')
async def update(request: UpdateRequest, definitionName: str):
    if (definitionName.lower() in myDictionary):
        myDictionary[definitionName.lower()] = request.NewDefinition
        return BaseResponse(
            Status = 200,
            Message = f'Successfully changed definition of {definitionName.capitalize()}'
        )
    else:
        return BaseResponse(
            Status=404,
            Message=f'{definitionName.capitalize()} does not exists in dictionary. Use /create instead.'
        )

# Удаление определения
@app.delete('/remove/{definitionName}')
async def remove(definitionName: str):
    if (definitionName.lower() in myDictionary):
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
