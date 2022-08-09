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


import random

choose = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

if int(choose) == 0:
	print(rock)
elif int(choose) == 1:
	print(paper)
else:
	print(scissors)
print("Computer choice:")
comp = [rock, paper, scissors]
comp_int = len(comp)
new = random.randint(0, comp_int - 1)
if new == 0:
	print(rock)
elif new == 1:
	print(paper)
else:
	print(scissors)
if int(choose) == new:
	print("draw")
elif int(choose) == 0 and new > 1:
	print("You won")
elif int(choose) == 0 and new == 1:
	print("You won")
elif int(choose) > 1 and new == 0:
	print("You won")
elif int(choose) > 1 and new == 1:
	print("You won")
else:
	print("you failed")
