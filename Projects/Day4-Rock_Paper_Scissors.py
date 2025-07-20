import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) """)

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")
selection = [rock, paper, scissors]

players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0,2)

print(selection[players_choice])
print("Computer chose:")
print(selection[computer_choice])

if players_choice >= 3 or players_choice < 0:
    print("Invalid number. You Lose!")
elif players_choice == computer_choice:
    print("Draw")
elif players_choice == 2 and computer_choice == 0:
    print("Loser")
elif players_choice == 0 and computer_choice == 2:
    print("Winner")
elif players_choice > computer_choice:
    print("Winner")
else:
    print("Looser")