from typing import List
from pydantic import BaseModel

class ChildConceptEntry(BaseModel):
    child: str
    connector: str

class ConceptResponse(BaseModel):
    # id: ObjectId
    concept: str
    definition: str
    source: str
    childConcepts: List[ChildConceptEntry]

class BaseResponse(BaseModel):
    status: int
    message: str

# TODO rewise
class CreateRequest(BaseModel):
    concept: str
    definition: str

# TODO rewise
class UpdateRequest(BaseModel):
    newDefinition: str