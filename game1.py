import random
import time

print("Enter choice: 1:Rock, 2:Paper, 3:Scissor")
choice = int(input("choice (1/2/3):  "))
comp_choice = random.randint(1,3)
print(f"Computer: {comp_choice}")
if choice == comp_choice:
    print("Draw")
elif choice ==1:
    if comp_choice == 2:
        print("Computer wins")
    else:
        print("You win")
elif choice == 2:
    if comp_choice ==1:
        print("Computer Wins")
    else:
        print("You Win")
elif choice == 3:
    if comp_choice ==1:
        print("Computer Wins")
    else:
        print("You Win")
    
