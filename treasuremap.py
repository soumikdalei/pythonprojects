import for
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("Enter Left or Right")
direction=str(input())
if (direction.lower()=='left'):
    print("You will swim or wait ")
    direction1=str(input())
    if direction1.lower()=="wait":
        print("Which Door you will select")
        direction2=str(input())
        if direction2.lower()=="red":
            print("Burned by fire .\nGame Over.")
        elif direction2.lower()=="blue":
            print("Eaten By Beats.\nGame Over.")
        elif direction2.lower()=="yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")