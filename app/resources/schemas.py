
from pydantic import BaseModel

class InstanceRequest(BaseModel):
    plan: str
    name: str
    team: str
    user: str


class InstanceResponse(BaseModel):
    kind: str
    targetLink: str
    status: str
    user: str
    insertTime: str
    name: str





