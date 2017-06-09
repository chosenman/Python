class Car(object):
	"""docstring for Car"""
	def __init__(self, price, speed, fuel, mileage):
		if price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.display_all()
	def display_all(self):
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed) + "mph"
		print "Fuel: " + self.fuel
		print "Mileage: " + str(self.mileage) + " mpg"
		print "Tax: " + str(self.tax)
		return self

firstCar = Car(2000,35,"Full", 105)
firstCar = Car(2000,5,"Not Full", 105)
firstCar = Car(2000,15,"Kind of Full", 95)
firstCar = Car(2000,25,"Full", 25)
firstCar = Car(2000,45,"Empty", 25)
firstCar = Car(20000000,35,"Empty", 15)


