import modArithmetic

class Product(object):
	"""docstring for Product"""
	def __init__(self, price, itemName, weight, brand, cost, status='for sale'):
	
		self.price = price
		self.itemName = itemName
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status
	def sell(self):
		self.status = "sold"
		return self
	def add_tax(self, tax):
		print "Tax was applied " + str(self.price * (1+tax))
		return self
	def Return(self, reason):
		if reason == 'defective':
			self.status = reason
			self.price = 0
		if reason == 'like new':
			self.status = 'for sale'
		if reason == 'opened':
			self.status = 'used'
			self.price = self.price * 0.8
		return self
	def display(self):
		print "Item name: " + self.itemName,
		print " Weight: " + str(self.weight),
		print " Brand: " + self.brand,
		print " Cost: " + str(self.cost),
		print " Status: " + self.status
	
		

myProduct = Product(20,"mouse",0.15,"Genius",8)

myProduct.add_tax(0.1).sell().Return('defective').display()

print modArithmetic.add(5, 8)