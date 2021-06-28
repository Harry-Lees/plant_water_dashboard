from datetime import datetime, timedelta
from typing import List

from flask import Blueprint, render_template, current_app
from scipy import stats

from app.models import Watered, Schedule

blueprint = Blueprint('core', __name__, template_folder='templates')


def next_water_due():
    filter = Schedule.datetime.between(datetime.now() - timedelta(days = 10), datetime.now())
    water_data: List[Schedule] = Schedule.query.filter(filter).all()

    if water_data:
        x, y = zip(*[(w.datetime.timestamp(), w.voltage) for w in water_data])
        regression = stats.linregress(x, y)

        # calculate limit where plant is too dry
        predicted_day = (current_app.config['DRYNESS_THRESHOLD'] - regression.intercept) // regression.slope
        next_water_due = datetime.fromtimestamp(predicted_day).strftime('%Y-%m-%d')

        return next_water_due
    return 'n/a'


def last_time_watered() -> Watered:
    return Watered.query.order_by('date_watered').first().date_watered


@blueprint.route('/graph_data')
def graph_logic():
    x = []
    y = []
    graph_length = current_app.config['GRAPH_LENGTH']
    start_date = datetime.now() - timedelta(days=graph_length)

    for i in range(graph_length):
        date = start_date + timedelta(days=i)
        x.append(date.strftime('%Y-%m-%d'))

        schedule = Schedule.query.filter(Schedule.datetime == date).first()
        if schedule:
            y.append(schedule.voltage)
        else:
            y.append(0)
    return x, y


@blueprint.route('/')
def index():
    x, y = graph_logic()

    args = {
        'last_time_watered' : last_time_watered(),
        'next_water_due'    : next_water_due(),
        'x_axis_dates'      : x,
        'graph_data'        : y,
    }

    return render_template('index.html', **args)
