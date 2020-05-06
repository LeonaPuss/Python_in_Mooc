#4-2PrimeNumberIn100
def fun(num):
    sum = 0
    for num in range(2, num):
        n = int(pow(num, 0.5)) + 1
        for i in range(2, n):
            if num % i == 0:
                break
        else:
            sum += num
            #print(num)
    return sum

sum = fun(100)
print(sum)
