#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
liste1 = range(1, 51)
liste2 = []
i = 1

while True:
    k = random.randrange(1, 51)

    if k not in liste2:
            print k
     
    else:
            while (k in liste2):
                    k = random.randrange(1, 51)
            print k

    if i == 50:
            break

    i = i + 1
    liste2.append(k)

#Entera gerek duymadan 50 farkli random sayiyi ekrana doker.
#bu sefer liste elle girilmez. range le yapilir.
