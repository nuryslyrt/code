#!/usr/bin/env python
#-*- coding: utf-8 -*-

def sesli():
    m = raw_input("dizgiyi giriniz: ")
    sesli = "aeıioöuüAEIİOÖUÜ"
    for i in m:
        if i in sesli:
            i = '*'
        print i
	
sesli()
		


		
		
