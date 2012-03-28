#!/usr/bin/env python
#-*- coding: utf-8

def prime_number(x):
    s=range(3,x+1,2)
    mroot = x ** 0.5
    half=(x+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    prime_number = [2]+[x for x in s if x]
    print prime_number
    print "list length: ", len(prime_number)
