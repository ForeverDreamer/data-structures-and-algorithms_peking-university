"""{4}--404递归可视化：分形树10m54s"""
import turtle


pen = turtle.Turtle()
pen.left(90)
pen.penup()
pen.backward(100)
pen.pendown()
pen.pencolor('green')
pen.pensize(2)


def tree(p, branch_len):
    if branch_len <= 5:
        return
    else:
        p.forward(branch_len)
        p.right(20)
        tree(p, branch_len - 15)
        p.left(40)
        tree(p, branch_len - 15)
        p.right(20)
        p.backward(branch_len)


tree(pen, 75)
pen.hideturtle()
turtle.done()
