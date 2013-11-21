durations = ['2 godz. 3 min.','2 min.','1 godz. 52 min.']

for duration in durations:
	tab = duration.split(".")	
	hours = ""
	minutes = ""
	if len(tab) > 2:
		hours = str(tab[1][0:1])
		minutes = str(tab[1][:tab[1].find('min')]).strip()
	else:
		print duration
		# minutes = str(tab[1][:tab[1].find('min')]).strip()
	print hours + " godziny"
	print minutes + " minuty"
		# print "not ok"