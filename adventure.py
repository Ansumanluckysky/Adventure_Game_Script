name=input("Enter your name: ")
print("Welcome",name,"to this adventure!")

answer=input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer=="left":
    answer=input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    if answer=="walk":
        print("you walk for amny miles, ran out of water and lost the game")
    elif answer=="swim":
        print("You swam across and were eaten by aligator")
    else:
        print("Not a valid option. You lose.")
elif answer=="right":
    answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back) ")

    if answer=="back":
        print("You go back and lose.")
    elif answer=="cross":
        answer = input ( "You cross a bridge and meet a stranger. Do you talk to them (yes/no)? " )
        if answer=="yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer=="no":
            print("You ignored the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying",name)