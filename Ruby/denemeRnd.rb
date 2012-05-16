#!/usr/bin/ruby
# encoding: utf-8

require 'Random'

class Dice
  attr_reader :s
  def initialize(s)
    @s = s
  end

  def RollDice()
    x = Random.new.rand(1..s)
    return x
  end
end

def main
  roll1 = Dice.new 6
  roll2 = Dice.new 4
  roll3 = Dice.new 6
  roll4 = Dice.new 12
  print roll1.RollDice()
  print roll2.RollDice()
  print roll3.RollDice()
  print roll4.RollDice() 
end

if __FILE__ == $0
  main
end
