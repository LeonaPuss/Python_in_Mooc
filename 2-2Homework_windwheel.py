'''
3900351556843959479
turtle风轮绘制
 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬

描述
使用turtle库，绘制一个风轮效果，其中，每个风轮内角为45度，风轮边长150像素。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬

注意：这不是自动评阅题目，仅用于练习，没有评阅。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬

提示：turtle.goto(x,y)函数，能够将turtle画笔移动到坐标(x,y)
'''
import turtle
turtle.pensize(5)
for i in range(4):
    turtle.right(45)
    turtle.fd(150)
    turtle.left(90)
    turtle.circle(150,45)
    turtle.goto(0,0)
turtle.done()
'''
circle 的半径值影响圆心点，角度值会使得乌龟按角度旋转方向。
另外请尝试看看有没有可以从后方侧先绘制的办法。
'''
