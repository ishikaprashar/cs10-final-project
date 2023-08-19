#CS 10 Final Project
#Play Snowfall and Melt Your Stress Away!
#Ishika Prashar and Shivani Sharma
#12/9/2019


#to start the game type in the terminal "python3 snowfall_ishika.py"
#wait for turtle to finish drawing basket, tree, and board/border, then when apples fall 
#use left right keys to move basket and catch snow

import turtle
import random
import time

#this is a timer feature to provide starting screen and instructions on how to play the game
def timer(sec):
    while sec>0:
        print(sec)
        turtle.bgcolor("skyblue")
        turtle.penup()
        turtle.hideturtle()
        turtle.pencolor("midnightblue")
        turtle.goto(-450, 200)
        turtle.write("Welcome to Snowfall!", font=("courier", 30, "normal"))
        turtle.goto(-500, 130)
        turtle.write("How To Play:", font=("Arial", 30, "normal"))
        turtle.goto(-450, 70)
        turtle.write("Try to catch as many falling snowballs as you can!", font=("Arial", 30, "normal"))
        turtle.goto(-450, 20)
        turtle.write("Use the left and right arrows on your keyboard to control your basket", font=("Arial", 30, "normal"))
        turtle.goto(-450, -20)
        turtle.write("But Avoid the Fast and Fiery Red Snowballs!", font=("Arial", 30, "normal"))
        turtle.goto(-450, -60)
        turtle.write("Look out for the Rare Life-Saving Snowball! They are a darker shade of blue", font=("Arial", 30, "normal"))
        turtle.goto(-450, -100)
        turtle.write("The normal snowballs are different shades of blue and increase your score", font=("Arial", 30, "normal"))
        turtle.goto(-450, -200)
        turtle.write("Good luck! The game will begin shortly", font=("Arial", 30, "normal"))

        turtle.goto(-450, -10)


        time.sleep(1)
        sec-=1
        if sec==0:
            print("Start!")

timer(8)

#setting screen for specific background color and title----------------------------------
turtle.Screen().bgcolor("midnightblue")
turtle.hideturtle()
turtle.penup()
turtle.goto(0,270)
turtle.color("orchid")
turtle.write("Play Snowfall & Melt Away Your Stress!", align = "center", font=("courier", 40, "normal"))


#recursive tree background/alignment of around where snowballs fall from----------------------------------
tree=turtle.Turtle()
tree.penup()
tree.left(90)
tree.goto(0,-365)
tree.pendown()
tree.pensize(10)
tree.color("yellowgreen")

def recursive_tree(level,size): #this is a function that we defined ourselves. Essentially, we wanted to create a recursive tree to be used as placement for where snowballs should fall from. We used recursiion and base and recursive cases to implement. 
    if level ==1:
        tree.forward(size)
        tree.backward(size)
    else:
        tree.forward(size)
        tree.left(30)
        recursive_tree(level-1,size*.75)
        tree.right(60)
        recursive_tree(level-1,size*.75)
        tree.left(30)
        tree.backward(size)

recursive_tree(6,200)


#making the board list--------------------------------------------------------------------
#this is also a block we implemented ourselves which uses row and col numbers along with nested for loop to create a list of lists which makes a grid like list to represent board
def make_board_list(ROWS,COLS):
    a=[]
    for i in range(ROWS):
        y=[]
        for j in range(COLS):
            y.append(0*COLS)
        a.append(y)
    return (a)

#this is another block we implemented whihc uses turtle and variables to specify exactly how the board should look. For loops used to avoid repetitive code
#drawing the board--------------------------------------------------------------------
def draw_board(BOARD_WIDTH, BOARD_HEIGHT, ROWS, COLS):
    turtle.penup()
    turtle.color("orchid")
    turtle.goto(600,350)
    turtle.right(90)
    turtle.pendown() 
    turtle.pensize(2)
    for i in range(0,ROWS):
        turtle.forward(BOARD_HEIGHT)
        turtle.backward(BOARD_HEIGHT)
        turtle.right(90)
        turtle.forward(BOARD_WIDTH/ROWS)
        turtle.left(90)
    for j in range(0,COLS):
        turtle.forward(BOARD_HEIGHT/COLS)
        turtle.left(90)
        turtle.forward(BOARD_WIDTH)
        turtle.backward(BOARD_WIDTH)
        turtle.right(90)


# number of rows and columns--------------------------------------------------------------------
ROWS = 1 
COLS = 1

# the dimensions of the board being drawn----------------------------------
BOARD_WIDTH = 1200
BOARD_HEIGHT = 700

# Make a ROWSxCOLS list of lists.--------------------------------------------------------------------
BOARD_DATA = make_board_list(ROWS, COLS)
# Draw the interface.--------------------------------------------------------------------
draw_board(BOARD_WIDTH, BOARD_HEIGHT, ROWS, COLS)

#implemeting snowball types as a list and randomizing--------------------------------------------------------------------
#implemented using random library to take random snow color and then this function is used below starting from line 120 and onward to display random colored snow and have them fall down
def snow_types():
    types = ["lightcyan", "skyblue", "cornflowerblue", "azure"]
    random.shuffle(types)
    return types[0]

#making basket turtle --------------------------------------------------------------------
basketspeed = 20
# basket
basket = turtle.Turtle()
basket.turtlesize(3,3)
basket.shape("square")
basket.color("saddlebrown")
basket.speed(0)
basket.shape("square")
basket.penup()
basket.goto(0,-340)



# moving snowballs ------------------------------------------------------------------------------------------------------
snowballs = []
for i in range(0,5):
    for x in range(7,9):
        snowball = turtle.Turtle()
        snowball.speed(0)
        snowball.shape("circle")
        snowball.color(snow_types())
        snowball.penup()
        snowball.goto(0,50)
        snowball.speed = random.randint(10,20)
        snowballs.append(snowball)


navysnowballs = []
for i in range(3):
        navysnowball = turtle.Turtle()
        navysnowball.speed(0)
        navysnowball.shape("circle")
        navysnowball.color("navy")
        navysnowball.penup()
        navysnowball.goto(0,50)
        navysnowball.speed = random.randint(18,20)
        navysnowballs.append(navysnowball)

turtle.Screen().update()

redsnowballs = []
for i in range(5):
        redsnowball = turtle.Turtle()
        redsnowball.speed(0)
        redsnowball.shape("circle")
        redsnowball.color("firebrick")
        redsnowball.penup()
        redsnowball.goto(0,50)
        redsnowball.speed = random.randint(15,20)
        redsnowballs.append(redsnowball)

#implementing custom blocks to move basket --------------------------------------------------------------------
#we implemented this using turtle commands- we got the x coordinate and add the basket speed to the x to move right or subtract
#basket speed to move left. We also used the if statements to make sure basket does not go out of the screen.
#here, we also used our test cases, we actually did two cases. In basket right we made sure x was less than 320 because we did not want it to move any further right in the screen. 
#The assert cases are the same for basket_left only we assure that 
#x is greater than -320 because we don't want the basket to go any further left in the process. 
#in this case, the functions don't have any output but we still consider these test cases very very valuable
#as we need to ensure that the x and y positions for the basket are working exactly as we need them to even when the user moves the basket using their left or right keys. Any small mishap in coordinate numbers would cause this to error. 
def basket_right():
    x = basket.xcor()
    x = x+ basketspeed
    if x > 320:
        x = 320
    assert x<=320
    basket.setx(x)

def basket_left():
    x = basket.xcor()
    x = x - basketspeed
    if x <-320:
        x = -320
    assert x>=-320
    basket.setx(x)


turtle.Screen().listen()
turtle.Screen().onkey(basket_left, "Left")
turtle.Screen().onkey(basket_right, "Right")

turtle.Screen().update()


#catching the snowballs and adjusting score & lives -----------------------------------------------------------------------
score = 0
lives = 3



while True:
    for snowball in snowballs:
        y = snowball.ycor()
        y = y- snowball.speed
        snowball.sety(y)

        if y < -350:
            x = random.randint(-10,10)
            y = random.randint(-200, 200)
            snowball.goto(x,y)

        if snowball.distance(basket) < 40:
            x = random.randint(-300,300)
            y = random.randint(-200,200)
            snowball.goto(x,y)
            score += 1
            turtle.undo()
            turtle.write("Score: %s Lives: %d" %(score, lives),font=("Arial", 30, "normal"))
        
    for redsnowball in redsnowballs:
        y = redsnowball.ycor()
        y = y- redsnowball.speed
        redsnowball.sety(y)

        if y < -350:
            x = random.randint(-10,10)
            y = random.randint(-200, 200)
            redsnowball.goto(x,y)

        if redsnowball.distance(basket) < 40:
            x = random.randint(-300,300)
            y = random.randint(-200,200)
            redsnowball.goto(x,y)
            lives -= 1
            turtle.undo()
            turtle.write("Score: %s Lives: %d" %(score, lives),font=("Arial", 30, "normal"))
        elif lives==0:
            t=turtle.Turtle() #this all draws the game over screen once score reaches 0
            t.penup()
            t.fillcolor("rosybrown")
            t.goto(750,450)
            t.left(180)
            t.pendown()
            t.begin_fill()
            for i in range(2):
                t.forward(1500)
                t.left(90)
                t.forward(1000)
                t.left(90)
            t.end_fill()
            turtle.penup()
            turtle.goto(130,0)
            turtle.pendown()
            turtle.color("midnightblue")
            turtle.goto(-200,0)
            turtle.write("Game Over", font=("Arial", 60, "normal"))
            turtle.color("Black")
            turtle.penup()
            turtle.goto(-200,-50)
            turtle.pendown()
            turtle.write("Your score was: %s" %(score), font=("Arial", 30, "normal"))
    

    for navysnowball in navysnowballs:
        y = navysnowball.ycor()
        y = y- navysnowball.speed
        navysnowball.sety(y)

        if y < -350:
            x = random.randint(-10,10)
            y = random.randint(-200, 200)
            navysnowball.goto(x,y)


        if navysnowball.distance(basket) < 40:
            x = random.randint(-300,300)
            y = random.randint(-200,200)
            navysnowball.goto(x,y)
            lives += 1
            score+=5
            turtle.undo()
            turtle.write("Score: %s Lives: %d" %(score, lives),font=("Arial", 30, "normal")) #write and update score and lives
#-----------------------------------------------------------------------------------

turtle.Screen().update()

turtle.mainloop()








