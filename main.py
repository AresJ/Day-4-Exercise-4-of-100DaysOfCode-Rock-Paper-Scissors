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
gameImages = [rock, paper, scissors]
playersChoice = int(input("Let's play Rock-Paper-Scissors! \n Select 0 for Rock, 1 for Paper, or 2 for Scissors:"))

if playersChoice >= 3 or playersChoice < 0: 
  print("You typed an invalid number. You lose!")
else: 
  print(gameImages[playersChoice])

  computerChoice = random.randint(0, 2)
  print(f"Computer chose {computerChoice}")
  print(gameImages[computerChoice])

  if playersChoice == 0 and computerChoice == 2:
    print("You Win!")
  elif playersChoice == 2 and computerChoice == 0:
    print("You lose")  
  elif  computerChoice > playersChoice:
    print("You lose!")
  elif  playersChoice > computerChoice:
    print("You win!")
  elif computerChoice == playersChoice:
    print("Its a draw!")
