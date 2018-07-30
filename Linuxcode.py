#! /usr/bin/python

import sys
import os
import json

try:
	json_file = open("data.json","r")
except Exception :
	json_file.close() 		#if Error then close the file
	sys.exit("Error: File can't be accessed")

try:
	data = json.loads(json_file)
except Exception:
	json_file.close() 		#if Error then close the file
	sys.exit("Incorrect JSON format provided")
	
# Assuming that the data is in a known json format
dependencies = data['Dependencies']
not_Installed = dict()
for element in dependencies:
	try:
		if sys.version_info[0]<3:		#which python version is installed
			command = "pip install {}{}".format(element,dependencies[element])
			command	= os.system(str(command))
		else:
		command = "pip3 install {}{}".format(element,dependencies[element])
		command	= os.system(str(command))
		
		if command!=0:		#Checking response code returned by system 
			not_Installed[element] = dependencies[element]

# Print list of Packages which failed
if not_Installed:
	print("Failed Packages :"
	for i,j in not_Installed.items():
		print(i, j)
else:
	print("Successfully Installed Dependencies")

#Close the opened file
json_file.close()
