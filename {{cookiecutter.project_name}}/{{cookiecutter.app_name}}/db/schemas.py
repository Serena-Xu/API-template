from pydantic import BaseModel

class Main(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True