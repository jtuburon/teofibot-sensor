# -*- coding: utf-8 -*-

from flask import Flask
from tempviewer import TempViewer
from flask_socketio import SocketIO
from flask_socketio import send, emit
import random

from flask import request
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app)

def draw_thermometer(temperature):
	thermometer= TempViewer(temperature)
	return thermometer.tostring()


@app.route("/")
def index():
	return render_template('index.html')
	

@app.route("/temperature/export")
def export_temperature():
	temperature = int(request.args.get('temperature', '0'))
	return draw_thermometer(temperature)

@app.route("/sensor/set_data")
def set_data():
	temperature = round(float(request.args.get('t', '0')),2)
	humidity = round(float(request.args.get('h', '0')),2)
	sensor_data={
		"humidity": humidity, 
		"temperature": temperature
	}
	socketio.emit("sensor_data", sensor_data)
	return "SENT"



