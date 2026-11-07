from pydantic import BaseModel,Field
from typing import Literal,Optional


class TaskCreate(BaseModel):
    title:str=Field(min_length=3)
    description:str
    priority:Literal["Low","Medium","High"]
    status:Literal["Pending","In Progress","Completed"]="Pending"



class TaskUpdate(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    priority:Optional[Literal["Low","Medium","High"]]=None
    status:Optional[Literal["Pending","In Progress","Completed"]]=None
