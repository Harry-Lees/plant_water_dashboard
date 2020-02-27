#!/usr/bin/python3
# Dependancies Below
import time
import datetime
from plantDashboardClasses import *

# Main program Below
database = connection('username', 'password', 'localhost', 'databaseName')
databaseCommand = ("select cast(date_trunc('minute', date_watered) as text) from watered_schedule order by date_watered desc")

database.cursor.execute(databaseCommand)
database.connection.commit()

databaseData = (database.cursor.fetchone())

del database

print (databaseData[-1])
