#usr/bin/ruby
# encoding: utf-8

sum = 0
i = 1

while i <= 10 do
  sum = sum + (i * i)
  i = i + 1
end

puts "Kareler toplami #{sum}"
