from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired

class AddPlantForm(FlaskForm):
    name: StringField = StringField('Plant Name', validators=[InputRequired()])
    room: StringField = StringField('Room Name', validators=[InputRequired()])

    submit: SubmitField = SubmitField('Add Plant')