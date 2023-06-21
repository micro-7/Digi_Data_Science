from turtle import*

speed('slowest')
distance = 100
size = 10
for side in range(5):
    fd(size)
    rt(72)
    fd(size)
    rt(72 - 120)

mainloop()