# 21 Number Game!
import random

print("Player 2 is the computer!")
try:
    wish = input("Do you want to play the game (Yes/No)? - ")
    if wish.lower() == "yes":
        print('''Press "F" to be the first player''')
        print('''Press "S" to be the second player''')
        position = input("")

        list_ = []
        validated = False

        if position == "F":
            while not validated:
                print(f"The list of values after the computer's turn is {list_}")
                print("How many values do you want to enter: ")
                values = int(input(""))
                print("Enter the value(s)")

                for j in range(values):
                    value = int(input(": "))
                    list_.append(value)

                    if len(list_) == 1:
                        if value != 1:
                            print("You are disqualified!")
                            validated = True
                            break
                        break
                        
                    elif  len(list_) > 1:
                        if list_[-1] - list_[-2] != 1:
                            print("You are disqualified!")
                            validated = True
                            break

                if list_[-1] == 20:
                    print("You won! Congrats!")
                    break

                comp_values = random.randint(1,4)
                for _ in range(comp_values):
                    list_.append(1+list_[-1])

                if 21 in list_:
                    print("You won! Congrats!")
                    break
                
                elif list_[-1] == 20:
                    print(f"The list of values after the computer's turn is {list_}")
                    print("You lost!")
                    break
                
            
        elif position == "S":
            while True:
                comp_values = random.randint(1,4)
                if len(list_) == 0:
                    for i in range(comp_values):
                        list_.append(i+1)
                else:
                    for i in range(comp_values):
                        list_.append(list_[-1]+1)

                if list_[-1] == 20:
                    print(f"The list of values after the computer's turn is {list_}")
                    print("You lost!")
                    break
                elif 21 in list_:
                    print(f"The list of values after the computer's turn is {list_}")
                    print("You won! Congrats!")
                    break

                print(f"The list of values after the computer's turn is {list_}")
                print("How many values do you want to enter: ")
                values = int(input(""))
                print("Enter the value(s)")

                for j in range(values):
                    value = int(input(": "))
                    list_.append(value)
                    if list_[-1] - list_[-2] != 1:
                        print("You are disqualified!")
                        validated = True
                        break
                if list_[-1] == 20:
                    print("You won! Congrats")
                    break

    elif wish.lower() == "no":
        print("Cool! See ya later! ")

    else:
        print("Invalid input!")
except Exception as e:
    print(e)

