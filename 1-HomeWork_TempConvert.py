#TempConvert.py
TempStr=input()
if  TempStr[-1] in ["F","f"]:
    TempC=(eval(TempStr[0:-1])-32)/1.8    #摄氏温度
    print("{:.2f}C".format(TempC))
elif TempStr[-1] in ["C","c"]:
    TempF=eval(TempStr[0:-1])*1.8+32    #华氏温度
    print("{:.2f}F".format(TempF))
else:
    print("输入格式错误")  #输出错误提示，附上必须要求