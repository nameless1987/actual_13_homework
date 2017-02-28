#!/usr/bin/env python
high = int(raw_input("How hgih you want?"))
tip = '#'
space = ' '
for i in range(0,high):
	if i == 0:
		print high * space, tip
	elif i == high-1 :
		print space,tip * (high * 2 - 1)
	elif i == 1:
		print (high - i)* space,tip,tip
	else:
		print (high - i)* space,tip,space  * (2 * (i - 1) - 1),tip
	pass
