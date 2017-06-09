# x = [4, 6, 1, 3, 5, 7, 25]
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(list):

	for x in list:
		if type(x) == str:
			for star in range(len(x)):
				print x[0].lower(),
			print ""
		else: 
			for star in range(x):
				print "*",
			print ""


draw_stars(x)
