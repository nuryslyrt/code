#!/usr/bin/env python
# -*- coding: utf8 -*- 

def sillan(strg):
	for i in strg:
		if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
			pass
		else:
			i = ''
		print i
	
sillan("asd,hj!+asd")
