#!/usr/bin/ruby
# -*- coding utf-8 -*-

class Hmm
  attr_reader :x
  def initialize(x)
    @x = x
  end

  def ex()
    puts x
    if x == nil then
      puts 2
    end
  end
end

class Oops < Hmm
  attr_reader :x
  def initialize(x)
    @x = x
  end

  def ex()
    puts x
  end
end

def main()
  zin = Hmm.new 0 
  om = Oops.new 1
  print "simdik zin !"
  zin.ex()
  print "simdik om !"
  om.ex()
  print "mirasa bak !"
  #om.Hmm.class.ex()
end

if __FILE__ == $0
  main()
end
