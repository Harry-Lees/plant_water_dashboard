#!/usr/bin/python3
# Dependancies Below
from datetime import datetime, timedelta
from plantDashboardClasses import *

# Variables below
databaseCommands = []
databaseData = []
formattedDatabaseData = []
xAxisDates = []

graphLength = 30 # change for the time period that the graph shows
database = connection('username', 'password', 'localhost', 'databaseName')

startDate = (datetime.now() - timedelta(days = graphLength)) # defines the start date of the graph

# Main program Below
for i in range(graphLength+1):
        formattedDate = (startDate + timedelta(days = i)).strftime('%Y-%m-%d')
        xAxisDates.append(formattedDate)
        databaseCommands = (f"select coalesce(cast(round(avg(voltage), 2) as text), '0') from schedule where date(date) = '{formattedDate}'")
        database.cursor.execute(databaseCommands)
        databaseData.append(database.cursor.fetchone())

database.connection.commit()
formattedDatabaseData = [t[0] for t in databaseData]

print ("var hourlyData = document.getElementById('hourlyData');")
print ('var hourlyData = new Chart(hourlyData, {')
print ("type: 'line',")
print ('data: {')
print (f'labels: {str(xAxisDates)},')
print ('datasets: [{')
print (f'data: {str(formattedDatabaseData)},')
print ("label: 'Date',")
print ('fill: true,')
print ('borderWidth: 4,')
print ("backgroundColor: 'rgba(0, 71, 171, 0.2)',")
print ("borderColor: 'rgba(0, 71, 171, 1)',")
print ("pointHoverBackgroundColor: 'rgba(0, 71, 171, 0.2)'")
print ('},]')
print ('},')
print ('options: {')
print ('responsive: true,')
print ('legend: {display: false},')
print ('maintainAspectRatio: false,')
print ('elements: {line: {tension: 0.3}},')
print ("scales: {xAxes: [{scaleLabel: {display: true, labelString: 'Date'}}], yAxes: [{scaleLabel: {display: true, labelString: 'Voltage (V)'}, ticks: {beginAtZero: true}}]},")
print ('},')
print ('});')

del database
