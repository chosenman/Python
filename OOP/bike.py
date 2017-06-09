class Bike(object):
	"""docstring for Bike"""
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print "Bike's price: " + str(self.price) + " $"
		print "Maximum speed: " + str(self.max_speed) + " miles/hour"
		print "Total miles: " + str(self.miles) + " miles"
		return self
	def ride(self):
		print "Riding"
		self.miles +=10
		return self
	def reverse(self):
		print "Reversing"
		if (self.miles >= 5):
			self.miles -= 5
		return self


myBike = Bike(8000,200)
alexBike = Bike(9000,300)
cedricBike = Bike(10000,230)

myBike.ride().ride().ride().reverse().displayInfo()
alexBike.ride().ride().reverse().reverse().displayInfo()
cedricBike.reverse().reverse().reverse().displayInfo()




