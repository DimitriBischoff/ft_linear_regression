#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import math

class Gradient:

	def __init__(self, data):
		self.listX = data["listX"]
		self.listY = data["listY"]
		self.format_listX = []
		self.format_listY = []
		self.maxX = max(self.listX)
		self.maxY = max(self.listY)
		if len(self.listX) > 0 and len(self.listY):
			self.format_listX, self.format_listY = self.format()

	def max(self, liste):
		maxV = liste[0]
		for x in liste:
			if v * v > maxV * maxV:
				maxV = v
		if maxV < 0:
			return -maxV
		return maxV

	def format(self):
		format_listX = []
		format_listY = []

		for elem in self.listX:
			format_listX.append(elem / self.maxX)
		for elem in self.listY:
			format_listY.append(elem / self.maxY)
		return format_listX, format_listY

	def estimate(self, theta, x):
		return theta[0] + theta[1] * x

	def learn(self, theta, learn_rate, listX, listY):
		m = len(listX)
		ret = 0
		new_theta = [0, 0]

		if m < 1:
			return new_theta;
		for i_theta in range(len(theta)):
			error = 0
			for i in range(m):
				if i_theta == 0:
					error += self.estimate(theta, listX[i]) - listY[i]
				else:
					error += (self.estimate(theta, listX[i]) - listY[i]) * listX[i]
			error /= m
			new_theta[i_theta] = theta[i_theta] - learn_rate * error
			ret += error
		return new_theta, ret / 2

	def run(self, learn_rate = 1, errorMin = 0.0001):
		theta = [0, 0]
		error = 1
		it = 0
		errorMin = errorMin * errorMin
		while error * error > errorMin and it < 1000000:
			theta, error = self.learn(theta, learn_rate, self.format_listX, self.format_listY)
			it += 1
		theta[0] *= self.maxY
		theta[1] /= (self.maxX / self.maxY)
		return theta, it
