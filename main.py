import random
print("Rock, Paper or Scissors")

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

answer = int(input("Rock, Paper or Scissors? 0 = Rock, 1 = Paper & 2 = Scissors, Which do you choose? "))

if answer == 0:
    print("Your answer is:")
    print(rock)
elif answer == 1:
    print("Your answer is:")
    print(paper)
elif answer == 2:
    print("Your answer is:")
    print(scissors)
else:
    print("Please choose the listed values, please try again")

computer_answer = random.randint(0, 2)

if computer_answer == 0:
    print("Computer answer is:")
    print(rock)
elif computer_answer == 1:
    print("Computer answer is:")
    print(paper)
elif computer_answer == 2:
    print("Computer answer is:")
    print(scissors)
if answer == 0 and computer_answer == 0:
    print("It's a draw")
elif answer == 0 and computer_answer == 1:
    print("You lose")
elif answer == 0 and computer_answer == 2:
    print("You win")
elif answer == 1 and computer_answer == 0:
    print("You win")
elif answer == 1 and computer_answer == 1:
    print("It's a draw")
elif answer == 1 and computer_answer == 2:
    print("You lose")
elif answer == 2 and computer_answer == 0:
    print("You lose")
elif answer == 2 and computer_answer == 1:
    print("You win")
elif answer == 2 and computer_answer == 2:
    print("It's a draw")