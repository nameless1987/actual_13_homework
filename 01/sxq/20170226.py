#!/usr/bin/env python
#coding: utf-8

# 1: (4/3)*3.14*r**3

# r = int(raw_input('please input a num: '))
# r_total = (4/3.0 * 3.14) * r ** 3
#
# print "r=%s,r_total = %s" % (r,r_total)
# print "r=%s,r_total = %2d" % (r,r_total)
# print "r=%s,r_total = %.2f" % (r,r_total)
# print 'r={},r_total = {}'.format(r,r_total)

# 2:慢跑n圈用时8分钟15s，快跑m圈7分12s

# slow_count = int(raw_input('slow count : '))
# fast_count = int(raw_input('fast count : '))
#
# start_hour=6
# start_minute=52
# slow_time = (8*60+15) * slow_count
# fast_time = (7*60+12) * fast_count
# total_time = ( slow_time + fast_time )/60
#
# user_hour = total_time/60
# user_minute = total_time%60
# end_hour = start_hour + user_hour
# end_minute = user_minute + start_minute
#
# if end_minute >= 60:
#     end_minute = end_minute - 60
#     end_hour += 1
#     print '共使用%s min, start_time: 6:52, end_time: %s:%02d' % (total_time, end_hour, end_minute)
# else:
#     print '共使用%s min, start_time: 6:52, end_time: %s:%02d' % (total_time,end_hour,end_minute)

# #3: 两个数相加大于100，输出100，两个数相乘大于1000，输出 1000
#
# num_1 = int(raw_input('please input first num: '))
# num_2 = int(raw_input('please input second num: '))
#
# if num_1 + num_2 >=100 and num_1 * num_2 < 1000:
#     print 100
# elif num_1 * num_2 >=1000:
#     print 1000

# 4:慢跑n圈用时8分钟15s，快跑m圈7分12s

# 要求：
# 1.raw_input("还想不想接着跑")   y  n如果是y就是接着跑，如果是n就是不跑了
# 2. raw_input如果慢跑，输入1，如果快跑，输入2
# 3. raw_input 获取跑多长时间
# 4. 再接着问

# start_time = raw_input('Start time: ')
# while True:
#     input_str = raw_input('Whether continue ？(y/n): ')
#     if input_str == 'y':
#         run_type = int(raw_input('select slow:1 or fast:2: '))
#         run_time = int(raw_input('run time (min): '))
#         start_hour, start_minute = start_time.split(':')
#         if run_type == 1:
#
#             user_hour = run_time / 60
#             user_minute = run_time % 60
#             end_hour = int(start_hour) + user_hour
#             end_minute = int(start_minute) + user_minute
#             #
#             run_length=1.0/((8*60+15)) * run_time*60
#
#
#             if end_minute >= 60:
#                 end_minute = end_minute - 60
#                 end_hour += 1
#                 print '{0}公里共使用{1} min, end_time: {2}:{3} go home'.format(run_length,run_time, end_hour, end_minute)
#             else:
#                 print '{0} 公里共使用{1} min, end_time: {2}:{3} go home'.format(run_length,run_time, end_hour, end_minute)
#
#
#         elif run_type == 2:
#
#             user_hour = run_time / 60
#             user_minute = run_time % 60
#             end_hour = int(start_hour) + user_hour
#             end_minute = int(start_minute) + user_minute
#             run_length = (3.0 / (7 * 60 + 12)) * run_time*60
#
#             if end_minute >= 60:
#                 end_minute = end_minute - 60
#                 end_hour += 1
#                 print '{0}公里共使用{1} min, end_time: {2}:{3} go home'.format(run_length,run_time, end_hour, end_minute)
#             else:
#                 print '{0} 公里共使用{1} min, end_time: {2}:{3} go home'.format(run_length,run_time, end_hour, end_minute)
#
#     elif input_str == 'n':
#          print 'Go home.'
#          break

# 5、计算list最大值
# num_list=[98259,14686, 98259, 22884, 95795, 59961, 50760, 57134, 65016, 24004, 70019, 1608, 59894, 67975, 1677, 60617, 87739, 61754, 20229, 93120, 64838]
# f_max_num = None
# s_max_num = None
# for i in num_list:
#     if i > f_max_num:
#         f_max_num=i
#     if i <= f_max_num and i > s_max_num:
#         s_max_num=i
#
# print f_max_num,s_max_num

#6、所以字符串的重复次数
# str_list=['Python', 'JavaScript', 'JavaScript', 'HTML', 'PHP', 'Python', 'Go', 'Java', 'C++', 'C', 'HTML', 'CSS', 'Java', 'PHP', 'C++', 'C', 'Go', 'PHP', 'Go', 'Java', 'JavaScript', 'CSS', 'C++', 'Java', 'HTML', 'PHP', 'Java', 'C++', 'Java', 'PHP', 'Java', 'C', 'JavaScript', 'Python', 'HTML', 'C++', 'C', 'C', 'C++', 'JavaScript', 'HTML', 'Go', 'Java', 'CSS', 'Java', 'Java', 'HTML', 'Go', 'Go', 'HTML']
# str_dict={}
# for i in str_list:
#     if i not in str_dict:
#         str_dict[i] = 1
#     else:
#         str_dict[i] += 1
# print str_dict

#7、我现在有10000块钱，银行的利息为3.25%（利滚利），我要存够多少年，我的钱能翻倍？

# old_num=10000
# year=1
# new_num = old_num * (1 + 0.0325 )
# while new_num <= 20000:
#     new_num *= 1.0325
#     year +=1
#
# print year

# 8、99乘法表
# *可选作业
# 等腰三角形
# 等腰空心三角
# 等腰空心三角形套空心三角形

