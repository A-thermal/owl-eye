#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01 12:51:08
# @Author  : Termal (Termal@example.org)
# @Link    : http://Thermal.org
# @Version : $Id$
#功能：比较a，b两个字符串
def comparison(a,b):
    ib=0
    for ia in range(len(a)):
    	if ord(a[ia:ia+1])-ord(b[ib:ib+1])==0:
        	ib=ib+1
        	if ib==len(b):
        		print('a and b are equall')
    	else:
        	print('a and b are not equall')
        	break






