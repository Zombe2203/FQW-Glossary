from typing import List
from pydantic import BaseModel

class ChildConceptEntry(BaseModel):
    child: str
    connector: str

class ConceptResponse(BaseModel):
    concept: str
    definition: str
    source: str
    childConcepts: List[ChildConceptEntry]

class BaseResponse(BaseModel):
    status: int
    message: str