# bonjour.py : mon premier programme
print("Bonjour, je m'appelle Astou")
print(2025-1991)
import turtle          # charge la bibliothèque Turtle (fournie avec Python)
 
t = turtle.Turtle()    # crée une tortue : au centre de la fenêtre, cap 0° (elle regarde vers la droite)
 
t.forward(100)         # avance de 100 pas dans la direction où elle regarde (vers la droite)
t.left(90)             # pivote sur place de 90° vers SA gauche : elle regarde maintenant vers le haut
t.forward(50)          # avance de 50 pas vers le haut
t.right(45)            # pivote sur place de 45° vers SA droite : cap 45° (haut-droite)
t.backward(30)         # recule de 30 pas : elle va à l'opposé de son cap, sans tourner
 
turtle.done()          # garde la fenêtre ouverte jusqu'à ce que vous la fermiez

#import turtle
 
#t = turtle.Turtle()
 
#t.left(90)
#t.forward(100)
#t.left(90)
#t.forward(100)
 
#turtle.done()

#import turtle
 
#t = turtle.Turtle()
 
#t.forward(80)
#t.left(120)
#t.forward(80)
#t.left(120)
#t.forward(80)
#t.left(120)
 
#turtle.done()