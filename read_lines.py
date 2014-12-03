""" Doc String	"""

from xml.dom.minidom import parse, parseString

def read_lines():
	"""	"""
	datasource = open('stations.xml')
	dom  = parse(datasource)

	return dom

if __name__ == "__main__":
