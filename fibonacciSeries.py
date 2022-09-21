
def fibonacciSum(n):
    if n <= 0:
        return 0
    fibo = [0] *(n+1)
    fibo[1] = 1

    sum = fibo[0] + fibo[1]

    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        sum = sum + fibo[i]

    return sum
    
num = int(input('enter the length of series :'))
print('sum of the series :', fibonacciSum(num))
