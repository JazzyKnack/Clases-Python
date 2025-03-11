# Programa que haga avanzar 100 pasos a la tortuga y deje un trazo en pantalla.
# Primero se importarán los elementos necesarios del módulo turtle.
# Luego crearemos una pantalla a la que daremos un tamaño
# Después crearemos una tortuga y le diremos que avence 100 pasos.
# Y finalmente detendremos el programa hasta que el usuario pulse el boón del ratón en
# la superficie del dibujo.

from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

tortuga = Turtle()
tortuga.forward(180)

pantalla.exitonclick()