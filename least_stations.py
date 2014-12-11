from read_stations import *
from read_lines import *
#--------------------------------------------------------------------------------
#-         This Area with see if the stations are on the same line              -
#--------------------------------------------------------------------------------
def same_line(start,end):
	"""
	This is a check to see if the 2 stations are on the same line
	"""
	start_Station_Dic = read_stations(start)
	end_Station_Dic = read_stations(end)
	route_Line = read_lines()
	overall_route = {}

	for line in start_Station_Dic[start][2]:
		#print(line)
		current_Line = route_Line[line]

		if line in end_Station_Dic[end][2]:

			for fork in route_Line[line]:
				if start in fork and end in fork:

					#Using the line db, we check to check the indexs of the start and end station, and go through the inbetween stations to find the name of them
			
					start_Index = fork.index(start)
					end_Index = fork.index(end)
					station_Stops = end_Index - start_Index

					#We add alls the stops in the list and return this to a dic to give the different option.
					if station_Stops > 0:
						route = fork[start_Index:end_Index]
						route.append(fork[end_Index])
					else:
						route = fork[start_Index:end_Index:-1]
						route.append(fork[end_Index])
					station_Stops = abs(station_Stops)
					
					return True, station_Stops, route
	return False, False, False
					
#--------------------------------------------------------------------------------
#-    [END]This Area with see if the stations are on the same line[END]         -
#--------------------------------------------------------------------------------
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
	#We first check if they are on the same line
	check, station_Stops, route = same_line(start,end)
	if check == True:
		various_Routes[station_Stops] = route


	for line in start_Station_Dic[start][2]:
		route = []
		route_Line = read_lines()
		route_Line = route_Line[line]

		for fork in route_Line:
			#This will go through the fork on that line and see if the starting station is there
		
			#print(start, fork)

			if start in fork:
				start_line_index = fork.index(start)
				index_Position = start_line_index

				#We will then go though all the stations below the start station and sees a route through that way
				while index_Position >= 0:

					current_Station = fork[index_Position]
					this_station_dic = read_stations(fork[index_Position])
					#This gets the lines for the next station
					this_station_lines = this_station_dic[current_Station][2]


					#used the same line fuction to see if its on the same line
					same_line_check, station_Stops, route  = same_line(current_Station, end)
					#print(same_line_check)
					#Check to see if on same line, and then added it to the dictionary of viable routes to take
					if same_line_check == True:
						amount_stops = index_Position - start_line_index
						#Find stations inbetween the indexes
						if amount_stops > 0:
							first_route = fork[start_line_index:index_Position]
							first_route.append(fork[index_Position])
						else:
							first_route = fork[start_line_index:index_Position:-1]
							first_route.append(fork[index_Position])					
					 
						amount_stops = abs(amount_stops)
						#print(amount_stops, station_Stops)
						overall_stops = amount_stops + station_Stops
						various_Routes[overall_stops] = first_route + route


					#this is to make sure you only check the station that are in the line
					if index_Position == 0:
						index_Position = int(-1)
					else:
						index_Position = index_Position - 1
				

				#print("-------------------------------------------------------------------------------------------------")
				#Doing the sam here but in the other way of the list
				index_Position = start_line_index
				while index_Position <= (len(fork) - 1):

					current_Station = fork[index_Position]
					this_station_dic = read_stations(fork[index_Position])
					#This gets the lines for the next station
					this_station_lines = this_station_dic[current_Station][2]


					#print("This is the current station being looked at : ", current_Station)
					current_Station = fork[index_Position]

					same_line_check, station_Stops, route  = same_line(current_Station, end)
					#print(same_line_check)
					#Check to see if on same line, and then added it to the dictionary of viable routes to take
					if same_line_check == True:
						amount_stops = index_Position - start_line_index
						#Find stations inbetween the indexes
						if amount_stops > 0:
							first_route = fork[start_line_index:index_Position]
							first_route.append(fork[index_Position])
						else:
							first_route = fork[start_line_index:index_Position:-1]
							first_route.append(fork[index_Position])
						#to make it postive make the dic better looking 
						amount_stops = abs(amount_stops)
						#print(amount_stops, station_Stops)
						overall_stops = amount_stops + station_Stops
						various_Routes[overall_stops] = first_route + route

					index_Position += 1
				if various_Routes == "":
					best_route = min(various_Routes, key=various_Routes.get)
					best_route = various_Routes[best_route]
					return True, best_route
				else:
					break


		return False, ("There are no routes that can be calculated, please try again later")








#===============================================================================================================================================================
#This is a testing area for this function
#===============================================================================================================================================================
if __name__ == '__main__':
#These variables below are going to be the teseting database values
#Line_db = {"Bakerloo": ['Elephant & Castle', 'Lambeth North', 'Waterloo', 'Embankment', 'Charing Cross', 'Piccadilly Circus', 'Oxford Circus', "Regent's Park", 'Baker Street', 'Marylebone', 'Edgware Road', 'Paddington', 'Warwick Avenue', 'Maida Vale', 'Kilburn Park', "Queen's Park", 'Kensal Green', 'Willesden Junction', 'Harlesden', 'Stonebridge Park', 'Wembley Central', 'North Wembley', 'South Kenton', 'Kenton', 'Harrow & Wealdstone']}
#station_One_Info = {'Waterloo': (51.50322, -0.11328, ['Bakerloo', 'Waterloo & City'], 1) }
#station_Two_Info = {'Charing Cross': (51.507108, -0.122963, ['Bakerloo', 'Northern' ], 1) }

#Latitudes_Bakerloo = [51.49467, 51.49894, 51.50322, 51.50717, 51.507108, 51.51022, 51.51517, 51.52344, 51.52265, 51.52266, 51.51956, 51.5151846554, 51.52329728, 51.52989409, 51.53495818, 51.534179, 51.53060655, 51.53032031, 51.53628278, 51.54402388, 51.55122817, 51.56258091, 51.57044666, 51.58173809, 51.59205973]
#Longtitudes_Bakerloo = [-0.10047, -0.11216, -0.11328, -0.12195, -0.122963, -0.13392, -0.14119, -0.14713, -0.15704, -0.162996, -0.169068, -0.17553880792, -0.183777837, -0.185888819, -0.193963023, -0.205257721, -0.224253545, -0.229378995, -0.257622488, -0.275978856, -0.29577538, -0.304072648, -0.308566354, -0.316870809, -0.334725352]

#print(station_Two_Info)
#print(station_One_Info)
	print(least_stations("Watford", "Waterloo"))
	#print(same_line("Baker Street", "Elephant & Castle"))