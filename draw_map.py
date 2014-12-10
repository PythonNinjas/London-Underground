from exturtle import *
from math import sin, cos

def draw_line(turtle, Line, Stations_Coordinates):
	"""
	Draws one line on the map.
	"""
	
	hideturtle(turtle)
	screensize(30000, 30000)
	
	for Fork in Line:
		if Fork == []:
			break
		else:
		
			# Create a dictionary of the stations of this fork, with their coordinates in
			# the format: Stations_Coordinates = {"Station": [latitude, longitude]}
			#Stations_Coordinates = {}
			#for Station in Fork:
				#Latitude = read_stations(Station)[0]
				#Longitude = read_stations(Station)[1]
				#New_Station = {Station: [Latitude, Longitude]}
				#Stations_Coordinates.append(New_Station)
				
			# Move the turtle to the starting point of each line:
			penup(turtle)
			
			#R = 6371*(10**3)
			#X_start = R*cos(radians(Stations_Coordinates[Line[0]][0]))*cos(radians(Stations_Coordinates[Line[0]][1]))
			#X_start = degrees(X_start)*5000
			#Y_start = R*cos(radians(Stations_Coordinates[Line[0]][0]))*sin(radians(Stations_Coordinates[Line[0]][1]))
			#Y_start = degrees(Y_start)*5000 - 257700
			
			X_start = Stations_Coordinates[Fork[0]][1]*5000 + 500
			Y_start = Stations_Coordinates[Fork[0]][0]*5000 - 257700
			goto(turtle, X_start, Y_start)
			pendown(turtle)
			
			# Start drawing the line:
			for Station in Fork:
				#X = degrees(R*cos(radians(Stations_Coordinates[Station][0]))*cos(radians(Stations_Coordinates[Station][1])))*5000
				#Y = degrees(R*cos(radians(Stations_Coordinates[Station][0]))*sin(radians(Stations_Coordinates[Station][1])))*5000 - 257700
				X = Stations_Coordinates[Station][1]*5000 + 500
				Y = Stations_Coordinates[Station][0]*5000 - 257700
				print("X is:", X, "Y is:", Y)
			
				goto(turtle, X, Y)
				dot(turtle, 5, "black")
				# Display the name of each station:
				write(turtle, Station, move = False, align = "left", font = ("Arial", 5, "normal"))

def draw_map(turtle, All_Lines, Stations_Coordinates):
	"""
	Draws a map of the London Underground.
	"""
	Colours	= {"Bakerloo": "#D16F18", "Central_1": "#DF3C2A", "Hammersmith & City": "#F2ABEB", "Circle": "#F5EF4F", "District": "#109B19", "Jubilee": "#B0B0B0", "Metropolitan": "#870995", "Northern": "#484848", "Piccadily": "#1935EB", "Victoria": "#46A9EB", "Waterloo & City": "#5AE5E5"}
	screensize(30000, 30000)
	
	for Line_Name in All_Lines:
		# Determine the line colour according to commonly acceptable colour scheme of the London underground:
		if Line_Name in Colours:
			pencolor(turtle, Colours[Line_Name])
		else:
			pencolor(turtle, "black")
		Line = All_Lines[Line_Name]
		draw_line(turtle, Line, Stations_Coordinates)
	
	# Now draw the best route with another colour, in bold:
	# pencolour(turtle, "#8BF512")
	# pensize(turtle, 3)
	# draw_line(???)
		
	
#################################################################################################################################################################################
#						Main program starts here																																#
#################################################################################################################################################################################

Colours	= {"Bakerloo": "#D16F18", "Central": "#DF3C2A", "Hammersmith & City": "#F2ABEB", "Circle": "#F5EF4F", "District": "#109B19", "Jubilee": "#B0B0B0", "Metropolitan": "#870995", "Northern": "#484848", "Piccadily": "#1935EB", "Victoria": "#46A9EB", "Waterloo & City": "#5AE5E5"}
Stations_Coordinates = {"Elephant & Castle": [51.49467, -0.10047], "Lambeth North": [51.49894, -0.11216], "Waterloo": [51.50322, -0.11328], "Embankment": [51.50717, -0.12195], "Charing Cross": [51.507108, -0.122963], "Piccadilly Circus": [51.51022, -0.13392], "Oxford Circus": [51.51517, -0.14119], "Regent's Park": [51.52344, -0.14713], "Baker Street": [51.52265, -0.15704], "Marylebone": [51.52266, -0.162996], "Edgware Road": [51.51956, -0.169068], "Paddington": [51.5151846554, -0.17553880792], "Warwick Avenue": [51.52329728, -0.183777837], "Maida Vale": [51.52989409, -0.185888819], "Kilburn Park": [51.53495818, -0.193963023], "Queen's Park": [51.534179, -0.205257721], "Kensal Green": [51.53060655, -0.224253545], "Willesden Junction": [51.53032031, -0.229378995], "Harlesden": [51.53628278, -0.257622488], "Stonebridge Park": [51.54402388, -0.275978856], "Wembley Central": [51.55122817, -0.29577538], "North Wembley": [51.56258091, -0.304072648], "South Kenton": [51.57044666, -0.308566354], "Kenton": [51.58173809, -0.316870809], "Harrow & Wealdstone": [51.59205973, -0.334725352], "Epping": [51.69365, +0.11495], "Theydon Bois": [51.67246, +0.10354], "Debden": [51.64535, +0.08364], "Loughton": [51.6417, +0.05583], "Buckhurst Hill": [51.62611, +0.04705], "Woodford": [51.60582, +0.03328], "South Woodford": [51.59088, +0.02726], "Snaresbrook": [51.58002, +0.02133], "Leytonstone": [51.56828, 0.00739], "Leyton": [51.556483, -0.005669], "Stratford": [51.541208, -0.003776], "Mile End": [51.525306, -0.033471], "Bethnal Green": [51.52718, -0.05504], "Liverpool Street": [51.517675, -0.082458], "Bank": [51.5134047, -0.08905843], "St. Paul's": [51.515285, -0.097598], "Chancery Lane": [51.51836, -0.11115], "Holborn": [51.51711, -0.12055], "Tottenham Court Road": [51.5164, -0.13027], "Bond Street": [51.51461, -0.14897], "Marble Arch": [51.513597, -0.15869195], "Lancaster Gate": [51.512083, -0.175067], "Queensway": [51.510484, -0.18705], "Notting Hill Gate": [51.509028, -0.1962847], "Holland Park": [51.50722, -0.20553], "Shepherd's Bush": [51.50474, -0.21881], "White City": [51.512206, -0.224226], "East Acton": [51.51753, -0.24827], "North Acton": [51.5237, -0.26019], "West Acton": [51.51818, -0.28064], "Ealing Broadway": [51.51482, -0.30118]}
#Bakerloo = [["Elephant & Castle", "Lambeth North", "Waterloo", "Embankment", "Charing Cross", "Piccadilly Circus", "Oxford Circus", "Regent's Park", "Baker Street", "Marylebone", "Edgware Road", "Paddington", "Warwick Avenue", "Maida Vale", "Kilburn Park", "Queen's Park", "Kensal Green", "Willesden Junction", "Harlesden", "Stonebridge Park", "Wembley Central", "North Wembley", "South Kenton", "Kenton", "Harrow & Wealdstone"]]
#Central_1 = [["Epping", "Theydon Bois", "Debden", "Loughton", "Buckhurst Hill", "Woodford", "South Woodford", "Snaresbrook", "Leytonstone", "Leyton", "Stratford", "Mile End", "Bethnal Green", "Liverpool Street", "Bank", "St. Paul's", "Chancery Lane", "Holborn", "Tottenham Court Road", "Oxford Circus", "Bond Street", "Marble Arch", "Lancaster Gate", "Queensway", "Notting Hill Gate", "Holland Park", "Shepherd's Bush", "White City", "East Acton", "North Acton", "West Acton", "Ealing Broadway"]]

All_Lines = {"Bakerloo": [["Elephant & Castle", "Lambeth North", "Waterloo", "Embankment", "Charing Cross", "Piccadilly Circus", "Oxford Circus", "Regent's Park", "Baker Street", "Marylebone", "Edgware Road", "Paddington", "Warwick Avenue", "Maida Vale", "Kilburn Park", "Queen's Park", "Kensal Green", "Willesden Junction", "Harlesden", "Stonebridge Park", "Wembley Central", "North Wembley", "South Kenton", "Kenton", "Harrow & Wealdstone"]], "Central_1": [["Epping", "Theydon Bois", "Debden", "Loughton", "Buckhurst Hill", "Woodford", "South Woodford", "Snaresbrook", "Leytonstone", "Leyton", "Stratford", "Mile End", "Bethnal Green", "Liverpool Street", "Bank", "St. Paul's", "Chancery Lane", "Holborn", "Tottenham Court Road", "Oxford Circus", "Bond Street", "Marble Arch", "Lancaster Gate", "Queensway", "Notting Hill Gate", "Holland Park", "Shepherd's Bush", "White City", "East Acton", "North Acton", "West Acton", "Ealing Broadway"]]}
	
bob = Turtle()
#Draw_Bakerloo = draw_line(bob, Bakerloo, Stations_Coordinates)
#Draw_Central_1 = draw_line(bob, Central_1, Stations_Coordinates)

Map_all = draw_map(bob, All_Lines, Stations_Coordinates)
mainloop()
