import sqlite3
import time

import explorerhat

from config import DATABASE_LOGIN


def read_water():
    TEMPLATE = '''INSERT INTO schedule(date, voltage) VALUES(datetime('now'), ?)'''
    voltage = explorerhat.analog.one.read()

    with sqlite3.connect(DATABASE_LOGIN) as connection:
        cursor = connection.cursor()
        cursor.execute(TEMPLATE, (voltage,))

    return voltage


def water_plant(water_time : int = 10):
    TEMPLATE = '''INSERT INTO watered_schedule VALUES(datetime('now'))'''

    explorerhat.output[0].on()
    explorerhat.light[0].on()
    
    time.sleep(water_time)

    explorerhat.output[0].off()
    explorerhat.light[0].off()

    with sqlite3.connect(DATABASE_LOGIN) as connection:
        cursor = connection.cursor()
        cursor.execute(TEMPLATE)


if __name__ == '__main__':
    voltage = read_water()

    if voltage > 0.25:
        water_plant()
