import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Bubble Shooting Game")

# Create the shooter
shooter = turtle.Turtle()
shooter.shape("triangle")
shooter.color("white")
shooter.shapesize(stretch_wid=1, stretch_len=2)
shooter.penup()
shooter.goto(0, -280)

# Create the bubble
bubble = turtle.Turtle()
bubble.shape("circle")
bubble.color("blue")
bubble.penup()
bubble.goto(random.randint(-250, 250), 250)
bubble.dy = -2

# Create a variable to store the score
score = 0

# Function to move the shooter left
def move_left():
    x = shooter.xcor()
    if x > -280:
        x -= 20
        shooter.setx(x)

# Function to move the shooter right
def move_right():
    x = shooter.xcor()
    if x < 280:
        x += 20
        shooter.setx(x)

# Function to shoot the bubble
def shoot():
    global score
    if bubble.ycor() < -280:
        bubble.goto(shooter.xcor(), -260)
        score += 10

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(shoot, "space")

# Function to update the score display
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Create the score display turtle
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
update_score()

# Function to show "Game Over" message
def game_over():
    bubble.hideturtle()
    shooter.hideturtle()
    game_over_display = turtle.Turtle()
    game_over_display.color("white")
    game_over_display.penup()
    game_over_display.goto(0, 0)
    game_over_display.write("Game Over", align="center", font=("Courier", 36, "normal"))
    play_again = turtle.textinput("Game Over", "Play again? (yes or no)")
    while play_again.lower() not in ["yes", "no"]:
        play_again = turtle.textinput("Game Over", "Invalid input. Play again? (yes or no)")
    if play_again.lower() == "yes":
        bubble.goto(random.randint(-250, 250), 250)
        bubble.showturtle()
        shooter.goto(0, -280)
        shooter.showturtle()
        global score
        score = 0
        update_score()
        game_over_display.clear()
    else:
        turtle.bye()

# Main game loop
while True:
    # Move the bubble down
    bubble.sety(bubble.ycor() + bubble.dy)

    # Check for collision
    if bubble.distance(shooter) < 20:
        bubble.goto(random.randint(-250, 250), 250)
        score -= 5
        update_score()

    # Check if the bubble is out of bounds
    if bubble.ycor() < -300:
        game_over()

screen.mainloop()
