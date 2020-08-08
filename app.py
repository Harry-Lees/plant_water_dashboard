from flask import Flask, render_template, abort
from flask_caching import Cache
from config import *
import pandas as pd
from scipy import stats
from datetime import datetime, timedelta
import sqlite3
import itertools

app = Flask(__name__)

cache = Cache(
    config = {
        'CACHE_TYPE' : 'simple',
        'CACHE_DEFAULT_TIMEOUT' : 600
    }
)

calc_y = lambda x : regression.slope * x + regression.intercept

def setup_database():
    with sqlite3.connect(DATABASE_LOGIN) as connection:
        cursor = connection.cursor()
        
        for table in [WATERED_SCHEDULE_TABLE, SCHEDULE_TABLE]:
            cursor.execute(table)

def next_water_due(date_range : int = 10):
    x_axis = []
    y_axis = []
    today = datetime.today()

    with sqlite3.connect(DATABASE_LOGIN) as connection:
        cursor = connection.cursor()

        template = f"SELECT DISTINCT date FROM schedule WHERE date BETWEEN DATETIME('NOW') AND DATETIME('NOW', '-' || ? || ' DAYS') ORDER BY date"
        cursor.execute(template, [date_range])
        x_axis = itertools.chain.from_iterable(cursor)

        for date in x_axis:
                template = 'select voltage from schedule where date(date) = ?'
                cursor.execute(template, date)
                
                y_axis.append(cursor.fetchall())

        if x_axis and y_axis:
            regression = stats.linregress(x_axis, y_axis)
            model = list(map(calc_y, x_axis))
            predicted_day = math.floor(0 - regression.intercept/regression.slope)
            next_water_due = predicted_day - int(current_day)

            return next_water_due
        else:
            return

def last_time_watered():
    template = 'SELECT date_watered FROM watered_schedule ORDER BY date_watered DESC LIMIT 1'
    
    with sqlite3.connect(DATABASE_LOGIN) as connection:
        cursor = connection.cursor()
        cursor.execute(template)

        return cursor.fetchone()

@app.route('/graph_data')
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

@app.route('/')
def return_index():
    x_axis_dates, graph_data = graph_logic()

    args = {
        'last_time_watered' : last_time_watered(),
        'next_water_due'    : next_water_due(),
        'x_axis_dates' : x_axis_dates,
        'graph_data' : graph_data
    }

    return render_template('index.html', **args)

setup_database() # run on startup regardless of how the script is run

if __name__ == '__main__':
    app.run(**FLASK_CONFIG)