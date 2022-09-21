


find = int(input('enter the number you want :'))
x = [12, 23, -45, 76, -17, 34]
flag = False
loc = 1

for i in range(0, len(x)):
    if x[i] == find:
        flag = True
        loc = i + 1

if flag == True:
    print(find, 'is present at position ', loc)
else:
    print(find, 'is not prsent in the array..')