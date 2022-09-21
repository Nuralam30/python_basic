
import math

r = float(input('enter the radius of the circle :'))

if r > 0:
    area = 4/3 * math.pi * r*r
    print('Area of the circle :', area)
else:
    print('enter radius value > 0..')