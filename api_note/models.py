from sqlalchemy import Column, Text, Integer

from database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)