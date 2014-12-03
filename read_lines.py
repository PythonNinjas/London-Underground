""" This program prints the first station of the line passed in - Not finished """

import xml.dom.minidom

def read_lines(line_id):

	dom = xml.dom.minidom.parse('lines.xml')
	a = dom.getElementsByTagName("line")
	#b = a[0].attributes["id"].value

	for tag in a:

		lineID = tag.attributes["id"].value

		if lineID == line_id:

			print(tag.getElementsByTagName("station1")[0].firstChild.nodeValue)


if __name__ == "__main__":
	
	read_lines("Circle")

	
