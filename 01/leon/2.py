#!/usr/bin/env python
slow_speed = 8 * 60 + 15
fast_speed = 7 * 60 + 12
begin_time = 0
q = 1

while  q == 1:
	s = 0
	f = 0
	if begin_time == 0:
		begin_time = raw_input("When you want start run?\n")
		begin_hour, begin_min, begin_second = begin_time.split(':')

	else:
		begin_hour = end_hour
		begin_min = end_min
		begin_second = begin_second
	choose = int(raw_input("if you want run slow,input 1:\nor you want run fast input 2:\n"))
	if choose == 1:
		s = int(raw_input("how long you speed low:\n "))
	elif choose == 2:
		f = int(raw_input("how long you speed fast:\n "))
	else:
		print "you should input a right chose"
		begin_time = 0
		continue
	total = f * fast_speed + s * slow_speed
	hour = total/3600
	total = total - hour*3600
	mi = total/60
	seceond = total % 60
	print "you run for {0}hour,{1}min,{2}seceond".format(hour,mi,seceond)
	end_hour = hour + int(begin_hour)
	end_min = mi + int(begin_min)
	end_second = seceond + int(begin_second)
	while end_second > 60 :
			end_min = end_min + 1
			end_second = end_second - 60	
	while end_min > 60 :
			end_hour = end_hour + 1
			end_min = end_min - 60
	print "when you go home the time is {0}:{1}:{2}" .format(end_hour,end_min,end_second)
	while q == 1:
		run = raw_input( "Do you want countiue run?:")
		if run == 'yes':
			break
		elif run == 'no':
			q = 0
		else:
			print "please input yes/no"


