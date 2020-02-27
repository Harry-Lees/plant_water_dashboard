# Dependancies Below
import psycopg2
import time
import explorerhat
from plantDashboardClasses import *

# Main Program Below
database = connection('username', 'password', 'localhost', 'databaseName')

voltage = explorerhat.analog.one.read() # Someone with more electrical knowledge than me will have to tell me if this is actually measuring voltage

databaseCommand = (f"insert into schedule(date, voltage) values(current_timestamp, '{voltage}')")
database.cursor.execute(databaseCommand)
database.connection.commit()

if voltage < 0.25:
        explorerhat.output[0].on()
        explorerhat.light[0].on() # The light turning on is not necessary although was helpful for testing
        time.sleep(10) # The amount of time the pump needs to be on will change depending on the plant and pump
        explorerhat.output[0].off()
        explorerhat.light[0].off()

        database.cursor.execute(f"insert into watered_schedule values (current_timestamp))")
        database.connection.commit()

del database