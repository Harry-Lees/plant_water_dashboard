from .extensions import database

class Watered(database.Model):
    __tablename__: str = 'watered_tab'

    date_watered: database.Column = database.Column(database.DateTime, primary_key=True)


class Schedule(database.Model):
    __tablename__: str = 'schedule_tab'

    id: database.Column = database.Column(database.Integer, primary_key=True)

    plant_id: database.Column = database.Column(database.Integer)
    datetime: database.Column = database.Column(database.DateTime, nullable=False)

    # sensor statistics
    voltage: database.Column = database.Column(database.Float, nullable=True)
    temp: database.Column = database.Column(database.Float, nullable=True)
    humidity: database.Column = database.Column(database.Float, nullable=True)

    def __repr__(self) -> str:
        return f'Schedule(plant={self.plant_id}, datetime={self.datetime})'