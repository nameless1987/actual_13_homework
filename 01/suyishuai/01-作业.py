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


nums = raw_input("输入要打印三角形的行数(奇数行):")
int_nums = int(nums)
first_row = 2*int_nums-1 #第一行要打印的*数
curent_fuhao = first_row #每行行要打印的*数
kongge =0  #每行的空格数

print "第一行打印{0}".format(first_row)

for i in range(int_nums,0,-1):
    str=''
    for y in range(0,kongge):
        str=str +"A"
    for j in range(curent_fuhao,0,-1):
        if j==curent_fuhao or j==1:
            str = str + "*"
        else:
            str = str + "A"
    curent_fuhao = curent_fuhao - 2;
    kongge = kongge+1
    if i==int_nums:
        print str.replace("A","*"),
    else:
        print str.replace("A"," "),
    print ""

	
print ""
print ""

print ("乘法表")
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print "{0}*{1}={2}".format(j,i,i*j).rjust(8),
    print ""