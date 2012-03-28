#!/usr/bin/env python
#-*- coding: utf-8 -*-

def anagram(s1,s2):

  List1 = list(s1)  
  List2 = list(s2)

  List1.sort()      
  List2.sort()

  i = 0
  state = "True"         

  while i < len(s1) and state:
    if List1[i]==List2[i]:
       i = i + 1
    else:
       state = "False"

  print state


anagram("earth","heart")
