import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.choice([rock, paper, scissors])
if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
print("Computer chose:")
print(computer_choice)
if player_choice == 0 and computer_choice == rock or player_choice == 1 and computer_choice == paper or player_choice == 2 and computer_choice == scissors:
    print("Draw")
elif player_choice == 0 and computer_choice == paper or player_choice == 1 and computer_choice == scissors or player_choice == 2 and computer_choice == rock:
    print("You Loose")
elif player_choice == 0 and computer_choice == scissors or player_choice == 1 and computer_choice == rock or player_choice == 2 and computer_choice == paper:
    print("You win")
print("-")