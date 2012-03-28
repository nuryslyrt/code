#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print self.num, "/", self.den
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
    #Assume that m and n are greater than zero
    def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
            return n
    def __cmp__(self,otherfraction):
        num1 = self.num*otherfraction.den
        num2 = self.den*otherfraction.num
        if num1 < num2:
            return -1
        else:
            if num1 == num2:
                return 0
            else:
                return 1
    

