# Treasure Hunt 

print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")

step_1 = input("You're on a cross road. Where do you want to go? Type 'left' or 'right' ").lower()

if step_1 == "left":
    step_2 = input("Yoy come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across ").lower()
    if step_2 == "wait":
        step_3 = input("You arrive at island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower()
        if step_3 == "yellow":
            print("You Win!!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")