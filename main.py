from turtle import Turtle, Screen
import random
colors = ['red', 'blue', 'green', 'yellow', 'violet', 'black']
y_index = [-120, -65, -10, 45, 100, 155]
screen = Screen()
screen.screensize(500, 400, 'white')
x = -230
turt_objects = []

for i in range(6):
    puppy = Turtle(shape='turtle')
    puppy.color(colors[i])
    puppy.penup()
    puppy.goto(x, y_index[i])
    turt_objects.append(puppy)

user_guess = screen.textinput(title='make your guess', prompt='Make a guess that which turtle is going to win the contest???')
is_race_end = False

if not user_guess:
    is_race_end = True

while not is_race_end:
    for a_turtle in turt_objects:
        rand_distance = random.randint(0, 10)
        a_turtle.fd(rand_distance)
        if a_turtle.xcor() > 360:
            if user_guess == a_turtle.pencolor():
                print(f"You win!, {a_turtle.pencolor()} Turtle wins the race")
            else:
                print(f"You lost!, {a_turtle.pencolor()} Turtle wins the race")
            is_race_end = True

screen.exitonclick()
