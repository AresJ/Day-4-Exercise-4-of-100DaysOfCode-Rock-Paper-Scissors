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

playersChoice = input("Let's play Rock-Paper-Scissors! \n Select 0 for Rock, 1 for Paper, or 2 for Scissors:")
import random
computerChoice = random.randint(0, 2)
if computerChoice == 2:
  print(rock)
elif computerChoice == 1:
  print(paper)
elif computerChoice == 0:
  print(scissors)
else: 
  print("Game Over!")
