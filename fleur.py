import turtle

# Création de la tortue
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Fonction pour dessiner un pétale
def dessiner_petale():
    t.fillcolor("pink")
    t.begin_fill()

    t.circle(80, 60)
    t.left(120)
    t.circle(80, 60)
    t.left(120)

    t.end_fill()

# Dessiner les 12 pétales
for k in range(12):
    dessiner_petale()
    t.left(30)

# Dessiner le centre de la fleur
t.penup()
t.dot(25, "yellow")

turtle.done()