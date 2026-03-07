import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Projects\Day25-US-States\blank_states_img.gif"
screen.addshape(image)
screen.setup(width= 730, height=490)
turtle.shape(image)

data = pandas.read_csv(r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Projects\Day25-US-States\50_states.csv")
all_states = data.state.to_list()
guessed_states = set()
score = 0

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Score: {score}/50", prompt="Guess a state's name").title()
    if answer_state == "Exit":
        game_is_on = False
    if answer_state in all_states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
        guessed_states.add(answer_state)
        score += 1

missed_states = []
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)
learning_output = pandas.DataFrame(missed_states)
learning_output.to_csv(fr"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Projects\Day25-US-States\missed_states.csv")


print(f"Well done. Your score was: {score} out of 50 states.")
screen.exitonclick()


# TODO: Convert the guess to title case
# TODO: Check if the guess is among the 50 states
# TODO: Write correct guesson onto the map
# TODO: Use a loop to allow the user to keep guessing
# TODO: Record the correct guess in a list
# TODO: Keep track of the score
# TODO: States to learn
