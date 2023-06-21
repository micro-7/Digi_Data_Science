from turtle import*

speed('slowest')

distance = 100
sides = 10


for i in range(sides):
    fd(distance)
    rt(360/sides)

hideturtle()
mainloop()