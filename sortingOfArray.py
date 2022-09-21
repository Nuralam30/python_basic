
n = int(input('Enter the array length :'))
x = []

for i in range(1,n+1):
    element = float(input('Enter value :'))
    x.append(element)

for i in range(0, n-1):
    temp = x[i]
    if x[i] > x[i+1]:
        x[i] = x[i+1]
        x[i+1] = temp
        temp = x[i+1]

print(x)

