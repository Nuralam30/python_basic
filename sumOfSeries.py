
n = int(input('Enter the last number of the series :'))
# i = 1
# sum = 0

# while i <= n :
#     sum = sum + i*i
#     i += 1
# print(sum)


# recursive method for series
def sum(n):
    if n == 1:
        return 1
    else:
        return  n*n + sum(n-1)

print(sum(n))
