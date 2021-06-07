import random

while True:
    computer_choice=random.choice(['rock','paper', 'scissors'])
    user_choice=input("Enter your choice: rock, paper or scissors?")
    if computer_choice==user_choice:
        print("Tie")
    if (user_choice=="paper" and computer_choice=="rock") or(user_choice=="rock" and computer_choice=="scissors") or(user_choice=="scissors" and computer_choice=="paper"):
        print("You win!")
    else:
        print ("Better luck next time!")

