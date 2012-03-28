#!/usr/bin/env python
#-*- coding: utf-8

import random 

class Dice:
    def __init__(self, s = 6):
        self.sides = s
    def RollDice(self):
        x = random.randint(1, self.sides)
        return x

roll1 = Dice()
roll2 = Dice(4)
roll3 = Dice(6)
roll4 = Dice(12)

print roll1.RollDice()
print roll2.RollDice()
print roll3.RollDice()
print roll4.RollDice()
