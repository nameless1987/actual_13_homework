#!/usr/bin/env python
# coding: utf-8
# author: Liu Yue
# e-mail: liuyue@qding.me
# Pw @ 2016-06-21 17:07:56

import sys

high = raw_input("Please input a number of the triangle' high: ")

try:
    high = int(high)
except ValueError:
    print "Please input a number."
    sys.exit(1)


def print_chars(n, m, x, y='\n'):
    if i == m:
        sys.stdout.write(x[0][1]+y)
    elif i == n:
        sys.stdout.write(x[0][0]*(i-m)+x[0][1]+x[0][2]*(i-m)+y)
    elif m < i < n:
        sys.stdout.write(x[0][0])
        print_chars(n-1, m+1, list(reversed(x)), '')
        sys.stdout.write(x[0][2]+y)

for i in range(1, high+1):
    print ' ' * (high-i),
    print_chars(high, 1, [['*', '*', '*'], [' ']*3])