class MathDojo(object):
	def __init__(self):
		self.res = 0
	def add(self, *arg):
		for index in arg:
			if type(index) == int:
				self.res += index
			elif type(index) == float:
				self.res += index
			elif type(index) == list:
				for elem in index:
					self.res += elem
			elif type(index) == tuple:
				for val in index:
					self.add(val)
		return self
	def subtract(self, *arg):
		for index in arg:
			if type(index) == int:
				self.res -= index
			elif type(index) == float:
				self.res -= index
			elif type(index) == list:
				for elem in index:
					self.res -= elem
			elif type(index) == tuple:
				for val in index:
					self.subtract(val)
		return self
	def result(self):
		print self.res

MathDojo().add(2).add(2, 5).subtract(3, 2).result()
MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
MathDojo().add((2,3),3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, (2,3), [1.1, 2.3]).result()

# print MathDojo().add(2).add(2, 5).subtract(3, 2).result