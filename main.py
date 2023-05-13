print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input("Would you like to go left or right? \n").lower()
if choice1 == ("right"):
  print(" Oh no! You  have fallen into quicksand. As you sink lower and lower, you grapple with your own mortality as you realize it is Game Over.\n")
else: 
  choice2 = input("You have chosen wisely. Would you like to swim or wait? \n").lower()
  if choice2 == ("swim"):
    print("I get it. You saw the beautiful mermaids and thought, \"Looks safe to me!\" Little did you know that they enjoy a tasty landlover when they get the chance. You shall be the main course at the feast of the Mer King later today. Game Over.\n")
  else:
    choice3 = input("You have chosen wisely. Now comes the hardest choice of all. There are three doors in front of you, which shall you choose? Red, Blue, or Yellow? \n").lower()
    if (choice3 == ("Red")) or (choice3 == ("red")):
      print("This is the house of the dread pirate Blackbeard. He has sent you off the plank. Game Over.\n")
    elif (choice3 == ("Blue")) or (choice3 == ("blue")):
      print("You have wandered into the house of the evil witch Calypso. She has turned you into a frog.\n")
    else:
      print("Congratulations! You have found the treasure! There's a pirate's soul in yer heart. You Win!\n")

