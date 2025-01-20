# How to run
To run this project install `Pydantic`, `uvicorn` and `FastAPI`: `pip install pydantic uvicorn fastapi`.<br>
Then run command `uvicorn main:app --reload` from repository root.<br>
Keep in mind that all changes you make will not be saved as this version of project does not support database integration.<br>
## How to run as docker
From this project root run `docker-compose build`. When build is completed run `docker-compose up`. Then use Docker Desktop to manage your container or use `docker-compose down`.

# Handles descriptions and usage

## /about
Gives basic information about glossary and its topic.
### GET
#### Request
Basic GET request to the handle.
#### Response
Contains JSON object with one field `about`. Value of that field is glossary description.

## /author
### GET
#### Request
Basic GET request to the handle.
#### Response
Contains JSON object with one field `author`. Value of that field is first and last name of glossary and app original author. 

## /fullGlossary
### GET
#### Request
Basic GET request to the handle.
#### Response
Contains JSON object with fields representing all concepts in the glossary. Values are nested documents, containing fields `definition` (concept definition), `source` (source of given definition) and `childConcepts` (list of documents, each of them contains fields `child` for child concept name nd `connector` for connection description).

## /allConcepts
### GET
#### Request
Basic GET request to the handle.
#### Response
Contains JSON object with fields concepts index number. Value of each field is name of the concept with that number.

## /concept/{}
### GET
#### Request
Basic GET request to the handle. Handle should contain concept name, for example `/concept/web`
#### Response
Contains JSON object with two fields. Field `concept` contains concept name, field `definition` contains its definition, field `source` contains source of given definition and field `childConcepts` contains list of documents, each of them has fields `child` for child concept name nd `connector` for connection description. 

#TODO
## /create
### POST
#### Request
POST request to the handle. Request body should contain two fields: `concept` with new concept name and `definition` with definition of that concept. This method can not be used to modify already existing concepts or add multiple concepts with identical name. <be>
For concept modification see `/update` and `/remove`.
#### Response
Contains JSON object with four fields. Field `status` represents response status and field `message` contains response message. <br>
Possible response statuses:
- 200: OK
- 406: Already exists

#TODO
## /update/{}
### PUT
#### Request
PUT request to the handle. Handle should contain concept name, for example `/update/web`. Request body should contain one field: `newDefinition` with new definition that will replace previous one. This method can not create new definitions or completely remove existing ones from glossary. <br>
For concept creation see `/create`. For concept removal see `remove`.  
#### Response
Contains JSON object with two fields. Field `status` represents response status and field `message` contains response message. <br>
Possible response statuses:
- 200: OK
- 404: Does not exist

## /remove/{}
### DELETE
#### Request
DELETE request to the handle. Handle should contain concept name, for example `/remove/web`.
#### Response
Contains JSON object with two fields. Field `status` represents response status and field `message` contains response message. <br>
Possible response statuses:
- 200: OK
- 404: Does not exist


# Request examples using JS
## /create
POST request for /create 
```
fetch('http://127.0.0.1:8000/create', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json', 
    },
    body: JSON.stringify({
        concept: 'javascript', 
        definition: 'A programming language commonly used for web development.' 
    })
})
.then(response => response.json()) 
.then(data => console.log(data)) 
.catch(error => console.error('Error:', error)); 
```

## /update
PUT request for /update/{definition}
Replace {definition} with definition name
```
fetch('http://127.0.0.1:8000/update/javascript', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json', 
    },
    body: JSON.stringify({
        newDefinition: 'New definition of javascript is awesome!' 
    })
})
.then(response => response.json()) 
.then(data => console.log(data)) 
.catch(error => console.error('Error:', error));
```

## /remove
DELETE request for /remove/{definition
Replace {definition} with definition name
```
fetch('http://127.0.0.1:8000/remove/javascript', {
    method: 'DELETE',
    headers: {
        'Content-Type': 'application/json', 
    }
})
.then(response => response.json()) 
.then(data => console.log(data)) 
.catch(error => console.error('Error:', error));
```