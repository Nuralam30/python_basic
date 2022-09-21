
# first determine the fibonacci series
def fibonacci(n):
    if( n==0 ):
        return [0]
    
    elif( n==1 ):
        return [0,1]
    
    else:
        fibo = fibonacci(n-1)
        nextElement = fibo[n-1] + fibo[n-2]
        fibo.append(nextElement)
        return fibo

n = int(input('enter the length of the series :'))
series = fibonacci(n)


# summation of fibonacci series
i = 0
sum = 0

while i <= n :
    sum = sum + series[i]
    i += 1
print('total =', sum)