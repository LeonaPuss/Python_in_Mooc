'''星号三角形
描述
读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬

第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬'''
#num=int(input())
'''
line=int((num+1)/2)
 
for i in range(1,line+1):
 
    #这两行打印的是左半个三角形
    print(' '*int((num+1)/2-i),end='') #左部分的空格
    #print('*'*i,end='') #左部分的*含中间的
 
    #这两行打印的是右半个三角形
    print('*'*(2*i-1),end='') #右部分的*
    #print(' '*int((num+1)/2-i)) #右部分的空格，其实换行就可以了。这里应当是从C，复制过来的。所以仍然有个填充空格的思想。保持算法的一致对称。
    print('')
'''
num=int(input())
for i in range(1,num+1,2):
    print("{0:^{1}}".format("*"*i,str(num)))
#简洁之道：重点理解print，formart用法