#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import sys
from data import *
from graph import *
from gradient import *

def saveTheta(name, theta):
	name += ".theta"
	with open(name, "w") as file:
		file.write(str(theta[0]) + "," + str(theta[1]))
		print("Create file", "\"" + name + "\"")

def main(path):
		tmp = Data(path)
		if not tmp.valid:
			return print("Invalid data.")
		data = tmp.get()
		gr = Gradient(data)
		theta, it = gr.run()
		print ("theta", theta, "iteration:", it)
		name = (data["titleX"] + "_" + data["titleY"])
		saveTheta(name, theta)
		Graph(data, theta)

if __name__ == "__main__":
	i = 1
	argc = len(sys.argv)

	if argc > 1:
		while i < argc:
			main(sys.argv[i])
			i += 1
	else:
		print("No file.")
