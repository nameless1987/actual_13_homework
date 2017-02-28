# -*- coding: utf-8 -*-
# @Author: gaoss
# @Date:   2017-02-27 14:11:33
# @Last Modified by:   gaoss
# @Last Modified time: 2017-02-27 14:33:05
extent=int(raw_input('请输入高度:  '))
i=1
symbol1=' '
symbol2='*'
while i < extent:
	print (symbol1*(extent-i-1)), 
	if i == 1:
		print symbol2 + symbol1*(i-1)
	else:
		print symbol2 + symbol1*(i-1)+symbol1*(i-2)+symbol2

	i+=1
	if i == extent:
		print symbol2*i+symbol2*(i-1)