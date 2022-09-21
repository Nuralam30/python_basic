
# factorial number using loop
n = int(input('Enter a number :'))
i = 1
result = 1

while i <= n :
    result = result * i
    i += 1    
print('Factorial of ',n ,' is ',result)



# or using recursive function
def factorial(n):
    if n == 1 :
        return 1
    else :
        return n * factorial(n-1)

print('factorial of ', n , 'is', factorial(n))
