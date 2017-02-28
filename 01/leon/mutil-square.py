#!/usr/bin/env python
high = int(raw_input("How hgih you want?"))
tip = '#'
tip_new = '*'
space = ' '
single = 1
k = 3

high_new = high
while single:
	pass
	if high < 3:
		high = int(raw_input("Please in put a bigger than 2 numbers :"))
		high_new = high
	else:
		for i in range(0,high):
			if i == 0:
				print (high ) * space, tip
			elif high_new - 2 >= -1 and i <= high/2 - 1  :
				print (high - i)* space,tip + tip_new * (high - high_new) + tip_new + tip
				high_new = high_new - 2
			elif i == high - 1 :
				print space,tip + tip_new + tip_new * (high * 2 - 5) + tip_new + tip
				single = 0
			else:
				if high_new  == 3 or high_new == 2:
					print (high - i)* space,tip + tip_new * (i - 1)+ space + tip_new * (i - 1)+tip
					high_new = 0
				else :
					print (high - i)* space,tip + tip_new * (high/2  - 1 )+ space * k + tip_new *(high/2 - 1  )+tip
					k +=2
