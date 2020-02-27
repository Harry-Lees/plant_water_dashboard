import psycopg2
import time
import explorerhat
from plantDashboardClasses import *

database = connection('username', 'password', 'localhost', 'databaseName')

voltage = explorerhat.analog.one.read()

databaseCommand = (f"insert into schedule(date, voltage) values(current_timestamp, '{voltage}')")
database.cursor.execute(databaseCommand)
database.connection.commit()

if voltage < 0.25:
        explorerhat.output[0].on()
        explorerhat.light[0].on()
        time.sleep(10)
        explorerhat.output[0].off()
        explorerhat.light[0].off()

        database.cursor.execute(f"insert into watered_schedule values (current_timestamp))")
        database.connection.commit()

del database