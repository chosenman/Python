# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"

print words.find('day')

newStr = words.replace('day','month')

print newStr

# Min and Max
x = [2,54,-2,7,12,98]
print "min: " , min(x) , "max: " , max(x)

# First and Last
y = ["hello",2,54,-2,7,12,98,"world"]
print 'First el. of list: ' + y[0]
print 'last el. of list: ' +y[len(y)-1]

# New List
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
# [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
# [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
count = 0
newZ = []
resultZ = []
while count < (len(z)-1)/2:
	newZ += [z[count]]
	count+=1
else: 
	print newZ
	resultZ.append(newZ)
	lastEl = len(z)-1
	for index in range(0,len(z)):
		if index >= (len(z)-1)/2:
			resultZ += [z[index]]

print resultZ

