from read_stations import *

def least_stations(start, end):
	"""
	Find the route with the least number of stations.
	"""
	#================================================================================
	#Here we need to get the information for the other functions files in this area
	#and save the information to variables
	start_Station_Dic = read_stations(start)
	end_Station_Dic = read_stations(end)
	#print(start_Station_Dic[start][2])
	#print(end_Station_Dic[end][2])
	various_Routes = {}
	
	#================================================================================
	#First check to see if they are on the same line (NEED TO CHECK FOR THE DIFFERENT PARTS IN A LINE)
	#This will loop through the stations that the first station are on. From this we can work out the different routes to the end station


	#--------------------------------------------------------------------------------
	#-         This Area with see if the stations are on the same line              -
	#--------------------------------------------------------------------------------
	for line in start_Station_Dic[start][2]:
		route = []

		#print(line)
		if line in end_Station_Dic[end][2]:
			
			route_Line = Line_db[line]

			#Using the line db, we check to check the indexs of the start and end station, and go through the inbetween stations to find the name of them
			
			start_Index = route_Line.index(start)
			end_Index = route_Line.index(end)
			station_Stops = end_Index - start_Index


			#We add alls the stops in the list and return this to a dic to give the different option.
			if station_Stops > 0:
				route = route_Line[start_Index:end_Index]
			else:
				route = route_Line[start_Index:end_Index:-1]

			print(route)

			#print(station_Stops)

			#various_Routes[station_Stops] = route
	return route

	#--------------------------------------------------------------------------------
	#-    [END]This Area with see if the stations are on the same line[END]         -
	#--------------------------------------------------------------------------------

	# #This will make sure to check the other parts of the line
	#--------------------------------------------------------------------------------
	#-                                 Next area                                    -
	#--------------------------------------------------------------------------------
	
	







#===============================================================================================================================================================
#This is a testing area for this function
#===============================================================================================================================================================
#These variables below are going to be the teseting database values
Line_db = {"Bakerloo": ['Elephant & Castle', 'Lambeth North', 'Waterloo', 'Embankment', 'Charing Cross', 'Piccadilly Circus', 'Oxford Circus', "Regent's Park", 'Baker Street', 'Marylebone', 'Edgware Road', 'Paddington', 'Warwick Avenue', 'Maida Vale', 'Kilburn Park', "Queen's Park", 'Kensal Green', 'Willesden Junction', 'Harlesden', 'Stonebridge Park', 'Wembley Central', 'North Wembley', 'South Kenton', 'Kenton', 'Harrow & Wealdstone']}
station_One_Info = {'Waterloo': (51.50322, -0.11328, ['Bakerloo', 'Waterloo & City'], 1) }
station_Two_Info = {'Charing Cross': (51.507108, -0.122963, ['Bakerloo', 'Northern' ], 1) }

Latitudes_Bakerloo = [51.49467, 51.49894, 51.50322, 51.50717, 51.507108, 51.51022, 51.51517, 51.52344, 51.52265, 51.52266, 51.51956, 51.5151846554, 51.52329728, 51.52989409, 51.53495818, 51.534179, 51.53060655, 51.53032031, 51.53628278, 51.54402388, 51.55122817, 51.56258091, 51.57044666, 51.58173809, 51.59205973]
Longtitudes_Bakerloo = [-0.10047, -0.11216, -0.11328, -0.12195, -0.122963, -0.13392, -0.14119, -0.14713, -0.15704, -0.162996, -0.169068, -0.17553880792, -0.183777837, -0.185888819, -0.193963023, -0.205257721, -0.224253545, -0.229378995, -0.257622488, -0.275978856, -0.29577538, -0.304072648, -0.308566354, -0.316870809, -0.334725352]

#print(station_Two_Info)
#print(station_One_Info)
least_stations("Edgware Road", "Lambeth North")