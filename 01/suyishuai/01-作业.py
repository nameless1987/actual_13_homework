#/usr/bin/env python
#encoding=utf-8

nums = raw_input("输入要打印三角形的行数:")
int_nums =int(nums)
for i in range(0, int_nums):
    for j in range(10, -1,-1):
         if j>i:
             print "",
         else:
             print "*",
    print ""

print ""
print ""

print ("乘法表")
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print "{0}*{1}={2}".format(j,i,i*j).rjust(8),
    print ""