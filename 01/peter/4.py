#!/usr/bin/env python
# coding: utf-8
start_hour = 6
start_min = 52
start_second = 0

slow_speed = 8 * 60 + 15
fast_speed = 7 * 60 + 12

slow_gongli = int(raw_input("how longe you speed slow: "))
fast_gongli = int(raw_input("how longe you speed fast: ")) 

totle_time = slow_gongli * slow_speed + fast_gongli * fast_speed

used_second = totle_time
used_min = used_second / 60
used_second = used_second % 60

used_hour = used_min / 60
used_min %= 60

end_hour = start_hour + used_hour
end_min = start_min + used_min
end_second = start_second + used_second

end_min = end_min + end_second / 60
end_second = end_second % 60
end_hour = end_hour + end_min / 60
end_min %= 60

print "开始时间为：{0}:{1}:{2}".format(start_hour, start_min, start_second)
print "结束时间为：{0}:{1}:{2}".format(end_hour, end_min, end_second)
