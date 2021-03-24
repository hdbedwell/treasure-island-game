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
direction = input("You have come to the Crossroads. Which way would you like to go? \nType L (left) or R (right)? ")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

if direction == "R":
  direction2 = input("You have come to a vast ocean. Would you like to swim or wait for a boat?\n S (swim) or W (wait)? ")
  if  direction2 == "W":
    direction3 = input("You have come to three doors on your journey and must choose one. \nWhich door would you like to enter? Type: R (red), B (blue), or G (green)? ")
    if direction3 == "R":
      print("You got burned by DRAGON FIRE! ROAR!!! Ssssss... GAME OVER!")
    elif direction3 == "G":
      print("You got AVADA KADAVRAed!! by Voldemort. GAME OVER!")
    elif direction3 == "B":
      print("YOU WIN!")
    else:
      print("GAME OVER!")
  else:  
    print("You got attacked by ELECTRIC EELS. GAME OVER!")
else:
  print("You fell into a hole. GAME OVER!")
  
  

