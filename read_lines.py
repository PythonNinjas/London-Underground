""" Returns dictionary of lines with stations - Not finished """

import xml.etree.ElementTree as ET

def read_lines():

	""" Returns dictionary of stations """

	tree = ET.parse('dbs/lines.xml')
	root = tree.getroot()

	lines = {}  # Dictionary

	for line in root.findall('line'):

		line_name = line.get('id')

		print(line_name)

		for child in line.getchildren():

			print(child.text)


if __name__ == "__main__":

	read_lines()

	
