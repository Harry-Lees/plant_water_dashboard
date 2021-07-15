<h1 align="center">
  Plant Water Dashboard :seedling:
</h1>

<h4 align="center">
  A Simple Flask application to help you keep track of your plants.
</h4>
  
<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#license">License</a>
</p>

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

## How To Use

### Dashboard

After installing the requirements, the dashboard can be run. You will be greeted with an empty homescreen. Before starting the moisture sensors, you must add a plant to the dashboard.

### Moisture Sensors

Once the dashboard has been setup and a plant has been added, you may setup a moisture sensor.

```python
from sensors import sensors

database_uri: str = 'postgresql://postgres:password@localhost/postgres'
test_sensor: sensors.TestSensor = sensors.TestSensor(database_uri)

plant_id: int = 1 # Plant ID can be seen on the dashboard
sensors.read_moisture(plant_id)
```

The above program can be seen in sensors/examples/test_sensor.py. It is an example of how the interface can be used to read sensor data. The TestSensor() is used to generate random moisture levels. There are several premade examples of moisture sensor classes, including the [ExplorerHat()](https://thepihut.com/products/explorer-hat) which is a nice introduction to using this project with Raspberry Pi. Adding a custom moisture sensor can be accomplished by subclassing `sensors.sensors.BaseSensor`.

## Contributing
This is an open source project written almost entirely in Python3. If you would like to contribute, please feel free to clone this project or create an issue that I can look at.

### Development

When developing this project, I recommend running the Flask development server using `flask run` with the database in a Docker container. The `start-database.sh` script runs an empty PostgreSQL database in Docker which will then be populated when the flask development server is run.

## License
[MIT](https://choosealicense.com/licenses/mit/)
