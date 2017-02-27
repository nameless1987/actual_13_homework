# -*- coding: utf-8 -*-
# @Author: gaoss
# @Date:   2017-2-27 
# @Last Modified by:   gaoss
# @Last Modified time: 2017-2-27 14:10:29

for i in range(1,9):
	for j in range(1,9):
		# print '%s * %s = %s '%(j,i,i*j),
		print "{} * {} = {}".format(j,i,i*j),
		if i == j :
			print 
			break
