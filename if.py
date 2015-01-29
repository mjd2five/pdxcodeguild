age = raw_input("how old are you?: ")
gender = raw_input("male or female?: ")
location = raw_input("location?: ")

if int(age) <= 18: 
	print "too young"
elif int(age) >= 18: 
	print "too old"
else: 
	"numbers please"
if gender == "male": 
	print "male"
elif gender == "female": 
	print "female"
else: 
	"male or female"
if location == "Portland": 
	print "good"
elif location == "Beaverton": 
	print "good"
else:  
	print "bad"

