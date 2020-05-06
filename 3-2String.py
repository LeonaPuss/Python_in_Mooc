'''
字符串分段组合
描述
获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。
'''
Str=input()
StrA=Str.split("-")
print("{0}+{1}".format(StrA[0],StrA[-1]))