from pydantic import BaseModel

class PlantSummary(BaseModel):
    id: int
    name: str
    type: int
    master: str | None
    installer: str | None
    email: str | None
    phone: str | None
