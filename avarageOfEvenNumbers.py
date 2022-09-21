
n = int(input('Enter the list length :'))
x = []

for i in range(1,n+1):
    element = float(input('Enter value :'))
    x.append(element)



# avarage the even numbers
sum = 0
c = 0

for i in range(0, n):
    if x[i] % 2 == 0:
        sum = sum + x[i]
        c += 1
avg = sum / c
print('Avarage of the even numbers :',avg)
