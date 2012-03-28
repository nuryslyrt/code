#!/usr/bin/env python
#-*- coding: utf-8 -*-

def fibonacci(n):
   a, b = 0, 1
   golden = 1
   toplam = 1
   while b < n:
      print b, '\t', '\t', golden, '\t', '\t', '\t', toplam
      a, b = b, a + b
      golden = (b / float(a))
      toplam = toplam + b        


fibonacci(10)
