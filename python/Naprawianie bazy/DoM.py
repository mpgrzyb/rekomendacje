from math import sqrt, log


# def calculaterDegreeOfMembership(position, numOfElements):
# 	alpha = 1.2
# 	degreeOfMembership = 0.0

# 	degreeOfMembership = position/pow(2.0, (sqrt(alpha*(numOfElements * (position-1)))))
# 	return round(degreeOfMembership, 5)

def calculaterDegreeOfMembership(position, numOfElements):
	degreeOfMembership = 0.0
	degreeOfMembership = (numOfElements - (position-1.0)) / sumOfsSer(numOfElements)
	return round(degreeOfMembership, 5)

def sumOfsSer(length):
	result = 0
	for x in range(1, length+1):
		result = result + x
	return result

# print calculaterDegreeOfMembership(1,1)