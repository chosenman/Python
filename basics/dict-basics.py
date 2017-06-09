myInfo = {
	"name": "Yarik",
	"age": 31,
	"country": "Ukraine",
	"language": "Python"
}

def showInfo(arg):
	print "My name is " + arg['name']
	print "My age is " + str(arg['age'])
	print "My country of birth is The " + arg['country']
	print "My favorite language is  " + arg['language']

showInfo(myInfo)