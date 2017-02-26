#/usr/bin/env python
#encoding=utf-8

count =0
begin_time_str = raw_input("输入几点开始跑: ")


while True:
    if count>=1:
        is_run = raw_input("还继续跑吗，输入1，跑，输入2 停")
        if is_run =='2':
            break

    print "开始时间 {}".format(begin_time_str)
    begin_hour,begin_mi,begin_ss =begin_time_str.split(":")

    slow_speed=8*60+15  #单位 秒
    run_fast_speed=7*60+12
    speed = 0

    leixing = raw_input("如果慢跑，输入1，如果快跑，输入2")
    if leixing=="1":
        speed = run_fast_speed
    else:
        speed = slow_speed

    use_gongli =  raw_input("输入跑了几英里")
    print "速度是{}秒/英里 ".format(speed)

    totle_time =  int(speed) * int(use_gongli)
    use_hour =  totle_time/3600 #小时
    use_mi,use_ss= divmod((totle_time - use_hour*3600),60)  #分钟
    print "一共用了{0}秒   合计 = {3}:{1}:{2}".format(totle_time,use_mi,use_ss,use_hour)

    end_ss  = use_ss + int(begin_ss)
    end_mi = use_mi +int(begin_mi)
    end_hour = int(begin_hour) + use_hour


    if end_ss >60:
        end_ss = end_ss -60
        end_mi =end_mi +1

    if end_mi >60:
        end_mi =end_mi-60
        end_hour = end_hour +1

    print "结束时间 {}:{}:{}".format(end_hour,end_mi,end_ss)
    begin_time_str = "{0}:{1}:{2}".format(end_hour,end_mi,end_ss)
    count =count+1
