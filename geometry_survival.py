import turtle
import time
import winsound


time.sleep(1)

print("¤ ================================= ¤")
print("             Welcome")
winsound.Beep(200, 100)


print("     Geometry Survival 1.3")
print("        by DandyTheWood")

print("¤ ================================= ¤")

time.sleep(1)

winsound.Beep(150, 200)
winsound.Beep(150, 200)
winsound.Beep(100, 200)
winsound.Beep(70, 500)

time.sleep(2)

winsound.Beep(200, 100)

winsound.Beep(200, 100)

play = input("""  Type "P" Play: """)

if play != "P":
    time.sleep(1)
    print(" =¤=======¤=======¤=======¤=====¤=")
    print(" =¤=======¤=======¤=======¤=====¤=")
    print(" =¤=======¤=======¤=======¤=====¤=")
    print("""  Wrong letter, Write capital "P" next time""")
    
    winsound.Beep(200, 300)
    winsound.Beep(150, 300)
    winsound.Beep(100, 300)
    winsound.Beep(70, 700)
    
    time.sleep(3)
    quit()

time.sleep(1)
print(" =¤=======¤=======¤=======¤=====¤=")
print(" =¤=======¤=======¤=======¤=====¤=")
print(" =¤=======¤=======¤=======¤=====¤=")
time.sleep(1.5)
print("  Lets Go!!!")
winsound.Beep(200, 100)

winsound.Beep(200, 100)

winsound.Beep(200, 100)

winsound.Beep(200, 100)

time.sleep(1.5)
print(" =================================")
print("  Dodge The Small Circles")
print(" =================================")
winsound.Beep(70, 500)
time.sleep(1)
print("  Control With Arow Keys or WSAD")
print(" =================================")
winsound.Beep(70, 500)
time.sleep(1)
print("  Red Is Main Ball That Gives You Score")
print(" =================================")
winsound.Beep(70, 500)
time.sleep(1)
print("  Game Will Open In New Window")
print(" =================================")
winsound.Beep(70, 500)
time.sleep(1.5)

print(" 3")
winsound.Beep(200, 100)
time.sleep(1)
print(" 2")
winsound.Beep(200, 100)
time.sleep(1)
print(" 1")
winsound.Beep(200, 100)
time.sleep(1)
print(" 0")
winsound.Beep(200, 900)

time.sleep(1)


# Screen
wn = turtle.Screen()
wn.title("Geometry Survival 1.3")
wn.bgcolor("midnight blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# Bounce
bounce = 0

# Man
man = turtle.Turtle()
man.speed(0)
man.shape("circle")
man.color("white")
man.shapesize(stretch_wid=2, stretch_len=2)
man.penup()
man.goto(0, 0)

# Enemy
enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(-300, 250)
enemy.dx = 0.15
enemy.dy = 0.15

# Enemy 2
enemy2 = turtle.Turtle()
enemy2.speed(0)
enemy2.shape("circle")
enemy2.color("green")
enemy2.penup()
enemy2.goto(-300, -250)
enemy2.dx = 0.15
enemy2.dy = 0.15

# Enemy 3
enemy3 = turtle.Turtle()
enemy3.speed(0)
enemy3.shape("circle")
enemy3.color("yellow")
enemy3.penup()
enemy3.goto(300, 0)
enemy3.dx = 0.2
enemy3.dy = 0.2


# Point Counter
pt = turtle.Turtle()
pt.speed(0)
pt.color("white")
pt.penup()
pt.hideturtle()
pt.goto(0, 260)
pt.write("0 : SCORE", align="center", font=("Courier", 24, "bold"))


# Functions
def man_up():
    y = man.ycor() 
    y += 20
    man.sety(y)

def man_down():
    y = man.ycor() 
    y -= 20
    man.sety(y)

def man_left():
    x = man.xcor() 
    x -= 20
    man.setx(x)
    
def man_right():
    x = man.xcor() 
    x += 20
    man.setx(x)


# Key Bindings
wn.listen()
wn.onkeypress(man_up, "Up")
wn.onkeypress(man_down, "Down")
wn.onkeypress(man_left, "Left")
wn.onkeypress(man_right, "Right")

# Key Bindings 2
wn.listen()
wn.onkeypress(man_up, "w")
wn.onkeypress(man_down, "s")
wn.onkeypress(man_left, "a")
wn.onkeypress(man_right, "d")

# Key Bindings 2 Caps
wn.listen()
wn.onkeypress(man_up, "W")
wn.onkeypress(man_down, "S")
wn.onkeypress(man_left, "A")
wn.onkeypress(man_right, "D")

# Main Loop
while True:
    wn.update()

    
    # Enemy Movement
    enemy.setx(enemy.xcor() + enemy.dx)
    enemy.sety(enemy.ycor() + enemy.dy)

    # Enemy 2 Movement
    enemy2.setx(enemy2.xcor() + enemy2.dx)
    enemy2.sety(enemy2.ycor() + enemy2.dy)

    # Enemy 3 Movement
    enemy3.setx(enemy3.xcor() + enemy3.dx)
    enemy3.sety(enemy3.ycor() + enemy3.dy)

    
    # Border
    if enemy.ycor() > 290:
        enemy.sety(290)
        enemy.dy *= -1
        bounce += 1
        winsound.Beep(200, 120)
        pt.clear()
        pt.write("{} : SCORE".format(bounce), align="center", font=("Courier", 24, "normal"))
    
    if enemy.ycor() < -290:
        enemy.sety(-290)
        enemy.dy *= -1
        bounce += 1
        winsound.Beep(200, 120)
        pt.clear()
        pt.write("{} : SCORE".format(bounce), align="center", font=("Courier", 24, "normal"))
        
    if enemy.xcor() > 390:
        enemy.setx(390)
        enemy.dx *= -1
        bounce += 1
        winsound.Beep(200, 120)
        pt.clear()
        pt.write("{} : SCORE".format(bounce), align="center", font=("Courier", 24, "normal"))
    
    if enemy.xcor() < -390:
        enemy.setx(-390)
        enemy.dx *= -1
        bounce += 1
        winsound.Beep(200, 120)
        pt.clear()
        pt.write("{} : SCORE".format(bounce), align="center", font=("Courier", 24, "normal"))


    # Border 2
    if enemy2.ycor() > 290:
        enemy2.sety(290)
        enemy2.dy *= -1

    if enemy2.ycor() < -290:
        enemy2.sety(-290)
        enemy2.dy *= -1

    if enemy2.xcor() > 390:
        enemy2.setx(390)
        enemy2.dx *= -1

    if enemy2.xcor() < -390:
        enemy2.setx(-390)
        enemy2.dx *= -1

    # Border 3
    if enemy3.ycor() > 290:
        enemy3.sety(290)
        enemy3.dy *= -1

    if enemy3.ycor() < -290:
        enemy3.sety(-290)
        enemy3.dy *= -1

    if enemy3.xcor() > 390:
        enemy3.setx(390)
        enemy3.dx *= -1

    if enemy3.xcor() < -390:
        enemy3.setx(-390)
        enemy3.dx *= -1


    # Man Border
    if man.ycor() > 290:
        man.sety(290)   

    if man.ycor() < -290:
        man.sety(-290)

    if man.xcor() > 390:
        man.setx(390)

    if man.xcor() < -390:
        man.setx(-390)
      
    # Game End
    if enemy.distance(man) <35: 
        eg = turtle.Turtle()
        eg.speed(0)
        eg.color("white")
        eg.penup()
        eg.hideturtle()
        eg.goto(0, 0)
        eg.write("GAME OVER", align="center", font=("Courier", 69, "bold"))
        
        eg2 = turtle.Turtle()
        eg2.speed(0)
        eg2.color("white")
        eg2.penup()
        eg2.hideturtle()
        eg2.goto(0, -120)
        eg2.write("GAME WILL AUTOMALTICLY CLOSE", align="center", font=("Courier", 20, "normal"))

        eg3 = turtle.Turtle()
        eg3.speed(0)
        eg3.color("white")
        eg3.penup()
        eg3.hideturtle()
        eg3.goto(0, -90)
        eg3.write("GG MAN TRY AGAIN", align="center", font=("Courier", 20, "normal"))
        
        eg4 = turtle.Turtle()
        eg4.speed(0)
        eg4.color("white")
        eg4.penup()
        eg4.hideturtle()
        eg4.goto(0, -290)
        eg4.write("Created By DandyTheWood", align="center", font=("Courier", 12, "normal"))

        winsound.Beep(200, 300)
        winsound.Beep(150, 300)
        winsound.Beep(100, 300)
        winsound.Beep(70, 700)
                        
        time.sleep(3.7)
        quit()

    # Game End 2
    if enemy2.distance(man) <35:
        eg = turtle.Turtle()
        eg.speed(0)
        eg.color("white")
        eg.penup()
        eg.hideturtle()
        eg.goto(0, 0)
        eg.write("GAME OVER", align="center", font=("Courier", 69, "bold"))
        
        eg2 = turtle.Turtle()
        eg2.speed(0)
        eg2.color("white")
        eg2.penup()
        eg2.hideturtle()
        eg2.goto(0, -120)
        eg2.write("GAME WILL AUTOMALTICLY CLOSE", align="center", font=("Courier", 20, "normal"))

        eg3 = turtle.Turtle()
        eg3.speed(0)
        eg3.color("white")
        eg3.penup()
        eg3.hideturtle()
        eg3.goto(0, -90)
        eg3.write("GG MAN TRY AGAIN", align="center", font=("Courier", 20, "normal"))
        
        eg4 = turtle.Turtle()
        eg4.speed(0)
        eg4.color("white")
        eg4.penup()
        eg4.hideturtle()
        eg4.goto(0, -290)
        eg4.write("Created By DandyTheWood", align="center", font=("Courier", 12, "normal"))
        
        winsound.Beep(200, 300)
        winsound.Beep(150, 300)
        winsound.Beep(100, 300)
        winsound.Beep(70, 700)
                        
        time.sleep(3.7)
        quit()

    # Game End 3
    if enemy3.distance(man) <35:
        eg = turtle.Turtle()
        eg.speed(0)
        eg.color("white")
        eg.penup()
        eg.hideturtle()
        eg.goto(0, 0)
        eg.write("GAME OVER", align="center", font=("Courier", 69, "bold"))
        
        eg2 = turtle.Turtle()
        eg2.speed(0)
        eg2.color("white")
        eg2.penup()
        eg2.hideturtle()
        eg2.goto(0, -120)
        eg2.write("GAME WILL AUTOMALTICLY CLOSE", align="center", font=("Courier", 20, "normal"))

        eg3 = turtle.Turtle()
        eg3.speed(0)
        eg3.color("white")
        eg3.penup()
        eg3.hideturtle()
        eg3.goto(0, -90)
        eg3.write("GG MAN TRY AGAIN", align="center", font=("Courier", 20, "normal"))
        
        eg4 = turtle.Turtle()
        eg4.speed(0)
        eg4.color("white")
        eg4.penup()
        eg4.hideturtle()
        eg4.goto(0, -290)
        eg4.write("Created By DandyTheWood", align="center", font=("Courier", 12, "normal"))
        
        winsound.Beep(200, 300)
        winsound.Beep(150, 300)
        winsound.Beep(100, 300)
        winsound.Beep(70, 700)
                        
        time.sleep(3.7)
        quit()

#=================================
# Dev: DandyTheWood ©
# Start of project - 8.9.2021
# End of project - 3.12.2021
#=================================
