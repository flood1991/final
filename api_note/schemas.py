from pydantic import BaseModel


class NoteCreate(BaseModel):
    text: str

class NoteView(NoteCreate):
    id: int
    

    class Config:
        orm_mode = True