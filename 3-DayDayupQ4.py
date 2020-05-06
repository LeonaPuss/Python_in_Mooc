'''def dayup(dfup,dfwn):
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup=dayup*(1-dfwn)
        else:
            dayup=dayup*(1+dfup)
        return dayup
'''

def day365(dfup):
    dayup=1
    for i in range(365):
        dayup=dayup*(1+dfup)
    return dayup
def dayup(dfup):
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+dfup)
    return dayup
dayfactor=0.01
#daydown=0.01
dayupByA=0.01
#print('{:.2f}'.format(day365(dayupByA)))
#PowerByA=round(day365(dayupByA),4)
PowerByA=day365(dayupByA)
while dayup(dayfactor)<=PowerByA:
        dayfactor+=0.001
print('{:.3f}'.format(dayfactor))


#双参数的方案为什么不行？
#另外作出的结果是0.018，而官方导学给出的是0.019。对比代码后发现是dayfactor自增的步长我的精度是0.0001它的是0.001导致的。