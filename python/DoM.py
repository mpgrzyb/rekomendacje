from math import sqrt, log


def calculaterDegreeOfMembership(position, numOfElements):
	alpha = 1.2
	degreeOfMembership = 0.0

	degreeOfMembership = position/pow(2.0, (sqrt(alpha*(numOfElements * (position-1)))))
	return round(degreeOfMembership, 5)

# def CalculateLj(p, mi):
# 	x = 0.0
# 	x = pow((log(p/mi)/log(2)),2)/1.2
# 	return x