Num = int(input())
if Num%2 != 0:
    for j in range(Num+1): #需要输入N个那么循环要走到N+1
        for i in range(j):
            print('*',end="")
        print("\n")
        j+=1    # 这个简写形式原来搞错了“j+=j,错的离谱”
else:
    print("Please enter a odd number!")