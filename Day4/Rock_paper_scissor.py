# Rock paper scissor game

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
choice_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissor: "))
print("Your choice: ")
print(choice_list[user_choice])

print("Computer Choose: ")
import random
comp_choice= random.randint(0,len(choice_list)-1)
print(choice_list[comp_choice])

if(user_choice==0 and comp_choice==2):
    print("You Win")
elif(user_choice==2 and comp_choice==1):
    print("You Win")
elif(user_choice==1 and comp_choice==0):
    print("You Win")
elif(user_choice==comp_choice):
    print("Draw")
else:
    print("You Lose")