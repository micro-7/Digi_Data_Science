from turtle import*

speed('fastest')

distance = 100
sides = 10


for i in range(sides):
    fd(distance)
    rt(360/sides)
    for i in range(sides):
        fd(distance/2)
        rt(360/sides)
        circle(distance/2)
        write(i)

hideturtle()
mainloop()