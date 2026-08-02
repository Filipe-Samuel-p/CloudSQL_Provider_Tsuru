
from pydantic import BaseModel

class InstanceRequest(BaseModel):
    region: str
    plan: str
    instance_name: str


class InstanceResponse(BaseModel):
    kind: str
    targetLink: str
    status: str
    user: str
    insertTime: str
    name: str





