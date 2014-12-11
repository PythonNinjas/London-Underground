from change import *
from draw_map import *
from read_stations import *

def main():
	"""
	This function is written by Sai...
	The main function brings all of the other function together.
	"""
	print("============================================================================================")
	print("=  Welcome to the London Underground System, please follow the instuctions on the screen   =")
	print("============================================================================================")
	
	
	double_check = False
	#This need some validation to make sure no bad input is done
	while double_check == False:
		check = False
		start = ""
		end = ""

		while check == False:

			start = str(input("Please enter your starting station :"))

			check, Dic = read_stations(start)

			if check == False:
				print("Sorry the station that you want to start from does not exist.")
	
		check = False

		while check == False:
			end = str(input("Please enter the ending station :")) 

			check, Dic = read_stations(end)
			if check == False:
				print("Sorry the station that you want to go to does not exist.")
		print(start, end)
		if start != end:
			break
		else:
			print("You have entered the same station names, please choose different stations... ")



			


	#print("Please make sure your spelling is correct, and you are including Capital Letters...")
			

	print("____________________________________________________________________________________________")
	print("")
	print("                Please wait while we calculate the how much this would cost...")
	print("")
	
	print("")
	try:
		fares(start,end)
	except:
		print("Sorry we have hit a speed bump on the change machine, please try that again later.")
	print("")
	print("____________________________________________________________________________________________")
	print("")
	print("   Please wait while we now draw you the map of the London UnderGround with your route...")
	print("")

	try:
		draw_map(start,end)
	except:
		print("")
		print("Sorry we have hit a speed bump on the map drawing, please try that again later.")
		print("")
		print("____________________________________________________________________________________________")
		print("")








#===============================================================================================================================================================
#This is a testing area for this function
#===============================================================================================================================================================
if __name__ == '__main__':
	main()
