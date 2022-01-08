"""{4}--404递归可视化：分形树10m54s"""
import turtle

pen = turtle.Turtle()


def draw_spiral(p, line_len):
    if line_len < 0:
        return
    else:
        p.forward(line_len)
        p.right(90)
        draw_spiral(p, line_len - 5)


draw_spiral(pen, 100)
turtle.done()
