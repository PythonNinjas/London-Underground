from exturtle import *
from read_stations import *
from read_lines import *
from least_stations import *

def draw_line(turtle, Line):
	"""
	This fuction was writen by Marta...
	Draws one line called "Line" on the map.
	"""
	hideturtle(turtle)			# To draw faster.
	screensize(30000, 30000)
	
	for Fork in Line:
		
		# Create a dictionary of the stations of this fork, with their coordinates in
		# the format: Stations_Coordinates = {"Station": [latitude, longitude]}	
		Stations_Coordinates = {}
		for Station in Fork:
			Latitude = read_stations(Station)
			Latitude = float(Latitude[Station][0])
			Longitude = read_stations(Station)
			Longitude = float(Longitude[Station][1])
			Coordinates = [Latitude, Longitude]
			Stations_Coordinates[Station] = Coordinates
				
		# Move the turtle to the starting point of each line:
		penup(turtle)
		Sc = 4500
		X_adjustment = 500
		Y_adjustment = -232000
		X_start = Stations_Coordinates[Fork[0]][1]*Sc + X_adjustment		# Longitude is X!
		Y_start = Stations_Coordinates[Fork[0]][0]*Sc + Y_adjustment		# Latitude is Y!
		goto(turtle, X_start, Y_start)
		pendown(turtle)
			
		# Draw the fork:
		for Station in Fork:
			X = Stations_Coordinates[Station][1]*Sc + X_adjustment
			Y = Stations_Coordinates[Station][0]*Sc + Y_adjustment
			#print("X is:", X, "Y is:", Y)
			goto(turtle, X, Y)
			dot(turtle, 5, "black")
			
			# Display the name of each station:
			write(turtle, Station, move = False, align = "left", font = ("Arial", 5, "normal"))

def draw_map(Starting_Station, Ending_Station):
	"""
	This fuction was writen by Marta...
	Draws a map of the London Underground.
	"""
	turtle = Turtle()
	
	# Define the colour scheme for the different lines:
	Colours	= {"Bakerloo": "#D16F18", "Central": "#DF3C2A", "Hammersmith & City": "#F2ABEB", "Circle": "#F5EF4F", "District": "#109B19", "Jubilee": "#B0B0B0", "Metropolitan": "#870995", "Northern": "#484848", "Piccadilly": "#1935EB", "Victoria": "#46A9EB", "Waterloo & City": "#5AE5E5"}
	
	screensize(30000, 30000)
	
	# Create a dictionary of all the lines in the format:
	# {"Line_Name": [[Fork], ... , [Fork]], ...}
	All_Lines = read_lines()
	
	# Iterate over this dictionary, to plot every line:
	for Line_Name in All_Lines:
		
		# Determine the line colour according to commonly acceptable colour scheme of the London underground:
		if Line_Name in Colours:
			pencolor(turtle, Colours[Line_Name])
		
		# Make sure that if someone tests the function with lines, other than those of
		# the London tube, it will still work, but plot them in black:
		else:
			pencolor(turtle, "black")
		
		# Draw the line:
		Line = All_Lines[Line_Name]
		draw_line(turtle, Line)
	
	# Now draw the best route with another colour, in bold:
	pencolor(turtle, "#8BF512")
	pensize(turtle, 3)
	check, Best_Route = least_stations(Starting_Station, Ending_Station)
	Route = [Best_Route]
	if check == True:
		draw_line(turtle, Route)
		
	
#########################################################################################################################################
#						Main program starts here																						#
#########################################################################################################################################

# Some testing of the functions:
if __name__ == "__main__":
	
	# Bakerloo_and_Central = {"Bakerloo": [["Elephant & Castle", "Lambeth North", "Waterloo", "Embankment", "Charing Cross", "Piccadilly Circus", "Oxford Circus", "Regent's Park", "Baker Street", "Marylebone", "Edgware Road", "Paddington", "Warwick Avenue", "Maida Vale", "Kilburn Park", "Queen's Park", "Kensal Green", "Willesden Junction", "Harlesden", "Stonebridge Park", "Wembley Central", "North Wembley", "South Kenton", "Kenton", "Harrow & Wealdstone"]], "Central": [["Epping", "Theydon Bois", "Debden", "Loughton", "Buckhurst Hill", "Woodford", "South Woodford", "Snaresbrook", "Leytonstone", "Leyton", "Stratford", "Mile End", "Bethnal Green", "Liverpool Street", "Bank", "St. Paul's", "Chancery Lane", "Holborn", "Tottenham Court Road", "Oxford Circus", "Bond Street", "Marble Arch", "Lancaster Gate", "Queensway", "Notting Hill Gate", "Holland Park", "Shepherd's Bush", "White City", "East Acton", "North Acton", "West Acton", "Ealing Broadway"], ["Hanger Lane", "Perivale", "Greenford", "Northolt", "South Ruislip", "Ruislip Gardens", "West Ruislip"], ["Woodford", "Roding Valley", "Grange Hill", "Chigwell", "Hainault", "Fairlop", "Barkingside", "Newbury Park", "Gants Hill", "Redbridge", "Wanstead", "Leystone"]]}
	#All_Lines = read_lines()
	
	#bob = Turtle()

	Map_all = draw_map("Acton Town", "Bank")
	mainloop()
