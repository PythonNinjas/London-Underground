def read_stations(station):
	"""
	Read the stations from xml into a ???.
	"""
	import xml.etree.ElementTree as ET
	
	tree = ET.parse('dbs/stations.xml')
	root = tree.getroot()

	for station_name in root.findall('Station'):

		if station_name.get('id') == station:
		
			latitude = station_name.find('Latitude').text
			longitude = station_name.find('Longitude').text
			line = station_name.find('Line').text
			line = line.replace("[","")
			line = line.replace("]","")
			line = line.replace(" ","")
			line = line.split(',')
			zone = station_name.find('Zone').text
			station_dic = {station: (latitude, longitude, line, zone)}
			
			return station_dic

#print(read_stations("Waterloo"))