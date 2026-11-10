# --- Compatibilité plateforme : ne pas modifier ---
#try:
 #cept Exception:
  #  from types import SimpleNamespace

   # class FauxTurtle:
    #    def __init__(self):
     #  def __getattr__(self, nom):
      #         self.journal.append((nom, *args))
       #     return commande

    #turtle = SimpleNamespace(Turtle=FauxTurtle, done=lambda: None)

# --- Réglages ---
#cote = 150
#angle = 60

# --- Programme : un carré ---
#t = turtle.Turtle()



# Prédiction 1 :
# Prédiction 2 :
# Prédiction 3 :
#t.color ("red")
#t.forward(cote)
#t.left(angle)
#t.forward(cote)
#t.left(angle)
#t.forward(cote)
#t.left(angle)
#t.forward(cote)
#t.forward(cote)
#t.left(angle)
#t.forward(cote)
#t.left(angle)
    
#turtle.done()

# Écart :
import turtle
 
t = turtle.Turtle()
 
def carre(taille):
    t.forward(taille)
    t.left(90)
    t.forward(taille)
    t.left(90)
    t.forward(taille)
    t.left(90)
    t.forward(taille)
    t.left(90)
 
carre(50)
carre(120)
 
turtle.done()