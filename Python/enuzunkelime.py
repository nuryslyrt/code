#!/usr/bin/python
# -*- coding: utf-8 -*-


def uzun_kelime(cumle):
    liste = cumle.split()
    uzunluk = []
    for kelime in liste:
        uzunluk.append(len(kelime))
    m= uzunluk.index(max(uzunluk))
    print liste[m]


uzun_kelime("zinnur yesilyurt")
