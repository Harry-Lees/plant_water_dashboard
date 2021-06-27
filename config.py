GRAPH_LENGTH = 30
DATABASE_LOGIN = './water_database.db'
DRYNESS_THRESHOLD = 2.0

WATERED_SCHEDULE_TABLE = '''
CREATE TABLE IF NOT EXISTS watered_schedule (
    date_watered TIMESTAMP,
    PRIMARY KEY(date_watered)
)
'''

SCHEDULE_TABLE = '''
CREATE TABLE IF NOT EXISTS schedule (
    date TIMESTAMP,
    voltage FLOAT,
    temp FLOAT,
    humidity FLOAT,
    PRIMARY KEY(date)
)
'''

FLASK_CONFIG = {
    'host'  : '0.0.0.0', # allows connection outside of localhost
    'port'  : 5000,
    'debug' : True ,
}
