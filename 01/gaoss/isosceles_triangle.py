# -*- coding: utf-8 -*-
# @Author: gaoss
# @Date:   2017-02-27 14:11:33
# @Last Modified by:   gaoss
# @Last Modified time: 2017-02-27 14:33:05
extent=int(raw_input('请输入高度:  '))
i=0
while i <= extent:
	print (' '*(extent-i)),
	print '*'*i+'*'*(i-1)
	i+=1
