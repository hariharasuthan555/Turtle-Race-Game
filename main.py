import random
from turtle import Turtle,Screen


screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput("Choose your bet","Which turtle do you bet on?Enter a color:")

forward=[100,50,20,25,50]

t1=Turtle()
t1.penup()
t1.shape("turtle")
t1.color(user_bet)
t1.goto(x=-230,y=-100)

t2=Turtle()
t2.penup()
t2.shape("turtle")
t2.goto(x=-230,y=-150)

t3=Turtle()
t3.penup()
t3.shape("turtle")
t3.goto(x=-230,y=-0)

t4=Turtle()
t4.penup()
t4.shape("turtle")
t4.goto(x=-230,y=100)

t5=Turtle()
t5.penup()
t5.shape("turtle")
t5.goto(x=-230,y=150)

t6=Turtle()
t6.penup()
t6.shape("turtle")
t6.goto(x=-230,y=50)

t7=Turtle()
t7.penup()
t7.shape("turtle")
t7.goto(x=-230,y=-50)

tutlelist=[t2,t3,t4,t5,t6]
full_turtles=[t1,t2,t3,t4,t5,t6,t7]
colours=["red","green","yellow","brown","orange","blue","violet"]

colours.remove(user_bet)

print(colours)

t2.color(colours[0])
t3.color(colours[1])
t4.color(colours[2])
t5.color(colours[3])
t6.color(colours[4])
t7.color(colours[5])

t1.forward(200)
bool_val=True
winner_color=""
while bool_val:
    for i in full_turtles:
        i.forward(random.choice(forward))
        if i.xcor()>=150:
            bool_val=False
            winner_color=i.pencolor()
            if winner_color==user_bet:
                screen.title("Your turtle Won the race...!")
                break
            else:
                screen.title(f"Sorry, {winner_color} turtle won the race.")
                break






screen.exitonclick()