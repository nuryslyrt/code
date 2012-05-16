#!/usr/bin/ruby -w
# -*- coding: utf-8 -*-

def bolen(sayi)
  dolgu = []
  (1..sayi).each do |i|
    if sayi%i == 0 then
      dolgu << i
    end
  end
  puts dolgu
end

bolen(20)
