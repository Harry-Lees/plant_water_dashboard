#!/usr/bin/python3
# Dependancies below
import pandas as pd
from scipy import stats
import datetime
import itertools
from plantDashboardClasses import *
import math

# Variables Below
xAxis = list()
yAxis = list()
currentDay = datetime.datetime.now().strftime('%d')
currentMonthYear = datetime.datetime.now().strftime('%m/%Y')

# Functions Below
calcY = lambda x : regression.slope * x + regression.intercept # function to return the Y value for a given X value (y = mx + c)
database = connection('postgres', 'cobdtl26', 'localhost', 'plant_dashboard') # Creates a connection to the database

# Main program Below
databaseCommand = (f'select distinct(extract(day from date)) from schedule where extract(month from date) = extract(month from current_date) order by date_part')
database.cursor.execute(databaseCommand)
xAxis = list(itertools.chain.from_iterable(database.cursor))

for date in xAxis:
        databaseCommand = (f"select (cast(round(avg(voltage), 2) as text)) from schedule where date(date) = '{int(date)}/{currentMonthYear}'")
        database.cursor.execute(databaseCommand)
        yAxis.append(list(itertools.chain.from_iterable(database.cursor))) # Flattens the returned list

yAxis = list(itertools.chain.from_iterable(yAxis)) # flattens the entire list
yAxis = list(map(float, yAxis)) # converts all elements of the list to float with the very helpful map function

regression = stats.linregress(xAxis, yAxis) # returns many objects and assigns them to regression

myModel = list(map(calcY, xAxis)) # Makes a list of Y Values for the line

predictedDay = math.floor(0 - regression.intercept/regression.slope) # floor is used here to get the lowest number of whole days

nextWaterDue = predictedDay - int(currentDay)

print(nextWaterDue)