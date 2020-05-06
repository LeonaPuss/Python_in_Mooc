#WindWheel.py
import turtle as t
for i in range(4):
    t.seth(90*i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0,0)
t.done()

#这一段应当是和官方版本代码的一致的。第一步，是确立朝向，第二步绘制直线段，第三步，绘制弧线段，第四步绘制回中心点（原点）的直线段。以上述四步为循环体，朝向、次数为循环转子，次数是出循环条件。