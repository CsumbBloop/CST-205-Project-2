#Team 43, Project 2, CST 205
#Eric Haro, Lesley Amezcua, David Beach
#This program extracts GPS metadata from an iPhone image, and displays it
#on a map

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import argparse
from PIL import Image
from PIL.ExifTags import TAGS
import random
import os
#this asks for the path of the image
#askimg = raw_input("path your image: ")
askFolder = raw_input("name of image folder: ")
#this creates the file name to be created and tells user
randomnumber = random.random()
strrandomnumber = str(randomnumber) + '.txt'
datafile = strrandomnumber
#datafile = askimg.split(".")[0] + '.txt'
print "Exif data location: " + datafile
#'askimg' is the path of the image
#imgpath = askimg

#exif scraper
#creates a text file after the name of the image that ends with ".txt"
def getMetaData(imgname, out): # imagename is the name of image and out is out of text file
	try:
		metaData = {}

		imgFile = Image.open(imgname)
		#print "Getting meta data..."
		info = imgFile._getexif()
		if info:
			#print "found meta data!"
			for (tag, value) in info.items():
				tagname = TAGS.get(tag, tag)
				metaData[tagname] = value
				if not out:
					print tagname, value

			if out:
				#print "Outputting to file..."
				with open(out, 'w') as f:
					for (tagname, value) in metaData.items():
						f.write(str(tagname)+"\t"+\
							str(value)+"\n")
		
	except:
		print "Failed"


#look for the 3 numbers used for the North direction and puts them into the correct format for the tranlator
#returns the latitudes found
def North(phrase):
	tempLatList = []
	i = phrase.index('N')
	comma = 0
	while True:
		if phrase[i] == ",":
			comma += 1
		if comma == 2:
			t = i
			end = 0
			while True:
				
				onelat = []
				if phrase[t] == "(":
					while True:
						
						if phrase[t+1] == ",":
							end = 1
							break
						onelat.append(phrase[t+1])
						t += 1
					
				
				if end == 1:
					break
				
				t -= 1
			onelatstr = ''.join(onelat)
			#latlist.append(onelatstr)
			tempLatList.append(onelatstr)
			comma += 1
		if comma == 6:
			t = i
			end = 0
			while True:
				
				onelat = []
				if phrase[t] == "(":
					while True:
						
						if phrase[t+1] == ",":
							end = 1
							break
						onelat.append(phrase[t+1])
						t += 1
					
				
				if end == 1:
					break
				t -= 1
			onelatstr = ''.join(onelat)
			#latlist.append(onelatstr)
			tempLatList.append(onelatstr)
			comma += 1
		if comma == 8:
			t = i
			end = 0
			while True:
				
				onelat = []
				if phrase[t] == "(":
					while True:
						if phrase[t+1] == ",":
							end = 1
							break
						onelat.append(phrase[t+1])
						
						t += 1
					
				
				if end == 1:
					break
				t -= 1
			onelatstr = ''.join(onelat)
			#latlist.append(onelatstr)
			tempLatList.append(onelatstr)
			comma += 1	
			break
		i += 1
	#print latlist
	return tempLatList		
#look for the 3 numbers used for the west direction and puts them into the correct format for the tranlator
#returns the longitudes found
def West(phrase):
	tempLonList = []
	if set('W').issubset(phrase):
		i = phrase.index('W')
		comma = 0
		while True:
			if phrase[i] == ",":
				comma += 1
			if comma == 2:
				t = i
				end = 0
				while True:
				
					onelat = []
					if phrase[t] == "(":
						while True:
						
							if phrase[t+1] == ",":
								end = 1
								break
							onelat.append(phrase[t+1])
							t += 1
					
				
					if end == 1:
						break
				
					t -= 1
				onelatstr = ''.join(onelat)
				#lonlist.append(onelatstr)
				tempLonList.append(onelatstr)
				comma += 1
			if comma == 6:
				t = i
				end = 0
				while True:
				
					onelat = []
					if phrase[t] == "(":
						while True:
						
							if phrase[t+1] == ",":
								end = 1
								break
							onelat.append(phrase[t+1])
							t += 1
					
				
					if end == 1:
						break
					t -= 1
				onelatstr = ''.join(onelat)
				#lonlist.append(onelatstr)
				tempLonList.append(onelatstr)
				comma += 1
			if comma == 8:
				t = i
				end = 0
				while True:
				
					onelat = []
					if phrase[t] == "(":
						while True:
							if phrase[t+1] == ",":
								end = 1
								break
							onelat.append(phrase[t+1])
						
							t += 1
					
				
					if end == 1:
						break
					t -= 1
				onelatstr = ''.join(onelat)
				#lonlist.append(onelatstr)
				tempLonList.append(onelatstr)
				comma += 1	
				break
			i += 1
	return tempLonList
	#print lonlist
#look for the 3 numbers used for the west direction and puts them into the correct format for the tranlator
def East():
	if set('E').issubset(phrase):
		i = phrase.index('E')
		comma = 0
		while True:
			if phrase[i] == ",":
				comma += 1
			if comma == 2:
				t = i
				end = 0
				while True:
				
					onelat = []
					if phrase[t] == "(":
						while True:
						
							if phrase[t+1] == ",":
								end = 1
								break
							onelat.append(phrase[t+1])
							t += 1
					
				
					if end == 1:
						break
				
					t -= 1
				onelatstr = ''.join(onelat)
				lonlist.append(onelatstr)
				comma += 1
			if comma == 6:
				t = i
				end = 0
				while True:
				
					onelat = []
					if phrase[t] == "(":
						while True:
						
							if phrase[t+1] == ",":
								end = 1
								break
							onelat.append(phrase[t+1])
							t += 1
					
				
					if end == 1:
						break
					t -= 1
				onelatstr = ''.join(onelat)
				lonlist.append(onelatstr)
				comma += 1
			if comma == 8:
				t = i
				end = 0
				while True:
				
					onelat = []
					if phrase[t] == "(":
						while True:
							if phrase[t+1] == ",":
								end = 1
								break
							onelat.append(phrase[t+1])
						
							t += 1
					
				
					if end == 1:
						break
					t -= 1
				onelatstr = ''.join(onelat)
				lonlist.append(onelatstr)
				comma += 1	
				break
			i += 1

#maps the latitudes and longitudes list of lats and longs
def mapTut(dLat, dLon):

     m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
     m.bluemarble()

     for i in xrange(len(dLat)):
	    x,y = m(dLon[i],dLat[i])
	    m.plot(x,y, 'ro')
	    plt.title("Geo Plotting")
     plt.show()

#gets the info from the image and returns the lat and lon after being processed
# Function
def getGPS(imgpath, datafile):
	getMetaData(imgpath, datafile)
	#img.txt reader
	strdatafile  = str(datafile) 
	file = open(strdatafile,'r+')
	linenumber = 0
	searchlines = file.readlines()
	file.close
	phrase  = []
	phrasetemp = []
	
	#this searches for 'GPS' in the exif data file
	for i, line in enumerate(searchlines):
		if "GPS" in line:
			 for l in searchlines[i:i+1]:
			 	y = str(l)
			 	#print y
			 	for letter in y:
			 		phrase.append(letter)


	#lats = East()		
	lats = North(phrase)
	lons = West(phrase)

	#GPS translator 
	
	lat = lats
	lon = lons

	dlat = int(lat[0]) + (float(lat[1])/60.0) + (float(lat[2])/3600.0)
	dlon = int(lon[0]) + (float(lon[1])/60.0) + (float(lon[2])/3600.0)

	dlat = dlat -0.27
	dlon = -dlon + 1.39

	return dlat,dlon

#creates a path based on the fodler that the user says they want to use
imageDir = os.getcwd()+"/"+askFolder+"/"
#gets all the images inside of the foolder
folderImages=os.listdir(imageDir)

totalLats = []
totalLons = []

for img in folderImages:
	print img
	#filters based on the image extension
	if(img.split(".")[1] == "JPG" or img.split(".")[1] == "jpg"):
		#sends in the path to the image and the name of the textfile that will contain the metadata
		imgLat, imgLon = getGPS(imageDir+img, img.split("/")[-1]+".txt")
		print "lat: "
		print imgLat 
		print "lon: "    
		print imgLon
		#appends the lats and lons to a list so that they can all be displayed
		totalLats.append(imgLat)
		totalLons.append(imgLon)

#function call sequence
#getGPS->getMetaData
#		->North
#		->West
#mapPut

#plots the map
mapTut(totalLats,totalLons)
