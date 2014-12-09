from decimal import Decimal, getcontext
from readstation import read_stations
from readzone import read_zones

def fares(Starting_Point, Ending_Point):
	"""
	This function will find the fares for the trip and prompt the customer 
	to enter money for the first time
	"""
	Travelcard = str(input("Do you have a travel card, Yes or No?")) 
	print("Answers other than Yes are treated as No")
	s = read_stations(Starting_Point)
	e = read_stations(Ending_Point)
	Zone_id_starting = int(s[Starting_Point][3])
	Zone_id_ending = int(e[Ending_Point][3])
	print("Your Trip is from", Starting_Point, "to", Ending_Point)
	print("It is from zone", Zone_id_starting, "to zone", Zone_id_ending)
	zone_start = "Zone" + str(Zone_id_starting)
	zone_list = read_zones(zone_start)
	fees = float(zone_list[zone_start][Zone_id_ending-1])
	if Travelcard == "Yes":
		getcontext().prec = 3
		fees = Decimal(fees) * Decimal(0.7)
	print("The Fare is", fees)
	Amount_paid = float(input("Please enter coins or notes: "))
	print("you entered", Amount_paid, "pound")
	change(Amount_paid, fees)

	
def change(Money_inserted, Total_fees):
	"""
	This function check if the money entered at the first time is enough
	or not, if it is not, it will prompt the customer for more money untill
	it is enough to cover the fares. Then it will give changes according to 
	how much the customer paid and the fares are.
	"""
	Amount_paid_initial = Money_inserted
	if Money_inserted < Total_fees:
		getcontext().prec = 3
		fee_remain = Decimal(Total_fees) - Decimal(Money_inserted)
		print("You have not insert enough money, You need to insert", fee_remain, "pounds more")
		Money_inserted = Money_inserted + float(input("Amount not enough Please enter more : "))
		change(Money_inserted, Total_fees)
	Total_money_inserted = Money_inserted
	getcontext().prec = 3
	Changes = Decimal(Total_money_inserted) - Decimal(Total_fees)
	if Amount_paid_initial > Total_fees:
		print("You paid", Total_money_inserted, "in total and your changes is", Changes)


#fares("Acton Town", "Amersham")
