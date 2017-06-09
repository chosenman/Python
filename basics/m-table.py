# print "x",
print "  x",
for x in range(1, 13):
 # print x,
 print "{:>4}".format(x),
print ''

for x in range(1, 13):
 # print x,
 print '{:>3}'.format(x),
 for y in range(1, 13):
  print "{:>4}".format(x*y),
  # print x*y,
 print ''