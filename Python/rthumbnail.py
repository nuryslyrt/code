#!/usr/bin/env python

import os
import Image

klasor = 'tux'
kucukler = 'onizleme'

if not os.path(kucukler):
    os.mkdir(kucukler)
for i in os.listdir(klasor):
    res = Image.open(klasor + '/' + i)
    res.thumbnail((100, 100))
    res.save(kucukler + '/' + i)
