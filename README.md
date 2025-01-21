# How to run
To run this project install `Pydantic`, `uvicorn` and `FastAPI`: `pip install pydantic uvicorn fastapi`.<br>
Then run command `uvicorn main:app --reload` from repository root.<br>
Keep in mind that all changes you make will not be saved as this version of project does not support database integration.<br>
## How to run as docker
From this project root run `docker-compose build`. When build is completed run `docker-compose up`. Then use Docker Desktop to manage your container or use `docker-compose down`.

# Handles descriptions and usage

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

## /concept/{}
### GET
#### Request
Basic GET request to the handle. Handle should contain concept name, for example `/concept/web`
#### Response
Contains JSON object with two fields. Field `concept` contains concept name, field `definition` contains its definition, field `source` contains source of given definition and field `childConcepts` contains list of documents, each of them has fields `child` for child concept name nd `connector` for connection description.
