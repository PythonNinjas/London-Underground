"""
In this program we are simulating the game of patience, and to see how often the player wins and the different amount of times
the certain number of cards in a deck appears.
"""
from shuffle import shuffle
from histogram import histogram

def add_to_11(visible):
	"""
	Here we have taken in the stack of cards that are in play and see if any of
	them add to 11. and if there is, return there indexes
	"""

	for first in range(len(visible)):
		
		for moveable in range(len(visible)):
			
			if(visible[first] + visible[moveable]) == 11:
				return(first, moveable)
	return ()

def jqk(visible):
	"""
	We are looking at the stacks that are in play, and seeing if any of them are J (11) Q (12) or K(13), 
	and if they all are in the stacks then return there indexes
	"""

	J = False
	Jpos = 0
	Q = False
	Qpos = 0
	K = False
	Kpos = 0
	for item in range(len((visible))):
		if visible[item] == 11:
			J = True
			Jpos = item
		if visible[item] == 12:
			Q = True
			Qpos = item
		if visible[item] == 13:
			K = True
			Kpos = item
	if J and Q and K == True:
		return(Jpos,Qpos,Kpos)
	return ()

def play(deck, verbose):
	"""
	We will be simulating one game of patience, and making sure that if they win, or lose it is recorded with the amount of cards remaining.
	"""
	sDeck = shuffle(deck)
	win = False
	stacks = [sDeck.pop(0),sDeck.pop(1)]

	if verbose == True:
		for item in stacks:
			print(item, end=" ")
		print("\n")

	while len(stacks) < 10 and len(stacks) > 0 and win == False:
		adds_11 = add_to_11(stacks)
		jqk_indexs = jqk(stacks)

		if len(adds_11) != 0:
			
			if len(sDeck) > 1:

				stacks[adds_11[0]] = sDeck.pop(0)
				stacks[adds_11[1]] = sDeck.pop(0)
			else:
				win = True

		elif len(jqk_indexs) != 0:
			if len(sDeck) > 2:

				stacks[jqk_indexs[0]] = sDeck.pop(0)
				stacks[jqk_indexs[1]] = sDeck.pop(0)
				stacks[jqk_indexs[2]] = sDeck.pop(0)
			else:
				win = True
		else:

			stacks.append(sDeck.pop(0))

		if verbose == True:
			for item in stacks:
				print(item, end=" ")
			print("\n")

	if win == True:
		return 0
	else:
		return len(sDeck)

def many_plays(N):
	"""
	THis will find out the average amount of times a certain win / cards left in the deck appears in a certain amount of plays of the game.
	"""

	lDeck = [0]*53


	for item in range(N):
		deck = create_deck()
		left = play(deck, False)
		lDeck[left] = lDeck[left] + 1
	#Convetion to percentages
	for item in range(len(lDeck)):
		lDeck[item] = lDeck[item] / N * 100

	return lDeck


def create_deck():
	"""
	This fuction creates a fresh new deck with the card in numeric order.
	"""
	deck = []
	for item in range(1,14):
		deck.append(item)
		deck.append(item)
		deck.append(item)
		deck.append(item)
	return deck


#==============================================================================================
#Below commands are used to test the different functions i have used.


# visible = [3,10,12,8,11,12,13]
# print(add_to_11(visible))
# print(jqk(visible))
if __name__ == '__main__':
	outcome = many_plays(10000)
	histogram(list(range(53)),outcome, 4)
