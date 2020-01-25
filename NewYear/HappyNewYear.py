'''
   Happy new year! Happy Spring Festival!
'''
import turtle

def love_circle(x, y, r, d):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('red', 'pink')
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(d)
    turtle.circle(r, 180)
    turtle.left(270)
    turtle.circle(r, 180)
    turtle.forward(d)
    turtle.end_fill()
    turtle.left(45)


def love(lover):
    # 设置画布
    turtle.setup(800, 700, 70, 70)

    # 画第一个气球
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()
    turtle.color('red')
    turtle.circle(50)
    turtle.right(90)
    turtle.forward(150)

    # 画第二个气球str
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.color('green')
    turtle.right(270)
    turtle.circle(50)
    turtle.right(90)
    turtle.forward(150)

    # 画第三个气球
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    turtle.color('blue')
    turtle.right(270)
    turtle.circle(50)
    turtle.right(90)
    turtle.forward(150)

    # 画第四个气球
    turtle.penup()
    turtle.goto(300, 0)
    turtle.pendown()
    turtle.color('purple')
    turtle.right(270)
    turtle.circle(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)

    # 分别在四个坐标写上 "新"、"年"、"快"、"乐"
    turtle.penup()
    turtle.goto(-300, 35)
    turtle.pendown()
    turtle.color('red')
    turtle.write("新", move=False, align='center', font=("微软雅黑", 30, 'normal'))

    turtle.penup()
    turtle.goto(-100, 35)
    turtle.pendown()
    turtle.color('green')
    turtle.write("年", move=False, align='center', font=("微软雅黑", 30, 'normal'))

    turtle.penup()
    turtle.goto(100, 35)
    turtle.pendown()
    turtle.color('blue')
    turtle.write("快", move=False, align='center', font=("微软雅黑", 30, 'normal'))

    turtle.penup()
    turtle.goto(300, 35)
    turtle.pendown()
    turtle.color('purple')
    turtle.write("乐", move=False, align='center', font=("微软雅黑", 30, 'normal'))

    # 写上标题
    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()
    turtle.color('pink')
    turtle.write("Send to my favorite lover of {}".format(lover), move=False, align='center', font=("微软雅黑", 30, 'normal'))

    # 调用 love_circle()画爱心
    love_circle(-50, -300, 35, 75)
    # 在爱心里写字
    turtle.penup()
    turtle.goto(-50, -240)
    turtle.pendown()
    turtle.color('red')
    turtle.write("LZ", move=False, align='center', font=("微软雅黑", 30, 'normal'))

    # 画第二个爱心
    love_circle(50, -300, 35, 75)
    turtle.penup()
    turtle.goto(50, -240)
    turtle.pendown()
    turtle.color('red')
    turtle.write("YQ", move=False, align='center', font=("微软雅黑", 30, 'normal'))

    # 丘比特之箭
    turtle.penup()
    turtle.pensize(2)
    turtle.color('red')
    turtle.goto(-150, -240)
    turtle.pendown()
    turtle.forward(300)

    turtle.done()

def main():
    lover = input('Please input your name(initial):')
    love(lover)

if __name__ == "__main__":
    main()
