import turtle                      #import the turtle module
import random                      #import the random module

wn = turtle.Screen()               #create a screen
wn.bgcolor('lightblue')            #set background color
wn.title("Turtle Race")            #label the screen

lance = turtle.Turtle()            #create two turtles
andy = turtle.Turtle()
lance.color('red')                 #set color for lance
andy.color('blue')                 #set color for lance
lance.shape('turtle')              #set shape for lance
andy.shape('turtle')               #set shape for andy

andy.up()                          #move the turtles to their starting points
lance.up()
andy.goto(-100, 20)
lance.goto(-100, -20)

start = turtle.Turtle()            #create a third turtle object called start that will be used to display the winner of the game
start.hideturtle()                 #hide the third turtle object until the game is over for aesthetic purposes

andyTotalDistance = 0
lanceTotalDistance = 0

for i in range(130):               #iterate through the loop to run the forward method on both turtles 150 times.
    #Indent to begin the loop
    andyDistance = random.randrange(1, 5)       #make a random distance for andy to move
    lanceDistance = random.randrange(1, 5)      #make a random distance for lance to move
    andy.forward(andyDistance)   #move andy forward and use the andyDistance variable to determine the amount to move forward by.
    lance.forward(lanceDistance) #move lance forward and use the lanceDistance variable to determine the amount to move forward by.
    andyTotalDistance = andyTotalDistance + andyDistance   #this section is to determine the winner of the game and be used to print who the winner is.  It calculates total distance for lance and for andy.
    lanceTotalDistance = lanceTotalDistance + lanceDistance
    #De-indent to end the loop

for eachInt in range(125):
    # Indent to begin the loop
    if andyTotalDistance > lanceTotalDistance:   #use a cascading set of if conditions to determine the winner.
        start.write("Andy is the winner!", move=False, align="center", font=("Arial", 22, "bold"))
    elif lanceTotalDistance > andyTotalDistance:
        start.write("Lance is the winner!", move=False, align="center", font=("Arial", 22, "bold"))
    else: print("Tie Game")
    # De-indent to end the loop
wn.exitonclick()                                #exit on click of the window