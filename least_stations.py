def least_stations(start, end):
	"""
	Find the route with the least number of stations.
	"""
	#================================================================================
	#Here we need to get the information for the other functions files in this area
	#and save the information to variables
	start_Station_Dic = station_One_Info[start]
	end_Station_Dic = station_Two_Info[end]
	print(start_Station_Dic[2])
	print(end_Station_Dic[2])
	#================================================================================
	#First check to see if they are on the same line
	for line in start_Station_Dic[2]:
		if line in end_Station_Dic[2]:
			route_Line = Line[line]
			start_Index = route_Line.index(start)
			end_Index = route_Line.index(end)
			station_Stops = end_Index = start_Index
			print(station_Stops)






#===============================================================================================================================================================
#This is a testing area for this function
#===============================================================================================================================================================
#These variables below are going to be the teseting database values
Line = {"Bakerloo": ['Elephant & Castle', 'Lambeth North', 'Waterloo', 'Embankment', 'Charing Cross', 'Piccadilly Circus', 'Oxford Circus', "Regent's Park", 'Baker Street', 'Marylebone', 'Edgware Road', 'Paddington', 'Warwick Avenue', 'Maida Vale', 'Kilburn Park', "Queen's Park", 'Kensal Green', 'Willesden Junction', 'Harlesden', 'Stonebridge Park', 'Wembley Central', 'North Wembley', 'South Kenton', 'Kenton', 'Harrow & Wealdstone']}
station_One_Info = {'Waterloo': (51.50322, -0.11328, ['Bakerloo', 'Waterloo & City'], 1) }
station_Two_Info = {'Charing Cross': (51.507108, -0.122963, ['Bakerloo', 'Northern' ], 1) }

Latitudes_Bakerloo = [51.49467, 51.49894, 51.50322, 51.50717, 51.507108, 51.51022, 51.51517, 51.52344, 51.52265, 51.52266, 51.51956, 51.5151846554, 51.52329728, 51.52989409, 51.53495818, 51.534179, 51.53060655, 51.53032031, 51.53628278, 51.54402388, 51.55122817, 51.56258091, 51.57044666, 51.58173809, 51.59205973]
Longtitudes_Bakerloo = [-0.10047, -0.11216, -0.11328, -0.12195, -0.122963, -0.13392, -0.14119, -0.14713, -0.15704, -0.162996, -0.169068, -0.17553880792, -0.183777837, -0.185888819, -0.193963023, -0.205257721, -0.224253545, -0.229378995, -0.257622488, -0.275978856, -0.29577538, -0.304072648, -0.308566354, -0.316870809, -0.334725352]

#print(station_Two_Info)
#print(station_One_Info)
least_stations("Waterloo", "Charing Cross")