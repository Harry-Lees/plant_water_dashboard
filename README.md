# Plant Water Dashboard :seedling:

Plant water dashboard is an updated version of the bonsaiWaterer repo. This project allows the tracking of a plants water level over time with tracking to detect when the next water is required.

## Installation

This project can be installed by cloning this repo and then running the app.py script to start flask running. There is a requirements.txt file for installing the project dependancies.

```bash
python3 -m pip install -r requirements.txt
python3 app.py
```

## Usage

There are two main scripts that are required for this project. read_signal.py is used for reading the sensor data and inputting it into the sqlite3 database (water_database.db by default). The read_signal.py script can be run automatically using cron or a similar scheduling program. If you would like to use a different sensor, a new script can be created to push data directly into the database that can then be read by the flask dashboard without changing anything in the app.py script.

## Contributing
This is an open source project written almost entirely in Python3. If you would like to contribute, please feel free to clone this project or create an issue that I can look at.

## License
[MIT](https://choosealicense.com/licenses/mit/)
