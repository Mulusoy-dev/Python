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

#Write your code below this line 👇
selection=int(input("What do you choouse? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(selection)

if selection == 0:
    print(rock)
elif selection == 1:
    print(paper)
elif selection == 2:
    print(scissors)


print("Computer chose:")

computer_selection=random.randint(0,2)

if computer_selection == 0:
    print(rock)
elif computer_selection == 1:
    print(paper)
elif computer_selection == 2:
    print(scissors)

if selection == 0 and computer_selection == 2:
    print("You win")
elif selection == 1 and computer_selection == 0:
    print("You win")
elif selection == 2 and computer_selection == 1:
    print("You win")
elif selection==computer_selection:
    print("It's a draw")
else:
    print("You lose")









