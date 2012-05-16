#!/usr/bin/ruby
# encoding: utf-8

def multiplier(n)
  lambda {|data| data.collect{|x| x*n}}
end

doubler = multiplier(2)
eval(n = 3, doubler)  
puts doubler.call([1,2,"i", 5])
