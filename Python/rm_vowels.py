#!/usr/bin/env python
#-*- coding: utf-8 -*-

def remove_vowels(s):
    vowels = "aeıioöuüAEIİOÖUÜ"
    out = ""
    for letter in s:
        if letter not in vowels:
            out = out + letter
    print out

remove_vowels("1zinnur9")
remove_vowels("Azteklerin kayboluşunu anlattılar.")
