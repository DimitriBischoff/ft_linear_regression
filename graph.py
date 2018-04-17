#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Graph:
	def __init__(self, data, theta):
		self.titleX = data["titleX"]
		self.titleY = data["titleY"]
		self.listX = data["listX"]
		self.listY = data["listY"]
		self.theta = theta
		self.line, = plt.plot([], [])
		self.initMinMax()
		self.showGraph()
		self.showLine()
		plt.show()

	def showGraph(self):
		plt.scatter(self.listX, self.listY)
		plt.xlabel(self.titleX)
		plt.ylabel(self.titleY)

	def searchMinMax(self, liste):
		m = liste[0]
		M = liste[0]
		for num in liste:
			if num < m:
				m = num
			if num > M:
				M = num
		return m, M

	def initMinMax(self):
		self.minX, self.maxX = self.searchMinMax(self.listX)
		self.minY, self.maxY = self.searchMinMax(self.listY)

	def animate(self, i):
		self.theta = self.func(self.theta, i)
		line = self.showLine()
		print("return animate")
		return line

	def showLine(self):
		theta = self.theta
		x = [0, self.maxX]
		y = [theta[0], theta[0] + theta[1] * self.maxX]
		plt.plot(x, y)
