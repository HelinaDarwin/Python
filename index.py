print('''
                                      --====|====--
                                            |  

                                        .-"""""-. 
                                      .'_________'. 
                                     /_/_|__|__|_\_\
                                    ;'-._       _.-';
               ,--------------------|    `-. .-'    |--------------------,
                ``""--..__    ___   ;       '       ;   ___    __..--""``
                          `"-// \\.._\             /_..// \\-"`
                             \\_//    '._       _.'    \\_//
                              `"`        ``---``        `"
''')
print("Welcome to Airport.")
print("Your mission is to get into the aeroplane.")
choice1=input("Where do you want to go 'left' or 'right'?").lower()
if choice1 == "left":
    choice2=input("How do you want to go. 'walk' or 'bus'").lower()
    if choice2 == "bus":
        choice3 = input("Which door you want to enter? 'red' or 'yellow' or 'blue'").lower()
        if choice3 == "red":
            print("Burned by fire. Game over")
        elif choice3 == "blue":
            print("Eaten by beasts. Game over")
        elif choice3 == "yellow":
            print("You Win!!! You are in aeroplane")
        else:
            print("You have pressed something. Game over")
    else:
        print("Attacked by trout. Game over")
else:
    print("You fell into a hole. Game over")
