'''100以内素数之和
描述
求100以内所有素数之和并输出。 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬
素数指从大于1，且仅能被1和自己整除的整数。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬

提示：可以逐一判断100以内每个数是否为素数，然后求和。
'''


def isPrimeNumber(num):
    SquarNum=int(pow(num,0.5)) + 1
    k = True
    for i in range(2,SquarNum):
        if num % i == 0:
            k1= False
        else:
            k1= True
        k=k and k1
    return k
sum=0
RangeN=100
for j in range(2,RangeN+1):
    if isPrimeNumber(j) == True:
        sum += j
    #print(j)
print(sum)

