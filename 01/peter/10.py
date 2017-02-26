#!/usr/bin/env python
# coding: utf-8
start_time = raw_input("几点开始跑：")
s_hour, s_min, s_second = start_time.split(":")

totle_time = 0
running = "yes"
count = 1

while True:
    if count != 1:
        running = raw_input("想不想接着跑：(yes/no)")
    if running == "y" or running == "yes":
        run_type = raw_input("慢跑还是快跑, 慢跑输入1，快跑输入2：")
        if run_type == "1":
            num = int(raw_input("跑几公里："))
            totle_time += num * (8 * 60 + 15)
        elif run_type == "2":
            num = int(raw_input("跑几公里："))
            totle_time += num * (7 * 60 + 12)
        else:
            print "输错了，重来"
            continue
    elif running == "n" or running == "no":
        print "不跑了"
        break
    else:
        print "please input 'y' or 'n'"
        continue
    count += 1

used_second = totle_time
used_min = used_second / 60
used_second = used_second % 60

used_hour = used_min / 60
used_min = used_min % 60

end_hour = int(s_hour) + used_hour
end_min = int(s_min) + used_min
end_second = int(s_second) + used_second

end_min = end_min + end_second / 60
end_second = end_second % 60
end_hour = end_hour + end_min / 60
end_min = end_min % 60


print "开始时间为：{0}:{1}:{2}".format(s_hour, s_min, s_second)
print "结束时间为：{0}:{1}:{2}".format(end_hour, end_min, end_second)
