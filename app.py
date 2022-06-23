import random
from turtle import Turtle, Screen

# Define and config the Screen and its size
screen = Screen()
screen.setup(width=500, height=400)

# Declare a pen "turtle" to write game result at the bottom of Screen
pen = Turtle()
pen.penup()
pen.goto(-200, -150)
pen.pendown()

# The list of Turtle colors
turtle_colors = ["red", "green", "yellow", "purple", "orange"]

# List of all created Turtles
all_turtles = []

# This controls the race while loop. It changes when one of the turtles reaches the right edge ~230
is_race_on = False

# Creating Turtles using list of colors
for index, color in enumerate(turtle_colors):
    alpha = Turtle(shape="turtle")
    alpha.color(color)
    alpha.penup()
    alpha.goto(-230, -90 + index * 50)
    all_turtles.append(alpha)

# Asking the user to choose his/her turtle by picking up a color
user_turtle_color = ""
while user_turtle_color not in turtle_colors:
    user_turtle_color = screen.textinput(
        "Choose a turtle color",
        "Please choose a color from this list: " + str(turtle_colors),
    )

# If user picked a color, then the game begins...
if user_turtle_color:
    is_race_on = True

# As soon as the race is on =True, turtles move forward by a random int distance between 0 and 10. if edge reached, then game finishes
while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False

            # Write the result with the pen we declared
            pen.write(
                "You win! Congrats!!"
                if t.color() == user_turtle_color
                else "Mmm...it seems you need to try again! stay strong ;)",
                font=("Calibri", 5, "bold"),
            )

        random_distance = random.randint(0, 10)
        t.forward(random_distance)

# Exit game on clicking in random place on game screen
screen.exitonclick()
