#!/usr/bin/env python
# coding:utf-8
from_home_time_h = 6
from_home_time_m = 52
from_home_time_s = 0
jogging_speed=8*60+15
run_fast_speed=7*60+12
time=jogging_speed*2+run_fast_speed*5+jogging_speed*3
s=str(time%60+from_home_time_s)
h=str(from_home_time_h+(time/60+52)/60)
m=str((time/60+from_home_time_m)%60)
go_home=h+':'+m+':'+s
print "第一次慢跑耗时:{}秒 快跑耗时:{}秒 第二次慢跑耗时:{}秒 到家时间:{}".format(jogging_speed*2,run_fast_speed*5,jogging_speed*3,go_home)
