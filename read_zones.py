def read_zones(zone):
	"""
	This function was Written by Sai, and Joel...
	Read the zones from xml into a ???.
	"""

	import xml.etree.ElementTree as ET

	tree = ET.parse('dbs/zones.xml')
	root = tree.getroot()
	zone_Prices = []
	#This will look through all the Zone names in the .xml
	for zones in root.findall('Zone'):
		#Here we check to see if the input matchs the Zone in the .xml file
		if zones.get('id') == zone:
			#This will loop through all the values in the child of the zone
			for item in range(1,10):
				
				dif_Zones = "Zone" + str(item)

				price = zones.find(dif_Zones).text

				price = price.replace(" ","")
				zone_Prices.append(price)
			#We get all the vaules and put them in a list, we then make a dic to give back to the user.
			zones_dic = {zone: zone_Prices}

			return zones_dic

	err_msg = "You entered an incorrect Zone name, please use the format - eg/ 'Zone1'"
	return err_msg


#Testing area to make sure that the function can work on its own with given details
#print(read_zones("Zone2"))