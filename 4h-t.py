'''PlainText=input()
CipherText=""
for i in PlainText:
    if ("a"<=i<="z"  ):
        CipherText+=chr(ord('a')+((ord(i)-ord('a')+3)%26))
    elif "A"<=i<="Z":
        CipherText+=chr(ord('A')+((ord(i)-ord('A')+3)%26))
    else:
        CipherText+=i
print("{0}".format(CipherText))
'''
'''import time
scale = 50
print("执行开始".center(scale//2,'-'))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))
'''
'''name="Python语言程序设计课程"
print(name[0],name[2:-2],name[-1])'''

'''ls="python123.io"
ls=max(ls[::-1])
print(ls)'''

'''ls=['cat',1,2,3,4,'tiger',1024]
print(ls)
ls=5*ls
print(ls)
for i in ls:
    ls[i]=ls.remove(3)
#ls=ls.remove(1)
#del ls[::3]
print(ls)
'''


'''
lt=[]
#lt=lt.append(1,2,3,4,5)
lt+=[1,2,3,4,5]
lt[2]=2
#lt[2:]='@'
lt.insert(2,"@")
del lt[1]
del lt[1:4]
0 in lt
if 0 in lt:
    print(True)
else:
    print(False)
lt=lt.append(0)
lt.index(0)
len(lt)
max(lt)
lt.clear()
'''


'''
k=10000
while k>1:
    print(k)
    k=k/2
'''

from datetime import datetime
#import datetime 库名不对
today = datetime.now()
print(today)
