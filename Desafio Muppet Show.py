import turtle
from turtle import *
from random import randint,choice
from turtle import Turtle, Screen
import os
from pydub import AudioSegment
from pydub.playback import play

turtle.hideturtle()

#Resolução do Ecran
screen = Screen()
screen.screensize(1366, 768)
screen.setup(width=1.0, height=1.0)



#muppet show
turtle.hideturtle()
penup()
track = Turtle(visible=False)
track.speed('fastest')
track.penup()
track.goto(-100, 200)
win = turtle.Screen()
win.bgcolor('orange')
turtle = Turtle()
speed(0)
penup()
track = Turtle(visible=False)
track.speed('fastest')
track.penup()
track.goto(-100, 200)

for step in range(16):
    track.color("white")
    #style = ('Arial', 13, 'bold')
    track.write(step,('Arial', 13, 'bold'), align='center')
    track.right(90)
    track.forward(10)
    track.pendown()
    track.forward(160)
    track.penup()
    track.backward(170)
    track.left(90)
    track.forward(20)

#PARTIDA:
inicio=Turtle()
inicio.up()
inicio.speed(0)
inicio.goto(-100, 260)
inicio.down()
inicio.right(90)
inicio.width(5)
inicio.color("white")
inicio.write("PARTIDA", align='center')
for i in range (40):
    inicio.color("white")
    inicio.forward(5)
    inicio.color("green")
    inicio.forward(5)

#META:
meta=Turtle()
meta.up()
meta.speed(0)
meta.goto(250, 260)
meta.down()
meta.right(90)
meta.width(5)
meta.color("white")
meta.write("META", align='center')
for i in range (40):
    meta.color("blue")
    meta.forward(5)
    meta.color("red")
    meta.forward(5)

penup()
backward(160)
left(90)
forward(20)

#COCAS
hideturtle()
win.register_shape("COCAS.gif")
cocas = Turtle()
cocas.penup()
cocas.shape("COCAS.gif")
cocas.penup()
cocas.goto(-130,175)
goto(-250,175)
write("Cocas")
for turn in range(10):
    cocas.right(36)


#MISS PIGGY
win.register_shape("PIGGY.gif")
piggy = Turtle()
piggy.penup()
piggy.shape("PIGGY.gif")
piggy.penup()
piggy.goto(-130,145)
goto(-250,145)
write("Miss Piggy")
for turn in range(72):
    piggy.left(5)


#FOZZY
win.register_shape("FOZZY.gif")
fozzy = Turtle()
fozzy.penup()
fozzy.shape("FOZZY.gif")
fozzy.penup()
fozzy.goto(-130,115)
goto(-250,115)
write("Fozzy")
for turn in range(60):
    fozzy.right(36)


#GONZO
win.register_shape("GONZO.gif")
gonzo = Turtle()
gonzo.penup()
gonzo.shape("GONZO.gif")
gonzo.penup()
gonzo.goto(-130,85)
goto(-250,85)
write("Gonzo")
for turn in range(60):
    gonzo.right(36)


#ANIMAL
win.register_shape("ANIMAL.gif")
animal = Turtle()
animal.penup()
animal.shape("ANIMAL.gif")
animal.penup()
animal.goto(-130,55)
goto(-250,55)
write("Animal")
for turn in range(10):
    animal.right(36)


screen = Screen()

while turtle.xcor()<261:
    turtle = choice([cocas,piggy,gonzo,animal,fozzy])
    turtle.forward(randint(1, 5))


if cocas.xcor()>260:
    goto(-200,70)
    track.color("green")
    track.write("Cocas é o Vencedor", font=("Arial", 20, 'bold'))
elif piggy.xcor()>260:
    goto(-200,70)
    track.color("pink")
    track.write("Miss Piggy é a Vencedora", font=("Arial", 20, 'bold'))
elif fozzy.xcor()>260:
    goto(-200,70)
    track.color("brown")
    track.write("Fozzy Bear é o Vencedor", font=("Arial", 20, 'bold'))
elif gonzo.xcor()>260:
    goto(-200,70)
    track.color("lightblue")
    track.write("Gonzo é o Vencedor", font=("Arial", 20, 'bold'))
elif animal.xcor()>260:
    goto(-200,70)
    track.color("red")
    track.write("Animal é o Vencedor", font=("Arial", 20, 'bold'))

#SOM
file = AudioSegment.from_mp3('the-muppet-show-ringtone .wav')
#os.system("mpg123 " + file)
play(file)

screen.exitonclick()
