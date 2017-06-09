import random

# print random.randrange(60,101) -
# random.random()

def howManyToss(num):
	print "Starting the program..."
	head = 0 # 1 head
	tail = 0 # 0 tail
	for i in range(num):
		if round(random.random()) == 1:
			head = head +1
			print "Attempt #1: Throwing a coin... It's a head! ... Got "+ str(head) + " head(s) so far and " + str(tail) +" tail(s) so far"
		else:
			tail = tail+1
			print "Attempt #1: Throwing a coin... It's a tail! ... Got "+ str(head) + " head(s) so far and " + str(tail) +" tail(s) so far"
	print "Ending the program, thank you!"


howManyToss(5000)