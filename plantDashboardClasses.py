# Dependancies Below
import psycopg2

# Classes Below
class connection: # holds all methods for importing and exporting data from the local database

        def __init__(self, username, password, host, database): # initiator runs when the class is constructed
                try: # tries to run the following block of code
                        self.connection = psycopg2.connect( # defines opens a psycopg2 connection to the database with the given credentials
                                user = username,
                                password = password,
                                host = host,
                                database = database,
                        )

                        self.cursor = self.connection.cursor() # initiates psycopg2 connection

                except psycopg2.OperationalError as exception:
                        print(f'[ERROR]: Unable to connect - {exception}')

        def __del__(self):
                try:
                        self.cursor.close() # closes psycopg2 database connection.
                except psycopg2.OperationalError as exception:
                        print(f'[ERROR]: {exception}')