<h1 align="center">
  Plant Water Dashboard :seedling:
</h1>

<h4 align="center">
  A Simple Flask application to help you keep track of your plants.
</h4>

## About

One of the most common beginner projects for someone looking to get into Raspberry Pi or Arduino is an automatic plant watering system. With a glass of water, a 5v pump, and a Raspberry Pi or Arduino, you can have a fully functioning plant watering system! This project assists in the last step of the puzzle, displaying your results. 

Plant Water Dashboard allows you to create your own custom plant watering device using any hardware/ software you want. To work with this project, you simply push a moisture level to the database, and all the results will be displayed on the site.

## Installation

The easiest way to run this project is with Docker. The included docker-compose file sets up a database and the Flask application. This will require Docker, and docker-compose to be installed. Once docker is installed, running 

```bash
sudo docker-compose up --build
```

will build and run the Docker containers.

## Usage

Please see the usage documentation for instructions on using this project.

## Contributing

This is an open source project written almost entirely in Python3. If you would like to contribute, please feel free to fork or create an issue that I can look at.

## License
[MIT](https://choosealicense.com/licenses/mit/)
