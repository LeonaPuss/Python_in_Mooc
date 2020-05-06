import random



#GuessNumber = eval(input("Please enter your number:")) 注意顺序结构对逻辑的影响
seed = 100  #为调式固定一组伪随机数
RightNumber = random.randint(1,100) #理解题意用randint实现
N = 0

while True :
    try :
        GuessNumber = eval(input("Please enter your number:")) #仅在此次方能表示猜数字错误一次后再猜另一次
        if GuessNumber==RightNumber:
            N +=1
            print('预测{0}次，你猜中了！'.format(N)) #书86页print.format
            break
        elif GuessNumber>=RightNumber:
            N +=1
            print('遗憾太大了')
            continue
        elif GuessNumber<=RightNumber:
            N +=1
            print('遗憾太小了')
            continue
    except :
        print('输入内容必须为整数！')