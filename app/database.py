from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Column, Float, Integer, TIMESTAMP


class Watered(Base):
    __tablename__: str = 'watered_tab'

    date_watered: Column = Column(Integer, primary_key=True)


class Schedule(Base):
    __tablename__: str = 'schedule_tab'

    id: Column = Column(Integer, primary_key=True)

    date: Column = Column(TIMESTAMP, nullable=False)
    voltage: Column = Column(Float, nullable=True)
    temp: Column = Column(Float, nullable=True)
    humidity: Column = Column(Float, nullable=True)