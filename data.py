#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

class Data:

	def __init__(self, path):
		self.titleX = ""
		self.titleY = ""
		self.listX = []
		self.listY = []
		self.path = path
		self.raw = ""
		self.format = []
		self.read()
		self.formatData()
		if self.isValid():
			self.valid = True
			self.run()
		else:
			self.valid = False

	def read(self):
		with open(self.path, "r") as file:
			self.raw = file.read()

	def formatData(self):
		tmp = self.raw.split('\n')
		for line in tmp:
			if line:
				self.format.append(line.replace(" ", "").split(','))

	def isValid(self):
		for i, line in enumerate(self.format):
			if len(line) != 2:
				return False
			for elem in line:
				if i > 0 and not elem.replace(".", "", 1).isdigit():
					return False
		return True

	def run(self):
		for i, line in enumerate(self.format):
			if i == 0:
				self.titleX = line[0]
				self.titleY = line[1]
			else:
				self.listX.append(float(line[0]))
				self.listY.append(float(line[1]))

	def get(self):
		return {"titleX" : self.titleX, "titleY": self.titleY, "listX": self.listX, "listY": self.listY}

if __name__ == "__main__":
	data = Data("data.csv")
	print(data.get())