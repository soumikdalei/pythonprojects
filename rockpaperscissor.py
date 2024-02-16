import random
computer_choice=random.randint(0,2)
print("Enter your Choice\n0 for rock \n1 for paper \n2 for scissors ")
your_choice1=input()
your_choice=int(your_choice1)
print(f"Computer's choice {computer_choice}")
if (computer_choice==your_choice):
    print("Game drawn")
elif (computer_choice==0 and your_choice== 1):
    print("You Won")
elif (computer_choice==1 and your_choice== 2):
    print("You Won")
elif (computer_choice==2 and your_choice== 0):
    print("You Won")
elif (computer_choice==1 and your_choice== 0):
    print("Computer Won")
elif (computer_choice==2 and your_choice== 1):
    print("Computer Won")
elif (computer_choice==0 and your_choice== 2):
    print("Computer Won")
