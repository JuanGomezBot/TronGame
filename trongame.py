import turtle
import random
import keyboard
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
previouscord = []
def moveplayer():
    if keyboard.is_pressed(keyboard.KEY_UP):
        d.setheading(90)
        d.forward(30)
    if keyboard.is_pressed(keyboard.KEY_DOWN):
        d.setheading(270)
        d.forward(30)
    if keyboard.is_pressed("left"):
        d.setheading(180)
        d.forward(30)
    if keyboard.is_pressed("right"):
        d.setheading(360)
        d.forward(30)
    if keyboard.is_pressed('c'):
        print(d.pos())
    posy = d.ycor()
    posx = d.xcor()

    cord = (str(posx),",",str(posy))

    if cord in previouscord:
        d.penup()
        print("You lost")

    else:
        previouscord.append(cord)


    if posx >= 640.00 or posy >= 330.00 or posx <= -640.00 or posy <= -330.00 :
        d.goto(600,-200) 
    
def initialize():
    turtle.bgcolor("Black")
    a.penup()
    a.pencolor("Yellow")
    a.goto(-600,200)
    a.pendown()
    b.penup()
    b.pencolor("Cyan")
    b.goto(-600,-200)
    b.pendown()
    c.penup()
    c.pencolor("Red")
    c.goto(600,200)
    c.left(180)
    c.pendown()
    d.penup()
    d.left(180)
    d.pencolor("Lime")
    d.goto(600,-200)
    d.pendown()


def moveopponent_a():
    movement = ['up','down','right','left']
    a.speed(2)
    posy = a.ycor()
    posx = a.xcor()
    ch = random.choice(movement)
    if ch == "up":
        a.setheading(90)
        a.forward(30)
    if ch == 'down':
        a.setheading(270)
        a.forward(30)
    if ch == 'right':
        a.setheading(360)
        a.forward(30)
    if ch == 'left':
        a.setheading(180)
        a.forward(30)
    posy = a.ycor()
    posx = a.xcor()
    cord = (str(posx),",",str(posy))
    
    if posx >= 640.00 or posy >= 330.00 or posx <= -640.00 or posy <= -330.00 :
        a.goto(-600,200) 
    
    if cord in previouscord:
        a.penup()
        print("Yellow player has lost")

    else:
        previouscord.append(cord)



    



    
def moveopponent_b():
    movement = ['up','down','right','left']
    b.speed(2)
    ch = random.choice(movement)
    if ch == "up":
        b.setheading(90)
        b.forward(30)
    if ch == 'down':
        b.setheading(270)
        b.forward(30)
    if ch == 'right':
        b.setheading(360)
        b.forward(30)
    if ch == 'left':
        b.setheading(180)
        b.forward(30)
    posy = b.ycor()
    posx = b.xcor()
    
    
    

    cord = (str(posx),",",str(posy))
    
    if posx >= 640.00 or posy >= 330.00 or posx <= -640.00 or posy <= -330.00 :
        b.goto(-600,-200) 
    
    if cord in previouscord:
        b.penup()
        print("Cyan player has lost")

    else:
        previouscord.append(cord)

    
    
def moveopponent_c():
    c.speed(2)
    movement = ['up','down','right','left']
    ch = random.choice(movement)
    
    if ch == "up":
        c.setheading(90)
        c.forward(30)
    if ch == 'down':
        c.setheading(270)
        c.forward(30)
    if ch == 'right':
        c.setheading(360)
        c.forward(30)
    if ch == 'left':
        c.setheading(180)
        c.forward(30)
    posy = c.ycor()
    posx = c.xcor()
    
    if posx >= 640.00 or posy >= 330.00 or posx <= -640.00 or posy <= -330.00 :

        c.penup()
        c.goto(600,200) 
        c.pendown()
    
    cord = (str(posx),",",str(posy))

    if cord in previouscord:
        c.penup()
        print("Red player has lost")
        

    else:
        previouscord.append(cord)

    
def main():

    initialize()
    while True:
        turtle.speed(1)
        moveplayer()
        moveopponent_a()
        moveopponent_b()
        moveopponent_c()
        if a.isdown and not b.isdown() and not c.isdown() and not d.isdown:
            print("Yellow won")
            return
        elif b.isdown and not a.isdown() and not c.isdown() and not d.isdown():
            print("Cyan won")
            return
        elif c.isdown and not b.isdown() and not a.isdown() and not d.isdown():
            print("red won")
            return
        elif d.isdown and not b.isdown() and not c.isdown() and not a.isdown():
            print("Player won")
            return
if __name__ == "__main__":
    main()
    input()