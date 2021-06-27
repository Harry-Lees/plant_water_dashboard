from datetime import datetime

from flask import Blueprint, render_template


blueprint = Blueprint('core', __name__, template_folder='templates')


def next_water_due(date_range : int = 10):
    x_axis = [] # dates
    y_axis = [] # voltages

    template = f"SELECT DISTINCT date, voltage FROM schedule WHERE date BETWEEN DATETIME('NOW', '-' || ? || ' DAYS') AND DATETIME('NOW') ORDER BY date"

    # [('2020-11-01 22:23:46', 0.0), ('2020-11-02 22:14:07', 4.122), ('2020-11-02 22:15:26', 4.143)]
    x_axis = [row[0] for row in results]
    y_axis = [row[1] for row in results]

    # convert string datetimes to ordinal for regression
    x_axis = pd.to_datetime(x_axis, format="%Y-%m-%d %H:%M:%S")
    x_axis = [t.timestamp() for t in x_axis]

    if x_axis and y_axis:
        regression = stats.linregress(x_axis, y_axis)

        # calculate limit where plant is too dry
        predicted_day = math.floor((DRYNESS_THRESHOLD - regression.intercept) / regression.slope)
        next_water_due = datetime.fromtimestamp(predicted_day).strftime('%c')

        return next_water_due


def last_time_watered():
    template = 'SELECT date_watered FROM watered_schedule ORDER BY date_watered DESC LIMIT 1'
    
    cursor = connection.cursor()
    cursor.execute(template)

    return cursor.fetchone()


@blueprint.route('/graph_data')
def graph_logic():
    database_data = []
    x_axis_dates = []
    start_date = datetime.now() - timedelta(days = GRAPH_LENGTH)

    with sqlite3.connect(DATABASE_LOGIN) as connection:
        cursor = connection.cursor()

        for i in range(GRAPH_LENGTH):
            date = (start_date + timedelta(days = i)).strftime('%Y-%m-%d')
            x_axis_dates.append(date)
            
            template = (f"SELECT voltage FROM schedule WHERE date(date) = ?")
            cursor.execute(template, [date])
            
            database_data.append(cursor.fetchone())

        return x_axis_dates, database_data


@blueprint.route('/')
def index():
    x, graph_data = graph_logic()

    args = {
        'last_time_watered' : last_time_watered(),
        'next_water_due'    : next_water_due(),
        'x_axis_dates'      : x,
        'graph_data'        : graph_data,
    }

    return render_template('index.html', **args)