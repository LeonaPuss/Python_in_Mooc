ls=['cat',1,2,3,4,'tiger',1024]
print(ls)
ls=5*ls
print(ls)
'''for i in ls:
    ls.remove('cat')#remove方法会抛出异常，得另寻他法。'''
#ls=ls.remove('cat') 会使得ls为空值
ls.remove(1)
#del ls[::3]
#ls=ls[:2]+ls[3:]
print(ls)