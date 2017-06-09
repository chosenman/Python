# Odd/Even

def odd_even(start,finish):
	for start in range(start,finish):
		if start % 2 == 0:
			print "Number is ",
			print start,
			print " This is an even number"
		else:
			print "Number is ",
			print start,
			print " This is an odd number"

odd_even(1,5) # 2000 is too big output

# Multiply

a = [2, 4, 10, 16]
def multiply(arr,num):
	for index in range(len(arr)):
		arr[index] *= num
	return arr

b = multiply(a,5)
print b

# Hacker Challenge
arr = [2,4,5]
# multiply(arr,3)
# [6, 12, 15]

def layered_multiples(arg):
  new_array = []

  for index in arg:
  	# print index
  	midTempArr = []
  	while index>0:

  		midTempArr +=[1]
  		index = index-1
  	new_array += [midTempArr]
  print new_array
  	

layered_multiples(multiply(arr,3))
  # return new_array
 


