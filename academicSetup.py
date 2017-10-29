import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Academic(Base):
    __tablename__ = 'academic'
    Student_ID = Column(Integer,primary_key=True)
    Term = Column(String(6),primary_key=True)
    ID_Subject = Column(String(10),primary_key=True)
    Grade = Column(String(4), nullable=True)

class Gpa(Base):
    __tablename__ = 'gpa'
    Student_ID = Column(Integer,primary_key=True)
    Term = Column(String(6),primary_key=True)
    sum_credit = Column(Integer, nullable=True)
    GPA = Column(String(5), nullable=True)

class Gpax(Base):
    __tablename__ = 'gpax'
    Student_ID = Column(Integer,primary_key=True)
    sum_all_credit = Column(Integer, nullable=False)
    GPAX = Column(String(5), nullable=True)

class Subject(Base):
    __tablename__ = 'subject'
    ID_Subject = Column(String(10),primary_key=True)
    name_subject = Column(String(50), nullable=False)
    Credit = Column(Integer, nullable=False)


engine = create_engine('sqlite:///Academics.db')


Base.metadata.create_all(engine)
