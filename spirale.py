import turtle

t = turtle.Turtle()
t.speed(0)

turtle.bgcolor("black")

couleurs = ["cyan", "magenta", "yellow", "orange"]

for i in range(120):
    t.color(couleurs[i % len(couleurs)])
    t.forward(i * 1.2)
    t.left(59)

turtle.done()