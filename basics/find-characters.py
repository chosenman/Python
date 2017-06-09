# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
# new_list = ['hello','world']

def findChar(list, c):
	output = []
	for index in list:
		if index.find(c) != -1:
			output += [index]
	print output

	return


findChar(word_list, char)


