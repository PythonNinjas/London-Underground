def changes(Dictionary, Starting_Point, Ending_Point, Amount_Paid):
	Zone_id_starting = Dictionary[Starting_Point]
	Zone_id_ending = Dictionary[Ending_Point]
	print("Your Trip is from", Starting_Point, "to", Ending_Point)
	fees = list_zone[Zone_id_starting - 1][Zone_id_ending - 1]
	print("The Fare is", fees)
	Changes = Amount_Paid - fees
	print("You paid", Amount_Paid, "and your changes is", Changes)
	

Victoria_Line = {"Brixton": 2, "Stockwell": 2, "Vauxhall": 1, "Pimlico": 1, "Victoria": 1, "Green Park": 1, "Oxford Circus": 1, "Warren Street": 1, "Euston": 1, "King's Cross": 1, "Highbury & Islington": 2, "Finsbury Park": 2, "Seven Sisters": 3, "Totteham Hale": 3, "Blackhorse Road": 3, "Walthamstow": 3}
zone1 = [1.2, 1.8, 2, 2.4, 2.8, 3.2, 3.5, 4, 4.8]
zone2 = [1.8, 1.2, 1.8, 2, 2.4, 2.8, 3.2, 3.5, 4]
zone3 = [2, 1.8, 1.2, 1.8, 2, 2.4, 2.8, 3.2, 3.5]
zone4 = [2.4, 2, 1.8, 1.2, 1.8, 2, 2.4, 2.8, 3.2]
zone5 = [2.8, 2.4, 2, 1.8, 1.2, 1.8, 2, 2.4, 2.8]
zone6 = [3.2, 2.8, 2.4, 2, 1.8, 1.2, 1.8, 2, 2.4]
zone7 = [3.5, 3.2, 2.8, 2.4, 2, 1.8, 1.2, 1.8, 2]
zone8 = [4, 3.5, 3.2, 2.8, 2.4, 2, 1.8, 1.2, 1.8]
zone9 = [4.8, 4, 3.5, 3.2, 2.8, 2.4, 2, 1.8, 1.2]
list_zone = [zone1, zone2, zone3, zone4, zone5, zone6, zone7, zone8, zone9]
Test = changes(Victoria_Line, "Seven Sisters", "Brixton", 5)
