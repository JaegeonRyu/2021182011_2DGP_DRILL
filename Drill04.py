import turtle

count = 6
while(count > 0):
    turtle.penup()
    turtle.goto(100,600 - count*100)
    turtle.pendown()
    turtle.forward(500)
    count = count -1

turtle.right(90)

c = 6
while(c > 0):
    turtle.penup()
    turtle.goto(700 - c*100,500)
    turtle.pendown()
    turtle.forward(500)
    c = c -1

