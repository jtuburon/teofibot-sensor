# -*- coding: utf-8 -*-

import svgwrite

class TempViewer():

	def __init__(self, temperature=0):
		self.dwg = svgwrite.Drawing('test.svg', size=('90px', '370px'), profile='full')
		self.temperature=temperature
		self.minTemp= 0
		self.maxTemp= 50
		self.__minTempYPos= 300
		self.__maxTempYPos= 50
		self.__init_thermo()
		self.__plot_temperature()
		
	def tostring(self):
		return self.dwg.tostring()

	def __init_thermo(self):
		self.dwg.add(svgwrite.shapes.Rect(
			(17, 30), 
			(26, 320), 
			stroke = "black", 
			stroke_width = 3, 
			fill = "white"
			)
		)
		self.dwg.add(svgwrite.shapes.Circle(
			(30, 335), 
			25, 
			stroke = "black", 
			stroke_width = 3, 
			fill = "white"
			)
		)
		self.dwg.add(svgwrite.shapes.Circle(
			(30, 335), 
			22, 
			fill = "red"
			)
		)

		self.dwg.add(svgwrite.shapes.Rect(
			(21, 300), 
			(18, 20), 
			fill = "red"
			)
		)
		self.__init_scale()

	def draw_scale_measure(self, tempValue):
		yPos= self.__minTempYPos - tempValue* self.unitSize
		self.dwg.add(svgwrite.shapes.Line(
			(38, yPos), 
			(48, yPos), 
			stroke = "black",
			stroke_width = 3, 
			)
		)
		self.dwg.add(svgwrite.text.Text(
			str(tempValue)+"°C", 
			(50, yPos),
			font_size=10
			)
		)

	def __init_scale(self):
		self.unitSize= abs(self.__maxTempYPos- self.__minTempYPos)/(self.maxTemp -self.minTemp)
		self.steps = 10 
		self.stepSize = (self.maxTemp -self.minTemp)/ self.steps
		for step in range(self.steps +1):
			self.draw_scale_measure(step* self.stepSize)

		
	def __plot_temperature(self):
		print self.temperature
		yPos= self.__minTempYPos - self.temperature* self.unitSize

		self.dwg.add(svgwrite.shapes.Rect(
			(21, yPos), 
			(18, self.temperature* self.unitSize), 
			fill = "red"
			)
		)