from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any, Tuple
from dataclasses import dataclass

from flask import Blueprint, render_template, current_app, request
from scipy import stats

from app.models import Watered, Schedule


blueprint = Blueprint('core', __name__, template_folder='templates')


def next_water_due(plant_id: int) -> str:
    '''function to get the next water due for the given plant.'''

    filter = Schedule.datetime.between(datetime.now() - timedelta(days = 10), datetime.now())
    water_data: List[Schedule] = Schedule.query.filter_by(plant_id=plant_id).filter(filter).all()

    if water_data:
        x, y = zip(*[(w.datetime.timestamp(), w.voltage) for w in water_data])
        regression = stats.linregress(x, y)

        # calculate limit where plant is too dry
        predicted_day = (current_app.config['DRYNESS_THRESHOLD'] - regression.intercept) // regression.slope
        next_water_due = datetime.fromtimestamp(predicted_day).strftime('%Y-%m-%d')

        return next_water_due
    return 'n/a'


def last_time_watered(plant_id: int) -> Optional[Watered]:
    '''function to get the last time the plant was watered'''

    watered = Watered.query.filter_by(plant_id=plant_id).order_by('date_watered').first()
    if watered:
        return watered.date_watered
    else:
        return None


def graph_logic(plant_id: int) -> Tuple[list, list]:
    '''function to return the Graph data for the watered graph on the index page.'''

    x = []
    y = []
    graph_length = current_app.config['GRAPH_LENGTH']
    start_date = datetime.today().date() - timedelta(days=graph_length)

    for i in range(graph_length):
        date = start_date + timedelta(days=i)
        x.append(date.strftime('%Y-%m-%d'))

        schedule = Schedule.query.filter_by(datetime=date, plant_id=plant_id).first()
        if schedule:
            y.append(schedule.voltage)
        else:
            y.append(0)
    return x, y


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    '''function to serve the index page for the user'''

    selected_plant: str = request.args.get('plant', default=0, type=int)
    x, y = graph_logic(selected_plant)

    args: Dict[str, Any] = {
        'plants'            : None,
        'last_time_watered' : last_time_watered(selected_plant),
        'next_water_due'    : next_water_due(selected_plant),
        'x_axis_dates'      : x,
        'graph_data'        : y,
        'selected'          : selected_plant,
    }

    return render_template('index.html', **args)