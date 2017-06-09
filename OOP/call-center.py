class Call(object):
	"""docstring for CallClass"""
	def __init__(self, id, name, phone_num, time, reason):
		self.id = id
		self.name = name
		self.phone_num = phone_num
		self.time = time
		self.reason = reason
	def display(self):
		print str(self.id), self.name, str(self.phone_num), str(self.phone_num), self.reason
		
class CallCenter(object):
	def __init__(self, calls=[]):
		self.calls = calls
		self.quee_size = len(calls)
	def add(self, *call):
		for index in call:
			if type(index) == Call:
				self.calls += [index] 
			else:	
				addList = []
				for val in call:
					addList.append(val)
					# print val
				# print addList
				self.calls += [Call(addList[0], addList[1], addList[2], addList[3], addList[4])]
				break
		return self
	def remove(self):
		self.calls.pop(0)
		return self
		# del self.calls[0]
	def info(self):
		for index in self.calls:
			index.display()
		


firstCall = Call(1,"Many", "443-2234","2pm","about work")
secondCall = Call(999,"Murka", "55-2234","6pm","private")
# firstCall.display()

center = CallCenter()
center.add(firstCall)
center.add(secondCall)

print type(firstCall) == Call
center.add(999,"Vitjok", "66-2234","9am","friend")
center.info()


