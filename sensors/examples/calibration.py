from sensors import Sensor, TestSensor

sensor: Sensor = TestSensor()

input('please place the sensor in the dry soil and press any button to continue...')
dry: float = sensor.read_moisture()

input('please water the plant and press any button to continue...')
wet: float = sensor.read_moisture()

upload = input('sensor calibration complete, would you like to upload to database Y/n')
if (upload.upper() == 'Y') or (not upload):
    pass
else:
    pass