#Team 43, Project 2, CST 205
#https://github.com/CsumbBloop/CST-205-Project-2
#Eric Haro, Lesley Amezcua, David Beach
#This program extracts GPS metadata from an iPhone image, and displays it
#on a map

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import argparse
from PIL import Image
from PIL.ExifTags import TAGS
import random
#this asks for the path of the image
askimg = raw_input("path your image: ")
#this creates the file name to be created and tells user
randomnumber = random.random()
strrandomnumber = str(randomnumber) + '.txt'
datafile = strrandomnumber
print "Exif data location: " + datafile
#'askimg' is the path of the image
imgpath = askimg

#exif scraper
def getMetaData(imgname, out):
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
getMetaData(imgpath, datafile)

#data.txt reader

strdatafile  = str(datafile) 

file = open(strdatafile,'r+')
linenumber = 0
searchlines = file.readlines()
file.close
phrase  = []
phrasetemp = []
latlist = []
lonlist = []
#this searches for 'GPS' in the exif data file
for i, line in enumerate(searchlines):
	if "GPS" in line:
		 for l in searchlines[i:i+1]:
		 	y = str(l)
		 	#print y
		 	for letter in y:
		 		phrase.append(letter)
#look for the 3 numbers used for the North direction and puts them into the correct format for the tranlator
def North():
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
			latlist.append(onelatstr)
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
			latlist.append(onelatstr)
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
			latlist.append(onelatstr)
			comma += 1	
			break
		i += 1
	#print latlist		
#look for the 3 numbers used for the west direction and puts them into the correct format for the tranlator
def West():
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
East()		
North()
West()

#GPS translator 
lat = latlist
lon = lonlist
dlat = int(lat[0]) + (float(lat[1])/60.0) + (float(lat[2])/3600.0)
dlon = int(lon[0]) + (float(lon[1])/60.0) + (float(lon[2])/3600.0)

dlat = dlat -0.27
dlon = -dlon + 1.39
print "lat: "
print dlat 
print "lon: " 
print dlon 

#matplotlib map
def mapTut():

    m = Basemap(projection='mill',llcrnrlat=20,urcrnrlat=50,\
                llcrnrlon=-130,urcrnrlon=-60,resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF')
    m.drawmapboundary(fill_color='#FFFFFF')




    lat,lon = dlat,dlon
    x,y = m(lon,lat)
    m.plot(x,y, 'ro')
    

    #lon, lat = -104.237, 40.125 # Location of Boulder

    xpt,ypt = m(lon,lat)
    m.plot(xpt,ypt, 'go')
    
    plt.title("Geo Plotting")
    plt.show()


mapTut()
