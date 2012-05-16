#!/usr/bin/ruby
# encoding: utf-8

mean = a.inject{|x,y| x+y}/a.size
sumofsquares = a.map{|x| (x-mean)**2}.inject{|x,y| x+y}
standarddeviation = Math.sqrt(sumofsquares/(a.size-1))
