import turtle
import pandas



data = pandas.read_csv("50_states.csv")
states = data['state'].to_list()


screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)




guessed_states = []



while int(len(guessed_states)) < 50:
    user_guess = screen.textinput(f"{int(len(guessed_states))}/50 STATES", "Which State now?").title()

    if user_guess == "Exit":
        missing_states = [item for item in states if item not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break


    if user_guess in states:
        guessed_states.append(user_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states1 = data[data.state == user_guess]
        t.goto(int(states1.x), int(states1.y))
        t.write(user_guess)









