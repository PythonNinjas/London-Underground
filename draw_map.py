from exturtle import *
line = ['Elephant & Castle', 'Lambeth North', 'Waterloo', 'Embankment', 'Charing Cross', 'Piccadilly Circus', 'Oxford Circus', "Regent's Park", 'Baker Street', 'Marylebone', 'Edgware Road', 'Paddington', 'Warwick Avenue', 'Maida Vale', 'Kilburn Park', "Queen's Park", 'Kensal Green', 'Willesden Junction', 'Harlesden', 'Stonebridge Park', 'Wembley Central', 'North Wembley', 'South Kenton', 'Kenton', 'Harrow & Wealdstone']
Latitudes = [51.49467, 51.49894, 51.50322, 51.50717]
Longtitudes = [-0.10047, -0.11216, -0.11328, -0.12195]

def draw_map(turtle, Longtitudes, Latitudes):
	"""
	Draw the whole underground map and then highlight the best route.
	"""
	screensize(1000, 1000)
	hideturtle(turtle)
	for Longtitude, Latitude in zip(Longtitudes, Latitudes):
		turtle.penup()
		turtle.goto(Longtitude, Latitude)
		turtle.pendown()
		turtle.dot(10, "black")

bob = Turtle()
Map = draw_map(bob, Longtitudes, Latitudes)
mainloop()