from sensors import sensors

database_uri: str = 'postgresql://postgres:password@localhost/postgres'
test_sensor: sensors.TestSensor = sensors.TestSensor(database_uri)

test_sensor.read_moisture(1)
test_sensor.water(1)