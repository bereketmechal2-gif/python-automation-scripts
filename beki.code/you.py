y = int(input("How many times do you want to rotate \n"))
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
artist = turtle.Turtle()
artist.speed(0)
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
for x in range(y):
    artist.pencolor(colors[x % 6])
    artist.width(x // 100 + 1)
    artist.forward(x)
    artist.left(59)
screen.exitonclick()
