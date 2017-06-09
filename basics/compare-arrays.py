list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

def comPare(arr1,arr2):
	if len(arr1) != len(arr2):
		print "The lists are not the same."
		return

	for index in (0, len(arr1)-1):
		if arr1[index] == arr2[index]:
			continue
		else:
			print "The lists are not the same."
			return

	print "The lists are the same"
	return

comPare(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
comPare(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
comPare(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
comPare(list_one, list_two)


