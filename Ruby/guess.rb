words = ['kestane', 'gurgen', 'palamut']
secret = words[rand(5)]

print "tahmin et? "
while guess = STDIN.gets
	guess.chop!
	if guess == secret
		print "Bildin!\n"
		break
	else
		print "uzgunum kaybettin.\n"
	end
	print "tahmin et? "
end

print "Kelime ", secret, ".\n"
