def read_stations(station):
	"""
	Read the stations from xml into a ???.
	"""
	import xml.etree.ElementTree as ET
	#here we are importing the .xml file
	tree = ET.parse('dbs/stations.xml')
	root = tree.getroot()
	
	#This will loop through all the ids with Station in the ID in the .xml file
	for station_name in root.findall('Station'):
		#Checks to make sure we are looking at the correct station with the station name given
		if station_name.get('id') == station:
			#Getting all the values of the station that we want, with some string manipulation to make a list from the lines given
			latitude = station_name.find('Latitude').text
			longitude = station_name.find('Longitude').text
			line = station_name.find('Line').text
			line = line.replace("[","")
			line = line.replace("]","")
			line = line.replace(" ","")
			line = line.replace("&"," & ")
			line = line.split(',')
			zone = station_name.find('Zone').text
			# Make a dictionary to return to the user
			station_dic = {station: (latitude, longitude, line, zone)}
			
			return True, station_dic
	err_msg = "You have inputed an incorrect Station name, please check your spelling and also your spacing."
	return False, err_msg
#Testing area to make sure that the function can work on its own with given details
#nprint(read_stations("Hammersmith&City"))
