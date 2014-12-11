from change import *
from draw_map import *


def main():
	print("============================================================================================")
	print("=  Welcome to the London Underground System, please follow the instuctions on the screen   =")
	print("============================================================================================")
	
	#This need some validation to make sure no bad input is done
	start = str(input("Please enter your starting station :")) 
	end = str(input("Please enter the ending station :")) 

	
	
	print("                Please wait while we calculate the how much this would cost...")
	print("")
	print("____________________________________________________________________________________________")
	print("")
	try:
		fares(start,end)
	except:
		print("Sorry we have hit a speed bump on the change machine, please try that again later.")
	print("")
	print("____________________________________________________________________________________________")
	print("")
	print("   Please wait while we now draw you the map of the London UnderGround with your route...")

	draw_map(start, end)







#===============================================================================================================================================================
#This is a testing area for this function
#===============================================================================================================================================================
if __name__ == '__main__':
	main()
