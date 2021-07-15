from sqlalchemy import Column, TIMESTAMP, Float, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta, declared_attr


'''SQLAlchemy models used for representing the database schema as Python objects'''

Base: DeclarativeMeta = declarative_base()

class Watered(Base):
    '''Model to hold the data for when the plant was last watered.'''

    __tablename__: str = 'watered_tab'

    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    date_watered: Column = Column(TIMESTAMP, nullable=False)

    @declared_attr
    def plant_id(cls) -> Column:
        return Column(Integer, ForeignKey('plants_tab.id'), primary_key=True)

    def __repr__(self) -> str:
        return f'Watered(plant={self.plant_id}, date_watered={self.date_watered})'


class Schedule(Base):
    '''Model to hold the values collected from the moisture sensors for a given plant.'''

    __tablename__: str = 'schedule_tab'

    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    datetime: Column = Column(TIMESTAMP, nullable=False)
    water_level: Column = Column(Float, nullable=False)

    @declared_attr
    def plant_id(cls) -> Column:
        return Column(Integer, ForeignKey('plants_tab.id'), primary_key=True)

    def __repr__(self) -> str:
        return f'Schedule(plant={self.plant_id}, datetime={self.datetime})'


class Plant(Base):
    '''Model to represent a plant.'''

    __tablename__: str = 'plants_tab'

    id: Column = Column(Integer, primary_key=True, autoincrement=True)

    room: Column = Column(String, nullable=False)
    name: Column = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f'Plant(id={self.id}, name={self.name}, room={self.room})'