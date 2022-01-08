"""谢尔宾斯基Sierpinski三角形"""
import turtle


def draw_triangle(t, points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()


def get_mid(p1, p2):
    return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2


def sierpinski(t, points, degree):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
    draw_triangle(t, points, color_map[degree])
    if degree > 0:
        sierpinski(t,
                   {
                       'left': points['left'],
                       'top': get_mid(points['left'], points['top']),
                       'right': get_mid(points['left'], points['right'])
                   },
                   degree - 1,
                   )
        sierpinski(t,
                   {
                       'left': get_mid(points['left'], points['top']),
                       'top': points['top'],
                       'right': get_mid(points['top'], points['right'])
                   },
                   degree - 1)
        sierpinski(t,
                   {
                       'left': get_mid(points['left'], points['right']),
                       'top': get_mid(points['top'], points['right']),
                       'right': points['right']
                   },
                   degree - 1)


sierpinski(turtle.Turtle(), {'left': (-200, -100), 'top': (0, 200), 'right': (200, -100)}, 5)
turtle.done()
