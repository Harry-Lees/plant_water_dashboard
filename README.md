# Plant Water Dashboard :seedling:

![Screenshot](./screenshot.PNG?raw=true "Title")

Plant water dashboard is an updated version of the bonsaiWaterer repo. This project allows the tracking of a plants water level over time with tracking to detect when the next water is required.

## Installation

### Docker

The easiest way to run this project is with Docker. The included docker-compose file sets up a database and the Flask application. This will require Docker, and docker-compose to be installed. Once docker is installed, running 

```bash
sudo docker-compose up --build
```

will build and run the Docker containers.

### Shell

This can be run natively in the shell by hosting a PostgreSQL database and running the Flask app as normal.

```bash
sudo apt update
sudo apt install -y postgresql

python3 -m pip install -r requirements.txt
python3 app.py
sudo apt install python3-scipy
```

## Usage

There are two main scripts that are required for this project. read_signal.py is used for reading the sensor data and inputting it into the database. The read_signal.py script can be run automatically using cron or a similar scheduling program. If you would like to use a different sensor, a new script should be created to push data directly into the database that can then be read by the flask dashboard without changing anything in the app.py script.

## Contributing
This is an open source project written almost entirely in Python3. If you would like to contribute, please feel free to clone this project or create an issue that I can look at.

### Development

When developing this project, I recommend running the Flask development server using `flask run` with the database in a Docker container. The `start-database.sh` script runs an empty PostgreSQL database in Docker which will then be populated when the flask development server is run.

## License
[MIT](https://choosealicense.com/licenses/mit/)
