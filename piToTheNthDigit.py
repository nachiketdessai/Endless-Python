import math
numDigits = int(raw_input('Enter the number of decimal places of Pi '))
while numDigits > 40:
	print "Enter a number less than 40"
	numDigits = int(raw_input('Enter the number of decimal places of Pi '))
else:	
    print '%.*f' % (numDigits, math.pi)

