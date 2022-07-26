from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from database import engine, Base, SessionLocal
from models import Note
from schemas import NoteView, NoteCreate
app = FastAPI()

def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()

Base.metadata.create_all(bind=engine)



note_router = SQLAlchemyCRUDRouter(
    schema=NoteView,
    create_schema=NoteCreate, 
    db_model=Note,
    db=get_db,
    prefix='notes'
)


app.include_router(note_router)