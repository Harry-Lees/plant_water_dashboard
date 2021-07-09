from .extensions import database


class Watered(database.Model):
    __tablename__: str = 'watered_tab'

    date_watered: database.Column = database.Column(database.DateTime, primary_key=True)


class Schedule(database.Model):
    __tablename__: str = 'schedule_tab'

    id: database.Column = database.Column(database.Integer, primary_key=True)

    plant_id: database.Column = database.Column(database.Integer, database.ForeignKey('plants_tab.id'), nullable=False)

    datetime: database.Column = database.Column(database.DateTime, nullable=False)
    water_level: database.Column = database.Column(database.Float, nullable=False)

    def __repr__(self) -> str:
        return f'Schedule(plant={self.plant_id}, datetime={self.datetime})'


class Plant(database.Model):
    __tablename__: str = 'plants_tab'

    id: database.Column = database.Column(database.Integer, primary_key=True)
    schedule = database.relationship('Schedule', backref='plants_tab', lazy=True)

    room: database.Column = database.Column(database.String, nullable=False)
    name: database.Column = database.Column(database.String, nullable=False)

    def __repr__(self) -> str:
        return f'Plant(id={self.id}, name={self.name}, room={self.room})'