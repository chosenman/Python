name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
uneven = ["foo", "bazz", "buzz", "puzle", "tuzle", "fuzl", "muzl", "Oplja"]

def make_dict(arr1, arr2):
  new_dict = {}
  # print 'function started...'
  if len(arr1) == len(arr2):
  	print 'both array lengths are equal'
  	for i in range(0,len(arr1)):
  		new_dict[ arr1[i] ] = arr2[i]
  		# print arr1[i]
  elif len(arr1) > len(arr2):
  	print 'arr1 > arr 2 ....'
  	for i in range(0,len(arr2)):
  		# arr1 is longer we use it as a keys
  		new_dict[ arr1[i] ] = arr2[i]
  else:
  	print 'arr2 > arr1 .....'
  	for i in range(0,len(arr1)):
  		# arr2 is longer we will use it for keys
  		new_dict[ arr2[i] ] = arr1[i]

  return new_dict


print make_dict(name,uneven)