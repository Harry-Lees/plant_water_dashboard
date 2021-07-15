from abc import ABC, abstractmethod
from datetime import datetime
import random
from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import explorerhat

from .models import Watered, Schedule


class BaseSensor(ABC):
    '''Base Sensor class for sensors'''

    def __init__(self, database_uri: str) -> None:
        self.engine = create_engine(database_uri)

    @abstractmethod
    def read_moisture(self) -> None:
        '''function to read the soil moisture and upload results to database'''
        ...

    @abstractmethod
    def water(self) -> None:
        '''function to water the plant and upload record to database'''
        ...


class ExplorerHat(BaseSensor):
    def __init__(self, database_uri: str, v_min: float, v_max: float):
        self.v_min: int = v_min
        self.v_max: int = v_max

        super().__init__(database_uri)

    def read_moisture(self, plant_id: int) -> None:
        '''function to read the moisture from the explorer hat'''

        voltage: float = explorerhat.analog.one.read()
        water_level: float = ((voltage - self.v_min) * 100) / (self.v_max - self.v_min) # calculate the % moisture of the soil

        obj: Schedule = Schedule(datetime=datetime.now(), water_level=water_level, plant_id=plant_id)
        with Session(self.engine) as session:
            session.add(obj)
            session.commit()

    def water(self, plant_id: int, water_time: float = 10.0) -> None:
        '''function to toggle the explorer hat's builtin Light and motor controls to water the plant'''

        explorerhat.output[0].on()
        explorerhat.light[0].on()
        sleep(water_time)
        explorerhat.output[0].off()
        explorerhat.light[0].off()

        watered_on: Watered = Watered(date_watered=datetime.now(), plant_id=plant_id)
        with Session(self.engine) as session:
            session.add(watered_on)
            session.commit()


class TestSensor(BaseSensor):
    def __init__(self, database_uri) -> None:
        super().__init__(database_uri)

    def read_moisture(self, plant_id: int) -> None:
        '''function to create a database entry mimicking the water level at the current date/ time'''

        water_level: Schedule = Schedule(datetime=datetime.now(), water_level=random.randint(0, 100), plant_id=plant_id)
        with Session(self.engine) as session:
            session.add(water_level)
            session.commit()

    def water(self, plant_id: int) -> None:
        '''function to create a database entry mimicking the plant being watered at the current date/ time'''

        watered_on: Watered = Watered(date_watered=datetime.now(), plant_id=plant_id)
        with Session(self.engine) as session:
            session.add(watered_on)
            session.commit()