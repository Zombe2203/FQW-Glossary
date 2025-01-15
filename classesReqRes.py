from pydantic import BaseModel

class DefinitionResponse(BaseModel):
    concept: str
    definition: str

class BaseResponse(BaseModel):
    status: int
    message: str

class CreateRequest(BaseModel):
    concept: str
    definition: str

class UpdateRequest(BaseModel):
    newDefinition: str