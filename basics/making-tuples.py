my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def makeTuples(dict):
	return my_dict.items()

print makeTuples(my_dict)

def makeTuplesV2(dict):
	arrOutput = []
	for key,value in dict.iteritems():
		arrOutput += [(key,value)]

	return arrOutput

print makeTuplesV2(my_dict)
