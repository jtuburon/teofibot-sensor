from flask_script import Manager
from threading import Thread
from flask_socketio import SocketIO
from flask_socketio import send, emit
import time
import random
import requests
import Adafruit_DHT

from main import app

manager = Manager(app)
socketio = SocketIO(app)
		
class SensorReader(Thread):
	def run(self):
		sensor, gpio= Adafruit_DHT.DHT11, 4
		while True:
			humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
			url="http://127.0.0.1:5000/sensor/set_data?t=%f&h=%f" % (temperature, humidity)
			r = requests.get(url)
			print temperature
			time.sleep(2)




@manager.command
def start_sensor():
	SensorReader().start()

if __name__ == "__main__":
    manager.run()