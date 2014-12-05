from exturtle import *

#def draw_line(turtle, Longtitudes, Latitudes):
#	"""
#	Draws one line of the map.
#	"""
#	penup(turtle)
#	goto(turtle, Longtitudes[0]*10000, Latitudes[0]*10000)
#	pendown(turtle)
#	for Longtitude, Latitude in zip(Longtitudes, Latitudes):
#		X = Longtitude*10000
#		Y = Latitude*10000
#		print('X, Y is:', X, Y)
#		goto(turtle, X, Y)
#		dot(turtle, 5, "black")
#
#def draw_map(turtle, Longtitudes, Latitudes):
#	"""
#	Draws the whole underground map and then highlights the best route.
#	"""
#	screensize(1200000, 1200000)
#	hideturtle(turtle)
#	for Line in All_Lines:
		
def draw_line(turtle, Line_List, Line_Dictionary):
	"""
	Draws one line of the map.
	"""
	screensize(30000, 30000)
	hideturtle(turtle)
	
	penup(turtle)
	goto(turtle, Line_Dictionary[Line_List[0]][1]*10000, Line_Dictionary[Line_List[0]][0]*10000 - 510000)
	pendown(turtle)
	
	for Station in Line_List:
		X = Line_Dictionary[Station][1]*10000
		Y = Line_Dictionary[Station][0]*10000 - 510000
		print("X, Y is:", X, Y)
		goto(turtle, X, Y)
		dot(turtle, 5, "black")	

#################################################################################################################################################################################
#						Main program starts here																																#
#################################################################################################################################################################################
		
Line_Bakerloo_Dictionary = {"Elephant & Castle": [51.49467, -0.10047], "Lambeth North": [51.49894, -0.11216], "Waterloo": [51.50322, -0.11328], "Embankment": [51.50717, -0.12195], "Charing Cross": [51.507108, -0.122963], "Piccadilly Circus": [51.51022, -0.13392], "Oxford Circus": [51.51517, -0.14119], "Regent's Park": [51.52344, -0.14713], "Baker Street": [51.52265, -0.15704], "Marylebone": [51.52266, -0.162996], "Edgware Road": [51.51956, -0.169068], "Paddington": [51.5151846554, -0.17553880792], "Warwick Avenue": [51.52329728, -0.183777837], "Maida Vale": [51.52989409, -0.185888819], "Kilburn Park": [51.53495818, -0.193963023], "Queen's Park": [51.534179, -0.205257721], "Kensal Green": [51.53060655, -0.224253545], "Willesden Junction": [51.53032031, -0.229378995], "Harlesden": [51.53628278, -0.257622488], "Stonebridge Park": [51.54402388, -0.275978856], "Wembley Central": [51.55122817, -0.29577538], "North Wembley": [51.56258091, -0.304072648], "South Kenton": [51.57044666, -0.308566354], "Kenton": [51.58173809, -0.316870809], "Harrow & Wealdstone": [51.59205973, -0.334725352]}
Line_Bakerloo_List = ["Elephant & Castle", "Lambeth North", "Waterloo", "Embankment", "Charing Cross", "Piccadilly Circus", "Oxford Circus", "Regent's Park", "Baker Street",
"Marylebone", "Edgware Road", "Paddington", "Warwick Avenue", "Maida Vale", "Kilburn Park", "Queen's Park", "Kensal Green", "Willesden Junction", "Harlesden", "Stonebridge Park",
"Wembley Central", "North Wembley", "South Kenton", "Kenton", "Harrow & Wealdstone"]
# Latitudes_Bakerloo = [51.49467, 51.49894, 51.50322, 51.50717, 51.507108, 51.51022, 51.51517, 51.52344, 51.52265, 51.52266, 51.51956, 51.5151846554, 51.52329728, 51.52989409, 51.53495818, 51.534179, 51.53060655, 51.53032031, 51.53628278, 51.54402388, 51.55122817, 51.56258091, 51.57044666, 51.58173809, 51.59205973]
# Longtitudes_Bakerloo = [-0.10047, -0.11216, -0.11328, -0.12195, -0.122963, -0.13392, -0.14119, -0.14713, -0.15704, -0.162996, -0.169068, -0.17553880792, -0.183777837, -0.185888819, -0.193963023, -0.205257721, -0.224253545, -0.229378995, -0.257622488, -0.275978856, -0.29577538, -0.304072648, -0.308566354, -0.316870809, -0.334725352]

# All_Lines = {}

bob = Turtle()
Map = draw_line(bob, Line_Bakerloo_List, Line_Bakerloo_Dictionary)

mainloop()