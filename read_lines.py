""" Returns dictionary of stations with line as key. Not finished. Doesn't handle <part1> tags etc. """

import xml.etree.ElementTree as ET

def read_lines():

	""" Returns dictionary of stations """

	tree = ET.parse('dbs/lines.xml')
	root = tree.getroot()

	lines = {}  # Dictionary

	for line in root.findall('line'):

		line_name = line.get('id')

		stations = []

		for station in line.getchildren():

			stations.append(station.text)

		lines[line_name] = stations

	return lines


if __name__ == "__main__":

	d = read_lines()
	print(d)

	
