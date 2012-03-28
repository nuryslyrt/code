#!/usr/bin/env python
# -*- coding: utf8 -*- 

def bork(x):
	if 65 <= ord(x) <= 90:
		print "True"
	elif 97 <= ord(x) <= 122:
		print "False"
	else:
		print "yanlis LAN !!!"
		
bork('A')
