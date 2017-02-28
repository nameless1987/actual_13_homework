list1 = list(range(1,10))
list2 = list(range(1,10))

for i in list1:
	for s in list2:
		a = i*s
		print "{0}*{1}={2}".format(i, s, a),
	print "\n"
