students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def fullNames(arr):
	for i in arr:
		for key,data in i.iteritems():
			print data,
		print ' '

fullNames(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def superDuperParser(arg):
	for oneL in arg:
		print oneL
		# print len(arg[oneL])
		for secondL in range(len(arg[oneL])):
			print secondL+1,
			print "-",

			for key,data in arg[oneL][secondL].iteritems():
				print data.upper(),
			print "-",

			namelen = 0
			for key,data in arg[oneL][secondL].iteritems():
				namelen += len(data)
			print namelen

			# print arg[oneL][secondL]

superDuperParser(users)



