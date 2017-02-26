#!/usr/bin/env python
# coding: utf-8
banjing = int(float(raw_input("Please input a name: ")))
tiji = 4/3.0*3.14*banjing**3
print "半径为"+str(banjing)+"的球的体积是："+str(tiji)
print "半径为{0}的面积为{1}, banjing: {0}".format(banjing, tiji)
print "半径为%s的面积为%s, banjing: %s" % (banjing, tiji, banjing)
