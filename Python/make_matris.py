#!/usr/bin/env python
#-*- coding: utf-8 -*-

def make_matrix(rows, columns):
    matrix = []
    for row in range(rows):
        matrix += [[0] * columns]
    return matrix
    print matrix

k = make_matrix(3, 5)
print "k matrisi = \n", k
m = make_matrix(4, 2)
print "m matrisi = \n", m
m[1][1] = 7   
print "m in 1.sutun 1.satiri 7 olsun! = \n", m
