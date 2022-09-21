
length = float(input('Enter length :'))
width = float(input('Enter width :'))

if length > 0 and width > 0 :
    area = length * width
    print('Area of the rectangle :', area, 'square unit')
else:
    print('Length or width cannot be negative..')