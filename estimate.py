#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import sys

def estimate(theta, x):
		return theta[0] + theta[1] * x

def loadTheta(name):
	with open(name, "r") as file:
		theta = file.read().split(",")
		if len(theta) == 2:
			for i, elem in enumerate(theta):
				try:
					theta[i] = float(elem)
				except:
					return -1
			return theta
		return -1

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc == 3:
		nb = sys.argv[1]
		theta = loadTheta(sys.argv[2])

		if not nb.replace(".", "", 1).isdigit():
			print("Invalid value.")
			exit()
		if theta == -1:
			print("Invalid theta.")
			exit()

		nb = float(nb)
		print(theta, nb)
		es = estimate(theta, nb)
		print("Estimate:", nb, "=>", es)
	else:
		print("Invalid arguments. (value fileName.theta)")
