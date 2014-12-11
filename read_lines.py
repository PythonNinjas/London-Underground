""" Returns dictionary of stations with line as key. Not finished. Doesn't handle <part1> tags etc. """

import xml.etree.ElementTree as ET

def read_lines():

	""" Returns dictionary of stations """

	tree = ET.parse('dbs/lines.xml')
	root = tree.getroot()

	lines = {}  # Dictionary

	for line in root.findall('line'):

		line_name = line.get('id')
		no_forks = []
		stations = []

		for station in line.getchildren():

			if "part" in station.tag:
				stations.append(get_part_contents(station))
			else:
				stations.append(station.text.replace("\"", ""))

		#Here we need to make sure that the lists/stations are represented in the same way. 
		stations_string = str(stations)
		#Here we are checking to see if the list of stations has forks in them, if not them we make them the same formate
		char = "["
		for char in stations_string:
			count = stations_string.count(char)


		if count < 2:
			no_forks.append(stations)
			lines[line_name] = no_forks
		else:
			lines[line_name] = stations


	return lines


def get_part_contents(part):

	""" Returns stations in part tag as list """

	stations = []

	for station in part.getchildren():

		stations.append(station.text.replace("\"", ""))

	return stations

if __name__ == "__main__":

	d = read_lines()
