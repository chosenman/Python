class Animal(object):
	"""parent class for all animals"""
	def __init__(self, name, health=100):
		self.health = health
		self.name = name

	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def display(self):
		print str(self.health)
		return self

		
class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name,150)
	def pet(self):
		self.health += 5
		return self

# Optional example of modification of parental method
	def speak(self):
		print "Woof im {}".format(self.health)
	def display(self):
		super(Dog, self).display()
		self.speak()
# ----------------------------------

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name,health=170)
	def fly(self):
		self.health -= 10
	def display(self):
		super(Dragon, self).display()
		print "I am a Dragon"


		
animal = Animal("horlum")
animal.walk().walk().walk().run().run().display()


chappi = Dog("Bob")
chappi.walk().walk().walk().run().run().display()

rafael = Dragon("Rafael")
rafael.display()



