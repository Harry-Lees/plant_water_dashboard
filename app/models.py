from .extensions import database


class Watered(database.Model):
    '''Model to hold the data for when the plant was last watered.'''

    __tablename__: str = 'watered_tab'

    id: database.Column = database.Column(database.Integer, primary_key=True)

    date_watered: database.Column = database.Column(database.DateTime, nullable=False)
    plant_id: database.Column = database.Column(database.Integer, database.ForeignKey('plants_tab.id'), primary_key=True)

    def __repr__(self) -> str:
        return f'Watered(plant={self.plant_id}, date_watered={self.date_watered})'


class Schedule(database.Model):
    '''Model to hold the values collected from the moisture sensors for a given plant.'''

    __tablename__: str = 'schedule_tab'

    id: database.Column = database.Column(database.Integer, primary_key=True)

    plant_id: database.Column = database.Column(database.Integer, database.ForeignKey('plants_tab.id'), nullable=False)

    datetime: database.Column = database.Column(database.DateTime, nullable=False)
    water_level: database.Column = database.Column(database.Float, nullable=False)

    def __repr__(self) -> str:
        return f'Schedule(plant={self.plant_id}, datetime={self.datetime})'


class Plant(database.Model):
    '''Model to represent a plant.'''

    __tablename__: str = 'plants_tab'

    id: database.Column = database.Column(database.Integer, primary_key=True)

    # Relationships
    schedule = database.relationship('Schedule', backref='plants_tab', lazy=True)
    watered = database.relationship('Watered', backref='watered_tab', lazy=True)

    room: database.Column = database.Column(database.String, nullable=False)
    name: database.Column = database.Column(database.String, nullable=False)

    def __repr__(self) -> str:
        return f'Plant(id={self.id}, name={self.name}, room={self.room})'