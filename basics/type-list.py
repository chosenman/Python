a = ['magical unicorns',19,'hello',98.98,'world'] 
b = [2,3,1,7,4,12]
c = ['magical','unicorns']

def typeList(l):

	numsum = 0 
	string = ''

	for index in range(0,len(l)):     
		if type(l[index]) == str:         
			string = string + ' ' + l[index] 

		elif type(l[index]) == int:         
			numsum += l[index]     
		elif type(l[index]) == float:         
			numsum += l[index] 


	if numsum != 0 and len(string) != 0:
		message = "The array you entered is of mixed type"
		print message 
		print "String: ", string 
		print "Sum: ", numsum 
		print "----"
	elif numsum == 0:
		message = "The array you entered is of string type"
		print message 
		print "String: ", string 
		print "----"
	else:
		message = "The array you entered is of integer type"
		print message 
		print "Sum: ", numsum 
		print "----"


	return


typeList(a)
typeList(b)
typeList(c)
