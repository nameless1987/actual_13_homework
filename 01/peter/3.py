#!/usr/bin/env python
slow_speed = 8 * 60 + 15
fast_speed = 7 * 60 + 12
begin_time = '6:52'
s = int(raw_input("how longe you speed low: "))
f = int(raw_input("how longe you speed fast: "))
total = f * fast_speed + s * slow_speed
hour = total/3600
total = total - hour*3600
mi = total/60
seceond = total % 60
print "you run for {0}hour,{1}min,{2}seceond".format(hour,mi,seceond)
end_hour = hour + 6
end_min = mi + 52
end_second = seceond
while end_min > 60 :
		end_hour = end_hour + 1
		end_min = end_min - 60
print "when you go home the time is {0}:{1}:{2}" .format(end_hour,end_min,end_second)
