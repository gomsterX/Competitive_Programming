#Problem ID: QUADROOT
#Problem Name: Roots of a Quadratic Equation

import math
a = int(input())
b = int(input())
c = int(input())

discriminant = math.sqrt((b**2) - 4*a*c)

print((-b+discriminant)/(2*a),"\n",(-b-discriminant)/(2*a), sep='')
